## 问题
```
PROTOC src/caffe/proto/caffe.proto
CXX .build_release/src/caffe/proto/caffe.pb.cc
CXX src/caffe/blob.cpp
In file included from ./include/caffe/blob.hpp:8:0,
                 from src/caffe/blob.cpp:4:
./include/caffe/common.hpp:5:27: fatal error: gflags/gflags.h: 没有那个文件或目录
compilation terminated.
Makefile:591: recipe for target '.build_release/src/caffe/blob.o' failed
make: *** [.build_release/src/caffe/blob.o] Error 1

```

## 解决方法
```
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
```


