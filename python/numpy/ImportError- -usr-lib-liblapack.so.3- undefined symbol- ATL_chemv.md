在ubuntu下使用numpy出现如下问题：
```
zhangxin@seele:~/github/caffe$ python
Python 2.7.6 (default, Oct 26 2016, 20:30:19) 
[GCC 4.8.4] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python2.7/dist-packages/numpy/__init__.py", line 153, in <module>
    from . import add_newdocs
  File "/usr/lib/python2.7/dist-packages/numpy/add_newdocs.py", line 13, in <module>
    from numpy.lib import add_newdoc
  File "/usr/lib/python2.7/dist-packages/numpy/lib/__init__.py", line 18, in <module>
    from .polynomial import *
  File "/usr/lib/python2.7/dist-packages/numpy/lib/polynomial.py", line 19, in <module>
    from numpy.linalg import eigvals, lstsq, inv
  File "/usr/lib/python2.7/dist-packages/numpy/linalg/__init__.py", line 50, in <module>
    from .linalg import *
  File "/usr/lib/python2.7/dist-packages/numpy/linalg/linalg.py", line 29, in <module>
    from numpy.linalg import lapack_lite, _umath_linalg
ImportError: /usr/lib/liblapack.so.3: undefined symbol: ATL_chemv
```
解决方法：
```
This issue arises when you have libopenblas-base and libatlas3-base installed, but don't have liblapack3 installed. This combination of packages installs conflicting versions of libblas.so (from OpenBLAS) and liblapack.so (from ATLAS).

Solution 1 (my favorite): You can keep both OpenBLAS and ATLAS on your machine if you also install liblapack3.

sudo apt-get install liblapack3

Solution 2: Uninstall ATLAS (this will actually install liblapack3 for you automatically because of some deb package shenanigans)

sudo apt-get uninstall libatlas3-base

Solution 3: Uninstall OpenBLAS

sudo apt-get uninstall libopenblas-base
```

参考资料：
[Installing lapack for numpy](https://stackoverflow.com/questions/8917977/installing-lapack-for-numpy)

