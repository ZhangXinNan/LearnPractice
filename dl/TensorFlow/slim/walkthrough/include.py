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