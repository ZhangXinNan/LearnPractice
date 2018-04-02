#ecoding=utf8
import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants

# 构造网络
a = tf.Variable([[3],[4]], dtype=tf.float32, name='a')
b = tf.Variable(4, dtype=tf.float32, name='b')
# 一定要给输出tensor取一个名字！！
output = tf.add(a, b, name='out')

# 转换Variable为constant，并将网络写入到文件
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # 这里需要填入输出tensor的名字
    graph = convert_variables_to_constants(sess, sess.graph_def, ["out"])
    tf.train.write_graph(graph, '.', 'graph.pb', as_text=False)
