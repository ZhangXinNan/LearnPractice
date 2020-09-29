

import numpy as np
import cv2
import math


def auto_resize(img, SH, SW):
    # Scale to the same height
    scale = SH / img.shape[0]
    img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
    print(img.shape)

    # Make the width greater or equal to SW by copying
    h, w, c = img.shape
    if w < SW:
        scale = math.ceil(SW / w)
        new_img = np.zeros((SH, w * scale, c))
        for i in range(scale):
            new_img[:, i*w:(i+1)*w, :] = img
        img = new_img
        print(img.shape)
    # Cut
    if img.shape[1] > SW:
        img = img[:, :SW]
        print(img.shape)
    return img


SH, SW = 48, 192
# SH, SW = 48, 500
img = cv2.imread('word_1.jpg')

print("48-192")
print(img.shape)
img1 = auto_resize(img, 48, 192)
cv2.imwrite("word_1_48-192.jpg", img1)

print("48-500")
print(img.shape)
img2 = auto_resize(img, 48, 500)
cv2.imwrite("word_1_48-500.jpg", img2)

