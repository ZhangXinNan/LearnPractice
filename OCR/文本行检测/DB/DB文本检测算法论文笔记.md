
Real-time Scene Text Detection with Differentiable Binarization

具有可微分二值化的实时场景文本检测

——————————



# 0 概述

Recently, segmentation-based methods are quite popular in scene text detection, as the segmentation results can more accurately describe scene text of various shapes such as curve text. However, the post-processing of binarization is essential for segmentation-based detection, which converts probability maps produced by a segmentation method into bounding boxes/regions of text. In this paper, we propose a module named Differentiable Binarization (DB), which can perform the binarization process in a segmentation network. Optimized along with a DB module, a segmentation network can adaptively set the thresholds for binarization, which not only simplifies the post-processing but also enhances the performance of text detection. Based on a simple segmentation network, we validate the performance improvements of DB on five benchmark datasets, which consistently achieves state-of-the-art results, in terms of both detection accuracy and speed. In particular, with a light-weight backbone, the performance improvements by DB are significant so that we can look for an ideal tradeoff between detection accuracy and efficiency. Specifically, with a backbone of ResNet-18, our detector achieves an F-measure of 82.8, running at 62 FPS, on the MSRA-TD500 dataset. Code is available at: https://github.com/MhLiao/DB.

最近，基于分割的方法在场景文本检测中非常流行，因为分割结果可以更准确地描述曲线文本等各种形状的场景文本。
然而，二值化的后处理对于基于分割的检测至关重要，它将分割方法产生的概率图转换为文本的边界框/区域。
在本文中，我们提出了一个名为Differential Binarization (DB) 的模块，它可以在分割网络中执行二值化过程。
与 DB 模块一起优化后，分割网络可以**自适应地设置二值化阈值**，这不仅简化了后处理，而且提高了文本检测的性能。
基于一个简单的分割网络，我们在五个基准数据集上验证了 DB 的性能改进，在检测精度和速度方面始终达到最先进的结果。
特别是，对于轻量级主干，DB 的性能改进是显着的，因此我们可以在检测精度和效率之间寻找理想的权衡。
具体来说，借助 ResNet-18 的主干，我们的检测器在 MSRA-TD500 数据集上实现了 82.8 的 F-measure，以 62 FPS 的速度运行。
代码位于：https://github.com/MhLiao/DB。

补充：F-measure 即：
$$
F_1=\frac {2 * PR}{ P + R}
$$
P 是精确率（Precision），R是召回率（Recall）。



# 1 介绍

当前大部分检测算法都是使用如下流程：

（1）设置一个固定的阈值，将概率图转成二值图。

（2）然后一些启发式的方法通过聚类得到文本区域 。

![image-20200821113749771](assets/image-20200821113749771.png)

而这篇论文 里的流程是插入一个二值化操作放到分割网络里来一起优化。在这种方式下，每个像素的阈值将自适应预测，更能区分前景背景。标准的二值化函数是不可微分的，我们使用一个近似的二值化函数，称为DB。

相比之前基于方法的方法有四个优点：

1. 更好的性能，包括水平、多方向、弯曲。
2. 更快。因为显著改善了后处理。
3. 在轻量级backbone上表现好。
4. 测试时没有额外内存和时间消耗。



# 2 相关工作回顾

文本检测主要分为两类方法：
- 基于回归的方法 Regression-based method
- 基于分割的方法 Segmentation-based method

## 2.1 基于回归的方法

优点：基于回归的方法，后处理简单。

缺点：很难表示不规则的形状，例如弯曲文本。

- 2017 TextBoxes 直接回归矩阵，基于SSD，修改了anchor和scale。
- 2017 DMPNet 、2018 TextBoxes++ 直接回归四边形，来检测多方向文本。
- 2017 SSTD 引入注意力机制来识别文本区域。
- 2018 RRD 旋转不变性做分类、旋转敏感性来做回归。
- 2017 EAST / DeepReg 像素级回归多方向 文本实例。
- 2017 SegLink 回归分割框和预测它们的连接。
- 2019 DeRPN 维度分解（dimension-decomposition）解决文本检测中的尺度问题。



## 2.2 基于分割的方法

- 2016 基于MSER 和语义分割，检测多方向 文本。
- 2018 文本边界分割文本实例
- 2018 Mask TextSpotter 基于 Mask R-CNN 检测任意形状文本。
- 2019 PSENet 渐进尺度扩张 ，使用不同的kernel。 

# 3 方法



1. 将图像喂给特征金字塔。
2. 特征金字塔降采样成相同尺度级联产生特征 $F$ 。
3. $F$ 预测概率图 $P$ 和阈值图 $T$。
4. 由 $P$ 和 $F$ 计算得到二值图 $B$ 。

在训练期间，监督应用于概率图、阈值图和近似二值图。 其中概率图和近似二值图共享相同的监督。
在推理期间，可以通过框公式模块从近似二值图或概率图中轻松获得边界框。

## 3.1 二值化

### 3.1.1 标准二值化

### 3.1.2 可微二值化

可微二值化不仅能区分文本区域和背景，而且把邻近的文本区域也分开。
$$
\hat B_{i,j}=\frac 1 {1 + e^{-k(P_{i,j}-T_{i,j})}} = \frac 1 {1 + e^{-kx}}= \frac {e^{kx}} {1 + e^{kx}}
$$


其中：
$$
x =P_{i,j}-T_{i,j}
$$


损失函数：
$$
l_+=-log\frac 1 {1 + e^{-kx}} 
= log(1 + e^{-kx})
$$

$$
l_-=-log(1-\frac 1 {1 + e^{-kx}})=-log(\frac {e^{-kx}}{1+e^{-kx}}) = -log(\frac{1}{1 + e^{kx}}) = log(1+e^{kx})
$$





后边的式子是我加的，简化上边的公式后对数函数里没有分式，后边求导就变得容易多了。
$$
\frac {\partial l_+} {\partial x} = -kf(x)e^{-kx}
$$

$$
\frac {\partial l_-} {\partial x} = kf(x)
$$


![](assets/dbnet_bin.png)

- 正样本
  - 预测对了，则$x>0$，损失会很小
  - 预测错了，则$x<0$，损失会很大
- 负样本
  - 预测对了，则$x<0$，损失很小
  - 预测错了，则$x>0$，损失很大

膨胀之后的框内所有点都计算loss。

### 3.1.3 适合的阈值

### 3.1.4 可变形卷积

### 3.1.5 标签生成 

受PSENet启发，文本区域用一组分割表示。

### 3.1.6 优化

