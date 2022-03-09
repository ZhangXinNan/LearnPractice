
from PIL import Image, ImageDraw, ImageFont
import random
random.seed(0)

img = Image.open('car.jpg')
print(img.mode, img.size)

h, w = img.height, img.width


draw = ImageDraw.Draw(img)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.polygon([w/4, h/4, w/2, h/4, w/2, h/2, w/4, h/2], outline=color)
img.save('car.polygon-outline.jpg')

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
draw.polygon([w/2, h/2, w*3/4, h/2, w*3/4, h*3/4, w/2, h*3/4], fill=color)
img.save('car.polygon-fill.jpg')