#encoding=utf8
import numpy as np
import cv2
import matplotlib.image as mpimg
import PIL
from PIL import Image as pil_image
fn = '/Users/zhangxin/pic/dog.jpg'


img_cv2 = cv2.imread(fn)
print img_cv2.shape
print type(img_cv2)
print img_cv2[0][:2]
print img_cv2[1][:2]

img = mpimg.imread(fn)
print img.shape
print type(img)
print img[0][:2]
print img[1][:2]


img_pil = pil_image.open(fn)
print img_pil
print img_pil.getpixel((0, 0))
print img_pil.getpixel((0, 1))
print img_pil.getpixel((1, 0))
print img_pil.getpixel((1, 1))