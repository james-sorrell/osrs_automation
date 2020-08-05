from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

CW_CHEST_LOC = [245, 250, 265, 270]
CHEST_CLR = [72, 65, 65]
CHEST_LOC = [245, 270, 270, 290]

VIAL_LOC = [85, 120, 95, 130]
GUAM_LOC = [135, 160, 140, 165]
SPELL_LOC = [560, 350, 565, 355]


weed = int(input('How many guam?\n'))
loops = weed//13
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

def getVial():
    b.per.moveToBox(VIAL_LOC, 'very_fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(50, 5)
    # inv = b.detection.getInventoryStatus()
    # print(inv)
    # while not (inv[1] and inv[2] and inv[3]):
    #     print("Getting seaweed")
    #     b.per.moveToBox(SEAWEED_LOC)
    #     t.randomSleep(150, 50)
    #     b.per.click('left')
    #     inv = b.detection.getInventoryStatus()


def getGuam():
    b.per.moveToBox(GUAM_LOC, 'very_fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(1000, 50)
    b.per.press('esc')
    while(b.detection.isBankOpen() is True):
        print("Waiting for bank to close...")
    print("Bank Closed.")
    t.randomSleep(75, 5)

def makePotions():
    LOC = b.getInvLoc(12)
    b.per.moveToBox(LOC, 'very_fast')
    t.randomSleep(50, 5)
    b.per.click('left')
    LOC = b.getInvLoc(13)
    b.per.moveToBox(LOC, 'very_fast')
    t.randomSleep(50, 5)
    b.per.click('left')
    t.randomSleep(800,50)
    b.per.press('1')
    t.randomSleep(7650, 200)

def bankPotions():
    b.per.moveToBox(CHEST_LOC, 'very_fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    cntr = 0
    while(b.detection.isBankOpen() is False):
        print("Waiting for bank to open...")
        cntr += 1
        if cntr == 1000:
            cntr = 0
            b.per.moveToBox(CHEST_LOC, 'very_fast')
            t.randomSleep(150, 50)
            b.per.click('left')
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
    b.per.moveToBox(DEPOSIT_ALL, 'very_fast')
    t.randomSleep(150, 50)
    b.per.click('left')
    t.randomSleep(450, 50)

while(loops > 0):
    # while(True):
    if (b.detection.isBankOpen() is False):
        valid_location = b.detection.colorSearch(CW_CHEST_LOC, CHEST_CLR)
        print("Correct location: {}".format(valid_location))
        if valid_location is False:
            quit()
        b.per.moveToBox(CHEST_LOC, 'very_fast')
        t.randomSleep(150, 50)
        b.per.click('left')
    while(b.detection.isBankOpen() is False):
        print("Waiting for bank to open...")
    print("Bank Open.")
    getVial()
    getGuam()
    makePotions()
    bankPotions()
    loops -= 1