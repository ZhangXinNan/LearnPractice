# 在OSX上安装Caffe，并且使用Anaconda的python环境。

[官网OSX安装Caffe教程](http://caffe.berkeleyvision.org/install_osx.html)

If using Anaconda Python, a modification to the OpenCV formula might be needed Do ```brew edit opencv``` and change the lines that look like the two lines below to exactly the two lines below.
```
-DPYTHON_LIBRARY=#{py_prefix}/lib/libpython2.7.dylib
-DPYTHON_INCLUDE_DIR=#{py_prefix}/include/python2.7
```
If using Anaconda Python, HDF5 is bundled and the hdf5 formula can be skipped.