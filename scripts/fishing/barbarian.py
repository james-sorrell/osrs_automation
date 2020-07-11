from osbrain.osbrain import OSBrain
import util.timingHelpers as t
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

MAIN_SCRN = (12, 33, 513, 358)
FISH_CLR1 = (100, 0, 100)
FISH_CLR2 = (255, 0, 255)
PLY_LOC = (262, 200)

b = OSBrain()

w = MAIN_SCRN[2] - MAIN_SCRN[0]
h = MAIN_SCRN[3] - MAIN_SCRN[1]


for y in range(0, y-20, 15):
    for x in range(0, w-20, 15):
         b.detection.findArea(MAIN_SCRN, FISH_CLR1, FISH_CLR2, PLY_LOC)

FISH_LOC = b.detection.findClosestPoint(MAIN_SCRN, FISH_CLR1, FISH_CLR2, PLY_LOC)

b.per._moveToPoint(FISH_LOC[0], FISH_LOC[1], speed='fast')