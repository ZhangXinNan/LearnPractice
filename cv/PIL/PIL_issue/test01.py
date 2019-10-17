

import os
from PIL import Image


# img_path = 'autoimg1.142.327.2495.1000248.1.100026033.jpg'
# x1, y1, x2, y2 = 322, 271, 1570, 1284
img_path = 'autoimg1.70.84.405.10659.1.1294113.jpg'
x1, y1, x2, y2 = 228, 331, 1667, 1142


image = Image.open(img_path)
print(image.size, image.mode)
if image.mode != 'RGB':
    image = image.convert('RGB')
try:
    image = image.crop((x1,y1,x2,y2))
except Exception as e:
    print(img_path, x1, y1, x2, y2, image.size, image.mode)
    traceback.print_exc(file=sys.stdout)

print(image.size, image.mode)
image.save('tmp.png', 'PNG')
