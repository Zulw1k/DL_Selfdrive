import numpy as np
from nvidia_model import nvidiaModel
import tensorflow as tf

#GPU
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)
  except RuntimeError as e:
    print(e)

#CPU
tf.config.threading.set_intra_op_parallelism_threads(2)
tf.config.threading.set_inter_op_parallelism_threads(2)

width = 200
height = 66
lr = 0.0001
epoch = 6
MODEL_NAME = ''.format(lr, 'nvidia', epoch)

model = nvidiaModel(width, height, lr)

train_data = np.load('', allow_pickle=True)

train = train_data[:-10000]
test = train_data[-10000:]

X = np.array([i[0] for i in train]).reshape(-1, width, height, 1)
Y = np.array([i[1] for i in train])

test_X = np.array([i[0] for i in test]).reshape(-1, width, height, 1)
test_Y = np.array([i[1] for i in test])

model.fit(X, Y, epochs=epoch, validation_data=(test_X, test_Y))

model.save(MODEL_NAME)