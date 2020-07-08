import time
from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

bars = int(input('How many bars?\n'))
loops = bars//(27*2)
print("Making {} bars, {} loops.".format(bars, loops))
start = time.time()

b = OSBrain()

MAIN_SCRN = (12, 33, 513, 358)
DISP_SCRN = (12, 209, 513, 358)

DISPENSOR_CLR = (255, 0, 0)
DISPENSOR_CLR_RDY = (0, 255, 0)
CONVEYOR_CLR = (0, 255, 0)

CHEST_CLR = (255, 0, 255)
STABLE_LOC = (375, 40, 385, 50)
BANK_X = (487, 45, 494, 55)
DISP_BAR_LOC = (240, 430, 250, 440)
COAL_LOC = (425, 155, 435, 165)
MITH_LOC = (425, 120, 435, 130)
POT_LOC = (425, 195, 435, 205)
INV1_LOC = (575, 250, 585, 260)
INV2_LOC = (620, 250, 630, 260)
PLY_LOC = (262, 200)

def distance(x1, y1, x2, y2):
    return (abs(x2-x1)**2+abs(y2-y1)**2)

def findClosestCorner(loc):
    d1 = distance(PLY_LOC[0], PLY_LOC[1], loc[0], loc[1])
    d2 = distance(PLY_LOC[0], PLY_LOC[1], loc[0], loc[3])
    d3 = distance(PLY_LOC[0], PLY_LOC[1], loc[2], loc[1])
    d4 = distance(PLY_LOC[0], PLY_LOC[1], loc[2], loc[3])
    return min(d1, d2, d3, d4)

def getOre(ore):
    if ore == "coal":
        b.per.moveToBox(COAL_LOC, 'fast')
    elif ore == "mith":
        b.per.moveToBox(MITH_LOC, 'fast')
    t.randomSleep(20, 5)
    b.per.click('left')
    t.randomSleep(75, 5)
    b.per.press('escape')
    t.randomSleep(20, 5)
    # b.per.moveToBox(BANK_X, 'fast')
    # t.randomSleep(20, 5)
    # b.per.click('left')
    t.randomSleep(200, 15)

def fillBag():
    b.per.moveToBox(INV1_LOC, 'fast')
    t.randomSleep(20, 5)
    b.per.click('left')
    t.randomSleep(125, 15)

