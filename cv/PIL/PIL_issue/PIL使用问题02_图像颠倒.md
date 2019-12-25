

在使用PIL读取图像又保存，发现有些图像是上下颠倒的，这可真坑 。

从网上没有搜到为什么，好在热心的网友告诉我：
> pil不读exif信息，所以反而它读的是最真实的，cv2会自动读exif信息做旋转，这个大坑前段时间害惨我了

原来opencv读图像会根据exif信息自动旋转，用windows下的软件看图片时也是如此。


我写了两个函数，从numpy.array和PIL.Image之间进行转换，权当参考：

```python
from PIL import Image
import numpy as np
import cv2

# 从opencv读进来的图片转为PIL的Image对象
def cv2pil(img):
    shape = img.shape
    if len(shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(img)

# 从PIL.Image 转为opencv中使用的numpy.array
def pil2cv(img_pil):
    img_np = np.array(img_pil)
    shape = img_np.shape
    if len(shape) == 3:
        img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    return img_np
```