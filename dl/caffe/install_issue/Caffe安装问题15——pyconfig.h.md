
# 1 问题

```
/usr/include/boost/python/detail/wrap_python.hpp:50:23: fatal error: pyconfig.h: No such file or directory
compilation terminated.
Makefile:591: recipe for target '.build_release/src/caffe/layer_factory.o' failed
make: *** [.build_release/src/caffe/layer_factory.o] Error 1
make: *** Waiting for unfinished jobs....
```


# 2 解决
解决办法，找到pyconfig.h的路径，其实就在默认路径里，有可能关闭了。修改Makefile.config
```
PYTHON_INCLUDE := /usr/include/python2.7 \
		/usr/lib/python2.7/dist-packages/numpy/core/include
```