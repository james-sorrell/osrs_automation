import time
import pyautogui as mh
import numpy as np
import util.config as c

class Mouse:
    def __init__(self, base_x, base_y):
        self.base_x = base_x
        self.base_y = base_y

    def _sleep(self, delay):
        duration = self._getDuration(delay)
        c.debugPrint("\tMouse: Sleeping for {}s.".format(duration), c.MODERATE)
        time.sleep(duration)

    def _getDuration(self, speed):
        if speed is 'slow':
            return np.random.uniform(2.45, 2.65)
        if speed is 'medium':
            return np.random.uniform(0.55, 0.85)
        if speed is 'fast':
            return np.random.uniform(0.2, 0.25)

    def _moveToPoint(self, x, y, speed='fast'):
        duration = self._getDuration(speed)
        c.debugPrint("\tMouse: Moving to {},{}.".format(x, y), c.MODERATE)
        mh.moveTo(self.base_x+x, self.base_y+y, duration)

    def click(self, delay='fast'):
        c.debugPrint("\tMouse: Clicking.", c.MODERATE)
        mh.click()
        self._sleep(delay)

    def moveToBox(self, loc, speed='fast'):
        c.debugPrint("Mouse: Moving {} to location {}.".format(speed, loc), c.MODERATE)
        x = np.random.randint(loc[0], loc[2])
        y = np.random.randint(loc[1], loc[3])
        self._moveToPoint(x, y, speed)