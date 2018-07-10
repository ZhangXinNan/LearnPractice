[FPN（feature pyramid networks）算法讲解](https://blog.csdn.net/u014380165/article/details/72890275)
[论文 - Feature Pyramid Networks for Object Detection (FPN)](https://xmfbit.github.io/2018/04/02/paper-fpn/)

# 论文概述

作者提出的多尺度的目标检测算法：FPN。
（1）原来的检测只采用顶层特征做预测。
（2）但我们知道低层特征语义信息少，但是目标位置准确；高层特征语义信息丰富，但是目标位置粗略。
（3）有些算法采用多尺度融合的方式，但是一般是采用融合后的特征做预测。
本方法不同的是预测在不同特征层独立进行。

# 论文详解

