

```python
from io import StringIO, BytesIO
from PIL import Image

img_path = './car.jpg'
# 从内存中读图片
stream = open(img_path, 'rb').read()
img = Image.open(StringIO(content))
print(img.size, img.mode)

# 往内存中写图片
img = Image.open(img_path)
with BytesIO as out:
    img.save(out, format='JPEG')
    with open('out_stream.jpg', 'wb') as fo:
        fo.write(out.getvalue())
```

