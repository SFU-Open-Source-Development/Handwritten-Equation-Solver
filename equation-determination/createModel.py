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

print(x_train[0][163])
x_train = x_train/255
print(x_train[0][163])

x_test = x_test.reshape(x_test.shape[0],784)
x_test = x_test/255
