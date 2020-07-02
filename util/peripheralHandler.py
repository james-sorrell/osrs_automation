import time
import pyautogui as ph
import numpy as np
import mouse as mh
from util.humanMouse import move
import util.config as c

class Peripherals:
    def __init__(self, base_x, base_y):
        self.base_x = base_x
        self.base_y = base_y

    # def _sleep(self, delay):
    #     duration = self._getDuration(delay)
    #     c.debugPrint("\tPeripherals: Sleeping for {:.3f}s.".format(duration), c.MODERATE)
    #     time.sleep(duration)

    def _getDuration(self, speed):
        if speed is 'very_slow':
            return 2#np.random.uniform(2.35, 2.45)
        if speed is 'slow':
            return 1#np.random.uniform(0.95, 1.05)
        if speed is 'medium':
            return 0.5#np.random.uniform(0.55, 0.65)
        if speed is 'fast':
            return 0.2#np.random.uniform(0.2, 0.25)
        if speed is 'very_fast':
            return 0.1#np.random.uniform(0.05, 0.15)

    def mousePosition(self):
        x, y =  mh.get_position()
        return x-self.base_x, y-self.base_y

    def _moveToPoint(self, x, y, speed='fast'):
        duration = self._getDuration(speed)
        c.debugPrint("\tMouse: Moving to {},{}.".format(x, y), c.MODERATE)
        move(self.base_x+x, self.base_y+y, duration)

    def click(self, button='left', delay='fast'):
        c.debugPrint("\tMouse: Clicking.", c.MODERATE)
        mh.click(button)
        #self._sleep(delay)

    def moveToBox(self, loc, speed='fast'):
        c.debugPrint("Mouse: Moving {} to location {}.".format(speed, loc), c.MODERATE)
        x = np.random.randint(loc[0], loc[2])
        y = np.random.randint(loc[1], loc[3])
        self._moveToPoint(x, y, speed)

    def press(self, key, delay='fast'):
        c.debugPrint("\tKey: Press {}.".format(key), c.MODERATE)
        ph.press(key)
        #self._sleep(delay)

    def keyDown(self, key, delay='fast'):
        c.debugPrint("\tKey: Key Down {}.".format(key), c.MODERATE)
        ph.keyDown(key)
        #self._sleep(delay)

    def keyUp(self, key, delay='fast'):
        c.debugPrint("\tKey: Key Up {}.".format(key), c.MODERATE)
        ph.keyUp(key)
        #self._sleep(delay)