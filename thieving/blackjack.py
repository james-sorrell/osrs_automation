from osbrain.osbrain import OSBrain
import util.timingHelpers as th
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

MAIN_SCRN = (12, 33, 513, 358)
OUTLINE_CLR = (0, 255, 0)
BRDY_LOC = (205, 100, 355, 135)
BRD_CLR1 = (159, 143, 6)
BRD_CLR1 = (237, 215, 10)

def _getKnockoutLocation():
  x, y = b.per.mousePosition()
  y1 = y+87
  y2 = y+90
  x1 = x-5
  x2 = x+5
  return (x1, y1, x2, y2)

def _getPickpocketLocation():
  x, y = b.per.mousePosition()
  y1 = y+57
  y2 = y+60
  x1 = x-5
  x2 = x+5
  return (x1, y1, x2, y2)

def _clickBox(loc, click='left', move_delay='very_fast', click_delay='very_fast'):
  b.per.moveToBox(loc, move_delay)
  b.per.click(click, click_delay)

b = OSBrain()

# while True:
#   res = b.detection.colorRangeSearch(BRDY_LOC, BRD_CLR1, BRD_CLR1)
#   if res is True:
#     print("Birdy found")

for _ in range(2):
  BANDIT_LOC = b.detection.findArea(MAIN_SCRN, OUTLINE_CLR)
  if BANDIT_LOC is None:
    print("Couldn't find a bandit")
    quit()
  print("BANDIT LOC: ", BANDIT_LOC)
  b.per.moveToBox(BANDIT_LOC, 'fast')
  b.per.click('right', 'fast')
  KNKOUT_LOC = _getKnockoutLocation()
  # print("KNKOUT LOC: ", KNKOUT_LOC)
  # b.per.moveToBox(KNKOUT_LOC, 'very_fast')
  # b.per.click('left', 'very_fast')
  _clickBox(KNKOUT_LOC, move_delay='fast', click_delay='medium')
  searchTime = np.random.uniform(300, 50)
  KNKOUT_FAIL = th.timedFunction(searchTime, b.detection.colorRangeSearch, BRDY_LOC, BRD_CLR1, BRD_CLR1)
  #KNKOUT_FAIL = b.detection.colorRangeSearch(BRDY_LOC, BRD_CLR1, BRD_CLR1)
  if KNKOUT_FAIL is True:
    print("Birdies!")
    _clickBox(BANDIT_LOC, 'right')
    PCKPKT_LOC = _getPickpocketLocation()
    _clickBox(PCKPKT_LOC)
  else:
    BANDIT_LOC = b.detection.findArea(MAIN_SCRN, OUTLINE_CLR)
    _clickBox(BANDIT_LOC, 'right')
    PCKPKT_LOC = _getPickpocketLocation()
    _clickBox(PCKPKT_LOC)
    _clickBox(BANDIT_LOC, 'right')
    PCKPKT_LOC = _getPickpocketLocation()
    _clickBox(PCKPKT_LOC)
#   b.per.moveToBox(BANDIT_LOC, 'fast')
#   b.per.click('right', 'fast')
#   b.per.moveToBox(PCKPKT_LOC, 'very_fast')
#   b.per.click('left', 'very_fast')
# else:
#   b.per.moveToBox(BANDIT_LOC, 'fast')
#   b.per.click('right', 'fast')
#   b.per.moveToBox(PCKPKT_LOC, 'very_fast')
#   b.per.click('left', 'very_fast')
#   b.per.moveToBox(BANDIT_LOC, 'fast')
#   b.per.click('right', 'fast')
#   b.per.moveToBox(PCKPKT_LOC, 'very_fast')
#   b.per.click('left', 'very_fast')

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

