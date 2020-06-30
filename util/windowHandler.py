import util.config as c
import win32gui
import win32ui
from ctypes import windll
import matplotlib.pyplot as plt
from PIL import Image

class WindowHandler:
    def __init__(self, title):
        self.getWindow(title)

    def getWindow(self, title):
        """ 
        Function to get first window that contains title
        this function is case insensitive
        """
        print(type(title))
        if not isinstance(title, str):
            print("WindowHandler -> getWindow: Title needs to be string!")
            quit()
        def windowHandler(hwnd, windows):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))
            
        windows = []
        win32gui.EnumWindows(windowHandler, windows)
        for win in windows:
            if title.lower() in win[1].lower():
                if c.VERBOSE >= 1:
                    print("Found Window: {}".format(win))
                    self.hwnd = win[0]
                    self.title = win[1].lower()

    def getImage(self, location):
        c.debugPrint("WindowHandler: Getting image from {}".format(location), c.DEBUG)
        left, top, right, bot = self.getWindowRect()
        w = right - left
        h = bot - top

        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

        saveDC.SelectObject(saveBitMap)
        result = windll.user32.PrintWindow(self.hwnd, saveDC.GetSafeHdc(), 0)

        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        
        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
        im = im.crop(location)
        return im

    def getWindowRect(self):
        return win32gui.GetWindowRect(self.hwnd)

    def bringForward(self):
        win32gui.ShowWindow(self.hwnd, 5)
        win32gui.SetForegroundWindow(self.hwnd)