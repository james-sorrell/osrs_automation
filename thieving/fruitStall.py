import util.windowHandler as wh
import util.mouseHandler as mh
import util.detectionFunctions as df
import util.timingHelpers as th
import util.config as c

c.VERBOSE = 2

import numpy as np
import matplotlib.pyplot as plt

PEAR_lOC = (355, 205, 365, 215)
PEAR_CLR = (83, 165, 7)

window = wh.WindowHandler("runelite")
window.bringForward()
x, y, _, _ = window.getWindowRect()
mouse = mh.Mouse(x, y)
dh = df.DetectionHandler(window)

mouse.moveToBox(350, 380, 145, 180, 'fast')
detectedLastPoll = False

while(dh.isInventoryFull() is False):
  if (dh.colorSearch(PEAR_lOC, PEAR_CLR)):
    if (detectedLastPoll is False):
      mouse.click('fast')
    detectedLastPoll = True
  else:
    detectedLastPoll = False
  th.random_sleep_ms(500,50)

print("Stop doing stuff")
  

# inv = df.getInventoryStatus(window)
# # Check if all true (used)
# if all(inv):
#   print("Inventory is full")


# for i in range(3):
#   mouse.click()
#   mouse._sleep('slow')
#   mouse._sleep('slow')

