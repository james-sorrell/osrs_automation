from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

CW_CHEST_LOC = [245, 250, 265, 270]
CHEST_CLR = [72, 65, 65]
CHEST_LOC = [245, 270, 270, 290]

SEAWEED_LOC = [90, 125, 95, 130]
SAND_LOC = [135, 125, 140, 130]
SPELL_LOC = [560, 350, 565, 355]


weed = int(input('How many seaweed?\n'))
loops = weed//3
print("{} loops.".format(loops))

b = OSBrain()

# def _clickOnPotion():
#     inv = b.detection.getInventoryStatus()
#     for i in range(27):
#         print(inv[i+1])
#         if inv[i+1] == True:
#             print("Clicking on {}".format(i+1))
#             loc = b.getInvLoc(i+1)
#             b.per.moveToBox(loc, 'fast')
#             t.randomSleep(150, 50)
#             b.per.click('left')
#             t.randomSleep(2000, 800)
#             return

def getSeaweed():
    b.per.moveToBox(SEAWEED_LOC)
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(150, 50)
    b.per.click('left')
    # t.randomSleep(1000, 50)
    # inv = b.detection.getInventoryStatus()
    # print(inv)
    # while not (inv[1] and inv[2] and inv[3]):
    #     print("Getting seaweed")
    #     b.per.moveToBox(SEAWEED_LOC)
    #     t.randomSleep(150, 50)
    #     b.per.click('left')
    #     inv = b.detection.getInventoryStatus()


def getSand():
    b.per.moveToBox(SAND_LOC)
    t.randomSleep(150, 50)
    b.per.click('right')
    x, y = b.per.mousePosition()
    WIDTHRAW_X_LOC = [x-1, y+68, x+1, y+70] 
    b.per.moveToBox(WIDTHRAW_X_LOC, 'fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(1000, 50)
    b.per.press('esc')
    while(b.detection.isBankOpen() is True):
        print("Waiting for bank to close...")
    print("Bank Closed.")
    t.randomSleep(150, 50)

def castSpell():
    b.per.press('f4')
    b.per.moveToBox(SPELL_LOC)
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(3000, 50)

def bankGlass():
    b.per.press('f3')
    b.per.moveToBox(CHEST_LOC)
    t.randomSleep(150, 50)
    b.per.click('left')
    while(b.detection.isBankOpen() is False):
        print("Waiting for bank to open...")
    print("Bank Open.")
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
    b.per.moveToBox(DEPOSIT_ALL)
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(450, 50)
    b.per.press('esc')
    while(b.detection.isBankOpen() is True):
        print("Waiting for bank to close...")
    print("Bank Closed.")

def pickUpFloorGlass():
    TEXT_LOC = [190, 190, 205, 215]
    TEXT_CLR = [255, 255, 255]
    bankLater = False
    item_on_floor = b.detection.colorSearch(TEXT_LOC, TEXT_CLR)
    if item_on_floor is True:
        bankLater = True
    while (item_on_floor):
        print("Item on floor: {}".format(item_on_floor))
        FLOOR = [270, 210, 275, 215]
        b.per.moveToBox(FLOOR)
        t.randomSleep(150, 50)
        b.per.click('left')
        t.randomSleep(300, 50)
        item_on_floor = b.detection.colorSearch(TEXT_LOC, TEXT_CLR)
    if bankLater is True:
        bankGlass()
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')
    # t.randomSleep(150, 50)
    # b.per.click('left')





while(loops > 0):
    # while(True):
    valid_location = b.detection.colorSearch(CW_CHEST_LOC, CHEST_CLR)
    print("Correct location: {}".format(valid_location))
    if valid_location is False:
        quit()
    b.per.moveToBox(CHEST_LOC)
    t.randomSleep(150, 50)
    b.per.click('left')
    while(b.detection.isBankOpen() is False):
        print("Waiting for bank to open...")
    print("Bank Open.")
    getSeaweed()
    getSand()
    castSpell()
    bankGlass()
    pickUpFloorGlass()
    loops -= 1