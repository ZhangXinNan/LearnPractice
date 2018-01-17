# 第3章 TensorFlow 入门

## 3.1 TensorFlow计算模型——计算图
### 3.1.1 计算图的概念
TensorFlow中每一个计算都是计算图中的一个节点，节点之间的边描述了计算之间的依赖关系。

### 3.1.2 计算图的使用
TensorFlow的两个阶段：（1）定义计算图中所有的计算（2）执行计算。
tf.get_default_graph 获取默认的计算图
tf.Graph函数来生成新的计算图，不同计算图上的张量和运算不会共享。计算图还提供了管理张量和计算的机制。tf.Graph.device函数指定运行计算的设备。
在一个计算图中通过集合（collection）来管理不同类别的资源。

## 3.2 TensorFlow数据模型——张量
### 3.2.1 张量的概念
在张量中并没有真正保存数字，它保存的是如何得到这些数字的计算过程。

一个张量中保存了三个属性：名字(name)、维度(shape)、类型(type)。



## 3.3 TensorFlow运行模型——会话
session(会话)来执行定义好的运算。
使用会话的两种模式：
（1）明确调用session生成函数和session关闭函数
```
sess = tf.Session()
sess.close()
```
(2)
通过python上下文管理器机制，将所有的计算放在with内部。
```
with tf.Session as sess:
    sess.run()
```

TensorFlow会自动生成一个默认的计算图，如没有特殊指定，运算会自动加入这个计算图中。
Session：不会自动生成默认的会话，需要手动指定。
```
sess = tf.Session()
with sess.as_default():
    print(result.eval())
```


## 3.4 TensorFlow实现神经网络
## 3.4.1 TensorFlow游乐场
## 3.4.2 前向传播算法
tf.matmul ： 矩阵乘法
## 3.4.3 神经网络参数及TensorFlow变量
变量tf.Variable 就是保存和更新NN中参数 。
