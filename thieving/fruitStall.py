import util.windowHandler as wh
import util.mouseHandler as mh
import util.detectionFunctions as df

import numpy as np

import matplotlib.pyplot as plt

PEAR_lOC = (355, 205, 365, 215)
PEAR_CLR = (83, 165, 7)

window = wh.WindowHandler("runelite")
window.bringForward()
x, y, _, _ = window.getWindowRect()

mouse = mh.Mouse(x, y)
#mouse.moveToBox(350, 380, 145, 180, 'fast')

import time

while(all(df.getInventoryStatus(window)) is False):
  if (df.colorSearch(window, PEAR_lOC, PEAR_CLR)):
    print("\tFruit detected")
  else:
    print("\tFruit not detected")
  time.sleep(1)

print("Stop doing stuff")
  

# inv = df.getInventoryStatus(window)
# # Check if all true (used)
# if all(inv):
#   print("Inventory is full")


# for i in range(3):
#   mouse.click()
#   mouse._sleep('slow')
#   mouse._sleep('slow')

