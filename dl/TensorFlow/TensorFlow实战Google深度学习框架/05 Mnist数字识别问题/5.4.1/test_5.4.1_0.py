
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

# 第一次运行时
with tf.Session() as sess:
    sess.run(init_op)
    saver.save(sess, './model/model.ckpt')



