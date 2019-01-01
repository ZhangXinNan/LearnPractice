'''
防止过拟合：
（1）使用更多训练数据；
（2）正则化。

'''

import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)


# 下载 IMDB 数据集
NUM_WORDS = 10000

(train_data, train_labels), (test_data, test_labels) = keras.datasets.imdb.load_data(num_words=NUM_WORDS)

def multi_hot_sequences(sequences, dimension):
    # Create an all-zero matrix of shape (len(sequences), dimension)
    results = np.zeros((len(sequences), dimension))
    for i, word_indices in enumerate(sequences):
        results[i, word_indices] = 1.0  # set specific indices of results[i] to 1s
    return results

train_data = multi_hot_sequences(train_data, dimension=NUM_WORDS)
test_data = multi_hot_sequences(test_data, dimension=NUM_WORDS)


# 演示过拟合


# 创建基准模型
def create_baseline_model():
    baseline_model = keras.Sequential([
        # `input_shape` is only required here so that `.summary` works.
        keras.layers.Dense(16, activation=tf.nn.relu, input_shape=(NUM_WORDS,)),
        keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    baseline_model.compile(optimizer='adam',
                        loss='binary_crossentropy',
                        metrics=['accuracy', 'binary_crossentropy'])

    print(baseline_model.summary())
    baseline_history = baseline_model.fit(train_data,
                                        train_labels,
                                        epochs=20,
                                        batch_size=512,
                                        validation_data=(test_data, test_labels),
                                        verbose=2)
    return baseline_history

# 创建一个更小的模型
def create_smaller_model():
    smaller_model = keras.Sequential([
        keras.layers.Dense(4, activation=tf.nn.relu, input_shape=(NUM_WORDS,)),
        keras.layers.Dense(4, activation=tf.nn.relu),
        keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    smaller_model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy', 'binary_crossentropy'])

    print(smaller_model.summary())

    smaller_history = smaller_model.fit(train_data,
                                        train_labels,
                                        epochs=20,
                                        batch_size=512,
                                        validation_data=(test_data, test_labels),
                                        verbose=2)
    return smaller_history


# 创建一个更大的模型
def create_bigger_model():
    bigger_model = keras.models.Sequential([
        keras.layers.Dense(512, activation=tf.nn.relu, input_shape=(NUM_WORDS,)),
        keras.layers.Dense(512, activation=tf.nn.relu),
        keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    bigger_model.compile(optimizer='adam',
                        loss='binary_crossentropy',
                        metrics=['accuracy','binary_crossentropy'])

    print(bigger_model.summary())

    bigger_history = bigger_model.fit(train_data, train_labels,
                                    epochs=20,
                                    batch_size=512,
                                    validation_data=(test_data, test_labels),
                                    verbose=2)
    return bigger_history
                            

# 绘制训练损失和验证损失图表
def plot_history(histories, key='binary_crossentropy'):
  plt.figure(figsize=(16,10))

  for name, history in histories:
    val = plt.plot(history.epoch, history.history['val_'+key],
                   '--', label=name.title()+' Val')
    plt.plot(history.epoch, history.history[key], color=val[0].get_color(),
             label=name.title()+' Train')

  plt.xlabel('Epochs')
  plt.ylabel(key.replace('_',' ').title())
  plt.legend()

  plt.xlim([0,max(history.epoch)])





# 策略


# 添加权重正则化

'''
奥卡姆剃刀定律：如果对于同一现象有两种解释，最可能正确的解释是“最简单”的解释，即做出最少量假设的解释。
这也适用于神经网络学习的模型：给定一些训练数据和一个网络架构，有多组权重值（多个模型）可以解释数据，而简单模型比复杂模型更不容易过拟合。


在这种情况下，“简单模型”是一种参数值分布的熵较低的模型（或者具有较少参数的模型，如我们在上面的部分中所见）。
因此，要缓解过拟合，一种常见方法是限制网络的复杂性，具体方法是强制要求其权重仅采用较小的值，使权重值的分布更“规则”。
这称为“权重正则化”，通过向网络的损失函数添加与权重较大相关的代价来实现。这个代价分为两种类型：

L1 正则化，其中所添加的代价与权重系数的绝对值（即所谓的权重“L1 范数”）成正比。

L2 正则化，其中所添加的代价与权重系数值的平方（即所谓的权重“L2 范数”）成正比。
L2 正则化在神经网络领域也称为权重衰减。不要因为名称不同而感到困惑：从数学角度来讲，权重衰减与 L2 正则化完全相同。
'''
def create_l2_model():
    l2_model = keras.models.Sequential([
        keras.layers.Dense(16, kernel_regularizer=keras.regularizers.l2(0.001),
                        activation=tf.nn.relu, input_shape=(NUM_WORDS,)),
        keras.layers.Dense(16, kernel_regularizer=keras.regularizers.l2(0.001),
                        activation=tf.nn.relu),
        keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    l2_model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy', 'binary_crossentropy'])
    print(l2_model.summary())
    l2_model_history = l2_model.fit(train_data, train_labels,
                                    epochs=20,
                                    batch_size=512,
                                    validation_data=(test_data, test_labels),
                                    verbose=2)
    return l2_model_history



# 添加丢弃层
def create_dropout_model():
    dpt_model = keras.models.Sequential([
        keras.layers.Dense(16, activation=tf.nn.relu, input_shape=(NUM_WORDS,)),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(16, activation=tf.nn.relu),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    dpt_model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy','binary_crossentropy'])
    print(dpt_model.summary())
    dpt_model_history = dpt_model.fit(train_data, train_labels,
                                    epochs=20,
                                    batch_size=512,
                                    validation_data=(test_data, test_labels),
                                    verbose=2)
    return dpt_model_history




# 添加丢弃层
def create_l2_dpt_model():
    L2_dpt_model = keras.models.Sequential([
        keras.layers.Dense(16, kernel_regularizer=keras.regularizers.l2(0.001), activation=tf.nn.relu, input_shape=(NUM_WORDS,)),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(16, kernel_regularizer=keras.regularizers.l2(0.001), activation=tf.nn.relu),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(1, activation=tf.nn.sigmoid)
    ])

    L2_dpt_model.compile(optimizer='adam',
                    loss='binary_crossentropy',
                    metrics=['accuracy','binary_crossentropy'])
    print(L2_dpt_model.summary())
    L2_dpt_model_history = L2_dpt_model.fit(train_data, train_labels,
                                    epochs=20,
                                    batch_size=512,
                                    validation_data=(test_data, test_labels),
                                    verbose=2)
    return L2_dpt_model_history



if __name__ == '__main__':
    baseline_history = create_baseline_model()
    # smaller_history = create_smaller_model()
    # bigger_history = create_bigger_model()
    # plot_history([('baseline', baseline_history),
    #           ('smaller', smaller_history),
    #           ('bigger', bigger_history)])
    # plt.show()

    # l2_model_history = create_l2_model()
    # plot_history([('baseline', baseline_history),
    #             ('l2', l2_model_history)])
    # plt.show()

    # dpt_model_history = create_dropout_model()
    # plot_history([('baseline', baseline_history),
    #           ('dropout', dpt_model_history)])
    # plt.show()

    L2_dpt_model_history = create_l2_dpt_model()
    plot_history([('baseline', baseline_history),
              ('L2_dropout', L2_dpt_model_history)])
    plt.show()
