[全卷积网络 FCN 详解](https://zhuanlan.zhihu.com/p/30195134)

# CNN与FCN


CNN网络在卷积层之后接上若干个全连接层，将卷积层的feature map映射成一个固定长度的特征向量。
FCN进行像素级的分类，从而解决语义级别的图像分割问题（semantic segmentation）。
FCN可以接受任意尺寸的输入图像，采用反卷积对最后一个卷积层的feature map进行上采样，使它恢复到输入图像相同的尺寸，从而对每一个像素都产生一个预测，同时保留了原始输入图像的空间信息。