import random
from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

from tqdm import trange
import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

CW_CHEST_LOC = [245, 250, 265, 270]
CHEST_CLR = [72, 65, 65]
CHEST_LOC = [245, 270, 270, 290]

HIDES_LOC = [280, 265, 290, 275]
SPELL_LOC = [605, 350, 610, 355]

hides = int(input('How many hides?\n'))
loops = hides//25
print("{} loops.".format(loops))

b = OSBrain()

def getHides():
    b.per.moveToBox(HIDES_LOC, 'very_fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(50, 5)
    b.per.press('esc')
    while(b.detection.isBankOpen() is True):
        c.debugPrint("Waiting for bank to close...", 1)
    c.debugPrint("Bank Closed.", 1)
    t.randomSleep(200,25)
    # inv = b.detection.getInventoryStatus()
    # print(inv)
    # while not (inv[1] and inv[2] and inv[3]):
    #     print("Getting seaweed")
    #     b.per.moveToBox(SEAWEED_LOC)
    #     t.randomSleep(150, 50)
    #     b.per.click('left')
    #     inv = b.detection.getInventoryStatus()

def castSpell(count):
    # Chance to move to spell location anyway
    eps1 = 0.1
    if count==0 or random.random() < eps1:
        b.per.press('f4')
        b.per.moveToBox(SPELL_LOC, 'very_fast')
    t.randomSleep(50, 5)
    b.per.click('left')
    # Chance to double click
    eps2 = 0.2
    if (random.random() < eps2):
        t.randomSleep(50, 25)
        b.per.click('left')

def bankHides():
    b.per.press('f3')
    b.per.moveToBox(CHEST_LOC, 'very_fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    cntr = 0
    while(b.detection.isBankOpen() is False):
        c.debugPrint("Waiting for bank to open...", 2)
        cntr += 1
        if cntr == 1000:
            cntr = 0
            b.per.moveToBox(CHEST_LOC, 'very_fast')
            t.randomSleep(150, 50)
            b.per.click('left')
    c.debugPrint("Bank Open.", 1)
    # LOC = b.getInvLoc(1)
    # b.per.moveToBox(LOC)
    t.randomSleep(300, 50)
    # b.per.click('right')
    # x, y = b.per.mousePosition()
    # BANK_ALL_LOC = [x-2, y+101, x+2, y+103] 
    # b.per.moveToBox(BANK_ALL_LOC, 'fast')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(1000, 50)
    DEPOSIT_ALL = [440, 335, 450, 345]
    b.per.moveToBox(DEPOSIT_ALL, 'very_fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(450, 50)


valid_location = b.detection.colorSearch(CW_CHEST_LOC, CHEST_CLR)
c.debugPrint("Correct location: {}".format(valid_location), 1)
if valid_location is False:
    quit()
b.per.moveToBox(CHEST_LOC, 'very_fast')
t.randomSleep(150, 50)
b.per.click('left')
while(b.detection.isBankOpen() is False):
    c.debugPrint("Waiting for bank to open...", 2)
c.debugPrint("Bank Open.", 1)

for _ in trange(loops):
    # while(True):
    getHides()
    valid_location = b.detection.colorSearch(CW_CHEST_LOC, CHEST_CLR)
    c.debugPrint("Correct location: {}".format(valid_location), 1)
    if valid_location is False:
        quit()
    for count in range(5):
        castSpell(count)
        t.randomSleep(1515, 40)
    bankHides()
    # Chance to move mouse away
    eps = 0.0005
    if (random.random() < eps):
        c.debugPrint("Randomly moving mouse somewhere.", 1)
        b.per.moveToBox([0, 0, 2000, 2000])
        t.randomSleep(4000, 3000)