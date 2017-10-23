# 安装
1. Any version of tensorflow version > 1.0 should be ok.
2. make lanms
```
cd lanms && make
```
3. 安装shapely
```
pip install shapely
```

# 测试
## 问题1
```
➜  EAST git:(zxdev_mac) ✗ python eval.py --test_data_path=/Users/zhangxin/pic/driving/good --checkpoint_path models/east_icdar2015_resnet_v1_50_rbox --output_path=tmp_good
find: -xtype: unknown primary or operator
make: `adaptor.so' is up to date.
('resnet_v1_50/block1', TensorShape([Dimension(None), Dimension(None), Dimension(None), Dimension(256)]))
('resnet_v1_50/block2', TensorShape([Dimension(None), Dimension(None), Dimension(None), Dimension(512)]))
('resnet_v1_50/block3', TensorShape([Dimension(None), Dimension(None), Dimension(None), Dimension(1024)]))
('resnet_v1_50/block4', TensorShape([Dimension(None), Dimension(None), Dimension(None), Dimension(2048)]))
Shape of f_0 (?, ?, ?, 2048)
Shape of f_1 (?, ?, ?, 512)
Shape of f_2 (?, ?, ?, 256)
Shape of f_3 (?, ?, ?, 64)
Shape of h_0 (?, ?, ?, 2048), g_0 (?, ?, ?, 2048)
Shape of h_1 (?, ?, ?, 128), g_1 (?, ?, ?, 128)
Shape of h_2 (?, ?, ?, 64), g_2 (?, ?, ?, 64)
Shape of h_3 (?, ?, ?, 32), g_3 (?, ?, ?, 32)
2017-10-17 06:46:03.265596: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-10-17 06:46:03.265635: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-10-17 06:46:03.265671: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-10-17 06:46:03.265689: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
Restore from models/east_icdar2015_resnet_v1_50_rbox/model.ckpt-49491
Find 38 images
7418 text boxes before nms
Fatal Python error: PyThreadState_Get: no current thread
[1]    5322 abort      /usr/local/Cellar/python/2.7.13/bin/python eval.py  --checkpoint_path  
```



解决方法：
Seem, there is many different python, so i got that error.