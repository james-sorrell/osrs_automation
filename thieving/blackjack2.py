from osbrain.osbrain import OSBrain
import util.timingHelpers as th
import util.config as c

import numpy as np
import matplotlib.pyplot as plt

c.VERBOSITY = 0

CHECK_LOC = (116, 474, 133, 478)
BANDIT_LOC = (364, 219, 369, 222)
b = OSBrain()

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

def _checkStatus(im):
  fail = np.load("data/blackjack/fail.npy")
  fail_fail = np.load("data/blackjack/fail-fail.npy")
  fail_succ = np.load("data/blackjack/fail-succ.npy")
  succ = np.load("data/blackjack/succ.npy")
  if (np.array_equal(fail, im)):
    return "fail"
  if (np.array_equal(succ, im)):
    return "succ"
  if (np.array_equal(fail_fail, im)):
    return "fail_fail"
  if (np.array_equal(fail_succ, im)):
    return "fail_succ"
  return None

for _ in range(5):

  b.per.moveToBox(BANDIT_LOC, 'fast')
  b.per.click('right', 'fast')

  KNKOUT_LOC = _getKnockoutLocation()
  b.per.moveToBox(KNKOUT_LOC, 'fast')
  b.per.click('left', 'fast')

  b.per.moveToBox(BANDIT_LOC, 'fast')
  b.per.click('right', 'fast')

  PCKPKT_LOC = _getPickpocketLocation()
  b.per.moveToBox(PCKPKT_LOC, 'fast')
  b.per.click('left', 'fast')

  # If successful knockout
  im = b.window.getImage(CHECK_LOC)
  im = np.mean(np.array(im), axis=2)
  status = _checkStatus(im)
  print("Status after first pick: {}".format(status))

  if (status == "succ"):
    b.per.moveToBox(BANDIT_LOC, 'very_fast')
    b.per.click('right', 'fast')
    PCKPKT_LOC = _getPickpocketLocation()
    b.per.moveToBox(PCKPKT_LOC, 'fast')
    b.per.click('left', 'fast')

  if (status == "fail"):
    while (True):
      th.random_sleep_ms(100, 10)
      im = b.window.getImage(CHECK_LOC)
      im = np.mean(np.array(im), axis=2)
      status = _checkStatus(im)
      print("\tLooped status: {}".format(status))
      if (status == "fail_fail"):
        th.random_sleep_ms(3500, 25)
        break
      if (status == "fail_succ"):
        break