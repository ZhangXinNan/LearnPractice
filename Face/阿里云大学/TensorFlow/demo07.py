import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
a = tf.constant(10)
b = tf.constant(20)
c = tf.add(a, b)

print(a, b, c)
# 第一种
sess = tf.Session()
c_value = sess.run(c)
c_value_eval = c.eval(session=sess)
print("c_value : ", c_value)
print("c_value_eval : ", c_value_eval)
sess.close()

print(a, b, c)
# 第二种
with tf.Session() as sess:
    c_value2 = sess.run(c)
    print("c_value2 : ", c_value2)

with tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True)) as sess:
    c_value3 = sess.run(c)
    print("c_value3 : ", c_value2)
