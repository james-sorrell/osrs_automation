from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

logs = input('How many bows?\n')
loop = ceil(int(logs)/27)
print("Looping {} times.".format(loop))

b = OSBrain()

CHEST_LOC = (281, 124, 345, 162)
CHEST_CLR1 = (77, 49, 31)
CHEST_CLR2 = (72, 45, 28)

for _ in range(loop):

    ALCH_LOC = (894, 410, 903, 418)

    b.per.moveToBox(ALCH_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)
    b.per.click('left')
    t.randomSleep(750, 100)
