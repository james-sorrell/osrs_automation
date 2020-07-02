import numpy as np
import util.config as c
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2

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
          c.debugPrint("\tDetectionHandler: Color Found.", c.DEBUG)
          return True
    c.debugPrint("\tDetectionHandler: Did not find.", c.DEBUG)
    return False

  def _getColorLimits(self, tar1, tar2):
    c1L = min(tar1[0], tar2[0])
    c1H = max(tar1[0], tar2[0])
    c2L = min(tar1[1], tar2[1])
    c2H = max(tar1[1], tar2[1])
    c3L = min(tar1[2], tar2[2])
    c3H = max(tar1[2], tar2[2])
    return c1L, c1H, c2L, c2H, c3L, c3H

  def colorRangeSearch(self, loc, tar1, tar2):
    c.debugPrint("DetectionHandler: Searching from C{}:C{} in L{}".format(tar1, tar2, loc), c.DEBUG)
    im = self.window.getImage(loc)
    h, w = im.size
    c1L, c1H, c2L, c2H, c3L, c3H = self._getColorLimits(tar1, tar2)
    for i in range(h):
      for j in range(w):
        clr = im.getpixel((i, j))
        if ((c1L <= clr[0] and clr[0] <= c1H) and
            (c2L <= clr[1] and clr[1] <= c2H) and
            (c3L <= clr[2] and clr[2] <= c3H)):
          c.debugPrint("\tDetectionHandler: Color Range Found.", c.DEBUG)
          return True
    c.debugPrint("\tDetectionHandler: Did not find.", c.DEBUG)
    return False

  def findArea(self, loc, tar):
    c.debugPrint("DetectionHandler: Searching for C{} in L{}".format(tar, loc), c.DEBUG)
    im = self.window.getImage(loc)

    w, h = im.size

    locations = {}

    for i in range(h):
      for j in range(w):
        clr = im.getpixel((j, i))
        if all([ c1 == c2 for c1, c2 in zip(clr, tar)]):
          # Found
          if i in locations:
            locations[i].append(j)
          else:
            locations[i] = [j]

    largestArea = 0
    largestBox = None
    currBox = None
    currBoxArea = 0
    prevKey = None
    for key in locations:
      
      xPos = locations[key]
      if currBox:
        boxL = max(xPos[0], currBox[0])
        boxR = min(xPos[-1], currBox[2])
      else:
        boxL, boxR = xPos[0], xPos[-1]
      newBoxWidth = boxR - boxL

      if (prevKey is None):
        prevKey = key
        continue

      # Check if sequential locations
      if (abs(key-prevKey) < 2 and newBoxWidth > 5):
        if currBox is None:
          currBox = [xPos[0], prevKey, xPos[1], key]
        else:
          currBox[0] = max(xPos[0], currBox[0])
          currBox[2] = min(xPos[-1], currBox[2])
          currBox[3] = key
      else:
        if currBox is not None:
          currBoxArea = (currBox[2]-currBox[0])*(currBox[3]-currBox[1])
          if currBoxArea > largestArea:
            largestBox = currBox
            largestArea = currBoxArea
        currBox = None
        currBoxArea = None

      prevKey = key

    if largestBox is None:
      return None
    
    largestBox[0] += loc[0]
    largestBox[2] += loc[0]
    largestBox[1] += loc[1]
    largestBox[3] += loc[1]
    width = largestBox[2] - largestBox[0]
    height = largestBox[3] - largestBox[1]

    # figure, ax = plt.subplots(1)
    # ax.imshow(im)
    # rect = patches.Rectangle((largestBox[0],largestBox[1]),width,height, edgecolor='r', facecolor="none")
    # ax.add_patch(rect)
    # plt.show()
    # quit()

    return largestBox