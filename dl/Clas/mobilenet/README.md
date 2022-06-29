

https://arxiv.org/pdf/1704.04861.pdf
https://arxiv.org/pdf/1801.04381.pdf

# code
[shicai/MobileNet-Caffe](https://github.com/shicai/MobileNet-Caffe)

# Depthwise separable convolution
MobileNet的基本单元是**深度级可分离卷积（depthwise separable convolution）**，其实这种结构之前已经被使用在Inception模型中。深度级可分离卷积其实是一种**可分解卷积操作（factorized convolutions）**，其可以分解为两个更小的操作：depthwise convolution和pointwise convolution，如图1所示。

Depthwise convolution和标准卷积不同，对于标准卷积其卷积核是用在所有的输入通道上（input channels），而depthwise convolution针对每个输入通道采用不同的卷积核，就是说一个卷积核对应一个输入通道，所以说depthwise convolution是depth级别的操作。

而pointwise convolution其实就是普通的卷积，只不过其采用1x1的卷积核。图2中更清晰地展示了两种操作。对于depthwise separable convolution，其首先是采用depthwise convolution对不同输入通道分别进行卷积，然后采用pointwise convolution将上面的输出再进行结合，这样其实整体效果和一个标准卷积是差不多的，但是会大大减少计算量和模型参数量。


这里简单分析一下depthwise separable convolution在计算量上与标准卷积的差别。假定输入特征图大小是 $D_F \times D_F \times M$ ，而输出特征图大小是 $D_F \times D_F \times N$ ，其中 $D_F$是特征图的width和height，这是假定两者是相同的，而$M$和$N$指的是通道数（channels or depth）。这里也假定输入与输出特征图大小（width and height）是一致的。采用的卷积核大小是尽管是特例，但是不影响下面分析的一般性。对于标准的卷积 $D_K \times D_K$ ，其计算量将是：
$$
D_K \times D_K \times M \times N \times D_F \times D_F
$$

而对于depthwise convolution其计算量为： $D_K \times D_K \times M \times D_F \times D_F$ ，pointwise convolution计算量是： $M \times N \times D_F \times D_F$ ，所以depthwise separable convolution总计算量是：

$$
D_K \times D_K \times M \times D_F \times D_F + M \times N \times D_F \times D_F
$$

可以比较depthwise separable convolution和标准卷积如下：

$$
\frac 1 N + \frac 1 {D_K^2}
$$

一般情况下 N 比较大，那么如果采用3x3卷积核的话，depthwise separable convolution相较标准卷积可以降低大约9倍的计算量。其实，后面会有对比，参数量也会减少很多。