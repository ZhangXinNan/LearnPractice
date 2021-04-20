# Mac上编译安装 opencv和opencv_contrib

# 下载源代码
github源代码地址：
[opencv](https://github.com/opencv/opencv)
[opencv_contrib](https://github.com/opencv/opencv_contrib)
这两个项目我放在同一级目录下。目录分别为：
```
/Users/zhangxin/github/opencv
/Users/zhangxin/github/opencv_contrib
```
# 编译
先进入到opencv目录下，依次执行以下操作
```bash
mkdir release
cd release

# 
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D INSTALL_C_EXAMPLES=OFF \
      -D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON \
      -D BUILD_opencv_legacy=OFF \
      ../opencv
# 

make
sudo make install
```
** 注意要写绝对路径 **

# 问题
## 问题 1 
### error: unknown type name 'constexpr'
```
/usr/local/include/tesseract/publictypes.h:33:1: error: unknown type name 'constexpr'
```
### 解决方法：
```
sudo vim /usr/local/include/tesseract/publictypes.h
//add this line
#define constexpr const
```

## 问题2
### RuntimeError: module compiled against API version 0xa but this version of numpy is 0x9
```
RuntimeError: module compiled against API version 0xa but this version of numpy is 0x9
Traceback (most recent call last):
  File "feature_matching.py", line 2, in <module>
    import cv2
  File "/Users/zhangxin/Library/Python/2.7/lib/python/site-packages/cv2/__init__.py", line 9, in <module>
    from .cv2 import *
ImportError: numpy.core.multiarray failed to import
```

解决方法:不使用mac上默认的python，而是用brew安装的python
```
alias python='/usr/local/Cellar/python/2.7.13/bin/python'
```



# 参考资料
[Installation in Linux](http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html)
[opencv/opencv_contrib](https://github.com/opencv/opencv_contrib)