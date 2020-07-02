import time
import numpy as np
import util.config as c

def random_sleep_ms(duration, delta):
  """ 
  Time to sleep and an error around that time
  specified in milliseconds
  """
  duration_s = duration/1000
  time_s = np.random.uniform(duration_s, delta/1000)
  c.debugPrint("TimingHelpers: Sleeping for {:.3f}s.".format(time_s), c.DEBUG)
  time.sleep(time_s)

def timedFunction(duration, function, *args):
  duration_s = duration/1000
  duration_s = duration_s//100
  for _ in range(100):
    res = function(*args)
    if res is True:
      return res
    time.sleep(duration_s)
  return False