
import time

from io import StringIO, BytesIO
from PIL import Image

import numpy as np
import cv2


img_path = '/Users/zhangxin/pic/car.jpg'

# 从内存中读图片
content = open(img_path, 'rb').read()
img = Image.open(BytesIO(content))
print(img.size, img.mode)
