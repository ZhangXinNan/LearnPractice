#encoding=utf8
import os
import tensorflow as tf
from tensorflow.python.platform import gfile

pb_file_path = os.getcwd()
sess = tf.Session()
with gfile.FastGFile(os.path.join(pb_file_path, 'model.pb'), 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    sess.graph.as_default()
    tf.import_graph_def(graph_def, name='') # 导入计算图

# 需要有一个初始化的过程    
sess.run(tf.global_variables_initializer())

# 需要先复原变量
print(sess.run('b:0'))
# 1

# 输入
input_x = sess.graph.get_tensor_by_name('x:0')
input_y = sess.graph.get_tensor_by_name('y:0')

op = sess.graph.get_tensor_by_name('op_to_store:0')

ret = sess.run(op,  feed_dict={input_x: 5, input_y: 5})
print(ret)
# 输出 26
