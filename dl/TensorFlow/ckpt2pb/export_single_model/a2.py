import tensorflow as tf
from tensorflow.python.framework.graph_util import convert_variables_to_constants

a = tf.Variable([[3],[4]], dtype=tf.float32, name='a')
b = tf.Variable(4, dtype=tf.float32, name='b')
input_tensor = tf.placeholder(tf.float32, name='input')
output = tf.add((a+b), input_tensor, name='out')

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    graph = convert_variables_to_constants(sess, sess.graph_def, ["out"])
    tf.train.write_graph(graph, '.', 'graph.pb', as_text=True)