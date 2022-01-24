import numpy as np
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# images
train_path = 'own-datasets/train'
valid_path = 'own-datasets/valid'
train_batches = ImageDataGenerator().flow_from_directory(directory=train_path, target_size=(28,28),classes=['zero','one','two','three','four','five','six','seven','eight','nine','plus','minus','multiplication','division'], batch_size=10)
valid_batches = ImageDataGenerator().flow_from_directory(directory=valid_path, target_size=(28,28),classes=['zero','one','two','three','four','five','six','seven','eight','nine','plus','minus','multiplication','division'], batch_size=10)

# hidden layers
model = Sequential()
model.add(Conv2D(input_shape=(28,28,3),filters=32,kernel_size=(3,3),activation="relu", padding="same"))
model.add(MaxPool2D(pool_size=(2,2),strides=2))
model.add(Conv2D(filters=64,kernel_size=(3,3),activation="relu", padding="same"))
model.add(MaxPool2D(pool_size=(2,2),strides=2)) 
#model.add(Conv2D(filters=128,kernel_size=(3,3),activation="relu", padding="same"))
#model.add(MaxPool2D(pool_size=(2,2),strides=2))
model.add(Conv2D(filters=512,kernel_size=(3,3),activation="relu", padding="same"))
model.add(MaxPool2D(pool_size=(2,2),strides=2)) 
model.add(Flatten())
model.add(Dense(units=14, activation="softmax"))

# train the model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x=train_batches, validation_data=valid_batches, epochs=20, verbose=2)

# save the model
from keras.models import load_model
model.save('handWritten_Detection.h5')
