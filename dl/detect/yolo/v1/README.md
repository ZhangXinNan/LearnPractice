# 0 参考
## 0.1 参考博客
* [目标检测（九）--YOLO v1,v2,v3](https://blog.csdn.net/App_12062011/article/details/77554288)
* [[目标检测]YOLO原理](https://www.cnblogs.com/fariver/p/7446921.html)
* [论文阅读笔记：You Only Look Once: Unified, Real-Time Object Detection](https://blog.csdn.net/tangwei2014/article/details/50915317)
* [目标检测|YOLO原理与实现](https://zhuanlan.zhihu.com/p/32525231)
* [目标检测|YOLOv2原理与实现(附YOLOv3)](https://zhuanlan.zhihu.com/p/35325884)
* [目标检测算法之YOLO](https://zhuanlan.zhihu.com/p/38125721)

## 0.2 开源实现：
* [https://github.com/gliese581gg/YOLO_tensorflow](https://github.com/gliese581gg/YOLO_tensorflow)




# 1. 核心思想
利用整张图作为网络的输入，直接在输出层回归bounding box的位置和bounding box所属的类别。

# 2. 实现
（1）一幅图像分成S*S个表格（grid cell）,如果某个object的中心落在这个网格中，这个网格就负责预测这个object。

（2）每个网络预测B个bounding box，包括自身位置和confidence。这个confidence包含box含有object的置信度和box预测的有多准两重信息，$ Pr(Object) * IOU^truth_pred $。

如果有object落在一个grid cell里，第一项取1，否则取0 。第二项是预测的bounding box与ground truth之间的IOU值。

（3）每个bounding box预测(x,y,w,h)和confidence5个值，每个网格还要预测一个类别。所以每个网络预测B个bounding box和C个类别。输出为 S*S*(5*B+C)。

（4）在test的时候，每个网格预测的class信息和bounding box预测的confidence信息相乘，就得到每个bounding box的class-specific confidence score:
$ Pr(Class_i|Object) * Pr(Object) * IOU^truth_pred = Pr(Class_i) * IOU^truth_pred $

（5）设置阈值，去除得分低的boxes，对保留的boxes进行NMS处理。


# 3 实现细节


# 4 YOLO的缺点
* 近的物体、小的物体检测效果不好。每个网络中只预测两个框、并只属于一个类。
* 同一类物体不常见长宽比泛化能力差
* 由于损失函数的问题，定位误差影响检测效果。

