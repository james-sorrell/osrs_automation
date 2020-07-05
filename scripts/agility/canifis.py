from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

laps = int(input('How many laps?\n'))
print("Looping {} times.".format(laps))

b = OSBrain("OpenOSRS")

MAIN_SCRN = (12, 33, 513, 358)
OBS_CLR = (0, 255, 0)
MOG_CLR = (255, 0, 0)
PLY_LOC = (262, 200)

def distance(x1, y1, x2, y2):
    return (abs(x2-x1)**2+abs(y2-y1)**2)

def findClosestCorner(loc):
    d1 = distance(PLY_LOC[0], PLY_LOC[1], loc[0], loc[1])
    d2 = distance(PLY_LOC[0], PLY_LOC[1], loc[0], loc[3])
    d3 = distance(PLY_LOC[0], PLY_LOC[1], loc[2], loc[1])
    d4 = distance(PLY_LOC[0], PLY_LOC[1], loc[2], loc[3])
    return min(d1, d2, d3, d4)

def findClosestLocToPlayer(loc1, loc2):
    d1 = findClosestCorner(loc1)
    d2 = findClosestCorner(loc2)
    print("MOG DIST: {}, OBS DIST: {}".format(d1,d2))
    if (d1 <= d2):
        return loc1
    return loc2

failsafe = 0

for _ in range(laps):

    MOG_LOC = b.detection.findArea(MAIN_SCRN, MOG_CLR)
    OBS_LOC = b.detection.findArea(MAIN_SCRN, OBS_CLR)

    print("MOG_LOC: {}, OBS_LOC: {}".format(MOG_LOC, OBS_LOC))
    
    if (OBS_LOC is None and MOG_LOC is None):
        print("Nothing found, incrementing failsafe count.")
        failsafe += 1
        if (failsafe >= 100):
            quit()
    else:
        print("Resetting failsafe.")
        failsafe = 0

    if (MOG_LOC is not None):
        # Find which is closest
        if (OBS_LOC is None):
            LOC = MOG_LOC
        else:
            print("Finding closest location!")
            LOC = findClosestLocToPlayer(MOG_LOC, OBS_LOC)
        b.per.moveToBox(LOC, 'very_fast')
        t.randomSleep(10, 1)
        b.per.click('left')
        t.randomSleep(400, 50)
    elif(OBS_LOC is not None):
        b.per.moveToBox(OBS_LOC, 'very_fast')
        t.randomSleep(10, 1)
        b.per.click('left')
        t.randomSleep(400, 50)
