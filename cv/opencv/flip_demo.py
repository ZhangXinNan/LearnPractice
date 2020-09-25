
import time
import numpy as np
import cv2

img = cv2.imread('232.jpg')
print("image.shape :", img.shape)
img1 = cv2.flip(img, -1)    # 上下、左右都镜像
img2 = cv2.flip(img, 0)     # 上下镜像
img3 = cv2.flip(img, 1)     # 左右镜像

img4 = cv2.transpose(img)

cv2.imwrite("1.png", img1)
cv2.imwrite("2.png", img2)
cv2.imwrite("3.png", img3)
cv2.imwrite("4.png", img4)


print("opencv")
print("90 -----------")
t0 = time.time()
img_90 = cv2.flip(cv2.transpose(img), 1)
cv2.imwrite("img_90.jpg", img_90)
print(time.time() - t0)

print("180 -----------")
t0 = time.time()
img_180 = cv2.flip(img, -1)
cv2.imwrite("img_180.jpg", img_180)
print(time.time() - t0)

print("270 ------------")
t0 = time.time()
img_270 = cv2.flip(cv2.transpose(img), 0)
cv2.imwrite("img_270.jpg", img_270)
print(time.time() - t0)

'''
测试环境：MacBook Pro 16inch
使用python调用 opencv旋转90度只需要0.328毫秒，使用scipy的旋转函数需要 5.59秒。
'''
from scipy import ndimage
print("90-rotate with scipy-----------")
t0 = time.time()
img_90_np = ndimage.rotate(img, 90, cval=255)
cv2.imwrite("img_90_np.jpg", img_90_np)
print(time.time() - t0)

