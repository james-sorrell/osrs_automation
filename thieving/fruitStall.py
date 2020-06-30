import util.windowHandler as wh
import util.mouseHandler as mh

import numpy as np

hndl = wh.getWindow('runelite')
wh.bringForward(hndl)

mouse = mh.Mouse()
mouse.moveToBox(495, 505, 495, 505, 'slow')