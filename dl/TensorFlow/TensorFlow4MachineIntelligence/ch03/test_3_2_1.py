# encoding=utf8

import tensorflow as tf

a = tf.constant(5, name='input_a')
b = tf.constant(3, name='input_b')
# c = tf.mul(a, b, name='mul_c') # 新版本改为multiply
c = tf.multiply(a, b, name='mul_c')
d = tf.add(a, b, name='add_d')
e = tf.add(c, d, name='add_e')

# 上边只是定义的数据流图。
# 要想体验运行效果，还要添加如下：
sess = tf.Session()
output = sess.run(e)
print output
# writer = tf.train.SummaryWriter('./my_graph', sess.graph)
# 新版本中用tf.summary.FileWriter()
writer = tf.summary.FileWriter('./my_graph', sess.graph)
# writer = tf.summary.FileWriter('./my_graph', tf.get_default_graph())
writer.close()
sess.close()