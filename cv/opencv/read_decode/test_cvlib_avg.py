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
n = 100
# test_read_image(imgfile)

print("----------opencv----------")
t0 = time.time()
for _ in range(n):
    img = cv2.imread(imgfile)
t = (time.time() - t0)/n
print('cv2.imread :', t, ', shape : ', img.shape)


print("----------PIL.Image----------")
t0 = time.time()
for _ in range(n):
    img = PIL.Image.open(imgfile)
t = (time.time() - t0)/n
print('PIL.Image.open   :', t, ', size : ', img.size, ', mode: ', img.mode)


print("-----------skimage----------")
t0 = time.time()
for _ in range(n):
    img = skimage.io.imread(imgfile)
t = (time.time() - t0)/n
print('skimage.io.imread :', t, ', shape : ', img.shape)


print("-----------matplotlib-----------")
import matplotlib.pyplot as plt
t0 = time.time()
for _ in range(n):
    img = plt.imread(imgfile)
t = (time.time() - t0)/n
print('matplotlib.pyplot.imread :', t, ', shape : ', img.shape)


