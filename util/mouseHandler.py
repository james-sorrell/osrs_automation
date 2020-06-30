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
        c.debugPrint("\tMouse: Sleeping for {}s.".format(duration), c.DEBUG)
        time.sleep(duration)

    def _getDuration(self, speed):
        if speed is 'slow':
            return np.random.uniform(2.45, 2.65)
        if speed is 'medium':
            return np.random.uniform(0.55, 0.85)
        if speed is 'fast':
            return np.random.uniform(0.2, 0.025)

    def _moveToPoint(self, x, y, speed='fast'):
        duration = self._getDuration(speed)
        c.debugPrint("\tMouse: Moving to {},{}.".format(x, y), c.DEBUG)
        mh.moveTo(self.base_x+x, self.base_y+y, duration)

    def click(self, delay='fast'):
        c.debugPrint("\tMouse: Clicking.", c.DEBUG)
        mh.click()
        self._sleep(delay)

    def moveToBox(self, x1, x2, y1, y2, speed='fast'):
        print("{},{} , {},{}".format(x1, x2, y1, y2))
        x = np.random.randint(x1, x2)
        y = np.random.randint(y1, y2)
        print("{}, {}".format(x, y))
        self._moveToPoint(x, y, speed)