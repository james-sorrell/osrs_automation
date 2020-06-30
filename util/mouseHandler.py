import pyautogui as mh
import time
import scipy
from scipy import interpolate
import numpy as np

# Any duration less than this is rounded to 0.0 to instantly move the mouse.
mh.MINIMUM_DURATION = 0  # Default: 0.1
# Minimal number of seconds to sleep between mouse moves.
mh.MINIMUM_SLEEP = 0  # Default: 0.05
# The number of seconds to pause after EVERY public function call.
mh.PAUSE = 0  # Default: 0.1

class Mouse:

    def _getDuration(self, speed):
        if speed is 'slow':
            return np.random.uniform(1.95, 2.05)
        if speed is 'medium':
            return np.random.uniform(0.95, 1.05)
        if speed is 'fast':
            return np.random.uniform(0.45, 0.55)
        if speed is 'sanic':
            return np.random.uniform(0.20, 0.25)

    def _generateBezier(self, x2, y2):
        x1, y1 = mh.position()

        cp = np.random.randint(3, 5)  # Number of control points. Must be at least 2.
        # Distribute control points between start and destination evenly.
        x = scipy.linspace(x1, x2, num=cp, dtype='int')
        y = scipy.linspace(y1, y2, num=cp, dtype='int')

        # Randomise inner points a bit (+-RND at most).
        RND = 10
        xr = scipy.random.randint(-RND, RND, size=cp)
        yr = scipy.random.randint(-RND, RND, size=cp)
        xr[0] = yr[0] = xr[-1] = yr[-1] = 0
        x += xr
        y += yr

        # Approximate using Bezier spline.
        degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
                                          # Must be less than number of control points.
        tck, u = scipy.interpolate.splprep([x, y], k=degree)
        u = scipy.linspace(0, 1, num=max(mh.size()))
        points = scipy.interpolate.splev(u, tck)
        return points

    def moveToBox(self, x1, x2, y1, y2, speed='slow'):
        x = np.random.randint(x1, x2)
        y = np.random.randint(y1, y2)
        points = self._generateBezier(x, y)
        duration = self._getDuration(speed)
        timeout = duration/len(points[0])
        for point in zip(*(i.astype(int) for i in points)):
            _x, _y = point
            mh.moveTo(_x, _y)
            time.sleep(timeout)