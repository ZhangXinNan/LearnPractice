原文地址：[利用FCN-8s网络训练自己数据集（NYUD为例）](https://zhuanlan.zhihu.com/p/28573998)

下载代码：
```
git clone https://github.com/shelhamer/fcn.berkeleyvision.org.git
```



下载预训练模型
```
cd /fcn.berkeleyvision.org/ilsvrc-nets
wget http://www.robots.ox.ac.uk/~vgg/software/very_deep/caffe/VGG_ILSVRC_16_layers.caffemodel
```

获取与其相对应的deploy文件：
```
wget https://gist.githubusercontent.com/ksimonyan/211839e770f7b538e2d8/raw/0067c9b32f60362c74f4c445a080beed06b07eb3/VGG_ILSVRC_16_layers_deploy.prototxt
```

下载数据：
```
cd data/nyud/
wget http://people.eecs.berkeley.edu/~sgupta/cvpr13/data.tgz
tar -xvf data.tgz
```

其中data文件夹中有三个子文件夹：benchmarkData, colorImage, pointCloud. 其中benchmarkData/groundTruth中储存这所有我们需要的分割的真值，
colorImage文件夹储存着原始的RGB文件．
由于源代码设置的groundTruth路径和现有的路径不一样，所以我们要把groundTruth文件copy到指定路径：
```
mkdir segmentation
cp data/benchmarkData/groundTruth/*.mat segmentation/
```

同时，我们要合并train.txt和val.txt: 在nyud文件夹中新建一个空白的.txt文件并命名为trainval.txt，然后将train.txt和val.txt中的内容Copy过去．这个时候nyud文件夹应为是这个样子：
```
cat train.txt val.txt > trainval.txt
```
