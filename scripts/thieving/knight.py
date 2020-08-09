import time
import random

from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

from PIL import ImageChops
import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 1

total_time = int(input('How long do you want this to run for? (Minutes)\n'))
print("Running for {} minutes.".format(total_time))

b = OSBrain()

start = time.time()
end = time.time()

KNIGHT_CLR1 = [0, 225, 225]
KNIGHT_CLR2 = [0, 255, 255]

MAIN_SCRN = (12, 33, 513, 358)

def checkHealthLow():
    health_clr = (148, 7, 3)
    clr = b.window.getPixel(559, 75)
    print(clr)
    if all([ c1 == c2 for c1, c2 in zip(clr, health_clr)]):
        return False
    return True

def eatFood():
    print("Healing...")
    inv = b.detection.getInventoryStatus()
    locs = np.asarray(np.where(inv))[0]
    if len(locs) <= 2:
        res = clickOnBank()
        while res is False:
            res = clickOnBank()
        getLobster()
    for idx in range(len(locs)):
        if locs[idx] == 0 or locs[idx] == 1:
            continue
        else:
            if locs[idx] < 27:
                if locs[idx+1] != locs[idx]+1:
                    # Drop it
                    b.dropInventory([locs[idx]])
                    continue
            inv_loc = b.getInvLoc(locs[idx])
            b.per.moveToBox(inv_loc)
            t.randomSleep(100, 50)
            b.per.click('left')
            return True

def distance(x1, y1, x2, y2):
    return (abs(x2-x1)**2+abs(y2-y1)**2)

def findClosestCorner(loc):
    PLY_LOC = (262, 200)
    d1 = distance(PLY_LOC[0], PLY_LOC[1], loc[0], loc[1])
    d2 = distance(PLY_LOC[0], PLY_LOC[1], loc[0], loc[3])
    d3 = distance(PLY_LOC[0], PLY_LOC[1], loc[2], loc[1])
    d4 = distance(PLY_LOC[0], PLY_LOC[1], loc[2], loc[3])
    return min(d1, d2, d3, d4)

def waitIdle():
    STABLE_LOC = (450, 200, 455, 205)
    stationary = False
    while(stationary == False):
        im1 = b.window.getImage(STABLE_LOC)
        t.randomSleep(200,25)
        im2 = b.window.getImage(STABLE_LOC)
        stationary = np.array_equal(np.array(im1), np.array(im2))
        print("Stationary: {}".format(stationary))
    print("Character is idle.")

def clickOnBank(speed='fast', move_mouse=True):
    CHEST_CLR = (255, 0, 255)
    INV2_LOC = (620, 250, 630, 260)
    CHEST_LOC = b.detection.findArea(MAIN_SCRN, CHEST_CLR)
    if CHEST_LOC is None:
        print("Did not find chest: FATAL Exit")
        quit()
    b.per.moveToBox(CHEST_LOC, speed)
    t.randomSleep(50, 5)
    b.per.click('left')
    if move_mouse is True:
        b.per.moveToBox(INV2_LOC, speed)
    dist = findClosestCorner(CHEST_LOC)
    failsafe = 0
    distNotChanged = 0
    prevDist = 0
    while (dist > 1000):
        t.randomSleep(1000, 1)
        print("\tDistance to chest: {}".format(dist))
        CHEST_LOC = b.detection.findArea(MAIN_SCRN, CHEST_CLR)
        if CHEST_LOC is None:
            print("Did not find chest in loop")
            break
        dist = findClosestCorner(CHEST_LOC)
        if (dist == prevDist):
            distNotChanged += 1
        else:
            distNotChanged == 0
        if (distNotChanged >= 2):
            return False
        prevDist = dist
        failsafe += 1
        if (failsafe >= 100):
            quit()
    if CHEST_LOC is None:
        chest_sleep = 200
    else:
        chest_sleep = (dist//3)+200
    print("ARRIVED CHEST - Buffer sleep: {}".format(chest_sleep))
    t.randomSleep(chest_sleep, 15)
    return True

def getLobster():
    while(b.detection.isBankOpen() is False):
        print("Waiting for bank to open...")
    print("Bank is open.")
    LOB_LOC = [85, 120, 95, 130]
    b.per.moveToBox(LOB_LOC, 'very_fast')
    t.randomSleep(100, 50)
    b.per.click('left')
    t.randomSleep(700, 200)
    b.per.press('esc')
    t.randomSleep(700, 200)
    if (b.detection.isInventoryFull() is False):
        print("ERROR: Inventory failed to fill - buy more food")
        quit()
    inv_loc = b.getInvLoc(1)
    b.per.moveToBox(inv_loc)
    t.randomSleep(100, 50)
    b.per.click('left')

def imagesAreSame(im1, im2):
    diff = ImageChops.difference(im1, im2)
    if diff.getbbox():
        return False
    return True

while( (end-start) < 60*total_time ):
    # Find the knight
    waitIdle()
    KLOC = b.detection.findArea(MAIN_SCRN, KNIGHT_CLR1, KNIGHT_CLR2)
    if KLOC is None:
        t.randomSleep(250,10)
        continue
    b.per.moveToBox(KLOC)
    b.per.click('left')
    #
    health_low = checkHealthLow()
    print("Health Low: {}".format(health_low))
    if health_low is True:
        result = eatFood()
        print("Food Eaten: {}".format(result))
    #
    eps = 0.05
    if (random.random() < eps):
        inv_loc = b.getInvLoc(1)
        b.per.moveToBox(inv_loc)
        t.randomSleep(100, 50)
        b.per.click('left')
    #
    eps2 = 0.0005
    if (random.random() < eps2):
        print("Randomly moving mouse somewhere.")
        b.per.moveToBox([0, 0, 2000, 2000])
        t.randomSleep(4000, 3000)
    #
    end = time.time()
    print("Minutes elapsed: {:.1f}".format((end-start)/60))

# #   b.per.moveToBox(PEAR_lOC, 'fast')
# #   while(b.detection.isInventoryFull() is False):
# #     if (b.detection.colorSearch(PEAR_lOC, PEAR_CLR)):
# #       # It gets two chances to try and see it
# #       b.per.click('left')
# #       fruitNotFoundCount = 0
# #     else:
# #       fruitNotFoundCount += 1
# #       print("Fruit not found count: {}".format(fruitNotFoundCount))
# #     if (fruitNotFoundCount >= 10):
# #       print("Safeguard exit.")
# #       quit()
# #     th.randomSleep(1100,100)
# #   th.randomSleep(100, 25)
# #   print("Inventory Full.")
# #   b.dropInventory()


