import win32gui, win32ui, win32con
import numpy as np
import cv2


class WindowCapture:

    w = 0
    h = 0
    hwnd = None
    cropped_x = 250
    cropped_y = 300
    offset_x = 0
    offset_y = 0
    cutting_x = 500
    cutting_y = 400

    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0] - self.cutting_x
        self.h = window_rect[3] - window_rect[1] - self.cutting_y

        border_pixels = 7
        titlebar_pixels = 300
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels + 1

        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):

        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = cv2.Canny(img,100,200)

        return img
