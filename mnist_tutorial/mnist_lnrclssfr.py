import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
# mnist dataset
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# handling computations outside of python
x = tf.placeholder(tf.float32, [None, 784])
# weights
W = tf.Variable(tf.zeros([784, 10]))
# bias
b = tf.Variable(tf.zeros([10]))
# model
y = tf.nn.softmax(tf.matmul(x, W) + b)

# define the loss and optimiser
y_ = tf.placeholder(tf.float32, [None, 10])
# cross-entropy function
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))
# minimise cross-entropy using gradient descent
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# an operation to initialize the variables
init = tf.initialize_all_variables()
# launch model in a Session
sess = tf.Session()
sess.run(init)
# run the training step 1000 times
for i in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

# evaluate the model 
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))

