from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

alchs = int(input('How many alchs?\n'))
print("Looping {} times.".format(alchs))

b = OSBrain()

CHEST_LOC = (281, 124, 345, 162)
CHEST_CLR1 = (77, 49, 31)
CHEST_CLR2 = (72, 45, 28)

for _ in range(alchs):

    ALCH_LOC = (894, 410, 903, 418)

    b.per.moveToBox(ALCH_LOC, 'fast')
    b.per.click('left')
    t.randomSleep(180, 15)
    b.per.click('left')
    t.randomSleep(3500, 200)
