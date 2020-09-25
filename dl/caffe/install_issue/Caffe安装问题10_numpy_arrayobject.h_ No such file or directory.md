## 问题3
```
root@ac8da840c10b:/data/zhangxin/github/caffe# make py
CXX/LD -o python/caffe/_caffe.so python/caffe/_caffe.cpp
python/caffe/_caffe.cpp:10:31: fatal error: numpy/arrayobject.h: No such file or directory
compilation terminated.
Makefile:507: recipe for target 'python/caffe/_caffe.so' failed
make: *** [python/caffe/_caffe.so] Error 1
```


## 解决方法：
```
PYTHON_INCLUDE := /usr/include/python2.7 \
                /usr/lib/python2.7/dist-packages/numpy/core/include \
                /usr/local/lib/python2.7/dist-packages/numpy/core/include
# 可能路径不与上一行一致，按找到合适的路径添加上。比如也可能是如下路径。
# /home/zhangxin/.local/lib/python2.7/site-packages/numpy/core/include/

```

如果还没有安装pip和numpy ，则安装：
```
sudo apt install python-pip
pip install numpy
```