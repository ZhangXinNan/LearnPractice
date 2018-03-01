原文地址：[从特斯拉到计算机视觉之「图像语义分割」](https://zhuanlan.zhihu.com/p/21824299)



图像语义分割（Semantic image segmentation）
# 0 什么是图像语义分割
语义类别（Semantic label）
图像语义标注（Image semantic labeling）
像素语义标注（Semantic pixel labeling）
像素语义分组（Semantic pixel grouping）

# 1 前DL时代的语义分割

像素级别阈值法（Threading methods）
基于像素聚类的分割方法（Clustering-based segmentation methods）
图划分的分割方法（Graph partitioning segmentation methods）

## 1.1 Normalized cut
将图像抽象为图（Graph）的形式：
```
G = (V, E) # V 为图节点，E 为图的边
```

## 1.2 Grab cut

# 2 DL时代的语义分割
## 2.1 全卷积神经网络（Fully Convolutional Networks, FCN）
原图为```(H,W,3)```，原图对应的响应张量（Activation tensor）```(h_i, w_i, d_i)```。

为了解决下采样问题，FCN用双线性插值将响应张量的长度上采样 得到原图大小。

## 2.2 Dilated Convolutions
去掉池化层，将传统卷积层换成dilation=2的dilated convolution层。

## 2.3 以条件随机场为代表的后处理操作
条件随机场（Conditional random field, CRF）作为最后的后处理操作来对语义语义预测结果进行优化。

CRF将图像中每个像素点所属类别看作一个变量 `x_i \blong {y1, y2, ...,yc}`，然后考虑什么问题两个变量之间的关系，建立一个完全图。
 
