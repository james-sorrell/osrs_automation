from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

logs = input('How many logs?\n')
loop = int(logs)//27
print("Looping {} times.".format(loop))

b = OSBrain()

CHEST_LOC = (296, 152, 330, 161)
CHEST_COLOR_LOC = (249, 86, 389, 215)
b.per.moveToBox(CHEST_LOC, 'medium')
b.per.click('left')
t.randomSleep(500, 15)

CHEST_CLR1 = (90, 60, 50)
CHEST_CLR2 = (50, 20, 10)

for _ in trange(loop):

    LOGS_LOC = (104, 150, 123, 168)

    b.per.moveToBox(LOGS_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(200, 15)

    BANK_X = (607, 55, 616, 70)

    b.per.moveToBox(BANK_X, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    KNIFE_LOC = (714, 307, 731, 323)
    INV_LOC = (769, 307, 788, 323)

    b.per.moveToBox(KNIFE_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)

    b.per.moveToBox(INV_LOC, 'fast')
    b.per.click('left')
    t.randomSleep(450, 15)

    LONGBOW_LOC = (286, 530, 365, 584)
    b.per.moveToBox(LONGBOW_LOC, 'medium')
    t.randomSleep(200, 15)
    b.per.click('left')
    t.randomSleep(120, 15)

    chest_located = b.detection.colorRangeSearch(CHEST_COLOR_LOC, CHEST_CLR1, CHEST_CLR2)

    if(chest_located is False):
        print("Chest not located, quitting.")
        quit()

    t.randomSleep(48500, 400)

    b.per.moveToBox(CHEST_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(500, 15)

    b.per.moveToBox(INV_LOC, 'medium')
    b.per.click('left')
    t.randomSleep(160, 15)