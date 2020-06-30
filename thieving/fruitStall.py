import util.windowHandler as wh
import util.mouseHandler as mh

import numpy as np

window = wh.WindowHandler("runelite")
window.bringForward()
x, y, _, _ = window.getWindowRect()

mouse = mh.Mouse(x, y)
#mouse.moveToBox(350, 380, 145, 180, 'fast')

window.getImage()

# for i in range(3):
#   mouse.click()
#   mouse._sleep('slow')
#   mouse._sleep('slow')

555, 231
736, 491