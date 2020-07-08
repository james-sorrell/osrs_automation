import time
from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

total_time = int(input('How long do you want this to run for? (Minutes)\n'))
print("Running for {} minutes.".format(total_time))
start = time.time()

b = OSBrain("OpenOSRS")

MAIN_SCRN = (12, 33, 513, 358)
OBS_CLR = (254, 254, 0)
MOG_CLR = (254, 0, 254)
PLY_LOC = (262, 200)

STABLE_LOC = (215, 200, 220, 205)

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

end = time.time()

while( (end-start) < 60*total_time ):

    if (failsafe >= 100):
        print("First Failsafe exceeded threshold, quitting")
        quit()

    MOG_LOC = b.detection.findArea(MAIN_SCRN, MOG_CLR)
    OBS_LOC = b.detection.findArea(MAIN_SCRN, OBS_CLR)

    print("MOG_LOC: {}, OBS_LOC: {}".format(MOG_LOC, OBS_LOC))
    
    if (OBS_LOC is None and MOG_LOC is None):
        print("Nothing found, incrementing failsafe count.")
        failsafe += 1
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
        MOG_DIST = findClosestCorner(LOC)
        print("\tMOG DIST: {}".format(MOG_DIST))
        t.randomSleep(15, 1)
        b.per.click('left')
        t.randomSleep(300+MOG_DIST//4000, 1)
    elif(OBS_LOC is not None):
        b.per.moveToBox(OBS_LOC, 'very_fast')
        OBJ_DIST = findClosestCorner(OBS_LOC)
        print("\tOBJ DIST: {}".format(OBJ_DIST))
        t.randomSleep(15, 1)
        b.per.click('left')
        t.randomSleep(850+OBJ_DIST//4000, 1)

    # Check to see if the character is moving before continuing the loop
    im, im2 = 0, 1
    movement_failsafe = 0
    while(im != im2):
        im = b.window.getImage(STABLE_LOC)
        t.randomSleep(200,1)
        im2 = b.window.getImage(STABLE_LOC)
        #print("Resetting failsafe.")
        movement_failsafe = 0
        np.array_equal(np.array(im), np.array(im2))
    print("Character is idle.")
    end = time.time()
    print("Minutes elapsed: {:.1f}".format((end-start)/60))