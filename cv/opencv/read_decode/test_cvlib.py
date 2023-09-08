#encoding=utf8
'''
requirements.txt
numpy
scipy
opencv-python
pillow
scikit_image
matplotlib
'''
import time
import cv2
import numpy as np
import PIL
import skimage
import scipy
import matplotlib
# from PIL import Image
# from skimage import io, transform
# from scipy import misc, ndimage
# from matplotlib import image


imgfile = '../../pic/232.jpg'
# test_read_image(imgfile)

print("----------opencv----------")
t0 = time.time()
img = cv2.imread(imgfile)
print('cv2.imread :', time.time() - t0, ', shape : ', img.shape)

height, width = img.shape[:2]
new_height, new_width = height * 2, width * 2 # 将图像放大一倍
t0 = time.time()
img2 = cv2.resize(img, (new_width, new_height))
print('cv2.resize :', time.time() - t0, ', shape :', img2.shape)


print("----------PIL.Image----------")
t0 = time.time()
img = PIL.Image.open(imgfile)
img.load()
print('PIL.Image.open   :', time.time() - t0, ', size : ', img.size, ', mode: ', img.mode)
t0 = time.time()
img2 = img.resize((new_width, new_height), PIL.Image.BILINEAR)
print('PIL.Image.resize :', time.time() - t0, ', size : ', img2.size, ', mode: ', img2.mode)

print("-----------skimage----------")
t0 = time.time()
img = skimage.io.imread(imgfile)
print('skimage.io.imread :', time.time() - t0, ', shape : ', img.shape)
t0 = time.time()
img2 = skimage.transform.resize(img, (new_height, new_width), mode='constant')
print('skimage.transform.resize :', time.time() - t0, ', shape : ', img2.shape)


'''
print("----------scipy----------")
# AttributeError: scipy.misc is deprecated and has no attribute imread.
t0 = time.time()
img = scipy.misc.imread(imgfile)
print('scipy.misc.imread :', time.time() - t0, ', shape : ', img.shape)

t0 = time.time()
img = scipy.ndimage.imread(imgfile)
print('scipy.ndimage.imread :', time.time() - t0, ', shape : ', img.shape)
'''

print("-----------matplotlib-----------")
import matplotlib.pyplot as plt
t0 = time.time()
img = plt.imread(imgfile)
print('matplotlib.pyplot.imread :', time.time() - t0, ', shape : ', img.shape)


