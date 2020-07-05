from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

logs = input('How many bows?\n')
loop = int(np.ceil(int(logs)/14))
print("Looping {} times.".format(loop))

b = OSBrain()

CHEST_LOC = (320, 164, 330, 170)
CHEST_COLOR_LOC = (262, 107, 370, 195)
b.per.moveToBox(CHEST_LOC, 'medium')
b.per.click('left')
t.randomSleep(500, 15)

CHEST_CLR1 = (90, 60, 50)
CHEST_CLR2 = (50, 20, 10)

for _ in trange(loop):

    BOWS_LOC = (169, 149, 183, 163)

    b.per.moveToBox(BOWS_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(200, 15)

    BOWS_LOC = (225, 149, 240, 163)

    b.per.moveToBox(BOWS_LOC, 'fast')
    b.per.click('left')
    t.randomSleep(200, 15)

    BANK_X = (607, 55, 616, 70)

    b.per.moveToBox(BANK_X, 'medium')
    b.per.click('left')
    t.randomSleep(600, 15)

    INV14_LOC = (773, 441, 785, 457)
    INV15_LOC = (821, 441, 839, 457)

    b.per.moveToBox(INV14_LOC, 'fast')
    b.per.click('left')
    t.randomSleep(400, 15)

    b.per.moveToBox(INV15_LOC, 'very_fast')
    b.per.click('left')
    t.randomSleep(500, 15)

    LONGBOW_LOC = (286, 530, 365, 584)
    b.per.moveToBox(LONGBOW_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(100, 15)

    chest_located = b.detection.colorRangeSearch(CHEST_COLOR_LOC, CHEST_CLR1, CHEST_CLR2)

    if(chest_located is False):
        print("Chest not located, quitting.")
        quit()

    t.randomSleep(16850, 125)

    b.per.moveToBox(CHEST_LOC, 'fast')
    b.per.click('left')
    t.randomSleep(1500, 15)

    INV1_LOC = (769, 307, 788, 323)

    b.per.moveToBox(INV1_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(500, 15)