#encoding=utf8
import PIL

from PIL import Image

a = Image.open('car.jpg')
arr = []

arr.append(a.transpose(PIL.Image.FLIP_LEFT_RIGHT)) # 左右镜像
arr.append(a.transpose(PIL.Image.FLIP_TOP_BOTTOM)) # 上下镜像
arr.append(a.transpose(PIL.Image.ROTATE_90)) # 逆时针旋转90度
arr.append(a.transpose(PIL.Image.ROTATE_180)) # 旋转180
arr.append(a.transpose(PIL.Image.ROTATE_270)) # 逆时针旋转270
arr.append(a.transpose(PIL.Image.TRANSPOSE)) # 左右翻转后再逆时针旋转图像 90 度
arr.append(a.transpose(PIL.Image.TRANSVERSE)) # 左右翻转后再顺时针旋转图像 90 度

arr[0].save('pil-img_FLIP_LEFT_RIGHT.jpg')
arr[1].save('pil-img_FLIP_TOP_BOTTOM.jpg')
arr[2].save('pil-img_ROTATE_90.jpg')
arr[3].save('pil-img_ROTATE_180.jpg')
arr[4].save('pil-img_ROTATE_270.jpg')
arr[5].save('pil-img_TRANSPOSE.jpg')
arr[6].save('pil-img_TRANSVERSE.jpg')