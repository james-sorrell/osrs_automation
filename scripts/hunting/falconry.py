from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

MAIN_SCRN = (12, 33, 513, 358)
KEB_CLR1 = (0, 100, 100)
KEB_CLR2 = (0, 255, 255)
PLY_LOC = (262, 200)

CATCH_CLR1 = (200, 200, 0)
CATCH_CLR2 = (255, 255, 0)

b = OSBrain()


if (b.detection.isInventoryFull() is True):
    b.dropInventory(range(2,28))


# # for y in range(0, y-20, 15):
# #     for x in range(0, w-20, 15):
# #         b.detection.findArea(MAIN_SCRN, FISH_CLR1, FISH_CLR2, PLY_LOC)

# def waitIdle():
#     STABLE_LOC = (100, 200, 105, 205)
#     stationary = False
#     while(stationary == False):
#         im1 = b.window.getImage(STABLE_LOC)
#         t.randomSleep(400,25)
#         im2 = b.window.getImage(STABLE_LOC)
#         stationary = np.array_equal(np.array(im1), np.array(im2))
#         print("Stationary: {}".format(stationary))
#     print("Character is idle.")


# while(True):

#     if (b.detection.isInventoryFull() is True):
#         b.dropInventory(range(2,28))

#     waitIdle()
#     KEB_LOC = b.detection.findClosestPoint(MAIN_SCRN, CATCH_CLR1, CATCH_CLR2, PLY_LOC)
#     if KEB_LOC[0] == None or KEB_LOC[1] == None:
#         print("No caught kebbits found.")
#     else:
#         print("YELLOW_LOC:", KEB_LOC)
#         b.per._moveToPoint(KEB_LOC[0], KEB_LOC[1]-40, speed='very_fast')
#         t.randomSleep(100,50)
#         b.per.click('left')
#         t.randomSleep(1000,50)
#         continue

#     waitIdle()
#     KEB_LOC = b.detection.findClosestPoint(MAIN_SCRN, KEB_CLR1, KEB_CLR2, PLY_LOC)
#     if KEB_LOC[0] == None or KEB_LOC[1] == None:
#         print("No kebbits found.")
#     else:
#         print("KEBBIT_LOC:", KEB_LOC)
#         b.per._moveToPoint(KEB_LOC[0], KEB_LOC[1], speed='very_fast')
#         t.randomSleep(100,50)
#         b.per.click('left')