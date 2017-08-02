import tensorflow as tf
import numpy as np

x_data = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=np.float32)
y_data = np.array([[0],[1],[1],[0]], dtype = np.float32)
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

W1 = tf.Variable(tf.random_normal([2,10]), name = 'weight1')
b1 = tf.Variable(tf.random_normal([10]), name = 'bias1')
# layer 1의 임시 hypothesis를 구한다.
layer1 = tf.sigmoid(tf.matmul(X,W1) + b1)


# 맨 마지막 layer의 output은 항상 1이다.
W2 = tf.Variable(tf.random_normal([10,1]), name = 'weight2')
b2 = tf.Variable(tf.random_normal([1]), name = 'bias2')
# 그다음 layer hypothesis의 X값은 이전 layer의 y값이 들어간다.
hypothesis = tf.sigmoid(tf.matmul(layer1, W2) + b2)

# Cross Entropy
cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) * tf.log(1-hypothesis))
train = tf.train.GradientDescentOptimizer(learning_rate = 0.1).minimize(cost)

#True if hypothesis > 0.5 else Flase
predicted = tf.cast(hypothesis > 0.5, dtype = tf.float32)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype = tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(10001):
        sess.run(train, feed_dict={X:x_data, Y:y_data})
        if step % 100 == 0:
            print(step, sess.run(cost, feed_dict={X:x_data, Y:y_data}), sess.run([W1,W2]))

    # Accuracy report
    h, c, a = sess.run([hypothesis, predicted, accuracy], feed_dict={X:x_data, Y:y_data})
    print("\nHypothesis: ", h, "\nCorrect: ", c, "\nAccuracy: ", a)

    

                          
