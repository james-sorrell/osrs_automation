import util.config as c
import win32gui

def getWindow(title, verbose=False):
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
            if c.VERBOSE >= 1:
                print("Found Window: {}".format(win))
            return win[0]

def bringForward(hwnd):
    win32gui.ShowWindow(hwnd, 5)
    win32gui.SetForegroundWindow(hwnd)