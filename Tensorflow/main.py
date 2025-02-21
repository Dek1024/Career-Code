#A code snippet to run tensorflow
#This is from tensorflow userguide and 
import tensorflow as tf
print("Tensorflow Version",tf.__version__)

#Load mnist dataset from keras
mnist = tf.keras.datasets.mnist

#x_train is a numpy array containing (60000,28,28) 60000 images of digits, each digit is a (28,28) matrix of pixels
#y_train is a numpy array of (60,00,) it consists of integers from 0 to 9
#similarly for x_test and y_test
(x_train,y_train), (x_test,y_test) = mnist.load_data()
x_train,x_test = x_train/255.0,x_test/255.0

assert x_train.shape == (60000,28,28)
assert y_train.shape == (60000,)
assert x_test.shape == (10000,28,28)
assert y_test.shape == (10000,)

#Defining the model
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape = (28,28)),
                                    tf.keras.layers.Dense(128),
                                    tf.keras.layers.Dropout(0.2),
                                    tf.keras.layers.Dense(10)])

#Example of a prediction
predictions = model(x_train[:1]).numpy()
print(predictions)
print(tf.nn.softmax(predictions).numpy())

#Choice of loss function
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits = True)
print(loss_fn(y_train[:1],predictions).numpy())

#Compiling the model - choice of optimizer and metrics
model.compile(optimizer = 'adam',loss = loss_fn,metrics = ['accuracy'])
model.fit(x_train,y_train,epochs = 5)
model.evaluate(x_test,y_test,verbose = 2)

#Adding probabilty to the model
probability_model = tf.keras.Sequential([model,tf.keras.layers.Softmax()])
probability_model(x_test[:5])