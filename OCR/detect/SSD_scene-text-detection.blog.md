
# 1 前言

# 2 准备与转换数据集

## 2.1 将 ground truth 转换为 Pascal VOC XML 文件
见代码create_xml.py


## 2.2 生成训练图像与 XML 标签的位置文件
见代码create_train_test_file.py


## 2.3 生成 test name size 文本文件
见代码test_nmae_size.py


## 2.4 准备标签映射文件 labelmap
labelmap_voc.prototxt

# 3 生成 lmdb 数据库
见代码create_lmdbdata_scenetext.sh


# 4 训练模型

# 5 我的训练参数

# 6 用训练好的 model 进行 predict

# 7 参考