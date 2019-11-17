GPU转CPU代码参考[gpu2cpu.md](https://github.com/ZhangXinNan/text-detection-ctpn/blob/zxdev_mac/gpu2cpu.md)


```
python setup.py build_ext --include-dirs=/Users/zhangxin/anaconda2/lib/python2.7/site-packages/numpy/core/include
# or
python setup.py build
# or
python setup.py.zhao181 build_ext --inplace

# or
python setup.py.struCoder build
```


## 问题1：
```
python setup.py.struCoder build

# 。。。。
35 warnings generated.
/usr/bin/gcc -bundle -undefined dynamic_lookup -L/Users/zhangxin/anaconda2/lib -arch x86_64 /Users/zhangxin/anaconda2/lib/python2.7/site-packages/numpy/core/include -arch x86_64 build/temp.macosx-10.6-x86_64-2.7/bbox.o -L/Users/zhangxin/anaconda2/lib -o build/lib.macosx-10.6-x86_64-2.7/bbox.so
ld: can't map file, errno=22 file '/Users/zhangxin/anaconda2/lib/python2.7/site-packages/numpy/core/include' for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
error: command '/usr/bin/gcc' failed with exit status 1
```就好使了
在删除了brew 安装的python后，错误消失了。
```
brew uninstall python
```

## 问题2
```
➜  utils git:(zxdev_mac) ✗ python setup.py.zhao181 build
Traceback (most recent call last):
  File "setup.py.zhao181", line 11, in <module>
    ext_modules=cythonize(["bbox.pyx","cython_nms.pyx"], include_dirs=[numpy_include]),
  File "/Users/zhangxin/anaconda2/lib/python2.7/site-packages/Cython/Build/Dependencies.py", line 897, in cythonize
    c_options = CompilationOptions(**options)
  File "/Users/zhangxin/anaconda2/lib/python2.7/site-packages/Cython/Compiler/Main.py", line 559, in __init__
    raise ValueError(message)
ValueError: got unknown compilation option, please remove: include_dirs
```


## 问题3
```
➜  text-detection-ctpn git:(zxdev_mac) python ctpn/demo.py 
Traceback (most recent call last):
  File "ctpn/demo.py", line 8, in <module>
    from lib.networks.factory import get_network
  File "/Users/zhangxin/github/text-detection-ctpn/lib/__init__.py", line 1, in <module>
    from . import fast_rcnn
  File "/Users/zhangxin/github/text-detection-ctpn/lib/fast_rcnn/__init__.py", line 2, in <module>
    from . import train
  File "/Users/zhangxin/github/text-detection-ctpn/lib/fast_rcnn/train.py", line 5, in <module>
    from ..roi_data_layer.layer import RoIDataLayer
  File "/Users/zhangxin/github/text-detection-ctpn/lib/roi_data_layer/__init__.py", line 1, in <module>
    from . import roidb
  File "/Users/zhangxin/github/text-detection-ctpn/lib/roi_data_layer/roidb.py", line 5, in <module>
    from lib.utils.bbox import bbox_overlaps
  File "/Users/zhangxin/github/text-detection-ctpn/lib/utils/__init__.py", line 6, in <module>
    from . import gpu_nms
ImportError: cannot import name gpu_nms
```

解决方法：
注释掉lib/utils/__init__.py中的from . import gpu_nms
