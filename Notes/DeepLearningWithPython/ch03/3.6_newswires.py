

import keras

from keras.datasets import reuters
# 限定为前10000个最常用单词
(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)

# 样本整数列表转为单词形式
word_index = reuters.get_word_index()
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
# Note that our indices were offset by 3
# because 0, 1 and 2 are reserved indices for "padding", "start of sequence", and "unknown".
decoded_newswire = ' '.join([reverse_word_index.get(i - 3, '?') for i in train_data[0]])
print(decoded_newswire)



# 准备数据，将其向量化
import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

# Our vectorized training data
x_train = vectorize_sequences(train_data)
# Our vectorized test data
x_test = vectorize_sequences(test_data)
print(x_train.shape)
print(x_test.shape)

# 分类编码categorical encoding
def to_one_hot(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results

# Our vectorized training labels
one_hot_train_labels = to_one_hot(train_labels)
# Our vectorized test labels
one_hot_test_labels = to_one_hot(test_labels)
print(one_hot_train_labels.shape)
print(one_hot_test_labels.shape)

# keras内置方法
# from keras.utils.np_utils import to_categorical

# one_hot_train_labels = to_categorical(train_labels)
# one_hot_test_labels = to_categorical(test_labels)


from keras import models
from keras import layers

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))



# 验证
x_val = x_train[:1000]
partial_x_train = x_train[1000:]

# y_val = one_hot_train_labels[:1000]
# partial_y_train = one_hot_train_labels[1000:]
# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])


partial_y_train = train_labels[1000:]
y_val = train_labels[:1000]
model.compile(optimizer='rmsprop', loss='sparse_categorical_crossentropy', metrics=['acc'])
print(model.summary())
history = model.fit(partial_x_train,
                    partial_y_train,
                    epochs=20,
                    batch_size=512,
                    validation_data=(x_val, y_val))



import plot
plot.plot_accuracy(history)
plot.plot_loss(history)
