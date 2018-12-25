

## 问题
```
In file included from ./include/caffe/parallel.hpp:19:0,
                 from ./include/caffe/caffe.hpp:13,
                 from tools/caffe.cpp:15:
./include/caffe/util/nccl.hpp:5:18: fatal error: nccl.h: No such file or directory
compilation terminated.
Makefile:591: recipe for target '.build_release/tools/caffe.o' failed
make: *** [.build_release/tools/caffe.o] Error 1
make: *** Waiting for unfinished jobs....

```


## 解决方法
```
git clone https://github.com/NVIDIA/nccl.git
cd nccl
sudo make install -j4
sudo ldconfig
```
