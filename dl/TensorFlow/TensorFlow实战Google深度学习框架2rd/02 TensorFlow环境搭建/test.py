import os
import tensorflow as tf

os.environ["CUDA_VISIBLE_DEVICES"]="-1"
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.__version__)

a = tf.constant([1, 2.0], name='a')
b = tf.constant([3.0, 4.0], name='b')
c = tf.add(a, b)

print(a)
print(b)
print(c)

with tf.Session() as sess:
    aa, bb, cc = sess.run([a, b, c])
    print(a)
    print(b)
    print(c)
    print(aa, bb, cc)
