#encoding=utf8

import os, sys
import numpy as np
import cv2
from Layer import Layer

INPUT_SIZE = 784
HIDDEN_SIZE = 200
OUTPUT_SIZE = 10


def load_data(in_dir):
    filepath_label_list = []
    for label in range(10):
        sub_dir = os.path.join(in_dir, str(label))
        for filename in os.listdir(sub_dir):
            filepath = os.path.join(sub_dir, filename)
            if filename[0] == '.' or not os.path.isfile(filepath):
                continue
            filepath_label_list.append((filepath, label))
    return filepath_label_list

def load_image(filepath):
    im = cv2.imread(filepath, 0)
    # print type(im), im.shape
    return im.reshape(INPUT_SIZE)

def evaluate(data):
    cm = np.zeros((OUTPUT_SIZE + 1, OUTPUT_SIZE+1), np.int32)
    for filepath, label in data:
        lable = int(label)
        # print filepath, label, type(label)
        L.forward(load_image(filepath))
        y_output = L.output
        y_predict = L.predict_y
        # print y_output, y_predict
        # print type(label), type(y_predict)
        if label == y_predict:
            cm[-1, -1] += 1
        cm[label, -1] += 1
        cm[-1, y_predict] += 1
        cm[label, y_predict] += 1

    return cm

    

def main():
    train_data_dir = '/Users/zhangxin/pic/mnist/mnist_png/training'
    test_data_dir = '/Users/zhangxin/pic/mnist/mnist_png/testing'
    train_data = load_data(train_data_dir)
    test_data = load_data(test_data_dir)
    print 'train data :', len(train_data), 'test_data :', len(test_data)

    
    
    indices = np.random.randint(0, len(train_data), 100000)
    for i, index in enumerate(indices):
        if i % 100 == 0:
            cm = evaluate(test_data)
            print cm, i
            break
        filepath, label = train_data[index]
        print filepath, label
        L.forward(load_image(filepath))
        L.bp(label)
        # break
    

if __name__ == '__main__':
    L = Layer(INPUT_SIZE, OUTPUT_SIZE, lr = 0.001)
    main()
