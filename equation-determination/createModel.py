import tensorflow as tf
from tensorflow import keras

# load MNIST datasets
mnistDataSet = keras.datasets.mnist
((x_train, y_train), (x_test, y_test)) = mnistDataSet.load_data()

# print the number of datas
# print(x_train.shape)
# print(y_train.shape)
# print(x_test.shape)
# print(x_test.shape)

# change [][] --> [] (2D to one array/ list)
x_train = x_train.reshape(x_train.shape[0], 784)
#print(x_train.shape)

#print(x_train[0][163])
x_train = x_train/255
#print(x_train[0][163])

x_test = x_test.reshape(x_test.shape[0],784)
x_test = x_test/255

# create a model with multiple layers
model = keras.models.Sequential()
model.add(keras.layers.Dense(784, activation='relu')) # first hidden layer with 784 nodes
model.add(keras.layers.Dense(392, activation='relu')) # second hidden layer with 392 nodes
model.add(keras.layers.Dense(10, activation='softmax')) # 10 possible outcomes (0~9)

# set optimizer, loss function
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

# execute the model 3 times
model.fit(x_train, y_train, epochs = 3) # epochs can be greater

# check model
model.summary()

# evaluate model
# shows loss and accuracy
model.evaluate(x_test, y_test)

# save model
model.save('handWrittenNum_Detection.h5')
