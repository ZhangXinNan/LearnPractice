```

from keras.datasets import mnist

# 加载 MNIST 数据集
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 查看图片
import matplotlib.pyplot as plt 
plt.imshow(test_images[0], cmap=plt.cm.binary)
plt.show()

print(train_images.shape, len(train_labels))
print(test_images.shape, len(test_labels))

from keras import models
from keras import layers

# 构建网络
network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28, )))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
                loss='categorical_crossentropy',
                metrics=['accuracy'])

# 展开并除以255
train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255.0

test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255.0

# Converts a class vector (integers) to binary class matrix.
# 整数目标值改为分类目标值
from keras.utils import to_categorical
train_labels = to_categorical(train_labels)
print(test_labels[:10])
test_labels = to_categorical(test_labels)
print(test_labels[:10])
'''
[7 2 1 0 4 1 4 9 5 9]
# to_categorical 后
[[0. 0. 0. 0. 0. 0. 0. 1. 0. 0.]
 [0. 0. 1. 0. 0. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 1. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 1. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]
 [0. 0. 0. 0. 0. 1. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 1.]]
'''

# 训练(fit拟合)
network.fit(train_images, train_labels, epochs=5, batch_size=128)

# 测试集上的性能
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('test acc:', test_acc, ' test loss: ', test_loss)
```
