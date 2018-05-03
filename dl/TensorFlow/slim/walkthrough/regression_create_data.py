from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import matplotlib
# %matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np
import tensorflow as tf
import time

import sys
sys.path.append('/Users/zhangxin/github/models/research/slim')
from datasets import dataset_utils

# Main slim library
from tensorflow.contrib import slim

from regression_model import regression_model

def produce_batch(batch_size, noise=0.3):
    xs = np.random.random(size=[batch_size, 1]) * 10
    ys = np.sin(xs) + 5 + np.random.normal(size=[batch_size, 1], scale=noise)
    return [xs.astype(np.float32), ys.astype(np.float32)]

x_train, y_train = produce_batch(200)
x_test, y_test = produce_batch(200)
plt.scatter(x_train, y_train)

def convert_data_to_tensors(x, y):
    inputs = tf.constant(x)
    inputs.set_shape([None, 1])
    
    outputs = tf.constant(y)
    outputs.set_shape([None, 1])
    return inputs, outputs

# The following snippet trains the regression model using a mean_squared_error loss.
ckpt_dir = 'tmp/regression_model_multiple/'

with tf.Graph().as_default():
    inputs, targets = convert_data_to_tensors(x_train, y_train)
    predictions, end_points = regression_model(inputs, is_training=True)

    # Add multiple loss nodes.
    mean_squared_error_loss = tf.losses.mean_squared_error(labels=targets, predictions=predictions)
    absolute_difference_loss = slim.losses.absolute_difference(predictions, targets)

    # The following two ways to compute the total loss are equivalent
    regularization_loss = tf.add_n(slim.losses.get_regularization_losses())
    total_loss1 = mean_squared_error_loss + absolute_difference_loss + regularization_loss

    # Regularization Loss is included in the total loss by default.
    # This is good for training, but not for testing.
    total_loss2 = slim.losses.get_total_loss(add_regularization_losses=True)
    
    init_op = tf.global_variables_initializer()
    
    with tf.Session() as sess:
        sess.run(init_op) # Will initialize the parameters with random weights.
        
        total_loss1, total_loss2 = sess.run([total_loss1, total_loss2])
        
        print('Total Loss1: %f' % total_loss1)
        print('Total Loss2: %f' % total_loss2)

        print('Regularization Losses:')
        for loss in slim.losses.get_regularization_losses():
            print(loss)

        print('Loss Functions:')
        for loss in slim.losses.get_losses():
            print(loss)