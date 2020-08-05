from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

CW_CHEST_LOC = [250, 250, 270, 270]

b = OSBrain()

# def _clickOnPotion():
#     inv = b.detection.getInventoryStatus()
#     for i in range(27):
#         print(inv[i+1])
#         if inv[i+1] == True:
#             print("Clicking on {}".format(i+1))
#             loc = b.getInvLoc(i+1)
#             b.per.moveToBox(loc, 'fast')
#             t.randomSleep(150, 50)
#             b.per.click('left')
#             t.randomSleep(2000, 800)
#             return

# while(True):
im = b.window.getImage(CW_CHEST_LOC)
im_arr = np.array(im)
plt.imshow(im)
plt.show()
    # nine = np.load("scripts/magic/nmz_nine.npy")
    # if np.array_equal(nine, im_arr) is False:
    #     print("Is not 9XX")
    #     _clickOnPotion()
    # else:
    #     print("Absorption is OK.")
    # t.randomSleep(10000, 800)