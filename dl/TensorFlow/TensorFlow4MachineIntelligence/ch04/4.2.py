# encoding=utf8
import tensorflow as tf

def inference(X):
    print("inference")

def loss(X, y):
    print("loss")
    total_loss = 1
    return total_loss

def inputs():
    print("inputs")
    return X, y

def train(total_loss):
    print("train")

def evaluate(sess, X, y):
    print("evaluate")


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
        if step % 1000 == 0:
            saver.save(sess, 'my-model', global_step=step)
    
    saver.save(sess, 'my-model', global_step=training_steps)
    evaluate(sess, X, y)
    # coord.request_stop()
    # coord.join(threads)
    # sess.close()