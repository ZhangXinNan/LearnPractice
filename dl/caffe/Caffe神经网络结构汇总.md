[Caffe神经网络结构汇总](http://noahsnail.com/2017/06/01/2017-6-1-Caffe%E7%BD%91%E7%BB%9C%E7%BB%93%E6%9E%84%E6%80%BB%E7%BB%93/)

文章作者：Tyan
博客：noahsnail.com  |  CSDN  |  简书

自2012年Alexnet赢得了ImageNet竞赛以来，深度学习（神经网络）得到了飞速发展，产生了许多的神经网络结构，本文主要总结Caffe中使用的神经网络(分类的神经网络)，本文的神经网络作者都使用Caffe训练过，并在Kaggle的Intel癌症预测比赛中进行了测试与使用（top 8%）。

1. Alexnet
Alexnet，2012年ImageNet竞赛冠军，深度学习的里程碑。

网络结构地址：https://github.com/BVLC/caffe/tree/master/models/bvlc_alexnet

预训练模型地址：http://dl.caffe.berkeleyvision.org/bvlc_alexnet.caffemodel

2. Squeezenet
Squeezenet设计目标不是为了提高识别的准确率，而是希望简化网络复杂度。squeezenet的模型结构确实很小，没压缩的情况下才5M左右，而且识别的精度还可以。

网络结构地址：https://github.com/DeepScale/SqueezeNet

预训练模型地址：https://github.com/DeepScale/SqueezeNet

3. VGG系列
VGG和GoogLenet是2014年imagenet竞赛的双雄，VGG主要分为VGG16和VGG19。其网络结构与预训练模型的地址如下：

VGG16的网络结构：https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md

VGG16的预训练模型： http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel

VGG19的网络结构：https://gist.github.com/ksimonyan/3785162f95cd2d5fee77#file-readme-md

VGG19的预训练模型：http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_19_layers.caffemodel

备注：上面的网络结构需要进行细微调整才能在Caffe中直接训练，主要是网络结构中的Type类型。

4. Resnet系列
Resnet网络，2015年ImageNet竞赛冠军，网络结构主要分为Resnet-50、Resnet-101、Resnet-152三种，当然也有一些其它的结构，例如Resnet-18，Resnet-14。

Github地址：https://github.com/KaimingHe/deep-residual-networks

Resnet-50、Resnet-101、Resnet-152的网络结构及预训练模型的下载地址：https://onedrive.live.com/?authkey=%21AAFW2-FVoxeVRck&id=4006CBB8476FF777%2117887&cid=4006CBB8476FF777

5. Inception系列
Inception系列是Google发明的一系列神经网络结构。

Inception-v1：

Inception-v1，即大名鼎鼎的GoogLenet，2014年ImageNet竞赛冠军。

网络结构地址：https://github.com/BVLC/caffe/tree/master/models/bvlc_googlenet

预训练模型地址：http://dl.caffe.berkeleyvision.org/bvlc_googlenet.caffemodel

Inception-v2：

即Inception V1 + Batch Normalization。

网络结构地址：https://github.com/pertusa/InceptionBN-21K-for-Caffe

预训练模型地址：http://www.dlsi.ua.es/~pertusa/deep/Inception21k.caffemodel

Inception-v3：

网络结构地址：https://pan.baidu.com/s/1boC0HEf#list/path=%2F

预训练模型地址：https://pan.baidu.com/s/1boC0HEf#list/path=%2F

Inception-v4：

网络结构地址：https://pan.baidu.com/s/1c6D150#list/path=%2F

预训练模型地址：https://pan.baidu.com/s/1c6D150#list/path=%2F

Inception-resnet-v2：

网络结构地址：https://pan.baidu.com/s/1jHPJCX4#list/path=%2F

预训练模型地址：https://pan.baidu.com/s/1jHPJCX4#list/path=%2F