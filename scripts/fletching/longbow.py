from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

logs = input('How many logs?\n')
loop = int(logs)//27
print("Looping {} times.".format(loop))

b = OSBrain()

CHEST_LOC = (249, 99, 300, 134)
b.per.moveToBox(CHEST_LOC, 'medium')
b.per.click('left')
t.randomSleep(160, 15)

CHEST_CLR1 = (77, 49, 31)
CHEST_CLR2 = (72, 45, 28)

for _ in range(loop):

    LOGS_LOC = (84, 119, 96, 131)

    b.per.moveToBox(LOGS_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    BANK_X = (485, 44, 493, 53)

    b.per.moveToBox(BANK_X, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    KNIFE_LOC = (573, 247, 585, 263)
    INV_LOC = (612, 247, 631, 263)

    b.per.moveToBox(KNIFE_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    b.per.moveToBox(INV_LOC, 'fast')
    b.per.click('left')
    t.randomSleep(450, 15)

    LONGBOW_LOC = (229, 425, 290, 469)
    b.per.moveToBox(LONGBOW_LOC, 'medium')
    b.per.click('left')

    chest_located = b.detection.colorRangeSearch(CHEST_LOC, CHEST_CLR1, CHEST_CLR2)
    print("CHEST LOCATED: {}".format(chest_located))

    if(chest_located is False):
        quit()

    t.randomSleep(50000, 1000)

    b.per.moveToBox(CHEST_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    b.per.moveToBox(INV_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)