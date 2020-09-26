# Mac
## 问题1： RuntimeError: module compiled against API version 0xa but this version of numpy is 0x9
```
RuntimeError: module compiled against API version 0xa but this version of numpy is 0x9
Traceback (most recent call last):
  File "feature_matching.py", line 2, in <module>
    import cv2
  File "/Users/zhangxin/Library/Python/2.7/lib/python/site-packages/cv2/__init__.py", line 9, in <module>
    from .cv2 import *
ImportError: numpy.core.multiarray failed to import
```

解决方法:不使用mac上默认的python，而是用brew安装的python
```
alias python='/usr/local/Cellar/python/2.7.13/bin/python'
```
