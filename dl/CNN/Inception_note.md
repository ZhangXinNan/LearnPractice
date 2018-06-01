# 0 前言
AlexNet LeNet的扩展，ReLU/Dropout
VGG 常用于图像特征的抽取、目标检测候选框生成等。参数数据太大。
GoogLeNet 使用了Inception模块。它的目的是设计一种优良局部拓扑结构的网络，即对输入图像并行地执行多个卷积运算或者池化操作，即对输入图像并行地执行多个卷积或者池化操作，并将所有输出结果拼接为一个非常深的feature map.
因为1x1，3x3，5x5等将不同的卷积与池化操作获得输入图像的不同信息，并行处理这些运算并结合能获得更好的图像表征。

# 1 Inception V1
问题：
* 目标大小差异大
* 位置差异大
* 网络太深了会过拟合
* 大的卷积层耗资源

解决方案：
* 使网络变宽，9个Inception模块
* 使用3个不同大小的滤波器（1x1,3x3,5x5）对输入执行卷积操作
* 为降低算力，在3x3,5x5之前增加1x1卷积，限制输入通道数量。
* 避免梯度消失，增加两个辅助分类器。

# 2 Inception V2
问题：
* 减少特征表征瓶颈。减少维度会损失信息
* 因子分解更优秀，计算更高效

解决方案：
* 5x5 分解为两个3x3
* nxn 分解为1xn和nx1

# 3 Inception V3
问题：
* 作者认为辅助分类器的作用是正则化

解决方法：
* RMSPorp优化器
* Factorized 7x7卷积
* 辅助分类器使用BatchNorm
* 标签平滑


# 4 Inception V4
问题：
* 使模块更加一致
解决方法：
* 三个主要的Inception模块，称为A/B/C
* 引入了专用的缩减块

# 5 Inception-ResNet V1和V2


# 参考
[从Inception v1到Inception-ResNet，一文概览Inception家族的「奋斗史」](https://zhuanlan.zhihu.com/p/37505777)

