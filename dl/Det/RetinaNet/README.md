参考：
[Focal Loss论文阅读 - Focal Loss for Dense Object Detection](https://xmfbit.github.io/2017/08/14/focal-loss-paper/)
[如何评价Kaiming的Focal Loss for Dense Object Detection](https://www.zhihu.com/question/63581984)



# 为什么有Focal Loss
检测算法分为两类：
* one-stage，YOLO SSD。输出一个稠密的proposal，速度快，精度不够高。
* two-stage, RCNN系列。特点：在一个稀疏的候选目标中进行分类，通过前面的proposal过程实现的，例如Selective Search或者RPN。

论文作者指出，稠密分类的精度不高，核心问题是稠密proposal中前景和背景的极度不平衡。大量的负样本在loss中占据了很大比重，使得有用的loss占据了很大比重，有用的loss不能传回来。

# 物体检测的两种主流方法
R-CNN系列方法中，正负类别不平衡问题在proposal解决了。
YOLO/SSD大量的负样本带来两个问题：
* 过于简单，有效信息过少，使得训练效率低
* 简单的负样本在训练 过程中有压倒性优势，使得模型发生退化。





