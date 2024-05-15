# 0 介绍
根据李思琦操作步骤总结如下
* 原项目地址：[weiliu89/caffe](https://github.com/weiliu89/caffe/tree/ssd)
* 所用数据地址：[Robust Reading Competition Challenge 2: Reading Text in Scene Images](http://robustreading.opendfki.de/trac/wiki/SceneText) 本文以此数据为例，生成ssd训练所用的lmdb格式。
* 使用ssd进行文本检测的项目：[chenxinpeng/SSD_scene_text_detection](https://github.com/chenxinpeng/SSD_scene_text_detection)
* 使用ssd进行文本检测的博客 [SSD: Signle Shot Detector 用于自然场景文字检测](http://blog.csdn.net/u010167269/article/details/52851667)

注意：我没有直接将此项目中文件放入ssd[weiliu89/caffe](https://github.com/weiliu89/caffe/tree/ssd)的目录中，而是把此项目放入ssd同级目录下，这样比较清楚。当然路径要注意修改。

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
生成的文件trainval.txt和test.txt直接放到了data目录下
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


## 2.3 生成labelmap_voc.prototxt
创建文件labelmap_voc.prototxt，填写如下：
```
item {
  name: "none_of_the_above"
  label: 0
  display_name: "background"
}
item {
  name: "object"
  label: 1
  display_name: "text"
}
```
## 3 生成lmdb
```
python create_lmdbdata_scenetext.sh
```