import time
import random

from osbrain.osbrain import OSBrain
import util.timingHelpers as th
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

PEAR_lOC = (335, 195, 375, 225)
PEAR_CLR = (83, 165, 7)

total_time = int(input('How long do you want this to run for? (Minutes)\n'))
print("Running for {} minutes.".format(total_time))

b = OSBrain()

fruitNotFoundCount = 0


start = time.time()
end = time.time()

while( (end-start) < 60*total_time ):
  b.per.moveToBox(PEAR_lOC, 'fast')
  while(b.detection.isInventoryFull() is False):
    if (b.detection.colorSearch(PEAR_lOC, PEAR_CLR)):
      # It gets two chances to try and see it
      b.per.click('left')
      fruitNotFoundCount = 0
    else:
      fruitNotFoundCount += 1
      print("Fruit not found count: {}".format(fruitNotFoundCount))
    if (fruitNotFoundCount >= 10):
      print("Safeguard exit.")
      quit()
    th.randomSleep(1100,100)
  th.randomSleep(100, 25)
  print("Inventory Full.")
  b.dropInventory()

  eps2 = 0.005
  if (random.random() < eps2):
      print("Randomly moving mouse somewhere.")
      b.per.moveToBox([0, 0, 2000, 2000])
      t.randomSleep(4000, 3000)

  end = time.time()
  print("Minutes elapsed: {:.1f}".format((end-start)/60))

# inv = df.getInventoryStatus(window)
# # Check if all true (used)
# if all(inv):
#   print("Inventory is full")


# for i in range(3):
#   mouse.click()
#   mouse._sleep('slow')
#   mouse._sleep('slow')

