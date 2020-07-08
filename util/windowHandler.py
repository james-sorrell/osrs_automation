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
        if not isinstance(title, str):
            print("WindowHandler -> getWindow: Title needs to be string!")
            quit()
        def windowHandler(hwnd, windows):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))
            
        windows = []
        win32gui.EnumWindows(windowHandler, windows)
        for win in windows:
            if title.lower() in win[1].lower():
                c.debugPrint("Found Window: {}".format(win), c.MODERATE)
                self.hwnd = win[0]
                self.title = win[1].lower()

    def getPixel(self, x, y):
        rect = win32gui.GetWindowRect(self.hwnd)
        w = abs(rect[2] - rect[0])
        h = abs(rect[3] - rect[1])
        hwndDC = win32gui.GetWindowDC(self.hwnd)
        mfcDC = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()
        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)

        # This should have worked
        # ret=win32gui.GetPixel(hwndDC, 400, 100)

        result = windll.user32.PrintWindow(self.hwnd, saveDC.GetSafeHdc(), 0)
        c.debugPrint("getImage: PrintWindow Result {}".format(result), c.DEBUG)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)

        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
        r, g, b = im.getpixel((x, y))

        # Cleanup
        mfcDC.DeleteDC()
        saveDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwndDC)
        win32gui.DeleteObject(saveBitMap.GetHandle())
        return (r, g, b)

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
        c.debugPrint("getImage: PrintWindow Result {}".format(result), c.DEBUG)
        bmpinfo = saveBitMap.GetInfo()
        bmpstr = saveBitMap.GetBitmapBits(True)
        
        im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
        im = im.crop(location)

        #hwndDC.DeleteDC()
        mfcDC.DeleteDC()
        saveDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, hwndDC)
        win32gui.DeleteObject(saveBitMap.GetHandle())

        return im

    def getWindowRect(self):
        return win32gui.GetWindowRect(self.hwnd)

    def bringForward(self):
        win32gui.ShowWindow(self.hwnd, 5)
        win32gui.SetForegroundWindow(self.hwnd)