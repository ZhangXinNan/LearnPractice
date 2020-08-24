在开发时经常遇到读图片的问题，最笨的方式是先把图片写入硬盘，再用普通 方式读 ，其实PIL或者OPENCV都支持从内存文件流里读图片和往内存文件流里写图片的。
以下 是PIL的示例：

```python
from io import StringIO, BytesIO
from PIL import Image

img_path = './car.jpg'
# 从内存中读图片
content = open(img_path, 'rb').read()
img = Image.open(BytesIO(content))
print(img.size, img.mode)

# 往内存中写图片
img = Image.open(img_path)
with BytesIO() as out:
    img.save(out, format='JPEG')
    with open('out_stream.jpg', 'wb') as fo:
        fo.write(out.getvalue())
```

