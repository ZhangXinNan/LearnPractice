# encoding=utf8
import os
import tensorflow as tf

def inference(X):
    return tf.matmul(X, W) + b

def loss(X, y):
    y_predicted = inference(X)
    total_loss = tf.reduce_sum(tf.squared_difference(y, y_predicted))
    return total_loss

def inputs():
    weight_age = [[84, 46], [73, 20], [65, 52], [70, 30], [76, 57], [69, 25], [63, 28], [72, 36], [79, 57], [75, 44], [27, 24], [89, 31], [65, 52], [57, 23], [59, 60], [69, 48], [60, 34], [79, 51], [75, 50], [82, 34], [59, 46], [67, 23], [85, 37], [55, 40], [63, 30]]
    blood_fat_content = [354, 190, 405, 263, 451, 302, 288, 385, 402, 365, 209, 290, 346, 254, 395, 434, 220, 374, 308, 220, 311, 181, 274, 303, 244]
    return tf.to_float(weight_age), tf.to_float(blood_fat_content)

def train(total_loss):
    learning_rate = 0.0000001
    return tf.train.GradientDescentOptimizer(learning_rate).minimize(total_loss)

def evaluate(sess, X, y):
    print(sess.run(inference([[80., 25.]])))
    print(sess.run(inference([[65., 25.]])))


W = tf.Variable(tf.zeros([2,1]), name='weights')
b = tf.Variable(0., name='bias')



# 定义一个Saver对象
saver = tf.train.Saver()
with tf.Session() as sess:
    initial_step = 0
    tf.initialize_all_variables().run()
    ckpt = tf.train.get_checkpoint_state(os.path.dirname(__file__))
    if ckpt and ckpt.model_checkpoint_path:
        saver.restore(sess, ckpt.model_checkpoint_path)
        initial_step = int(ckpt.model_checkpoint_path.rsplit('-', 1)[1])

    X, y = inputs()

    total_loss = loss(X, y)
    train_op = train(total_loss)

    # coord = tf.train.Coordinator()
    # threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    training_steps = 1000
    for step in range(training_steps):
        sess.run([train_op])
        if step % 10 == 0:
            print "loss : ", sess.run([total_loss])
        # if step % 1000 == 0:
        #     saver.save(sess, 'my-model', global_step=step)
    
    # saver.save(sess, 'my-model', global_step=training_steps)
    evaluate(sess, X, y)
    # coord.request_stop()
    # coord.join(threads)
    # sess.close()