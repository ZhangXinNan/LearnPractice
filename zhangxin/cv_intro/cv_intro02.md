
# 1 数字图像处理基础

模拟图像又称连续图像，是指在二维坐标系中连续变化的图像，即图像的像点是无限稠密的，同时具有灰度值（即图像从暗到亮的变化值）。连续图像的典型代表是由光学透镜系统获取的图像，如人物照片和景物照片等，有时又称模拟图像。

## 1.1 基本概念
图像：就是一个矩阵，或者定义为一个二维函数f(x,y)，其中x,y是空间坐标
强度：图像任何坐标(x,y)处的值。
数字图像：x,y,f为有限的离散值。
数字图像处理：借助于计算机来处理数字图像。
像素：数字图像在每一点处的坐标和强度值。

## 1.2 颜色空间
彩色模型的上的是在某些标准下用通常可以接受的方式对彩色加以说明。
灰度图像：图像中每一个坐标处只有一个值。
彩色图像：图像中每一个坐标处有多个值。

人感知一个物体的颜色是由物体反射光的性质决定的。如果一个物体在反射的光在所有可见光波长范围内是平衡的，对观察者来说就是白色。否则物体呈现某种颜色。例如绿色物体反射具有500-750nm范围内的主要波长的光，吸收其他波长的多数能量。

### 1.2.1 RGB彩色模型

### 1.2.2 CMY、CMYK彩色模型

### 1.2.3 HSI、HSV彩色模型。
【例】
```python
import cv2
image = cv2.imread('boldt.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

channels = cv2.split(hsv)
cv2.imwrite('blodt_h.jpg', channels[0])
cv2.imwrite('blodt_s.jpg', channels[1])
cv2.imwrite('blodt_v.jpg', channels[2])
```


## 1.3 图像缩放
### 1.3.1 放大——像素插值
* 最近邻
* 双线性
* 立方插值

【注意】
1. 像素不只是一个点，而是一个网格，是数字图像的离散化表示，代表的是一块很小区域的值。
2. 像素的坐标（m, n），更准备理解应该是(m+0.5, n+0.5)
3. 在线性插值时以一维为例，在缩放图像时，原图像P，目标图像Q，Q中一个像素的值应该找到P中相对应的位置，并取其周边的点乘以权重得到。比如q = p1 * w1 + p2 * w2, w1+w2=1.0， w1和w2由p与q1和q2的距离远近决定。

### 1.3.2 缩小——缩减图像采样
以前我们可能认为要缩小一个图像，只要简单的消除图像中的一部分行和列即可，实际这样效果往往很差。当试图在图像中包含高频成分，就可能会造成空间假频的现象。图像中精致的细节对应着高频，在缩小图像时去除它的高频成分。


* 先放大后缩小，取相应区域的平均值
* 先平滑后插值


# 2 直方图
图像由有限个不同数值（颜色或者强度）的像素构成，像素值在整个图像中的分布情况是该图像的一个重要属性。

## 2.1 计算图像直方图
直方图表示一个图像（或者一组图像）中具有某个值的像素的数量。一般灰度图像中每个像素值我们用一个字节（0到255）来表示，那么灰度图像的直方图就有256个“箱子”，0号箱子表示图像中像素值为0的像素的数量。把所有箱子进行累加即得像素的总数。

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('boldt.jpg', 0)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
print hist
plt.hist(img.ravel(),256,[0,256])
plt.show()
```

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('boldt.jpg',0)
plt.hist(img.ravel(),256,[0,256]); 
plt.show()
```

```python
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('boldt.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.show()

```


## 2.2 直方图拉伸
使用的强度值范围太小。
在强度值中找到一个（最）小值min和一个（最）大值max，然后重映射强度值，使小于等于min的值变成0（或者某个小值），大于等于max的值变为255（或某个大值）。


```python
# 使用numpy
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('wiki.png',0)

# flatten : Return a copy of the array collapsed into one dimension.
# histogram : Compute the histogram of a set of data.
hist,bins = np.histogram(img.flatten(),256,[0,256])
# cumsum : Return the cumulative sum of the elements along a given axis.
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


```


