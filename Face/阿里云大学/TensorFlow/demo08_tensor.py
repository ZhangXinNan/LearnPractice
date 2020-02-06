import tensorflow as tf

a = tf.placeholder(dtype=tf.float32, shape=[None, None])
b = tf.placeholder(dtype=tf.float32, shape=[None, 10])
c = tf.placeholder(dtype=tf.float32, shape=[3, 2])
print('a:', a)
print('b:', b)
print('c:', c)

print('改变静态形状后：')
a.set_shape([2, 3])
b.set_shape([4, 10])
print('a:', a)
print('b:', b)

print('改变动态形状后：')
a_reshape = tf.reshape(a, shape=[2,3,1])
print('a_reshape:', a_reshape)
'''
a: Tensor("Placeholder:0", shape=(?, ?), dtype=float32)
b: Tensor("Placeholder_1:0", shape=(?, 10), dtype=float32)
c: Tensor("Placeholder_2:0", shape=(3, 2), dtype=float32)
改变后：
a: Tensor("Placeholder:0", shape=(2, 3), dtype=float32)
b: Tensor("Placeholder_1:0", shape=(4, 10), dtype=float32)
'''