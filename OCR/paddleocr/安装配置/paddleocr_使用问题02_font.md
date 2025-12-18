
# 1 问题

Traceback (most recent call last):
  File "/Users/zhangxin/github/PaddleOCR/test.py", line 4, in <module>
    font = ImageFont.load("./doc/fonts/simfang.ttf")
  File "/Users/zhangxin/miniconda3/envs/py39_paddleocr/lib/python3.9/site-packages/PIL/ImageFont.py", line 723, in load
    f._load_pilfont(filename)
  File "/Users/zhangxin/miniconda3/envs/py39_paddleocr/lib/python3.9/site-packages/PIL/ImageFont.py", line 98, in _load_pilfont
    raise OSError(msg)
OSError: cannot find glyph data file

# 2 解决办法
You don't have to ImageFont.load() the font first. Just directly pass the path or file to ImageFont.truetype(). ImageFont.load() tries to load a bitmap font.

