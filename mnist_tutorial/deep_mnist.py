# the MNIST dataset
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)

# Tensorflow library
import tensorflow as tf
# Tensorflow relies on a C++ backend to do its computation. 
# The connection to this backend is called a session. 
sess = tf.InteractiveSession()

# Building the softmax regression model:
# Placeholders - creating nodes for the input images and target output classes.
# x represents input images from the MNIST dataset
x = tf.placeholder(tf.float32, shape=[None, 784])
# y represents the output classes as in the 0 to 9 digits that an image may contain.
y_ = tf.placeholder(tf.float32, shape=[None, 10])
# Variables - model parameters W and b
# W represents the weights
W = tf.Variable(tf.zeros([784,10]))
# b represents the bias
b = tf.Variable(tf.zeros([10]))
# before Variables can be used, they must be initialised.
sess.run(tf.initialize_all_variables())

# implement the model
y = tf.nn.softmax(tf.matmul(x,W) + b)
# loss function - cross_entropy
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
# train the model - use gradient descent
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
# train the model - repeatedly run the train_step operation
for i in range(1000):
  batch = mnist.train.next_batch(100)
  train_step.run(feed_dict={x: batch[0], y_: batch[1]})

# evaluate the model
# did the model's prediction match the actual digit in the image?
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
# cast correct_prediction from boolean to floating point and calculate the mean.
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# evaluate the accuracy on the test data. expected output ~92%.
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
