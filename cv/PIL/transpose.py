#encoding=utf8
import PIL

from PIL import Image

a = Image.open('/Users/zhangxin/pic/car.jpg')
arr = []

arr.append(a.transpose(PIL.Image.FLIP_LEFT_RIGHT)) # 左右镜像
arr.append(a.transpose(PIL.Image.FLIP_TOP_BOTTOM)) # 上下镜像
arr.append(a.transpose(PIL.Image.ROTATE_90)) # 旋转90度
arr.append(a.transpose(PIL.Image.ROTATE_180)) # 旋转180
arr.append(a.transpose(PIL.Image.ROTATE_270)) # 旋转270
arr.append(a.transpose(PIL.Image.TRANSPOSE)) # 两个方向镜像

arr[0].save('FLIP_LEFT_RIGHT.jpg')
arr[1].save('FLIP_TOP_BOTTOM.jpg')
arr[2].save('ROTATE_90.jpg')
arr[3].save('ROTATE_180.jpg')
arr[4].save('ROTATE_270.jpg')
arr[5].save('TRANSPOSE.jpg')
