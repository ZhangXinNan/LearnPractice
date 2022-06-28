#encoding=utf8

import numpy as np

DTYPE = np.float32

def sigmoid(y):
    return 1.0 / (1.0 + np.exp(-y))

def sigmoid_prime(y):
    return sigmoid(y) * (1.0 - sigmoid(y))

class Layer:
    def __init__(self, n_in, n_out, lr=0.001):
        self.n_in = n_in
        self.n_out = n_out
        self.weights = np.random.rand(n_out, n_in) - 0.5 # 10 * 784
        self.biases = np.random.rand(n_out) - 0.5 # 10
        self.weights = self.weights.astype(DTYPE)
        self.biases = self.biases.astype(DTYPE)
        self.lr = lr
    def forward(self, input):
        self.input = input.astype(DTYPE) # 784
        self.output = sigmoid(np.dot(self.input, self.weights.T) + self.biases)
        self.predict_y = np.argmax(self.output)
        # print self.input
        # print self.biases
        # print self.weights
        # print self.output
        # print self.label
    def bp(self, label):
        self.y = np.zeros(self.output.shape)
        self.y[label] = 1.0
        # print self.output
        # print self.y
        self.delta = -self.output * ( 1 - self.output) * (self.output - self.y)
        self.delta_w = self.lr * self.input.T.dot(self.delta)
        
        
    