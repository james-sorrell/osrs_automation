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

MAIN_SCRN = (12, 33, 513, 358)
OBS_CLR = (254, 254, 0)
MOG_CLR = (254, 0, 254)
PLY_LOC = (262, 200)
CAMELOT_LOC = [695, 315, 705, 325]

b = OSBrain("OpenOSRS")
end = time.time()

def teleportCamelot():
    b.per.moveToBox(CAMELOT_LOC, 'very_fast')
    t.randomSleep(15, 1)
    b.per.click('left')
    t.randomSleep(500, 250)

def homeLocation(delay):
    OBS_LOC = b.detection.findArea(MAIN_SCRN, OBS_CLR)
    if (OBS_LOC is None):
        print("ERROR: Failed home location!")
        quit()
    else:
        b.per.moveToBox(OBS_LOC, 'very_fast')
        t.randomSleep(15, 1)
        b.per.click('left')
        t.randomSleep(delay, 250)    

def roof(delay):
    BOX_LOC = [115, 100, 170, 215]
    OBS_LOC = b.detection.findArea(BOX_LOC, OBS_CLR)
    if (OBS_LOC is None):
        print("Could not find normal roof box.")
        teleportCamelot()
        return False
    else:
        b.per.moveToBox(OBS_LOC, 'very_fast')
        t.randomSleep(15, 1)
        b.per.click('left')
        t.randomSleep(5500, 250)
    return True

def mogRoof(mog_delay, delay):
    MOG_LOC = b.detection.findArea(MAIN_SCRN, MOG_CLR)
    if (MOG_LOC is None):
        print("Could not find mog.")
    else:
        b.per.moveToBox(MOG_LOC, 'very_fast')
        t.randomSleep(15, 1)
        b.per.click('left')
        t.randomSleep(mog_delay, 250)    
    OBS_LOC = b.detection.findArea(MAIN_SCRN, OBS_CLR)
    if (OBS_LOC is None):
        print("Could not find mog-roof box.")
        teleportCamelot()
        return False
    else:
        b.per.moveToBox(OBS_LOC, 'very_fast')
        t.randomSleep(15, 1)
        b.per.click('left')
        t.randomSleep(delay, 250)
    return True

while( (end-start) < 60*total_time ):
    print("Starting new lap.")
    homeLocation(8000)
    print("Roof 1")
    status = mogRoof(3000, 8000)
    if status is False:
        print("Failed roof 1.")
        continue
    print("Roof 2")
    status = mogRoof(3000, 8000)
    if status is False:
        print("Failed roof 2.")
        continue
    print("Roof 3")
    status = mogRoof(3000, 8000)
    if status is False:
        print("Failed roof 3.")
        continue
    print("Roof 4")
    status = mogRoof(3000, 8000)
    if status is False:
        print("Failed roof 4.")
        continue
    print("Roof 5")
    status = mogRoof(3000, 8000)
    if status is False:
        print("Failed roof 5.")
        continue
    end = time.time()
