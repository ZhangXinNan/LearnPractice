
# 0 参考
## 0.1 代码
[marvis/pytorch-yolo2](https://github.com/marvis/pytorch-yolo2)

## 0.2 参考博客
* [YOLO2](https://zhuanlan.zhihu.com/p/25167153)
* [YOLOv2 论文笔记](https://blog.csdn.net/jesse_mx/article/details/53925356)
* [目标检测（九）--YOLO v1,v2,v3](https://blog.csdn.net/App_12062011/article/details/77554288)

# 1 摘要
1. 提出YOLOv2：代表着目前业界最先进物体检测的水平，它的速度要快过其他检测系统（FasterR-CNN，ResNet，SSD），使用者可以在它的速度与精确度之间进行权衡。
2. 提出YOLO9000：这一网络结构可以实时地检测超过9000种物体分类，这归功于它使用了WordTree，通过WordTree来混合检测数据集与识别数据集之中的数据。
3. 提出了一种新的联合训练算法（ Joint Training Algorithm ），使用这种联合训练技术同时在ImageNet和COCO数据集上进行训练。YOLO9000进一步缩小了监测数据集与识别数据集之间的代沟。


# 2 简介
目前的检测数据集（DetectionDatasets）有很多限制，分类标签的信息太少，图片的数量小于分类数据集（Classiﬁcation Datasets），而且检测数据集的成本太高，使其无法当作分类数据集进行使用。而现在的分类数据集却有着大量的图片和十分丰富分类信息。
文章提出了一种新的训练方法–联合训练算法，这种算法可以把这两种的数据集混合到一起。使用一种分层的观点对物体进行分类，用巨量的分类数据集数据来扩充检测数据集，从而把两种不同的数据集混合起来。
联合训练算法的基本思路就是：**同时在检测数据集和分类数据集上训练物体检测器（Object Detectors ），用检测数据集的数据学习物体的准确位置，用分类数据集的数据来增加分类的类别量、提升健壮性**。
YOLO9000就是使用联合训练算法训练出来的，他拥有9000类的分类信息，这些分类信息学习自ImageNet分类数据集，而物体位置检测则学习自COCO检测数据集。


# 3 better

## 3.1 Batch Normalization

使用Batch Normalization对网络进行优化，让网络提高了收敛性，同时还消除了对其他形式的正则化（regularization）的依赖。通过对YOLO的每一个卷积层增加Batch Normalization，最终使得mAP提高了2%，同时还使model正则化。使用Batch Normalization可以从model中去掉Dropout，而不会产生过拟合。

## 3.2 High resolution classifier

目前业界标准的检测方法，都要先把分类器（classiﬁer）放在ImageNet上进行预训练。从Alexnet开始，大多数的分类器都运行在小于256*256的图片上。而现在YOLO从224*224增加到了448*448，这就意味着网络需要适应新的输入分辨率。
为了适应新的分辨率，YOLO v2的分类网络以448*448的分辨率先在ImageNet上进行Fine Tune，Fine Tune10个epochs，让网络有时间调整他的滤波器（filters），好让其能更好的运行在新分辨率上，还需要调优用于检测的Resulting Network。最终通过使用高分辨率，mAP提升了4%。

## 3.3 Convolution with anchor boxes

YOLO一代包含有全连接层，从而能直接预测Bounding Boxes的坐标值。 Faster R-CNN的方法只用卷积层与Region Proposal Network来预测Anchor Box的偏移值与置信度，而不是直接预测坐标值。作者发现通过预测偏移量而不是坐标值能够简化问题，让神经网络学习起来更容易。
所以最终YOLO去掉了全连接层，使用Anchor Boxes来预测 Bounding Boxes。作者去掉了网络中一个Pooling层，这让卷积层的输出能有更高的分辨率。收缩网络让其运行在416*416而不是448*448。由于图片中的物体都倾向于出现在图片的中心位置，特别是那种比较大的物体，所以有一个单独位于物体中心的位置用于预测这些物体。YOLO的卷积层采用32这个值来下采样图片，所以通过选择416*416用作输入尺寸最终能输出一个13*13的Feature Map。 使用Anchor Box会让精确度稍微下降，但用了它能让YOLO能预测出大于一千个框，同时recall达到88%，mAP达到69.2%。

## 3.4 Dimension clusters

之前Anchor Box的尺寸是手动选择的，所以尺寸还有优化的余地。 为了优化，在训练集（training set）Bounding Boxes上跑了一下k-means聚类，来找到一个比较好的值。
如果我们用标准的欧式距离的k-means，尺寸大的框比小框产生更多的错误。因为我们的目的是提高IOU分数，这依赖于Box的大小，所以距离度量的使用：

$$ d(box, centroid) = 1 - IOU(box, centroid) $$

通过分析实验结果（Figure 2），左图：在model复杂性与high recall之间权衡之后，选择聚类分类数K=5。右图：是聚类的中心，大多数是高瘦的Box。
Table1是说明用K-means选择Anchor Boxes时，当Cluster IOU选择值为5时，AVG IOU的值是61，这个值要比不用聚类的方法的60.9要高。选择值为9的时候，AVG IOU更有显著提高。总之就是说明用聚类的方法是有效果的。

## 3.5 Direct location prediction

用Anchor Box的方法，会让model变得不稳定，尤其是在最开始的几次迭代的时候。大多数不稳定因素产生自预测Box的（x,y）位置的时候。按照之前YOLO的方法，网络不会预测偏移量，而是根据YOLO中的网格单元的位置来预测坐标，这就让Ground Truth的值介于0到1之间。而为了让网络的结果能落在这一范围内，网络使用一个 Logistic Activation来对于网络预测结果进行限制，让结果介于0到1之间。 网络在每一个网格单元中预测出5个Bounding Boxes，每个Bounding Boxes有五个坐标值tx，ty，tw，th，t0，他们的关系见下图（Figure3）。假设一个网格单元对于图片左上角的偏移量是cx，cy，Bounding Boxes Prior的宽度和高度是pw，ph，那么预测的结果见下图右面的公式：


## 3.6 Fine-Grained Features

YOLO修改后的Feature Map大小为13*13，这个尺寸对检测图片中尺寸大物体来说足够了，同时使用这种细粒度的特征对定位小物体的位置可能也有好处。Faster R-CNN、SSD都使用不同尺寸的Feature Map来取得不同范围的分辨率，而YOLO采取了不同的方法，YOLO加上了一个Passthrough Layer来取得之前的某个26*26分辨率的层的特征。这个Passthrough layer能够把高分辨率特征与低分辨率特征联系在一起，联系起来的方法是把相邻的特征堆积在不同的Channel之中，这一方法类似与Resnet的Identity Mapping，从而把26*26*512变成13*13*2048。YOLO中的检测器位于扩展后（expanded ）的Feature Map的上方，所以他能取得细粒度的特征信息，这提升了YOLO 1%的性能。


## 3.7 Multi-ScaleTraining

作者希望YOLO v2能健壮的运行于不同尺寸的图片之上，所以把这一想法用于训练model中。
区别于之前的补全图片的尺寸的方法，YOLO v2每迭代几次都会改变网络参数。每10个Batch，网络会随机地选择一个新的图片尺寸，由于使用了下采样参数是32，所以不同的尺寸大小也选择为32的倍数{320，352…..608}，最小320*320，最大608*608，网络会自动改变尺寸，并继续训练的过程。
这一政策让网络在不同的输入尺寸上都能达到一个很好的预测效果，同一网络能在不同分辨率上进行检测。当输入图片尺寸比较小的时候跑的比较快，输入图片尺寸比较大的时候精度高，所以你可以在YOLO v2的速度和精度上进行权衡。
Figure4，Table 3：在voc2007上的速度与精度



# 4 faster
YOLO使用的是GoogleLeNet，比VGG-16快，YOLO完成一次前向过程只用8.52 billion 运算，而VGG-16要30.69billion，但是YOLO精度稍低于VGG-16。

## 4.1 Draknet19

YOLO v2基于一个新的分类model，有点类似与VGG。YOLO v2使用3*3filter，每次Pooling之后都增加一倍Channels的数量。YOLO v2使用全局平均Pooling，使用Batch Normilazation来让训练更稳定，加速收敛，使model规范化。
最终的model–Darknet19，有19个卷积层和5个maxpooling层，处理一张图片只需要5.58 billion次运算，在ImageNet上达到72.9%top-1精确度，91.2%top-5精确度。

## 4.2 Training for classiﬁcation

网络训练在 ImageNet 1000类分类数据集，训练了160epochs，使用随机梯度下降，初始学习率为0.1， polynomial
rate decay with a power of 4, weight decay of 0.0005 and momentum of 0.9 。训练期间使用标准的数据扩大方法：随机裁剪、旋转、变换颜色（hue）、变换饱和度（saturation）， 变换曝光度（exposure shifts）。
在训练时，把整个网络在更大的448*448分辨率上Fine Turnning 10个 epoches，初始学习率设置为0.001，这种网络达到达到76.5%top-1精确度，93.3%top-5精确度。

## 4.3 Training for detection

网络去掉了最后一个卷积层，而加上了三个3*3卷积层，每个卷积层有1024个Filters，每个卷积层紧接着一个1*1卷积层， with
the number of outputs we need for detection。
对于VOC数据，网络预测出每个网格单元预测五个Bounding Boxes，每个Bounding Boxes预测5个坐标和20类，所以一共125个Filters，增加了Passthough层来获取前面层的细粒度信息，网络训练了160epoches，初始学习率0.001，dividing it by 10 at 60 and 90 epochs，a weight decay of 0.0005 and momentum of 0.9，数据扩大方法相同，对COCO与VOC数据集的训练对策相同。


# 5 stronger



# 6 总结
YOLO v2 代表着目前最先进物体检测的水平，在多种监测数据集中都要快过其他检测系统，并可以在速度与精确度上进行权衡。

YOLO 9000 的网络结构允许实时地检测超过9000种物体分类，这归功于它能同时优化检测与分类功能。使用WordTree来混合来自不同的资源的训练数据，并使用联合优化技术同时在ImageNet和COCO数据集上进行训练，YOLO9000进一步缩小了监测数据集与识别数据集之间的大小代沟。

文章还提出了WordTree，数据集混合训练，多尺寸训练等全新的训练方法。







```
# 检测不到
python detect_cpu.py ~/data_public/yolo/darknet/yolo2coco/yolov2-tiny.cfg ~/data_public/yolo/darknet/yolo2coco/yolov2-tiny.weights data/dog.jpg
# 正常，检测狗、自行车、车
python detect_cpu.py ~/data_public/yolo/darknet/yolo2coco/yolov2.cfg ~/data_public/yolo/darknet/yolo2coco/yolov2.weights data/dog.jpg
# 没检测到
python detect_cpu.py ~/data_public/yolo/darknet/yolo2voc/yolov2-voc.cfg ~/data_public/yolo/darknet/yolo2voc/yolov2-voc.weights data/dog.jpg
# 检测到狗和车
python detect_cpu.py ~/data_public/yolo/darknet/yolo2voc/yolov2-tiny-voc.cfg ~/data_public/yolo/darknet/yolo2voc/yolov2-tiny-voc.weights data/dog.jpg
```