## 2.3 直方图均衡
部分强度值的使用频率比其他高很多。
```python
import cv2
import numpy as np
img = cv2.imread('wiki.jpg',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)
```

## 2.4 直方图规定化



# 3 二值化
## 3.1 简单二值化

## 3.2 大津法二值化

## 3.3 自适应二值化


# 4 形态学运算来变换图像
## 4.1 腐蚀和膨胀

## 4.2 开运算与闭运算

## 4.3 形态学滤波器来检测边缘和角点

# 5 图像滤波
滤波是信号和图像处理中的一种基本操作。它的上的是选择性的提取图像中某些方面的内容。这些内容在特定应用中传达了重要信息。

当观察一幅图像时，我们看到不同的灰度级（颜色）在图像上的分布状况。
通过观察灰度分布来描述图像特征，称为空域（spatial domain）。

观察灰度级变化的频率来描述图像特征，称为频域（frequency domain）。
频域分析把图像分解成从低频到高频的频率成分。图像强度值变化慢的区域只包含低频率，强度值变化快的区域产生高频率。

在频域分析框架下，滤波器是一种放大某些频段、同时滤掉（减弱）其他频段的算子。
低通滤波器的作用是消除图像中高频部分，高通滤波消除图像中低频部分。


## 5.1 低通滤波器
### 5.1.1 均值平滑 （均值滤波器）（块滤波器box filter）
将每个像素的值替换成该像素邻域的平均值，从而使图像更加平滑

### 5.1.2 高斯平滑

### 5.1.3 中值平滑（中值滤波器）
中值滤波器非常有助于消除椒盐噪声。均值滤波器会受异常噪声影响大。
中值滤波器还有助于保留边缘。

## 5.2 用定向滤波器检测边缘
用低通滤波器可以移除或者减弱高频成分。放大图像中的高频成分，则可以使用高通滤波器进行边缘检测。
### 5.2.1 Sobel 滤波器
Sobel 算子是一种典型的用于边缘检测的线性滤波器，它基于两个3*3的内核，结构如下：

```
-1 -2 -1
 0  0 0
 1  2 1
```
和
```
-1 0 1
-2 0 2
-1 0 1
```
如果把图像看成二维函数，那么Sobel算子就是图像在垂直和水平方向变化的速度。这种速度（在数学中）一般称为梯度。它是一个二维向量，向量的元素是横竖两个方向的函数的一阶导数：
```
grad(I) = [dI/dx, dI/dy]^T
```

梯度是一个二维向量，它具有**模**和**方向**。梯度向量的模表示变化的振幅，计算机时可用欧几里德模（L2）或者绝对值之和作为模（L1）。梯度向量总是指向变化最剧烈的方向。对于一个图像来说，这意味着梯度的方向与边缘垂直，从较黑区域指向较亮区域。
```

```


# 6 提取直线、轮廓、区域
## 6.1 Canny
简单的求边缘的方法有两个主要缺点：（1）边缘过厚难以识别物体的边界；（2）阈值不好找，很难既能检测到图像中所有重要的边缘，又能避免产生太多无关紧要的边缘。（本身同一幅图像中不同光照或者不同物体，就难以使用同一个阈值来确定边缘。）

Canny 基于Sobel 算子，核心理念是：用两个不同的阈值来判断哪个点属于轮廓：一个低阀值，一个高阀值。
先把低阀值时，要保证包含重要图像轮廓的全部边缘像素。高阀值用来界定重要的边缘。
具体做法：在低阀值边缘分布图上只保留具有连续路径的边缘点，同时把那些边缘点连接到高阀值边缘分布图上的边缘上。
如果梯度幅值不是梯度方向上的最大值，那么对应的边缘点就会被移除。

## 6.2 霍夫变换检测直线
直线(线段)是图像中经常出现而且往往重要的特征。
```latex
p = x cos t + y sin t
```

* p是直线到图像原点（左上角）的距离，范围是0到图像对角线的长度
* t是直线与垂直线的角度，范围是0到pai

## 6.3 检测圆等
霍夫变换也能用来检测其他几何物体。事实上，任何可以用一个参数方程来表示的物体，都适合用霍夫变换来检测。


