## 问题：
 在做车系识别过程中，先用py-faster-rcnn检测物体位置，（py-faster-rcnn项目里有一个Caffe）。再用最新版本的caffe（caffe）训练（微调）一个分类器。现在想在一个程序里完成两步。都是调用 python接口，会出现如下错误：
```
GPU mode
[libprotobuf ERROR google/protobuf/text_format.cc:298] Error parsing text-format caffe.NetParameter: 6:15: Message type "caffe.LayerParameter" has no field named "input_param".
WARNING: Logging before InitGoogleLogging() is written to STDERR
F1118 15:47:17.330337 164439 upgrade_proto.cpp:68] Check failed: ReadProtoFromTextFile(param_file, param) Failed to parse NetParameter file: /home/zhangxin0627/gitlab/CarRecognition/_tmp/Train/20161022finetune_series/100/deploy1.prototxt
*** Check failure stack trace: ***
Aborted (core dumped)
```

## 原因：
py-faster-rcnn里用的是旧版本的caffe，不支持新版的input_param。



## 解决办法：

py-faster-rcnn/caffe-raster-rcnn/models/bvlc_googlenet/deploy.prototxt
```
name: "GoogleNet"
input: "data"
input_shape {
  dim: 10
  dim: 3
  dim: 224
  dim: 224
}

caffe/models/bvlc_googlenet/deploy.prototxt

name: "GoogleNet"
layer {
  name: "data"
  type: "Input"
  top: "data"
  input_param { shape: { dim: 10 dim: 3 dim: 224 dim: 224 } }
}
```
需要改成与旧版一致，即可。