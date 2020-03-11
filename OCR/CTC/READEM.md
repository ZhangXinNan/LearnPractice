算法介绍：
[白话CTC(connectionist temporal classification)算法讲解](https://blog.csdn.net/luodongri/article/details/77005948)
[语音识别中的CTC算法的基本原理解释](https://blog.csdn.net/luodongri/article/details/80100297)
[Sequence Modeling With CTC](https://distill.pub/2017/ctc/)
[基于CTC的语音识别基础与实现](https://zhuanlan.zhihu.com/p/33464788)
[CTC算法详解](https://www.jianshu.com/p/0cca89f64987)

代码：
[senlinuc/caffe_ocr](https://github.com/senlinuc/caffe_ocr)



CTC(Connectionist temporal classification)
---------
# 前言
语言模型(Language Model)
声学模型（Acoustic Model）
音素模型（Phoneme Model）


传统的方法需要知道每一帧的数据对应哪个发音音素。CTC作为损失函数的声学模型，是一种完全端对端的声学模型训练，不需要预先对数据进行对齐，只需要一个输入序列和一个输出序列即可以训练。

CTC 计算一种损失，主要优点可以对没有对齐的数据进行自动对齐。
一般译为联结主义时间分类器。

既然CTC的方法是关心一个输入序列到一个输出序列的结果，那么它只会关心预测输出的序列是否和真实的序列是否接近（相同），而不会关心预测输出序列中每个结果在时间点上是否和输入的序列正好对齐。 

CTC引入了blank（该帧没有预测值），每个预测的分类对应的一整段语音中的一个spike（尖峰），其他不是尖峰的位置认为是blank。对于一段语音，CTC最后的输出是spike（尖峰）的序列，并不关心每一个音素持续了多长时间。 
如图2所示，拿前面的nihao的发音为例，进过CTC预测的序列结果在时间上可能会稍微延迟于真实发音对应的时间点，其他时间点都会被标记会blank。

训练集S={(x1,z1),(x2,z2),(x3,z3),...}
其中一个样本(x,z)，
x={x1,x2,...,x_T}，对于一段语音信号，以25ms为单位分成若干小段，每段做MFCC后得到的结果。
z=(z1,z2,z3,...,z_u)，表示该训练语音对应的音素信息。
例如发音为“你好”的一段语音经过MFCC后得到特征x，对应的音素特征是z={n,i,h,a,o}
特征x经过DNN特征提取后，再经过一个softmax层，得到音素的后验概率y。y_k^t表示在t时刻，发音为音素k的概率。


blank 并不一定是空格，也可能 是被 网络抑制的信号。

valid Alignments 
invalid Alignments

所有 有效的alignments加起来的概率。
CTC假设每个时刻不相关。
