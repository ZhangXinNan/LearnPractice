 Caffe 提供的 python 接口是使用 scikit-image 作为图像处理库的, 其速度比 OpenCV 差了非常多. 比如 Resize速度比较可参照faster_rcnn与ssd算法对比。
 如果想速度更快, 可以使用 OpenCV 来做图像处理, 比如用 cv2.imread()来加载图片, 当然与 Caffe.io.load_image 加载图像有所区别, 转换方法非常简单

示例代码如下(三通道彩色图像和灰度图像示例):

OpenCV 与 Caffe 图像之间转换
```
import os
import sys
import numpy as np
import cv2
sys.path.append('/Users/zhangxin/github/caffe/python')
import caffe


def check_rgb(imgfile, x=20, y=30):
    im1 = cv2.imread(imgfile)
    im2 = caffe.io.load_image(imgfile)
    print im1.shape, im2.shape
    # opencv cv2.imread --> caffe.io.load_image
    im3 = im1[:, :, (2,1,0)].astype(np.float32) / 255.0
    # caffe.io.load_image --> opencv cv2.imread
    im4 = (im2[:, :, (2,1,0)] * 255).astype(np.uint8)
    print im1[y, x, :]
    print im2[y, x, :]
    print im3[y, x, :]
    print im4[y, x, :]

def check_gray(imgfile, y=3, x=3):
    im1 = cv2.imread(imgfile, 0)
    im2 = caffe.io.load_image(imgfile, False)
    print im1.shape, im2.shape
    # opencv cv2.imread --> caffe.io.load_image
    im3 = im1.astype(np.float32) / 255.0
    # caffe.io.load_image --> opencv cv2.imread
    im4 = (im2 * 255).astype(np.uint8)
    print im1[y, x]
    print im2[y, x]
    print im3[y, x]
    print im4[y, x]



imgfile = '../image/1.jpg'
check_rgb(imgfile)
check_gray(imgfile)
```
说明:

(1) caffe.io.load_image在加载图像时三通道顺序是 RGB, 而 OpenCV 默认是 BGR

(2) caffe.io.load_image 将图像原来[0,255]归一化到了0到1之间的32位浮点数.