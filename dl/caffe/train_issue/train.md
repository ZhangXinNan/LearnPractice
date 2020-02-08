## 问题1
```
F0101 22:55:26.495918  8615 caffe.cpp:254] Multi-GPU execution not available - rebuild with USE_NCCL
*** Check failure stack trace: ***
    @     0x7f7f26d835cd  google::LogMessage::Fail()
    @     0x7f7f26d85433  google::LogMessage::SendToLog()
    @     0x7f7f26d8315b  google::LogMessage::Flush()
    @     0x7f7f26d85e1e  google::LogMessageFatal::~LogMessageFatal()
    @           0x40bfd8  train()
    @           0x4072e0  main
    @     0x7f7f25cf4830  __libc_start_main
    @           0x407b09  _start
    @              (nil)  (unknown)
Aborted (core dumped)
```

解决方法：
```
# NCCL acceleration switch (uncomment to build with NCCL)
# https://github.com/NVIDIA/nccl (last tested version: v1.2.3-1+cuda8.0)
USE_NCCL := 1
```



## 问题2
```
In file included from ./include/caffe/parallel.hpp:19:0,
                 from src/caffe/net.cpp:13:
./include/caffe/util/nccl.hpp:5:18: fatal error: nccl.h: No such file or directory
compilation terminated.
Makefile:581: recipe for target '.build_release/src/caffe/net.o' failed
make: *** [.build_release/src/caffe/net.o] Error 1
```

解决办法：
```
Step 4 安装 NCCL库 
多GPUs进行并行计算，Caffe自带实现. 在多个 GPU 上运行 Caffe 需要使用 NVIDIA NCCL.
$ git clone https://github.com/NVIDIA/nccl.git
$ cd nccl
$ sudo make install -j4
$ sudo ldconfig

```


## 问题3
```
root@ac8da840c10b:/data/zhangxin/github/caffe# caffe
/data/zhangxin/github/caffe/build/tools/caffe.bin: error while loading shared libraries: libnccl.so.1: cannot open shared object file: No such file or directory
```

解决方法：
```
ldconfig
```


## 问题4
