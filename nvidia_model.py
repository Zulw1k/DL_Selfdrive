from tensorflow import keras
from keras.models import Sequential
from keras.layers import Convolution2D, Dense, Dropout, Flatten
import tensorflow as tf


def nvidiaModel(width, height, lr):
    tf.keras.losses.CategoricalCrossentropy(from_logits=True)
    model = Sequential()
    model.add(Convolution2D(24, (5, 5), strides=(2, 2), input_shape=(width, height, 1), activation="elu"))
    model.add(Convolution2D(36, (5, 5), strides=(2, 2), activation="elu"))
    model.add(Convolution2D(48, (5, 5), strides=(2, 2), activation="elu"))
    model.add(Convolution2D(64, (3, 3), activation="elu"))
    model.add(Convolution2D(64, (3, 3), activation="elu"))
    model.add(Dropout(0.5))

    model.add(Flatten())

    model.add(Dense(100, activation="elu"))
    model.add(Dropout(0.5))

    model.add(Dense(50, activation="elu"))
    model.add(Dropout(0.5))

    model.add(Dense(10, activation="elu"))
    model.add(Dropout(0.5))

    model.add(Dense(3, activation="softmax"))

    opt = keras.optimizers.Adam(learning_rate=lr)
    model.compile(optimizer=opt,
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    return model
