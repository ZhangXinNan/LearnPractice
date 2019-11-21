

该网络具有很大的意义，第一次将人脸检测和人脸特征点定位结合起来，而得到的人脸特征点又可以实现人脸校正。该算法由3个阶段组成：
* 第一阶段，通过CNN快速产生候选框体。
* 第二阶段，通过更复杂一点的CNN精炼候选窗体，丢弃大量的重叠窗体。
* 第三阶段，使用更强大的CNN，实现候选窗体去留，同时回归5个面部关键点。



# stage 0: Image pyramid
MTCNN网络在经过3个卷积网络处理之前，先进行了多尺度变换，将一幅人脸图像缩放为不同尺寸的图片，这样就构成了图像金字塔。然后这些不同尺度的图像作为3个阶段的输入数据进行训练，这样可以令MTCNN检测到不同尺寸的人脸。


# stage 1: Proposal Network (P-Net)
PNet(Proposal Network)的卷积神经网络，获得候选窗体和边界回归向量。同时，候选窗体根据边界框进行校准。然后利用非极大值抑制去除重叠窗体。 

# stage 2: Refine Network (R-Net)
R-Net(Refine Network)卷积神经网络进行操作，将经过P-Net确定的包含候选窗体的图片在R-Net中训练，最后使用全连接网络进行分类。利用边界框向量微调候选窗体，最后还是利用非极大值抑制算法去除重叠窗体。


# stage 3: Output Network (O-Net)
使用Onet(Output Network)卷积神经网络进行操作，该网络比R-Net多一层卷积层，功能与R-Net类似，只是在去除重叠候选窗口的同时标定5个人脸关键点位置。

# 参考
1. [MTCNN（Multi-task convolutional neural networks）人脸对齐](https://blog.csdn.net/qq_14845119/article/details/52680940)
2. [MTCNN算法](https://blog.csdn.net/lff1208/article/details/77247430)
3. [MTCNN-将多任务级联卷积神经网络用于人脸检测和对齐](https://blog.csdn.net/lff1208/article/details/77328357)
4. [精读深度学习论文(23) MTCNN](https://zhuanlan.zhihu.com/p/38520597)
5. [人脸识别系列三 | MTCNN算法详解上篇](https://zhuanlan.zhihu.com/p/92678271)
6. [人脸识别系列三 | MTCNN算法详解下篇](https://zhuanlan.zhihu.com/p/93006161)


# paper: 
[spl](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf)


