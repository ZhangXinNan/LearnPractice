## 问题
```
LD -o .build_release/lib/libcaffe.so.1.0.0
CXX tools/caffe.cpp
CXX tools/compute_image_mean.cpp
CXX tools/convert_imageset.cpp
/usr/bin/ld: 找不到 -lcblas
/usr/bin/ld: 找不到 -latlas
collect2: error: ld returned 1 exit status
Makefile:582: recipe for target '.build_release/lib/libcaffe.so.1.0.0' failed
make: *** [.build_release/lib/libcaffe.so.1.0.0] Error 1
make: *** 正在等待未完成的任务....

```



## 解决方法
安装openblas
```
sudo apt-get install libopenblas-dev
```

修改Makefile.config
```
BLAS := open
BLAS_INCLUDE := /usr/include/openblas
BLAS_LIB := /usr/lib

```


