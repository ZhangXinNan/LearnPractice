#encoding=utf8

import os
import tensorflow as tf


pb_file_path = os.getcwd()

with tf.Session(graph=tf.Graph()) as sess:
    tf.saved_model.loader.load(sess, ['cpu_server_1'], pb_file_path+'/savemodel')
    sess.run(tf.global_variables_initializer())

    input_x = sess.graph.get_tensor_by_name('x:0')
    input_y = sess.graph.get_tensor_by_name('y:0')

    op = sess.graph.get_tensor_by_name('op_to_store:0')

    ret = sess.run(op,  feed_dict={input_x: 5, input_y: 5})
    print(ret)
# 只需要指定要恢复模型的 session，模型的 tag，模型的保存路径即可,使用起来更加简单