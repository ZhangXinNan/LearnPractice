
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data

INPUT_NODE = 784
OUTPUT_NODE = 10

LARYER1_NODE = 500
BATCH_SIZE = 100

LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99

REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 30000
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
    W2 = tf.Variable(tf.truncated_normal((LAYER1_NODE, OUTPUT_NODE), std_dev=0.1))
    b2 = tf.Variable(tf.constant(0.1, shape=[OUTPUT_NODE]))
    y = inference(x, None, W1, b1, W2, b2)

    global_step = tf.Variable(0, trainable=False)

    variable_averages = tf.train.ExponentialMovingAverage(MOVING_AVERAGE_DECAY, global_step)
    
    variable_averages_op = variable_averages.apply(tf.trainable_variables)

    average_y = inference(x, variable_averages, W1, b1, W2, b2)
    