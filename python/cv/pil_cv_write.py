
import time

from io import StringIO, BytesIO
from PIL import Image

import numpy as np
import cv2


img_path = '/Users/zhangxin/pic/car.jpg'

# 1 使用PIL加载图片
img = Image.open(img_path)
print("img size {}, mode {}".format(img.size, img.mode))
# 1.1 往内存中写图片——JPEG格式
t0 = time.time()
with BytesIO() as out:
    img.save(out, format='JPEG')
    t1 = time.time()
    with open('out_stream.jpg', 'wb') as fo:
        fo.write(out.getvalue())

# 1.2 往内存中写图片——PNG格式
t2 = time.time()
with BytesIO() as out:
    img.save(out, format='PNG')
    t3 = time.time()
    with open('out_stream.png', 'wb') as fo:
        fo.write(out.getvalue())

print("PIL save image as jpeg : ", t1 - t0)
print("PIL save image as png  : ", t3 - t2)

# 2 使用opencv 加载图片
img = cv2.imread(img_path)
print("img shape : ", img.shape)

# 2.1 往内存中写图片——JPEG格式
t0 = time.time()
_, img_bytes = cv2.imencode(".jpg", img)
img_str = np.array(img_bytes).tostring()
t1 = time.time()
with open("cv_tmp.jpg", "wb") as f:
    f.write(img_str)

# 2.2 往内存中写图片——PNG格式
t2 = time.time()
_, img_bytes = cv2.imencode(".png", img)
img_str = np.array(img_bytes).tostring()
t3 = time.time()
with open("cv_tmp.png", "wb") as f:
    f.write(img_str)


print("OpenCV save image as jpeg : ", t1 - t0)
print("OpenCV save image as png  : ", t3 - t2)


'''输出：
img size (800, 600), mode RGB
PIL save image as jpeg :  0.025282859802246094
PIL save image as png  :  0.2618370056152344
img shape :  (600, 800, 3)
OpenCV save image as jpeg :  0.02747821807861328
OpenCV save image as png  :  0.030751943588256836
'''