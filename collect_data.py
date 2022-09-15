import window_capture
import time
import getkeys
import numpy as np
import cv2

starting_value = 1
file_name = ''

def keys_to_output(keys):
    output = [0,0,0]
    if 'W' in keys and 'A' in keys:
        output[0] = 1
    elif 'W' in keys and 'D' in keys:
        output[2] = 1
    elif 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')
    while (True):

        if not paused:
            screen = window_capture.WindowCapture('Roblox').get_screenshot()
            last_time = time.time()

            screen = cv2.resize(screen, (200, 66))

            keys = getkeys.key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])

            #print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()

            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

            if len(training_data) % 100 == 0:
                print(len(training_data))

                if len(training_data) == 1000:
                    np.save(file_name, training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = ''.format(starting_value)

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


main(file_name, starting_value)