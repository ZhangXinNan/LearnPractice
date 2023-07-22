import os
from PIL import ImageFont, ImageDraw


font_path = os.path.join('/Users/zhangxin/github/PaddleOCR', 'doc/fonts/simfang.ttf')
print(font_path)
# font = ImageFont.load("./doc/fonts/simfang.ttf")

font = ImageFont.truetype(font_path)
print(font.getbbox("we are chinese"))
print(font.getbbox("我们是中国人"))
# print(font.getsize("we are chinese"))
