
# 1 问题


编译都没有问题
```bash
make -j8
make py
make test -j8
make runtest -j8
```

然而在最后runtest时出现如下错误
```bash
error while loading shared libraries: libcudart.so.9.0: cannot open shared object file: No such file or directory
Makefile:542: recipe for target 'runtest' failed
make: *** [runtest] Error 127
```

# 2 解决

设置环境变量：
```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib
```