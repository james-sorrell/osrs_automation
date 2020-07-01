from osbrain.osbrain import OSBrain
import util.timingHelpers as th
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 2

PEAR_lOC = (338, 193, 389, 223)
PEAR_CLR = (83, 165, 7)

b = OSBrain()

b.dropInventory()
quit()

b.mouse.moveToBox(PEAR_lOC, 'fast')
while(b.detection.isInventoryFull() is False):
  if (b.detection.colorSearch(PEAR_lOC, PEAR_CLR)):
    # It gets two chances to try and see it
    b.mouse.click('medium')
  th.random_sleep_ms(1000,50)
print("Inventory Full.")
  

# inv = df.getInventoryStatus(window)
# # Check if all true (used)
# if all(inv):
#   print("Inventory is full")


# for i in range(3):
#   mouse.click()
#   mouse._sleep('slow')
#   mouse._sleep('slow')

