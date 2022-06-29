

# 1 问题
```
/usr/bin/ld:/usr/local/cuda/lib64/libcudnn.so: file format not recognized; treating as linker script
/usr/bin/ld:/usr/local/cuda/lib64/libcudnn.so:1: syntax error
collect2: error: ld returned 1 exit status
Makefile:582: recipe for target '.build_release/lib/libcaffe.so.1.0.0' failed
make: *** [.build_release/lib/libcaffe.so.1.0.0] Error 1
```



# 2 解决方法
```
sudo rm -rf libcudnn.so libcudnn.so.7


sudo ln -s libcudnn.so.7.0.2 libcudnn.so.7
sudo ln -s libcudnn.so.7 libcudnn.so
```

