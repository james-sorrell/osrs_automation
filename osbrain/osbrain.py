import util.windowHandler as wh
import util.peripheralHandler as ph
import util.config as c
import osbrain.detectionFunctions as df
import numpy as np
import  _thread
import keyboard

class OSBrain:
  def __init__(self, client="runelite"):
    keyboard.hook(self._killswitch)
    self.window = wh.WindowHandler(client)
    self.window.bringForward()
    x, y, _, _ = self.window.getWindowRect()
    self.per = ph.Peripherals(x, y)
    self.detection = df.DetectionHandler(self.window)
  
  def _killswitch(self, event):
    if(event.name == "ctrl"):
      self.per.keyUp(key='shift', delay='fast')
      _thread.interrupt_main()
    return

  def getInvLoc(self, location):
      x1, y1, x2, y2 = c.INV_LOC
      w = x2-x1
      h = y2-y1
      h_ = h//7
      w_ = w//4
      row = location%4
      col = location//4
      loc_x = x1+row*w_
      loc_y = y1+col*h_
      invSquare = (loc_x+c.CLK_BOX[0], loc_y+c.CLK_BOX[1],
                  loc_x+c.CLK_BOX[2], loc_y+c.CLK_BOX[3])
      return invSquare

  def dropInventory(self, pattern=None):
    patterns = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],
                [0,1,4,5,8,9,12,13,16,17,20,21,24,25,2,3,6,7,10,11,14,15,18,19,22,23,26,27],
                [0,1,2,3,7,6,5,4,8,9,10,11,15,14,13,12,16,17,18,19,23,22,21,20,24,25,26,27]]

    if pattern is None:
      pattern = patterns[np.random.randint(len(patterns))]

    self.per.keyDown('shift', 'fast')
    for location in pattern:
      invSquare = getInvLoc(location)
      self.per.moveToBox(invSquare, 'fast')
      self.per.click(delay='very_fast')
    self.per.keyUp(key='shift', delay='fast')

    # We need to hold down shift
    # Then we move the mouse to each index
    # Then we click
