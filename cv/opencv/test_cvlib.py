#encoding=utf8
import time
import cv2
import numpy as np
import scipy
import PIL
import skimage

import matplotlib

def test_read_image(imgfile, func, params=None):
    t0 = time.time()
    # for i in range(100):
    img = func(imgfile)
    return img, time.time() - t0


imgfile = './232.jpg'
# test_read_image(imgfile)

img, t = test_read_image(imgfile, cv2.imread)
height, width = img.shape[:2]
new_height, new_width = height * 2, width * 2 # 将图像放大一倍
t0 = time.time()
img2 = cv2.resize(img, (new_width, new_height))
t1 = time.time() - t0
print 'cv2.imread :', t, ', shape : ', img.shape, \
    ', cv2.resize : ', t1, ', shape :', img2.shape

from PIL import Image
img, t = test_read_image(imgfile, Image.open)
t0 = time.time()
img2 = img.resize((new_width, new_height), Image.BILINEAR)
t1 = time.time() - t0
print 'PIL.Image.open :', t, ', size : ', img.size, ', mode: ', img.mode, \
    ', PIL.Image.resize : ', t1, ' size : ', img2.size #, ', mode: ', img2.mode

from skimage import io, transform
img, t = test_read_image(imgfile, io.imread)
t0 = time.time()
img2 = transform.resize(img, (new_height, new_width), mode='constant')
t1 = time.time() - t0
print 'skimage.io.imread :', t, ', shape : ', img.shape, \
    ', skimage.transform.resize :', t1, ', shape : ', img2.shape

from scipy import misc, ndimage
img, t = test_read_image(imgfile, misc.imread)
# imresize is deprecated! imresize is deprecated in SciPy 1.0.0, 
# and will be removed in 1.2.0. Use skimage.transform.resize instead.
print 'scipy.misc.imread :', t, ', shape : ', img.shape

img, t = test_read_image(imgfile, ndimage.imread)
print 'scipy.ndimage.imread :', t, ', shape : ', img.shape

from matplotlib import image
img, t = test_read_image(imgfile, image.imread)
print 'matplotlib.image.imread :', t, ', shape : ', img.shape


