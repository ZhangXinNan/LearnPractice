
import time
import numpy as np
import cv2

img = cv2.imread('232.jpg')
print("image.shape :", img.shape)
img_n1 = cv2.flip(img, -1)      # 上下、左右都镜像
img_0 = cv2.flip(img, 0)        # 上下镜像
img_1 = cv2.flip(img, 1)        # 左右镜像
img_tsp = cv2.transpose(img)    # 转置（行列互换）

cv2.imwrite("img_flip-1.png", img_n1)
cv2.imwrite("img_flip_0.png", img_0)
cv2.imwrite("img_flip_1.png", img_1)
cv2.imwrite("img_transp.png", img_tsp)


print("opencv------flip+transpose")
# 顺时针90度
t0 = time.time()
img_90 = cv2.flip(cv2.transpose(img), 1)
print("[ 90] \t", time.time() - t0)
cv2.imwrite("img_90.jpg", img_90)

# 顺时针180度
t0 = time.time()
img_180 = cv2.flip(img, -1)
print("[180] \t", time.time() - t0)
cv2.imwrite("img_180.jpg", img_180)
# 顺时针270度
t0 = time.time()
img_270 = cv2.flip(cv2.transpose(img), 0)
print("[270] \t", time.time() - t0)
cv2.imwrite("img_270.jpg", img_270)


print("opencv-------rotate------")
t0 = time.time()
img_90_cv_rot = cv2.rotate(img, 0)
print("[ 90] \t", time.time() - t0)
cv2.imwrite("img_90_cv_rot.jpg", img_90_cv_rot)

t0 = time.time()
img_180_cv_rot = cv2.rotate(img, 1)
print("[180] \t", time.time() - t0)
cv2.imwrite("img_180_cv_rot.jpg", img_180_cv_rot)

t0 = time.time()
img_270_cv_rot = cv2.rotate(img, 2)
print("[270] \t", time.time() - t0)
cv2.imwrite("img_270_cv_rot.jpg", img_270_cv_rot)


'''
测试环境：MacBook Pro 16inch
使用python调用 opencv旋转90度只需要0.328毫秒，使用scipy的旋转函数需要 5.59秒。
'''
from scipy import ndimage
print("scipy----------rotate with-----------")
t0 = time.time()
# 逆时针转了90度
img_90_np = ndimage.rotate(img, 90, cval=255)
print("[ 90] \t", time.time() - t0)
cv2.imwrite("img_90_np_anticlockwise.jpg", img_90_np)



'''
opencv
image.shape : (4160, 3120, 3)
opencv------flip+transpose
[ 90] 	 0.0459132194519043
[180] 	 0.005445003509521484
[270] 	 0.0476832389831543
opencv-------rotate------
[ 90] 	 0.01723790168762207
[180] 	 0.014707803726196289
[270] 	 0.027275800704956055
scipy----------rotate with-----------
[ 90] 	 4.976858139038086
'''