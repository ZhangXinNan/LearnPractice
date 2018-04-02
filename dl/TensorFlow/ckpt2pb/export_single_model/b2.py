#encoding=utf8

import tensorflow as tf
from google.protobuf import text_format

with tf.Session() as sess:
    # 不使用'rb'模式
    with open('./graph.pb', 'r') as f:
        graph_def = tf.GraphDef()
        # 不使用graph_def.ParseFromString(f.read())
        text_format.Merge(f.read(), graph_def)
        output = tf.import_graph_def(graph_def, return_elements=['out:0'], input_map={'input:0':50.})
        print(sess.run(output))