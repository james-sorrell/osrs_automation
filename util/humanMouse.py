import mouse
import random
import scipy
import time
import numpy as np
from scipy import interpolate

def move(x2, y2, duration):
  cp = random.randint(3, 5)  # Number of control points. Must be at least 2.
  x1, y1 = mouse.get_position()
  # Distribute control points between start and destination evenly.
  x = scipy.linspace(x1, x2, num=cp, dtype='int')
  y = scipy.linspace(y1, y2, num=cp, dtype='int')

  dist = np.sqrt((x2-x1)**2+(y2-y1)**2)
  if (dist < 10):
    mouse.move(x2,y2)
    return

  # Randomise inner points a bit (+-RND at most).
  RND = np.sqrt(dist)/2
  RND = max(RND, 1)
  xr = scipy.random.randint(-RND, RND, size=cp)
  yr = scipy.random.randint(-RND, RND, size=cp)
  xr[0] = yr[0] = xr[-1] = yr[-1] = 0
  x += xr
  y += yr

  # Approximate using Bezier spline.
  degree = 3 if cp > 3 else cp - 1  # Degree of b-spline. 3 is recommended.
                                    # Must be less than number of control points.
  tck, u = scipy.interpolate.splprep([x, y], k=degree)
  u = scipy.linspace(0, 1, num=100)
  points = scipy.interpolate.splev(u, tck)

  # Move mouse.
  timeout = duration / len(points[0])
  for point in zip(*(i.astype(int) for i in points)):
    mouse.move(*point)
    time.sleep(timeout)