def clickOnChest(speed='medium'):
    CHEST_LOC = b.detection.findArea(MAIN_SCRN, CHEST_CLR)
    if CHEST_LOC is None:
        print("Did not find chest: FATAL Exit")
        quit()
    b.per.moveToBox(CHEST_LOC, speed)
    t.randomSleep(25, 5)
    b.per.click('left')
    b.per.moveToBox(INV2_LOC, speed)
    dist = findClosestCorner(CHEST_LOC)
    failsafe = 0
    while (dist > 1000):
        t.randomSleep(1000, 1)
        print("\tDistance to chest: {}".format(dist))
        CHEST_LOC = b.detection.findArea(MAIN_SCRN, CHEST_CLR)
        if CHEST_LOC is None:
            print("Did not find chest in loop")
            break
        dist = findClosestCorner(CHEST_LOC)
        failsafe += 1
        if (failsafe >= 100):
            quit()
    chest_sleep = (dist//10)+250
    print("ARRIVED CHEST - Buffer sleep: {}".format(chest_sleep))
    t.randomSleep(chest_sleep, 15)

def clickOnConveyor():
    CONV_LOC = b.detection.findArea(MAIN_SCRN, CONVEYOR_CLR)
    if CONV_LOC is None:
        print("Did not find conveyor: FATAL Exit")
        quit()
    b.per.moveToBox(CONV_LOC, 'medium')
    t.randomSleep(25, 5)
    b.per.click('left')
    b.per.moveToBox(INV1_LOC, 'medium')
    dist = findClosestCorner(CONV_LOC)
    failsafe = 0
    while (dist > 1000):
        t.randomSleep(1000, 1)
        print("\tDistance to conveyor: {}".format(dist))
        CONV_LOC = b.detection.findArea(MAIN_SCRN, CONVEYOR_CLR)
        if CONV_LOC is None:
            print("Did not find conveyor in loop")
            break
        dist = findClosestCorner(CONV_LOC)
        failsafe += 1
        if (failsafe >= 100):
            quit()
    conveyor_sleep = (dist//15)+250
    print("ARRIVED CONVEYOR - Buffer sleep: {}".format(conveyor_sleep))
    t.randomSleep(conveyor_sleep, 15)

def clickOnDispensor():
    DISP_LOC = b.detection.findArea(DISP_SCRN, DISPENSOR_CLR_RDY)
    if DISP_LOC is None:
        DISP_LOC = b.detection.findArea(DISP_SCRN, DISPENSOR_CLR)
    if DISP_LOC is None:
        DISP_LOC = b.detection.findArea(DISP_SCRN, DISPENSOR_CLR_RDY)
    if DISP_LOC is None:
        print("Did not find dispensor: FATAL Exit")
        quit()
    DISP_LOC[0] -= 20
    DISP_LOC[2] -= 20
    b.per.moveToBox(DISP_LOC, 'medium')
    t.randomSleep(20, 5)
    b.per.click('left')
    b.per.moveToBox(INV1_LOC, 'medium')
    dist = findClosestCorner(DISP_LOC)
    failsafe = 0
    while (dist > 1000):
        t.randomSleep(1000, 1)
        print("\tDistance to dispensor: {}".format(dist))
        DISP_LOC = b.detection.findArea(DISP_SCRN, DISPENSOR_CLR_RDY)
        if DISP_LOC is None:
            DISP_LOC = b.detection.findArea(DISP_SCRN, DISPENSOR_CLR)
        if DISP_LOC is None:
            DISP_LOC = b.detection.findArea(DISP_SCRN, DISPENSOR_CLR_RDY)
        if DISP_LOC is None:
            print("Did not find dispensor in loop")
            break
        dist = findClosestCorner(DISP_LOC)
        failsafe += 1
        if (failsafe >= 100):
            quit()
    SLEEP = (dist//15)+250
    print("ARRIVED DISPENSOR - Buffer sleep: {}".format(SLEEP))
    t.randomSleep(SLEEP, 15)

def getBarsFromDispensor():
    while b.detection.isInventoryFull() is False:
        DISP_LOC = None
        while DISP_LOC is None:
            print("Waiting for bars to be ready...")
            DISP_LOC = b.detection.findArea(DISP_SCRN, DISPENSOR_CLR_RDY)
            t.randomSleep(100, 1)
        t.randomSleep(20, 1)
        print("Bars ready!")
        b.per.moveToBox(DISP_LOC, 'fast')
        t.randomSleep(20, 5)
        b.per.click('left')
        t.randomSleep(275, 1)
        b.per.moveToBox(DISP_BAR_LOC, 'fast')
        t.randomSleep(20, 5)
        b.per.click('left')
        t.randomSleep(700, 15)

def emptyLootingBag():
    b.per.moveToBox(INV1_LOC, 'fast')
    t.randomSleep(20, 5)
    # b.per.click('right')
    # x, y = b.per.mousePosition()
    # EMPTY_LOC = [x-1, y+86, x+1, y+88] 
    # b.per.moveToBox(EMPTY_LOC, 'fast')
    # t.randomSleep(20, 5)
    # b.per.click('left')
    b.per.keyDown('shiftleft')
    t.randomSleep(20, 5)
    b.per.click('left')
    t.randomSleep(75, 5)
    #t.randomSleep(125, 15)

def drinkStaminaPotion():
    b.per.moveToBox(POT_LOC, 'fast')
    t.randomSleep(20, 5)
    b.per.click('right')
    t.randomSleep(20, 5)
    x, y = b.per.mousePosition()
    WD1_LOC = [x-1, y+41, x+1, y+43] 
    b.per.moveToBox(WD1_LOC, 'fast')
    t.randomSleep(20, 5)
    b.per.click('left')
    t.randomSleep(20, 5)
    b.per.press('escape')
    t.randomSleep(50, 5)
    b.per.moveToBox(INV2_LOC, 'fast')
    t.randomSleep(20, 5)
    b.per.click('left')
    t.randomSleep(125, 15)

def checkEnergyLow():
    no_energy_clr = (19, 19, 19)
    clr = b.window.getPixel(565, 143)
    if all([ c1 == c2 for c1, c2 in zip(clr, no_energy_clr)]):
        return True
    return False

def bankBars():
    b.per.moveToBox(INV2_LOC, 'medium')
    t.randomSleep(20, 5)
    b.per.click('left')
    t.randomSleep(20, 5)
    b.per.press('escape')
    t.randomSleep(20, 5)
    b.per.click('left')
    t.randomSleep(125, 15)

energyLow = False

while(loops > 0):

    print("Rotation One")
    clickOnChest()
    getOre("coal")
    fillBag()
    clickOnChest('fast')
    getOre("coal")
    clickOnConveyor()
    emptyLootingBag()
    clickOnConveyor()
    energyLow = checkEnergyLow()

    print("Energy Low: {}".format(energyLow))
    if energyLow is True:
        clickOnChest()
        drinkStaminaPotion()

    print("Rotation Two")
    clickOnChest()
    getOre("coal")
    fillBag()
    clickOnChest('fast')
    getOre("mith")
    clickOnConveyor()
    emptyLootingBag()
    clickOnConveyor()
    clickOnDispensor()
    getBarsFromDispensor()
    clickOnChest()
    bankBars()
    energyLow = checkEnergyLow()

    print("Energy Low: {}".format(energyLow))
    if energyLow is True:
        clickOnChest()
        drinkStaminaPotion()

    print("Rotation Three")
    clickOnChest()
    getOre("coal")
    fillBag()
    clickOnChest('fast')
    getOre("mith")
    clickOnConveyor()
    emptyLootingBag()
    clickOnConveyor()
    clickOnDispensor()
    getBarsFromDispensor()
    clickOnChest()
    bankBars()
    energyLow = checkEnergyLow()

    print("Energy Low: {}".format(energyLow))
    if energyLow is True:
        clickOnChest()
        drinkStaminaPotion()
