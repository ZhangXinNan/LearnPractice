[目标检测|YOLO原理与实现](https://zhuanlan.zhihu.com/p/32525231)

# 0 前言
近几年来，目标检测算法取得了很大的突破。比较流行的算法可以分为两类，一类是基于Region Proposal的R-CNN系算法（R-CNN，Fast R-CNN, Faster R-CNN），它们是two-stage的，需要先使用启发式方法（selective search）或者CNN网络（RPN）产生Region Proposal，然后再在Region Proposal上做分类与回归。而另一类是Yolo，SSD这类one-stage算法，其仅仅使用一个CNN网络直接预测不同目标的类别与位置。第一类方法是准确度高一些，但是速度慢，但是第二类算法是速度快，但是准确性要低一些。这可以在图2中看到。本文介绍的是Yolo算法，其全称是You Only Look Once: Unified, Real-Time Object Detection，其实个人觉得这个题目取得非常好，基本上把Yolo算法的特点概括全了：You Only Look Once说的是只需要一次CNN运算，Unified指的是这是一个统一的框架，提供end-to-end的预测，而Real-Time体现是Yolo算法速度快。这里我们谈的是Yolo-v1版本算法，其性能是差于后来的SSD算法的，但是Yolo后来也继续进行改进，产生了Yolo9000算法。本文主要讲述Yolo-v1算法的原理，特别是算法的训练与预测中详细细节，最后将给出如何使用TensorFlow实现Yolo算法。

# 1 滑动窗口与CNN
