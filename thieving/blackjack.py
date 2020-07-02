from osbrain.osbrain import OSBrain
import util.timingHelpers as th
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

MAIN_SCRN = (12, 33, 513, 358)
OUTLINE_CLR = (0, 0, 255)
BRDY_LOC = (149, 80, 370, 267)
BRD_CLR1 = (159, 143, 6)
BRD_CLR1 = (237, 215, 10)

def _getKnockoutLocation():
  x, y = b.per.mousePosition()
  y1 = y+87
  y2 = y+90
  x1 = x-5
  x2 = x+5
  return (x1, y1, x2, y2)

def _getPickpocketLocation():
  x, y = b.per.mousePosition()
  y1 = y+57
  y2 = y+60
  x1 = x-5
  x2 = x+5
  return (x1, y1, x2, y2)

def _clickBox(loc, click='left', move_delay='very_fast', click_delay='very_fast'):
  b.per.moveToBox(loc, move_delay)
  b.per.click(click, click_delay)

b = OSBrain()

BANDIT_LOC = b.detection.findArea(MAIN_SCRN, OUTLINE_CLR)
BANDIT_LOC = [BANDIT_LOC[0],BANDIT_LOC[1]+10,BANDIT_LOC[2],BANDIT_LOC[3]+10]

for _ in range(1):

  if BANDIT_LOC is None:
    quit()

  # RIGHT CLICK BANDIT
  b.per.moveToBox(BANDIT_LOC, 'fast')
  b.per.click('right', 'fast')
  KNKOUT_LOC = _getKnockoutLocation()
  b.per.moveToBox(KNKOUT_LOC, 'fast')
  b.per.click(click, 'fast')
  
  #_clickBox(KNKOUT_LOC, click_delay='very_fast')

  PCKPKT_LOC = _getPickpocketLocation()
  b.per.moveToBox(PCKPKT_LOC, 'fast')
