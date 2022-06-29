# tensorflow-fcn
是用tensorflow实现的全卷积网络。
反卷积层使用双线性升采样初始化。卷积层和FCN层参数使用VGG权重。
不需要运行caffe或者caffe-tensorflow。
使用这个网络之前先下载VGG16的npy文件。

# 依赖
```
pip install -r requirements.txt 
# or 
pip install numpy scipy pillow matplotlib
```

# TensorFlow 1.0rc
TensorFlow的版本需要大于等于1.0rc。

# 使用
