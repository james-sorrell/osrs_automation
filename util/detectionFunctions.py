import numpy as np
import util.config as c
import matplotlib.pyplot as plt

def getInventoryStatus(window):
  """ 
  Return status of current inventory
  1 = FULL
  0 = EMPTY
  Returns: Boolean Array length 28 
  """
  im = window.getImage(c.INV_LOC)
  im = np.mean(np.array(im), axis=2)
  empty_inv = np.load("data/inv.npy")
  h, w = im.shape
  currn_inv = np.array(im)
  # 28 items in inventory
  h_ = h//7
  w_ = w//4
  index = 0
  inv_status = np.zeros(28, dtype=bool)
  for i in range(0,h,h_):
    for j in range(0,w,w_):
      if np.array_equal(empty_inv[i:i+h_, j:j+w_], im[i:i+h_, j:j+w_]) is False:
        inv_status[index] = True
      index += 1
  return inv_status

def colorSearch(window, loc, tar):
  im = window.getImage(loc)
  h, w = im.size
  for i in range(h):
    for j in range(w):
      clr = im.getpixel((i, j))
      if all([ c1 == c2 for c1, c2 in zip(clr, tar)]):
        return True
  return False