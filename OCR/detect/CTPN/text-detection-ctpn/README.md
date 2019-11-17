tensorflow实现：[eragonruan/text-detection-ctpn](https://github.com/eragonruan/text-detection-ctpn)
caffe实现：[tianzhi0549/CTPN](https://github.com/tianzhi0549/CTPN)

参考博客：
[论文阅读与实现--CTPN](http://slade-ruan.me/2017/10/22/text-detection-ctpn/)


文本行检测中文本行的特点是长条状，常用的检测算法（Faster RCNN等）不适用，怎么才能生成好的text proposal ？检测一个一个小的，固定宽度的文本段，然后再后处理部分再将这些小的文本段连接起来，得到文本行。

具体的说，作者的基本想法就是去预测文本的竖直方向上的位置，水平方向的位置不预测。因此作者提出了一个vertical anchor的方法。与faster rcnn中的anchor类似，但是不同的是，vertical anchor的宽度都是固定好的了，论文中的大小是16个像素。而高度则从11像素到273像素变化，总共10个anchor.

同时，对于水平的文本行，其中的每一个文本段之间都是有联系的，因此作者采用了CNN+RNN的一种网络结构，检测结果更加鲁棒。


