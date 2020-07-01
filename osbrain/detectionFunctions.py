import numpy as np
import util.config as c
import matplotlib.pyplot as plt

class DetectionHandler:
  def __init__(self, window):
    self.window = window

  def getInventoryStatus(self):
    """ 
    Return status of current inventory
    1 = FULL
    0 = EMPTY
    Returns: Boolean Array length 28 
    """
    im = self.window.getImage(c.INV_LOC)
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
        plt.imshow(im[i:i+h_, j:j+w_])
        plt.show()
        if np.array_equal(empty_inv[i:i+h_, j:j+w_], im[i:i+h_, j:j+w_]) is False:
          inv_status[index] = True
        index += 1
    return inv_status
  
  def isInventoryFull(self):
    inv_status = self.getInventoryStatus()
    inv_full = all(inv_status)
    if (inv_full):
      c.debugPrint("DetectionHandler: Inventory Full", c.DEBUG)
    else:
      c.debugPrint("DetectionHandler: Inventory not Full", c.DEBUG)
    return inv_full

  def colorSearch(self, loc, tar):
    c.debugPrint("DetectionHandler: Searching for C{} in L{}".format(tar, loc), c.DEBUG)
    im = self.window.getImage(loc)
    h, w = im.size
    for i in range(h):
      for j in range(w):
        clr = im.getpixel((i, j))
        if all([ c1 == c2 for c1, c2 in zip(clr, tar)]):
          c.debugPrint("\tDetectionHandler: Found.", c.DEBUG)
          return True
    c.debugPrint("\tDetectionHandler: Did not find.", c.DEBUG)
    return False