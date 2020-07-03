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
b.per.moveToBox(CHEST_LOC, 'medium')
b.per.click('left')
t.randomSleep(500, 15)

CHEST_CLR1 = (77, 49, 31)
CHEST_CLR2 = (72, 45, 28)

for _ in range(loop):

    BOWS_LOC = (169, 149, 183, 163)

    b.per.moveToBox(BOWS_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    BANK_X = (607, 55, 616, 70)

    b.per.moveToBox(BANK_X, 'medium')
    b.per.click('left')
    t.randomSleep(250, 15)

    INV14_LOC = (773, 441, 785, 457)
    INV15_LOC = (821, 441, 839, 457)

    b.per.moveToBox(INV14_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    b.per.moveToBox(INV15_LOC, 'fast')
    b.per.click('left')
    t.randomSleep(450, 15)

    LONGBOW_LOC = (286, 530, 365, 584)
    b.per.moveToBox(LONGBOW_LOC, 'medium')
    t.randomSleep(300, 15)
    b.per.click('left')
    t.randomSleep(120, 15)

    chest_located = b.detection.colorRangeSearch(CHEST_LOC, CHEST_CLR1, CHEST_CLR2)
    print("CHEST LOCATED: {}".format(chest_located))

    if(chest_located is False):
        quit()

    t.randomSleep(50000, 1000)

    b.per.moveToBox(CHEST_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(500, 15)

    INV1_LOC = (769, 307, 788, 323)

    b.per.moveToBox(INV1_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)