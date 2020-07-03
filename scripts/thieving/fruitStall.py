from osbrain.osbrain import OSBrain
import util.timingHelpers as th
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

PEAR_lOC = (338, 203, 389, 223)
PEAR_CLR = (83, 165, 7)

b = OSBrain()

fruitNotFoundCount = 0

for _ in range(10):
  b.per.moveToBox(PEAR_lOC, 'fast')
  while(b.detection.isInventoryFull() is False):
    if (b.detection.colorSearch(PEAR_lOC, PEAR_CLR)):
      # It gets two chances to try and see it
      b.per.click('slow')
      fruitNotFoundCount = 0
    else:
      fruitNotFoundCount += 1
      print("Fruit not found count: {}".format(fruitNotFoundCount))
    if (fruitNotFoundCount >= 10):
      print("Safeguard exit.")
      quit()
    th.random_sleep_ms(500,50)
  th.random_sleep_ms(100, 25)
  print("Inventory Full.")
  b.dropInventory()
  

# inv = df.getInventoryStatus(window)
# # Check if all true (used)
# if all(inv):
#   print("Inventory is full")


# for i in range(3):
#   mouse.click()
#   mouse._sleep('slow')
#   mouse._sleep('slow')
