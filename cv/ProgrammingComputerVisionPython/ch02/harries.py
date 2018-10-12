
from scipy.ndimage import filters

def compute_harris_reponse(im, sigma=3):
    """在一幅灰度图像中，对每个像素计算Harries角点检测器响应函数
    """
    # 计算导数
    imx = zeros(im.shape)
    filters.gaussian_filter(im, (sigma, ))