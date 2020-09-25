问题：
```
./include/caffe/util/db_lmdb.hpp:8:18: fatal error: lmdb.h: No such file or directory
compilation terminated.
Makefile:591: recipe for target '.build_release/src/caffe/util/db.o' failed
make: *** [.build_release/src/caffe/util/db.o] Error 1

```


解决方法：
```
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
```
