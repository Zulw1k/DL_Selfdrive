from tensorflow import keras
from nvidia_model import nvidiaModel
import numpy as np

width = 200
height = 66
LR = 0.0001

final_model = keras.models.load_model('')
model = nvidiaModel(width, height, LR)

train_data = np.load('', allow_pickle=True)

train = train_data[:-500]
test = train_data[-500:]

X = np.array([i[0] for i in train]).reshape(-1, width, height)
Y = np.array([i[1] for i in train])

test_X = np.array([i[0] for i in test]).reshape(-1, width, height)
test_Y = np.array([i[1] for i in test])

loss, acc = model.evaluate(test_X, test_Y, verbose=2)
print("Untrained model, accuracy: {:5.2f}%".format(100 * acc))
loss, acc = final_model.evaluate(test_X, test_Y, verbose=2)
print("Trained model, accuracy: {:5.2f}%".format(100 * acc))