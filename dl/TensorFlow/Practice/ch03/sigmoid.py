#encoding=utf8
'''
softmax regression 实现手写数字识别
'''
import numpy as np
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

def sigmoid(z):
    '''sigmoid'''
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    '''sigmoid_prime'''
    return sigmoid(z) * (1 - sigmoid(z))

def predict(x, W, b):
    '''predict'''
    y = W * x + b




def main():
    '''main'''
    mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

    print(mnist.train.images.shape, mnist.train.labels.shape)
    print(mnist.test.images.shape, mnist.test.labels.shape)
    print(mnist.validation.images.shape, mnist.validation.labels.shape)

    train_set_num = mnist.train.images.shape[0]

    num_in = mnist.train.images.shape[1]
    num_out = mnist.train.labels.shape[1]
    num_hidden = 30
    print num_in, num_out, num_hidden
    eta = 0.01

    W1 = (np.random.rand(num_hidden, num_in) - 0.5) / 10.0
    b1 = (np.random.rand(num_hidden) - 0.5) / 10.0
    W2 = (np.random.rand(num_out, num_hidden) - 0.5) / 10.0
    b2 = (np.random.rand(num_out) - 0.5) / 10.0
    print W1.shape, b1.shape
    print W2.shape, b2.shape

    for i in range(1000):
        x = mnist.train.images[i % train_set_num]
        y_ = mnist.train.labels[i % train_set_num]
        # h = sigmoid(x * W1 + b1)
        h = sigmoid(np.dot(W1, x) + b1)
        # y = sigmoid(h * W2 + b2)
        y = sigmoid(np.dot(W2, h) +  b2)

        delta_out = y - y_
        loss = 

        print x
        print y_
        print h
        print y
        break

    # # 创建一个新的 InteractiveSession，使用这个命令将这个 session 注册为默认的 session。
    # sess = tf.InteractiveSession()
    # # 创建一个 placeholder，即输入数据的地方
    # x = tf.placeholder(tf.float32, [None,784])
    # # 存储模型参数,Variable在模型迭代中是持久化的。
    # W = tf.Variable(tf.zeros([784, 10]))
    # b = tf.Variable(tf.zeros([10]))
    # # Softmax Regression 算法,y是预测的概率分布，y_是真实的概率分布
    # y = tf.nn.softmax(tf.matmul(x, W) + b)
    # y_ = tf.placeholder(tf.float32, [None, 10])

    # # 随机梯度下降算法 SGD（Stochastic Gradient Descent）
    # # reduction_sum 求和
    # # reduction_mean 对每个 batch数据结果求平均值
    # cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

    # train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

    # # 对模型的准确率进行验证
    # correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    # # 用 tf.cast 将之前 correct_predict 输出的 bool 值转换为 flaot32，再求平均 
    # accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    # # tensorflow 的全局参数优化器
    # tf.global_variables_initializer().run()
    # # 迭代地执行训练操作
    # for i in range(1000):
    #     batch_xs, batch_ys = mnist.train.next_batch(100)
    #     sess.run(train_step, {x: batch_xs, y_:batch_ys})
    # 	print(i, accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))

    # # 计算模型在测试集上的准确率
    # print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))


if __name__ == '__main__':
    main()


