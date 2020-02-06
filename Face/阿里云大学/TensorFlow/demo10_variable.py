

import tensorflow as tf

a = tf.Variable(initial_value=50)
b = tf.Variable(initial_value=40)
c = tf.add(a, b)
print('a : ', a)
print('b : ', b)
print('c : ', c)

init = tf.global_variable_initializer()

with tf.Session() as sess:
    sess.run(init)
    a_value, b_value, c_value = sess.run([a, b, c])
    print(a_value, b_value, c_value)
