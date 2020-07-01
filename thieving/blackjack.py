from osbrain.osbrain import OSBrain
import util.timingHelpers as th
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

MAIN_SCRN = (12, 33, 513, 358)
OUTLINE_CLR = (0, 255, 0)

b = OSBrain()

BANDIT_LOC = b.detection.findArea(MAIN_SCRN, OUTLINE_CLR)
if BANDIT_LOC is None:
  print("Couldn't find a bandit")
  quit()
b.per.moveToBox(BANDIT_LOC, 'fast')

# fruitNotFoundCount = 0

# for _ in range(10):
#   b.per.moveToBox(PEAR_lOC, 'fast')
#   while(b.detection.isInventoryFull() is False):
#     if (b.detection.colorSearch(PEAR_lOC, PEAR_CLR)):
#       # It gets two chances to try and see it
#       b.per.click('slow')
#       fruitNotFoundCount = 0
#     else:
#       fruitNotFoundCount += 1
#       print("Fruit not found count: {}".format(fruitNotFoundCount))
#     if (fruitNotFoundCount >= 10):
#       print("Safeguard exit.")
#       quit()
#     th.random_sleep_ms(500,50)
#   th.random_sleep_ms(100, 25)
#   print("Inventory Full.")
#   b.dropInventory()
  

# inv = df.getInventoryStatus(window)
# # Check if all true (used)
# if all(inv):
#   print("Inventory is full")


# for i in range(3):
#   mouse.click()
#   mouse._sleep('slow')
#   mouse._sleep('slow')

