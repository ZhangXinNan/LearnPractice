

# 1 问题
```bash
Traceback (most recent call last):
  File "demo_zx2.py", line 7, in <module>
    import cv2
  File "/home/app/miniconda3/envs/py37_torch171/lib/python3.7/site-packages/cv2/__init__.py", line 5, in <module>
    from .cv2 import *
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

# 2 解决
```bash
# centos
yum install mesa-libGL.x86_64
# ubuntu
apt-get install ffmpeg libsm6 libxext6 -y
```
