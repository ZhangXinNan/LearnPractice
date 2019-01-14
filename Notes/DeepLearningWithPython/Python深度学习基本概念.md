


# 1 损失函数
## 1.1 binary_crossentropy 二元交叉熵损失
二分类用。
$$
    loss = -\sum_{i=1}^n \hat y_i log y_i + (1- \hat y_i)log (1-\hat y_i)
$$

$$
    \frac{\partial loss}{\partial y} = -\sum_{i=1}^n \frac{\hat y_i}{y_i} - \frac{1-\hat y_i}{1-y_i}
$$

## 1.2 mean_squared_error 均方误差 MSE
回归时用。
$$ 
    loss = \sum_{i=1}^n(y_i - \hat y_i)^2 
$$

$$
    \frac{\partial loss}{\partial y} = 2\sum_{i=1}^n(y_i - \hat y_i)
$$ 

## 1.3 mean absolute error 平均绝对误差 MAE


## 3.5 categorical_crossentropy 分类交叉熵
single task multi label时使用。
衡量两个概率分布之间的距离，这两个概率分布分别是网络输出的概率分布和标签的真实分布。

# 2 优化器
## 3.3 rmsprop 优化器




## 3.4 categorical encoding 分类编码
也叫 one-hot 编码
除了标签索引对应的元素为1，其他每个标签为0。



## 奥卡姆剃刀原理 Occam's razor
如果一件事情有两种解释，最可能正确的解释是最简章的那个，即假设更少的那个。

## L1正则化 L1 regularization L1范数

## L2 正则化 L2 regularization L2范数

## ROC 和 AUC
分类指标。

## 标准化 normalization
（1）减平均值，使其中心为0
（2）除以标准差，使其标准差为1
在网络的每一次变换后都应该考虑标准化。


## 批标准化 batch normalization
工作原理：训练过程中内部保存已读取每批数据均值和方差的移动平均值。
主要效果：有助于梯度传播。
在卷积层或者密集连接层之后使用。

## 深度可分离卷积层 depthwise separable convolution
（1）对输入每个通道分别执行空间卷积，
（2）通过逐点卷积将输出通道混合。

