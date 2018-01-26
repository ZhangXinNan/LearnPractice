# encoding=utf8
# ax + b = y ; a=2, b=3
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

with tf.Session() as sess:
    tf.initialize_all_variables().run()

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
    evaluate(sess, X, y)
    # coord.request_stop()
    # coord.join(threads)
    # sess.close()