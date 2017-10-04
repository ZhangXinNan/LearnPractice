# 0 介绍

根据李斯琦操作步骤总结如下：

* 原项目地址：[weiliu89/caffe](https://github.com/weiliu89/caffe/tree/ssd)
* 所用数据地址：[Robust Reading Competition Challenge 2: Reading Text in Scene Images](http://robustreading.opendfki.de/trac/wiki/SceneText) 本文以此数据为例，生成ssd训练所用的lmdb格式。
* 使用ssd进行文本检测的项目：[chenxinpeng/SSD_scene_text_detection](https://github.com/chenxinpeng/SSD_scene_text_detection)
* 使用ssd进行文本检测的博客 [SSD: Signle Shot Detector 用于自然场景文字检测](http://blog.csdn.net/u010167269/article/details/52851667)

注意：
（1）我没有直接将此项目中文件放入ssd [weiliu89/caffe](https://github.com/weiliu89/caffe/tree/ssd)的目录中，而是把此项目放入ssd同级目录下，这样比较清楚。当然路径要注意修改。
（2）所有代码及说明已经放到github上。地址：[ZhangXinNan/SSD_scene_text_detection](https://github.com/ZhangXinNan/SSD_scene_text_detection)
（3）我的目录结构如下：
```
github
    caffe_ssd
    SSD_scene_text_detection
```


# 1 SceneText数据介绍
下载数据解压后，有两个文件夹，test-textloc-gt和train-textloc，我们把它放到 xx/SSD_scene_text_detection/data/scenetext下边。目录结构如下
```
SSD_scene_text_detection
    data
        scenetext
            test-textloc-gt
            train-textloc
```

那两个文件夹下分别有xxx.jpg和gt_xxx.txt，xxx代表一个数字，gt_xxx.txt代表xxx.jpg所对应的标注数据，例如less data/scenetext/train-textloc/gt_100.txt 
```
158,128,412,182,"Footpath"
442,128,501,170,"To"
393,198,488,240,"and"
63,200,363,242,"Colchester"
71,271,383,313,"Greenstead"
```
每一行代表一个字符区域的标信息，每行有5列，用逗号分隔，前4列代表坐标，最后1列代表字符内容。

# 2 生成转lmdb所用文件
## 2.1 生成trainval.txt和test.txt
### 2.1.1 生成标注的xml文件
先将给定的 gt_**.txt 标签文件转换为 Pascal VOC XML 格式。
见代码create_xml.py
代码中是把xml文件也放到了jpg和txt文件所放目录。例如：
```
data/scenetext/test-textloc-gt/156.jpg
data/scenetext/test-textloc-gt/156.xml
data/scenetext/test-textloc-gt/gt_156.txt
```

### 2.1.2 生成文件列表
见代码create_train_test_file.py
生成的文件trainval.txt和test.txt直接放到了data/scenetext目录下
```
SSD_scene_text_detection
    data
        scenetext
            test-textloc-gt
            train-textloc
            test.txt
            trainval.txt
```

## 2.2 生成test_name_size.txt
见代码test_name_size.py，得到train_name_size.txt和test_name_size.txt
```
SSD_scene_text_detection
    data
        scenetext
            test-textloc-gt
            train-textloc
            test.txt
            trainval.txt
            test_name_size.txt
            train_name_size.txt
```


## 2.3 生成labelmap_voc_scenetext.prototxt
创建文件labelmap_voc_scenetext.prototxt，填写如下：
```
item {
  name: "none_of_the_above"
  label: 0
  display_name: "background"
}
item {
  name: "text"
  label: 1
  display_name: "text"
}
```
# 3 生成lmdb
```
sh create_lmdbdata_scenetext.sh
```
注意:
1. 修改一下caffe_root的路径（编译caffe版ssd的目录）。
例如：caffe_root=/data/zhangxin/github/caffe_ssd
2. 设置caffe/python的目录
例如： export PYTHONPATH=/data/dmcvcache/zhangxin/caffe_ssd/python
3. 如果遇到ImportError: No module named skimage.io
则：安装 一下， pip install scikit-image
4. 需要在caffe_ssd/models/VGGNet/目录下存放下载好的VGG_ILSVRC_16_layers_fc_reduced.caffemodel文件。
5. 错误：
```
F0628 14:18:57.290895 33280 relu_layer.cu:26] Check failed: error == cudaSuccess (11 vs. 0)  invalid argument
*** Check failure stack trace: ***
    @     0x7fdf009ffe6d  (unknown)
    @     0x7fdf00a01ced  (unknown)
    @     0x7fdf009ffa5c  (unknown)
    @     0x7fdf00a0263e  (unknown)
F0628 14:18:57.298449 33281 relu_layer.cu:26] Check failed: error == cudaSuccess (11 vs. 0)  invalid argument
*** Check failure stack trace: ***
    @     0x7fdf0a9b0ea0  caffe::ReLULayer<>::Forward_gpu()
    @     0x7fdf009ffe6d  (unknown)
    @     0x7fdf0a796435  caffe::Net<>::ForwardFromTo()
    @     0x7fdf00a01ced  (unknown)
    @     0x7fdf0a7967a7  caffe::Net<>::Forward()
    @     0x7fdf009ffa5c  (unknown)
F0628 14:18:57.298449 33281 relu_layer.cu:26] Check failed: error == cudaSuccess (11 vs. 0)  invalid argumentF0628 14:18:57.304498 33225 relu_layer.cu:26] Check failed: error == cudaSuccess (11 vs. 0)  invalid argument
*** Check failure stack trace: ***
    @     0x7fdf00a0263e  (unknown)
    @     0x7fdf0a907ba8  caffe::Solver<>::Step()
    @     0x7fdf009ffe6d  (unknown)
    @     0x7fdf0a90da66  caffe::P2PSync<>::InternalThreadEntry()
    @     0x7fdf00a01ced  (unknown)
    @     0x7fdf0a9b0ea0  caffe::ReLULayer<>::Forward_gpu()
    @     0x7fdf0a8feea0  caffe::InternalThread::entry()
    @     0x7fdf009ffa5c  (unknown)
    @     0x7fdf0a796435  caffe::Net<>::ForwardFromTo()
    @     0x7fdefed0224a  (unknown)
    @     0x7fdf00a0263e  (unknown)
    @     0x7fdefb853df3  start_thread
    @     0x7fdf0a7967a7  caffe::Net<>::Forward()
    @     0x7fdf0a9b0ea0  caffe::ReLULayer<>::Forward_gpu()
    @     0x7fdefb5813dd  __clone
^C[1]+  Done                    nohup python ssd_icdar_scenetext.py

You have mail in /var/spool/mail/root
```
解决方法：
```
I added the following lines to commands using multiple “arch” flags in Nvidia's NVCC compiler, and the error does not occur anymore.

-gencode=arch=compute_20,code=\"sm_20,compute_20\"
-gencode=arch=compute_30,code=\"sm_30,compute_30\"
-gencode=arch=compute_35,code=\"sm_35,compute_35\"
-gencode=arch=compute_50,code=\"sm_50,compute_50\" 

```

# 4 训练
```
python ssd_icdar_scenetext.py
```

# 5 检测
使用ssd_detect.py，根据caffe_ssd目录下 examples/ssd_detect.ipynb 重写。
使用方法：
```
python ssd_detect.py \
    --gpu_id 0 \
    --labelmap_file data/scenetext/labelmap_voc_scenetext.prototxt \
    --model_def models/VGGNet/scenetext/SSD_300x300/deploy.prototxt \
    --image_resize 300 \
    --model_weights models/VGGNet/scenetext/SSD_300x300/VGG_scenetext_SSD_300x300_iter_50000.caffemodel \
    --image_file data/scenetext/test-textloc-gt/101.jpg

```