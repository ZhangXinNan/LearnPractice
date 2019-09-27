

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('wiki.jpg',0)

hist,bins = np.histogram(img.flatten(), bins=256, range=[0,256])
print("hist : 直方图统计结果")
print(hist)
print("bins : 灰度值")
print(bins)

#cumsum : Return the cumulative sum of the elements along a given axis.
cdf = hist.cumsum()
print("cdf : 直方图累加结果")
print(cdf)
cdf_normalized = cdf * hist.max()/ cdf.max()
print("cdf_normalized : 累加结果归一化")
print(cdf_normalized)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
plt.save("hist_np.jpg")
exit()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]



