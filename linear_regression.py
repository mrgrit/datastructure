import numpy as np
import matplotlib.pyplot as plt
num_points = 1000
vectors_set = []

for i in range(num_points) :
    x1 = np.random.normal(0.0,0.55)
    y1 = x1*0.1 + 0.3 + np.random.normal(0.0,0.03)
    vectors_set.append([x1,y1])

x_data = [v[0] for v in vectors_set]
y_data = [v[1] for v in vectors_set]


plt.plot(x_data, y_data, 'ro')
plt.legend()
plt.show()

import tensorflow as tf

W = tf.Variable(tf.random_uniform([1],-1.0,1.0))
b = tf.Variable(tf.zeros([1]))
y = W*x_data + b

# 거리기반 비용함수
# 거리에 제곱, 그 합계에 평균
loss  = tf.reduce_mean(tf.square(y - y_data))

# 경사하강법 알고리즘
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)

for step in range(60) :
    sess.run(train)

    print(sess.run(W), sess.run(b))
    print(step, sess.run(loss))
"""
    plt.plot(x_data,y_data,'ro')
    plt.plot(x_data,sess.run(W) * x_data + sess.run(b))
    plt.xlabel('x')
    plt.xlim(-2,2)
    plt.ylim(0.1,0.6)
    plt.ylabel('y')
    plt.legend()
    plt.show()
"""
