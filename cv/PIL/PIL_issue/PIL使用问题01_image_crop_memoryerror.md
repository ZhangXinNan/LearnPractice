
```bash
D:\data_autohome\autoimg1\70.84.405\10659.1.1294113.jpg 228 331 1667 1142 (1920, 1440) RGB
Traceback (most recent call last):
  File "D:\gitlab\CarRecognition\Train\pytorch\CarDataset.py", line 64, in __getitem__
    image = image.crop((x1,y1,x2,y2))
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\PIL\Image.py", line 1163, in crop
    return self._new(self._crop(self.im, box))
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\PIL\Image.py", line 1183, in _crop
    return im.crop((x0, y0, x1, y1))
MemoryError
D:\data_autohome\autoimg1\142.327.2495\1000248.1.100026033.jpg 322 271 1570 1284 (1920, 1440) RGB

D:\data_autohome\autoimg1\97.191.3455\1002214.1.100056478.jpg 49 392 994 689 (945, 297) RGB
```



测试代码：
```python

```