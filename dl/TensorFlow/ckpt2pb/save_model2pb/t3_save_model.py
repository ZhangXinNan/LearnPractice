#encoding=utf8
import tensorflow as tf
import os
from tensorflow.python.framework import graph_util

pb_file_path = os.getcwd()

with tf.Session(graph=tf.Graph()) as sess:
    x = tf.placeholder(tf.int32, name='x')
    y = tf.placeholder(tf.int32, name='y')
    b = tf.Variable(1, name='b')
    xy = tf.multiply(x, y)
    # 这里的输出需要加上name属性
    op = tf.add(xy, b, name='op_to_store')

    sess.run(tf.global_variables_initializer())

    # convert_variables_to_constants 需要指定output_node_names，list()，可以多个
    constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def, ['op_to_store'])

    # 测试 OP
    feed_dict = {x: 10, y: 3}
    print(sess.run(op, feed_dict))

    # 写入序列化的 PB 文件
    with tf.gfile.FastGFile(pb_file_path+'model.pb', mode='wb') as f:
        f.write(constant_graph.SerializeToString())

    # INFO:tensorflow:Froze 1 variables.
    # Converted 1 variables to const ops.
    # 31
    
    
    # 官网有误，写成了 saved_model_builder  
    builder = tf.saved_model.builder.SavedModelBuilder(os.path.join(pb_file_path, 'savemodel'))
    # 构造模型保存的内容，指定要保存的 session，特定的 tag, 
    # 输入输出信息字典，额外的信息
    builder.add_meta_graph_and_variables(sess,
                                       ['cpu_server_1'])

'''
这样和之前的导入 PB 模型一样，也是要知道tensor的name。那么如何可以在不知道tensor name的情况下使用呢，实现彻底的解耦呢？ 给add_meta_graph_and_variables方法传入第三个参数，signature_def_map即可。
'''
# 添加第二个 MetaGraphDef 
#with tf.Session(graph=tf.Graph()) as sess:
#  ...
#  builder.add_meta_graph([tag_constants.SERVING])
#...

builder.save()  # 保存 PB 模型