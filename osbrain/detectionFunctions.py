import numpy as np
import util.config as c
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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
  
  def isBankOpen(self):
    im =  np.array(self.window.getImage(c.BANK_CHECK_LOC))
    empty_inv = np.load("data/bank_check.npy")
    if np.array_equal(im, empty_inv) is False:
      return False
    return True

  def isInventoryFull(self):
    inv_status = self.getInventoryStatus()
    inv_full = all(inv_status)
    if (inv_full):
      c.debugPrint("DetectionHandler: Inventory Full", c.DEBUG)
    else:
      c.debugPrint("DetectionHandler: Inventory not Full", c.DEBUG)
    return inv_full

  def _iterateImage(self, im):
    w, h = im.size
    for i in range(h):
      for j in range(w):
        yield(im.getpixel((j,i)), i, j)

  def colorSearch(self, loc, tar, tar2=None):
    if tar2 is None:
      return self.singleColorSearch(loc, tar)
    return self.colorRangeSearch(loc, tar, tar2)

  def _getColorLimits(self, tar1, tar2):
    c1L = min(tar1[0], tar2[0])
    c1H = max(tar1[0], tar2[0])
    c2L = min(tar1[1], tar2[1])
    c2H = max(tar1[1], tar2[1])
    c3L = min(tar1[2], tar2[2])
    c3H = max(tar1[2], tar2[2])
    return c1L, c1H, c2L, c2H, c3L, c3H

  def singleColorSearch(self, loc, tar):
    c.debugPrint("DetectionHandler: Searching for C{} in L{}".format(tar, loc), c.DEBUG)
    im = self.window.getImage(loc)
    for clr, i, j in self._iterateImage(im):
      if all([ c1 == c2 for c1, c2 in zip(clr, tar)]):
        c.debugPrint("\tDetectionHandler: Color Found.", c.DEBUG)
        return True
    c.debugPrint("\tDetectionHandler: Did not find.", c.DEBUG)
    return False

  def colorRangeSearch(self, loc, tar1, tar2):
    c.debugPrint("DetectionHandler: Searching from C{}:C{} in L{}".format(tar1, tar2, loc), c.DEBUG)
    im = self.window.getImage(loc)
    c1L, c1H, c2L, c2H, c3L, c3H = self._getColorLimits(tar1, tar2)
    for clr, i, j in self._iterateImage(im):
      if ((c1L <= clr[0] and clr[0] <= c1H) and
          (c2L <= clr[1] and clr[1] <= c2H) and
          (c3L <= clr[2] and clr[2] <= c3H)):
        c.debugPrint("\tDetectionHandler: Color Range Found.", c.DEBUG)
        return True
    c.debugPrint("\tDetectionHandler: Did not find.", c.DEBUG)
    return False

  def findClosestPoint(self, loc, tar1, tar2, reference_location, buffer=20):
    """ Gets an image and location "loc" and searches for the closest occurance 
    of a colour "tar" to the provided reference location """
    
    c.debugPrint("DetectionHandler: Searching for C{}:C{} in L{}".format(tar1, tar2, loc), c.DEBUG)
    im = self.window.getImage(loc)
    # w, h = im.size

    def _distance(x1, y1, x2, y2):
      return (abs(x2-x1)**2+abs(y2-y1)**2)

    dist = np.inf
    x, y = 0, 0

    for clr, i, j in self._iterateImage(im):
      c1L, c1H, c2L, c2H, c3L, c3H = self._getColorLimits(tar1, tar2)
      if ((c1L <= clr[0] and clr[0] <= c1H) and
          (c2L <= clr[1] and clr[1] <= c2H) and
          (c3L <= clr[2] and clr[2] <= c3H)):
        _dist = _distance(j, i, reference_location[0], reference_location[1])
        if _dist < dist:
          dist = _dist
          x, y = j, i

    if x == 0 and y == 0:
      return None, None

    # Add offset from original search location
    x += loc[0]
    y += loc[1]

    return x, y

  def checkColors(self, clr, tar, tar2=None):
    if tar2 is None:
      return all([ c1 == c2 for c1, c2 in zip(clr, tar)])
    c1L, c1H, c2L, c2H, c3L, c3H = self._getColorLimits(tar, tar2)
    return ((c1L <= clr[0] and clr[0] <= c1H) and
        (c2L <= clr[1] and clr[1] <= c2H) and
        (c3L <= clr[2] and clr[2] <= c3H))

  def findArea(self, loc, tar, tar2=None):
    c.debugPrint("DetectionHandler: Searching for C{} in L{}".format(tar, loc), c.DEBUG)
    im = self.window.getImage(loc)

    w, h = im.size

    locations = {}

    x1, y1, x2, y2 = np.inf, np.inf, 0, 0
    for clr, i, j in self._iterateImage(im):
      if self.checkColors(clr, tar, tar2):
        if (j < x1):
          x1 = j
        if (j > x2):
          x2 = j
        if (i < y1):
          y1 = i
        if (i > y2):
          y2 = i

    if (x1 == np.inf or y1 == np.inf
        or x2 == 0 or y2 ==0):
        return None

    #largestBox = [x1, y1, x2, y2]

    midX = (x1+x2)//2
    midY = (y2+y1)//2
    smallBox = [midX-1, midY-1, midX+1, midY+1]

    # figure, ax = plt.subplots(1)
    # ax.imshow(im)

    # width = largestBox[2] - largestBox[0]
    # height = largestBox[3] - largestBox[1]
    # rect = patches.Rectangle((largestBox[0],largestBox[1]),width,height, edgecolor='r', facecolor="none")
    # ax.add_patch(rect)

    # width = smallBox[2] - smallBox[0]
    # height = smallBox[3] - smallBox[1]
    # rect2 = patches.Rectangle((smallBox[0],smallBox[1]),width,height, edgecolor='r', facecolor="none")
    # ax.add_patch(rect2)

    # plt.show()

    # Add offset from original search location
    smallBox[0] += loc[0]
    smallBox[1] += loc[1]
    smallBox[2] += loc[0]
    smallBox[3] += loc[1]

    return smallBox