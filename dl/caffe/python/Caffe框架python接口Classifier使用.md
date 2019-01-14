
代码：/caffe-root/python/classify.py

# 1 model_def
传入的一般是deploy.prototxt，即部署时的网络结构文件。

# 2 pretrained_model
训练好的模型，例如:
../models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel\

# 3 center_only
* True 只从图像中心区域裁剪
* False 不同裁剪求平均

# 4 images_dim
缩放尺寸

# 5 mean_file
均值文件

# 6 input_scale
乘以此数结束预处理

# 7 raw_scale
预处理前，原始输入乘以此数


# 8 channel_sawp
交通通道顺序





