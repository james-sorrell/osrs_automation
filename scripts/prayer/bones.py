from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0
b = OSBrain()

ALT_LOC = [345, 200, 355, 210]

status = b.detection.getInventoryStatus()

def _isInventoryEmpty(status):
    return all(np.invert(status))

def _useBones(location):
    boneLoc = b.getInvLoc(location)
    print("Moving to Inventory: {}".format(location))
    b.per.moveToBox(boneLoc, 'fast')
    t.randomSleep(20,2)
    b.per.click('left')
    print("Moving to Altar.")
    b.per.moveToBox(ALT_LOC, 'fast')
    t.randomSleep(20,2)
    b.per.click('left')

prev_location = np.inf
noBonesUsedLastRun = True
bonesMonitor = False

while _isInventoryEmpty(status) is False:
    print("Inventory is not empty")
    bonesMonitor = True
    for location in range(status.size):
        if status[location] and (location != prev_location or noBonesUsedLastRun):
            prev_location = location
            _useBones(location)
            bonesMonitor = False
            break
    t.randomSleep(150,20)
    noBonesUsedLastRun = bonesMonitor
    status = b.detection.getInventoryStatus()

print("Inventory is Empty.")