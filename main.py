import cv2 as cv
import time
import window_capture

for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

wincap = window_capture.WindowCapture('Roblox')
loop_time = time.time()

while True:

    screenshot = wincap.get_screenshot()
    cv.imshow('Computer Vision', screenshot)

    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

