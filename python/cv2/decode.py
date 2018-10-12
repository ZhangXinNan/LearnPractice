#encoding=utf8

import numpy as np
import cv2
# 从硬盘中读取一个图片文件
img_file = open("/Users/zhangxin/pic/car.jpg", "rb").read()
print type(img_file)

# 从内存中读入图片
file_bytes = np.asarray(bytearray(img_file), dtype=np.uint8)
print type(bytearray(img_file))
print type(file_bytes)

img_data_ndarray = cv2.imdecode(file_bytes, cv2.CV_LOAD_IMAGE_UNCHANGED)
height, width = img_data_ndarray.shape[:2]
print type(img_data_ndarray)
print img_data_ndarray.shape

box = [width/4, height/4, width*3/4, height*3/4]
img_obj = img_data_ndarray[box[1]:box[3], box[0]:box[2], :]
print img_obj.shape
cv2.imshow("00", img_data_ndarray)
cv2.imshow("01", img_obj)
cv2.waitKey()

# encode  图片
_, img_obj_bytes = cv2.imencode(".jpg", img_obj)
print type(img_obj_bytes)
print img_obj_bytes
img_obj_str = np.array(img_obj_bytes).tostring()
print type(img_obj_str), len(img_obj_str)
# 保存图片文件到硬盘
with open("tmp.jpg", "wb") as f:
    f.write(img_obj_str)
