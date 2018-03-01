
#encoding=utf8
'''
model.ckpt.meta 计算图的结构 
checkpoint

'''
import tensorflow as tf

v1 = tf.Variable(tf.constant(1.0, shape=[1]), name='v1')
v2 = tf.Variable(tf.constant(2.0, shape=[1]), name='v2')

result = v1 + v2

init_op = tf.initialize_all_variables()
saver = tf.train.Saver()


# 用已经保存的模型
with tf.Session() as sess:
    saver.restore(sess, './model/model.ckpt')
    print sess.run(result)

