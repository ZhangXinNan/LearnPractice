# 存在问题
opencv 版本为： 4.2.0.32
```bash
(py37_taoche_ocr) [app@VM-12-138-centos ai-paggy]$ python Application.py 
Traceback (most recent call last):
  File "Application.py", line 9, in <module>
    import cv2
  File "/home/app/miniconda3/envs/py37_taoche_ocr/lib/python3.7/site-packages/cv2/__init__.py", line 3, in <module>
    from .cv2 import *
ImportError: libSM.so.6: cannot open shared object file: No such file or directory
```

# 解决方法
```bash
# centos
sudo yum install libXext libSM libXrender

```

