#encoding=utf8
'''
softmax regression 实现手写数字识别
'''

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def main():
    '''main'''
    mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

    print(mnist.train.images.shape, mnist.train.labels.shape)
    print(mnist.test.images.shape, mnist.test.labels.shape)
    print(mnist.validation.images.shape, mnist.validation.labels.shape)

    # 创建一个新的 InteractiveSession，使用这个命令将这个 session 注册为默认的 session。
    sess = tf.InteractiveSession()
    # 创建一个 placeholder，即输入数据的地方
    x = tf.placeholder(tf.float32, [None,784])
    # 存储模型参数,Variable在模型迭代中是持久化的。
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    # Softmax Regression 算法,y是预测的概率分布，y_是真实的概率分布
    y = tf.nn.softmax(tf.matmul(x, W) + b)
    y_ = tf.placeholder(tf.float32, [None, 10])

    # 随机梯度下降算法 SGD（Stochastic Gradient Descent）
    # reduction_sum 求和
    # reduction_mean 对每个 batch数据结果求平均值
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    # 对模型的准确率进行验证
    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    # 用 tf.cast 将之前 correct_predict 输出的 bool 值转换为 flaot32，再求平均 
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # tensorflow 的全局参数优化器
    tf.global_variables_initializer().run()
    # 迭代地执行训练操作
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        sess.run(train_step, {x: batch_xs, y_:batch_ys})
	print(i, accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))

    # 计算模型在测试集上的准确率
    print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))


if __name__ == '__main__':
    main()


