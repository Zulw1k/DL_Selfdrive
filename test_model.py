import cv2
import numpy as np
import time
import window_capture
import keras
from controls import PressKey, ReleaseKey
import getkeys

W = 0x11
A = 0x1E
D = 0x20


def move_straight():
    PressKey(W)
    ReleaseKey(D)
    ReleaseKey(A)


def move_right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)


def move_left():
    PressKey(A)
    ReleaseKey(D)
    ReleaseKey(W)


for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)


width = 200
height = 66
model = keras.models.load_model('Final_models/Roblox-drivesimulator-0.0001-nvidia-6-epochs.model')
wincap = window_capture.WindowCapture('Roblox')
loop_time = time.time()
paused = False

while True:
    if not paused:
        keys = getkeys.key_check()
        screenshot = wincap.get_screenshot()
        screenshot = cv2.resize(screenshot, (200, 66))
        prediction = model.predict([screenshot.reshape(-1, width, height, 1)])[0]
        moves = list(np.around(prediction))
        print(moves, prediction)
        print('FPS {}'.format(1 / (time.time() - loop_time)))
        loop_time = time.time()

        if moves == [1, 0, 0] and prediction[0] >= 0.9:
            move_left()
        elif moves == [0, 1, 0]:
            move_straight()
        elif moves == [0, 0, 1] and prediction[2] >= 0.9:
            move_right()

    keys = getkeys.key_check()
    if 'T' in keys:
        if paused:
            paused = False
            print('unpaused!')
            time.sleep(1)
        else:
            print('Pausing!')
            paused = True
            time.sleep(1)

