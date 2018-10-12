
导入库
```
import cv2
import matplotlib.image as mpimg

```

比较 | opencv-python | matplotlib.image | PIL | scipy | scikit-image
-- | -- | -- | -- | -- | -- 
读取函数 | cv2.imread | mpimg.imread | pil_image.open
数据类型 | numpy.ndarray | numpy.ndarray | 
数据顺序 | HWC | HWC | | 
数值类型 | int | int | int |
RGB顺序 | BGR | RGB | RGB |


比较 | 读取函数 | 数据类型 | 数据顺序 | 数值类型 | RGB顺序
-- | -- | -- | -- | -- | -- 
opencv-python | cv2.imread | numpy.ndarray | int | BGR
matplotlib.image | mpimg.imread | numpy.ndarray | int | RGB
PIL | pil_image.open | | 
scipy | 
scikit-image | 
