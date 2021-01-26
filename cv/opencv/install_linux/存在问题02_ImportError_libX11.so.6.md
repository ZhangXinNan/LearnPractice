
```bash
(py37_taoche_ocr) [app@VM-12-138-centos ~]$ python
Python 3.7.9 (default, Aug 31 2020, 12:42:55) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cv2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/app/miniconda3/envs/py37_taoche_ocr/lib/python3.7/site-packages/cv2/__init__.py", line 5, in <module>
    from .cv2 import *
ImportError: libX11.so.6: cannot open shared object file: No such file or directory
```


```bash
sudo yum install libX11
sudo yum install libXext
```