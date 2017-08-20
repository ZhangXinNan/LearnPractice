 [在Caffe中使用Baidu warpctc实现CTC Loss的计算](https://xmfbit.github.io/2017/02/22/warpctc-caffe/)

代码：[meijieru/crnn.pytorch](https://github.com/xmfbit/warpctc-caffe)

(1)
```
在ctc_loss_layer.cpp中加入头文件包含#include <numeric>
```
解决方法：
```
在ctc_loss_layer.cpp中加入头文件包含#include <numeric>
```

(2)python运行崩溃
```
➜  warpctc-caffe git:(zxdev) ✗ ./examples/warpctc_captcha/train.sh
[libprotobuf ERROR google/protobuf/descriptor_database.cc:57] File already exists in database: caffe.proto
[libprotobuf FATAL google/protobuf/descriptor.cc:1018] CHECK failed: generated_database_->Add(encoded_file_descriptor, size): 
libc++abi.dylib: terminating with uncaught exception of type google::protobuf::FatalException: CHECK failed: generated_database_->Add(encoded_file_descriptor, size): 

```


# 142
```
(venv2) [zhangxin0627@l22-240-142 warpctc-caffe-master]$ python examples/warpctc_captcha/generate_captcha.py
Process Process-2:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 258, in _bootstrap
    self.run()
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
Process Process-1:
  File "examples/warpctc_captcha/generate_captcha.py", line 30, in generate_image
Traceback (most recent call last):
    image.write(label_seq, os.path.join(img_path, '%05d-'%idx + label_seq + '.png'))
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 258, in _bootstrap
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 58, in write
    im = self.generate_image(chars)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 228, in generate_image
    self.create_noise_curve(im, color)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 137, in create_noise_curve
    Draw(image).arc(points, start, end, fill=color)
  File "/usr/lib64/python2.7/PIL/ImageDraw.py", line 161, in arc
    self.run()
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "examples/warpctc_captcha/generate_captcha.py", line 30, in generate_image
    self.draw.draw_arc(xy, start, end, ink)
TypeError: must be sequence of length 4, not 2
    image.write(label_seq, os.path.join(img_path, '%05d-'%idx + label_seq + '.png'))
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 58, in write
    im = self.generate_image(chars)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 228, in generate_image
    self.create_noise_curve(im, color)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 137, in create_noise_curve
    Draw(image).arc(points, start, end, fill=color)
  File "/usr/lib64/python2.7/PIL/ImageDraw.py", line 161, in arc
Process Process-3:
Traceback (most recent call last):
    self.draw.draw_arc(xy, start, end, ink)
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 258, in _bootstrap
TypeError: must be sequence of length 4, not 2
    self.run()
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "examples/warpctc_captcha/generate_captcha.py", line 30, in generate_image
    image.write(label_seq, os.path.join(img_path, '%05d-'%idx + label_seq + '.png'))
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 58, in write
    im = self.generate_image(chars)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 228, in generate_image
    self.create_noise_curve(im, color)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 137, in create_noise_curve
    Draw(image).arc(points, start, end, fill=color)
  File "/usr/lib64/python2.7/PIL/ImageDraw.py", line 161, in arc
    self.draw.draw_arc(xy, start, end, ink)
TypeError: must be sequence of length 4, not 2
Process Process-4:
Traceback (most recent call last):
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 258, in _bootstrap
    self.run()
  File "/usr/lib64/python2.7/multiprocessing/process.py", line 114, in run
    self._target(*self._args, **self._kwargs)
  File "examples/warpctc_captcha/generate_captcha.py", line 30, in generate_image
    image.write(label_seq, os.path.join(img_path, '%05d-'%idx + label_seq + '.png'))
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 58, in write
    im = self.generate_image(chars)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 228, in generate_image
    self.create_noise_curve(im, color)
  File "/data/zhangxin/github/warpctc-caffe-master/venv2/lib/python2.7/site-packages/captcha/image.py", line 137, in create_noise_curve
    Draw(image).arc(points, start, end, fill=color)
  File "/usr/lib64/python2.7/PIL/ImageDraw.py", line 161, in arc
    self.draw.draw_arc(xy, start, end, ink)
TypeError: must be sequence of length 4, not 2
```



