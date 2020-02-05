import tensorflow as tf

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.add(a, b)

with tf.Session() as sess:
    print('占位符的结果：', sess.run(c, feed_dict={a: 3, b:4}))
