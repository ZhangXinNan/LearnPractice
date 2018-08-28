
# 1 自动安装
```
sudo apt install caffe-cuda
```

# 2 源码安装

```
sudo apt  build-dep caffe-cuda
```

# 3 编译问题
## 3.1 could not get lock /var/lib/dpkg/lock-open

解决办法：
```
# 搜索运行的进程
ps -A | grep apt-get

# 杀死
sudo kill 2098

# 打开一个新的终端
```
或者重启

## 3.2 Error: you must put some 'source' URIs in your sources.list

解决办法：
```
# 打开software & updates -> Ubuntu Software -> source code 打勾
```

## 3.3 fatal error: boost/shared_ptr.hpp: no such file or directory
修改Makefile.config

## 3.4 nvcc fatal: Unsupported gpu architecture 'compute_20'
删掉这两行
```
-gencode arch=compute_20,code=sm_20 \
-gencode arch=compute_20,code=sm_21 \
```


## 3.5 libcudnn.so: file format recognized; treating as linker script

解决方法： 
移除除libcudnn.so.7.0.1以外的libcudnn.so文件 
```
/usr/local/cuda/lib64$ sudo rm -rf libcudnn.so libcudnn.so.7 
```
重新生成 
```
sudo ln -s libcudnn.so.7.0.1 libcudnn.so.7 
sudo ln -s libcudnn.so.7 libcudnn.so
```



## 3.6 cannot find -lpython3.6
```
cannot find -lpython3.6
cannot find -lcblas
cannot find -latlas
```

解决方法：
（1）修改PYTHON_INCLUDE路径，并检查是否正确。
（2）把mkl,open,atlas试一遍。结果还是不行，自己安装OpenBlas。

## 3.7 make runtest 
```
error while loading shared libraries: libhdf5_hl.so.100: cannot open shared object file: No such file or directory
```

修改makefile.config或者在环境变量里添加其路径