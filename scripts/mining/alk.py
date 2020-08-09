import time
import random
from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

total_time = int(input('How long do you want this to run for? (Minutes)\n'))
print("Running for {} minutes.".format(total_time))
start = time.time()

b = OSBrain("RuneLite")

failsafe = 0
end = time.time()

L_ORE = [155, 190, 200, 215]
M_ORE = [255, 280, 270, 300]
R_ORE = [335, 190, 360, 215]

ORE_CLR_L = [25, 10, 5]
ORE_CLR_H = [40, 25, 20]

L = b.detection.colorRangeSearch(L_ORE, ORE_CLR_L, ORE_CLR_H)
M = b.detection.colorRangeSearch(M_ORE, ORE_CLR_L, ORE_CLR_H)
R = b.detection.colorRangeSearch(R_ORE, ORE_CLR_L, ORE_CLR_H)

failSafe = 0

while( (end-start) < 60*total_time ):
    
    # Get Left Ore
    L = b.detection.colorRangeSearch(L_ORE, ORE_CLR_L, ORE_CLR_H)
    while L == True:
        print("L: {}".format(L))
        b.per.moveToBox(L_ORE, 'very_fast')
        t.randomSleep(180, 15)
        b.per.click('left')
        t.randomSleep(2400,200)
        L = b.detection.colorRangeSearch(L_ORE, ORE_CLR_L, ORE_CLR_H)
        failSafe += 1
        if failSafe == 100:
            quit()

    failSafe = 0

    # Get Middle Ore
    M = b.detection.colorRangeSearch(M_ORE, ORE_CLR_L, ORE_CLR_H)
    while M == True:
        print("M: {}".format(M))
        b.per.moveToBox(M_ORE, 'very_fast')
        t.randomSleep(180, 15)
        b.per.click('left')
        t.randomSleep(2100,200)
        M = b.detection.colorRangeSearch(M_ORE, ORE_CLR_L, ORE_CLR_H)
        failSafe += 1
        if failSafe == 100:
            quit()

    failSafe = 0

    # Get Right Ore
    R = b.detection.colorRangeSearch(R_ORE, ORE_CLR_L, ORE_CLR_H)
    while R == True:
        print("R: {}".format(R))
        b.per.moveToBox(R_ORE, 'very_fast')
        t.randomSleep(180, 15)
        b.per.click('left')
        t.randomSleep(2100,200)
        R = b.detection.colorRangeSearch(R_ORE, ORE_CLR_L, ORE_CLR_H)
        failSafe += 1
        if failSafe == 100:
            quit()

    failSafe = 0

    eps = 0.99
    if (random.random() < eps):
        print("Dropping Ore.")
        inv = b.detection.getInventoryStatus()
        loc = np.asarray(np.where(inv))[0]
        b.dropInventory(loc.tolist())

    eps2 = 0.005
    if (random.random() < eps2):
        print("Randomly moving mouse somewhere.")
        b.per.moveToBox([0, 0, 2000, 2000])
        t.randomSleep(4000, 3000)

    end = time.time()
    print("Minutes elapsed: {:.1f}".format((end-start)/60))