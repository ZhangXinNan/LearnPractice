
## 问题1
```
src/caffe/layers/hdf5_data_layer.cpp:13:18: fatal error: hdf5.h: No such file or directory
compilation terminated.
Makefile:581: recipe for target '.build_release/src/caffe/layers/hdf5_data_layer.o' failed
make: *** [.build_release/src/caffe/layers/hdf5_data_layer.o] Error 1
```

解决方法
```
在Makefile.config文件的第85行，添加/usr/include/hdf5/serial/ 到 INCLUDE_DIRS，也就是把下面第一行代码改为第二行代码。

INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include
-->>
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/
```

## 问题2
```
AR -o .build_release/lib/libcaffe.a
LD -o .build_release/lib/libcaffe.so.1.0.0
/usr/bin/ld: cannot find -lhdf5_hl
/usr/bin/ld: cannot find -lhdf5
/usr/bin/ld: cannot find -lcblas
/usr/bin/ld: cannot find -latlas
collect2: error: ld returned 1 exit status
Makefile:572: recipe for target '.build_release/lib/libcaffe.so.1.0.0' failed
make: *** [.build_release/lib/libcaffe.so.1.0.0] Error 1
```

解决方法：
```
############################## openblas
# BLAS choice:
# atlas for ATLAS (default)
# mkl for MKL
# open for OpenBlas
BLAS := open
# Custom (MKL/ATLAS/OpenBLAS) include and lib directories.
# Leave commented to accept the defaults for your choice of BLAS
# (which should work)!
BLAS_INCLUDE := /usr/include
BLAS_LIB := /usr/lib




# Whatever else you find you need goes here.
INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu/hdf5/serial


```

## 问题3
```
root@ac8da840c10b:/data/zhangxin/github/caffe# make py
CXX/LD -o python/caffe/_caffe.so python/caffe/_caffe.cpp
python/caffe/_caffe.cpp:10:31: fatal error: numpy/arrayobject.h: No such file or directory
compilation terminated.
Makefile:507: recipe for target 'python/caffe/_caffe.so' failed
make: *** [python/caffe/_caffe.so] Error 1
```


解决方法：
```
PYTHON_INCLUDE := /usr/include/python2.7 \
                /usr/lib/python2.7/dist-packages/numpy/core/include \
                /usr/local/lib/python2.7/dist-packages/numpy/core/include

```


## nvcc fatal   : Unsupported gpu architecture 'compute_20'
```
nvcc fatal   : Unsupported gpu architecture 'compute_20'
```
解决方法：
去掉这两行：
```
-gencode arch=compute_20,code=sm_20 \
-gencode arch=compute_20,code=sm_21 \
```


##　错误４
```
/usr/bin/ld: cannot find -lhdf5_hl
/usr/bin/ld: cannot find -lhdf5
collect2: error: ld returned 1 exit status
Makefile:582: recipe for target '.build_release/lib/libcaffe.so.1.0.0' failed
make: *** [.build_release/lib/libcaffe.so.1.0.0] Error 1
make: *** Waiting for unfinished jobs....
```
解决办法：
添加lib路径
```
/usr/lib/x86_64-linux-gnu/hdf5/serial
```



参考资料：
[Caffe - Ubuntu 安装及问题解决](https://blog.csdn.net/zziahgf/article/details/72900948)

