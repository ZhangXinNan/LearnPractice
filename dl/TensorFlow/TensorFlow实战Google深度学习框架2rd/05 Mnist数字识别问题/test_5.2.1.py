#encoding=utf8
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

INPUT_NODE = 784
OUTPUT_NODE = 10

LAYER1_NODE = 500
BATCH_SIZE = 100

LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99

REGULARIZATION_RATE = 0.0001
# 4000次后就收敛了，不必要运行3万次。
TRAINING_STEPS = 10000
MOVING_AVERAGE_DECAY = 0.99

def inference(input_tensor, avg_class, W1, b1, W2, b2):
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, W1) + b1)
        return tf.matmul(layer1, W2) + b2
    else:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, avg_class.average(W1)) + avg_class.average(b1))
        return tf.matmul(layer1, avg_class.average(W2)) + avg_class.average(b2)


def train(mnist):
    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')

    W1 = tf.Variable(tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1))
    b1 = tf.Variable(tf.constant(0.1, shape=[LAYER1_NODE]))
    W2 = tf.Variable(tf.truncated_normal((LAYER1_NODE, OUTPUT_NODE), stddev=0.1))
    b2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))
    y = inference(x, None, W1, b1, W2, b2)

    global_step = tf.Variable(0, trainable=False)
    # 初始化初始滑动平均类
    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    # 在所有nn参数的变量上使用滑动平均
    variable_averages_op = variable_averages.apply(tf.trainable_variables())
    # 计算使用了滑动平均之后的前向传播计算结果
    average_y = inference(x, variable_averages, W1, b1, W2, b2)

    # 交叉熵作为损失函数
    # 新版本需要参加参数名称logits和lables
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=y, labels=tf.argmax(y_, 1))
    # 计算当前batch样例中所有样例的交叉熵平均值
    cross_entropy_mean = tf.reduce_mean(cross_entropy)
    # L2正则化损失函数
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    # 计算模型的正则化损失
    regularization = regularizer(W1) + regularizer(W2)
    # 总损失=交叉熵损失+正则损失
    loss = cross_entropy_mean + regularization
    # 设置指数衰减的学习率
    learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE, global_step, mnist.train.num_examples/BATCH_SIZE, LEARNING_RATE_DECAY)
    # 优化损失函数
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss, global_step=global_step)
    with tf.control_dependencies([train_step, variable_averages_op]):
        train_op = tf.no_op(name='train')
    
    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    with tf.Session() as sess:
        tf.initialize_all_variables().run()
        validate_feed = {x: mnist.validation.images, y_: mnist.validation.labels}
        test_feed = {x: mnist.test.images, y_:mnist.test.labels}
        for i in range(TRAINING_STEPS):
            if i % 1000 == 0:
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print("After %d training step(s), validation accuracy using average model is %g " % (i, validate_acc))
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x:xs, y_:ys})
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print("After %d training step(s), test accuracy using average mode is %g " % (i, validate_acc))

    writer = tf.summary.FileWriter('../log', tf.get_default_graph())
    writer.close()



def main(argv=None):
    mnist = input_data.read_data_sets('../tmp/data', one_hot=True, source_url='http://yann.lecun.com/exdb/mnist/')
    train(mnist)

# tf.app.run 会调用上面的main函数
if __name__ == '__main__':
    tf.app.run()






