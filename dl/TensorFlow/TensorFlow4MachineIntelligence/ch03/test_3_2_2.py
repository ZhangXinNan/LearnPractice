#encoding=utf8

import tensorflow as tf

a = tf.constant([5,3], name='input_a')
b = tf.reduce_prod(a, name='prod_b')
c = tf.reduce_sum(a, name='sum_c')
d = tf.add(b, c, name='add_d')

writer = tf.summary.FileWriter('./my_graph', tf.get_default_graph())
writer.close()