import time
import numpy as np
import util.config as c

def randomSleep(duration, delta):
  """ 
  Time to sleep and an error around that time
  specified in milliseconds
  """
  duration_s = duration/1000
  time_s = np.random.uniform(duration_s-delta/1000, duration_s+delta/1000)
  c.debugPrint("TimingHelpers: Sleeping for {:.3f}s.".format(time_s), c.MODERATE)
  time.sleep(time_s)

def loopedFunction(loops, function, *args):
  print("Start search")
  for _ in range(loops):
    res = function(*args)
    if res is True:
      print("Found")
      return res
  print("Finish search")
  return False