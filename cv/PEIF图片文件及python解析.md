
# 1 简介
高效率图像文件格式（英语：High Efficiency Image File Format, HEIF；也称高效图像文件格式[1]）是一个用于单张图像或图像序列的文件格式。它由动态影像专家小组（MPEG）开发，并在MPEG-H Part 12（ISO/IEC 23008-12）中定义。

HEIF规范也定义了高效率视频编码（HEVC）编码的内嵌图像和HEVC编码的图像序列的存储方式，其中以受约束的方式应用帧间预测。

HEIF文件与ISO基本媒体文件格式（ISOBMFF，ISO/IEC 14496-12）兼容，并且还可以包括其他媒体流，例如定时的文本和音频。


.heic 只是一个HEIF文件格式的一种扩展名，言外之意是：HEIF不仅有 .heic 这种扩展名，还有其它的，比如说：.heif 和 .avci，它们都是属于HEIF文件格式。当然，常见的只有 .heif 和 .heic 这两种，而 .avci 很少见。

在苹果的实现中，单个图片采用 .heic 文件扩展名，它默认使用的都是 HEVC 的编码格式。当然，苹果官方未来会对 H.264/MPEG-4 AVC 编码的 .avci 文件进行支持，以及 .heif 文件。 

# 2 安装heif包
```bash
# centos
yum install libffi libheif-devel libde265-devel

# mac
brew install libheif
```

安装python包
```bash
pip install pyheif
```

使用
```python



import whatimage
import pyheif
from io import BytesIO
from PIL import Image

def read_image_heif(img_file, to_fmt='JPEG'):
    heif_file = pyheif.read(img_file)
    image = Image.frombytes(heif_file.mode,
                            heif_file.size,
                            heif_file.data,
                            "raw",
                            heif_file.mode,
                            heif_file.stride,
                            )
    # image.save('5.jpg', 'JPEG')
    with BytesIO() as out:
        image.save(out, format=to_fmt)
        img_file = out.getvalue()
    return img_file


def main():
    img_file = open('/home/zhangxin/gitlab_md/urs-client/mit/5.png', 'rb').read()
    fmt = whatimage.identify_image(img_file)
    if fmt in ['heic']:
        img_file = read_image_heif(img_file)
        with open('5.jpg', 'wb') as fo:
            fo.write(img_file)

if __name__ == '__main__':
    main()
```

# 3 参考文档
- [HEIF/heic图片文件解析](https://zhuanlan.zhihu.com/p/35847861)
- [高效率图像文件格式](https://zh.wikipedia.org/wiki/%E9%AB%98%E6%95%88%E7%8E%87%E5%9B%BE%E5%83%8F%E6%96%87%E4%BB%B6%E6%A0%BC%E5%BC%8F)


