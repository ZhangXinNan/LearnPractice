


# 1 安装OpenCV 3.3.1
[tutorial_linux_install](https://docs.opencv.org/3.3.1/d7/d9f/tutorial_linux_install.html)

## 1.1 安装依赖包
We need CMake to configure the installation, GCC for compilation, Python-devel and Numpy for building Python bindings etc.
```bash
sudo apt-get install cmake
sudo apt-get install gcc g++
```
to support python2:
```bash
sudo apt-get install python-dev python-numpy
```
to support python3:
```bash
sudo apt-get install python3-dev python3-numpy
```
Next we need GTK support for GUI features, Camera support (v4l), Media Support (ffmpeg, gstreamer) etc.
```bash
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
```
to support gtk2:
```bash
sudo apt-get install libgtk2.0-dev
```
to support gtk3:
```bash
sudo apt-get install libgtk-3-dev
```


Optional Dependencies
Above dependencies are sufficient to install OpenCV in your Ubuntu machine. But depending upon your requirements, you may need some extra dependencies. A list of such optional dependencies are given below. You can either leave it or install it, your call :)

OpenCV comes with supporting files for image formats like PNG, JPEG, JPEG2000, TIFF, WebP etc. But it may be a little old. If you want to get latest libraries, you can install development files for system libraries of these formats.
```bash
sudo apt-get install libpng-dev libjpeg-dev libopenexr-dev libtiff-dev libwebp-dev
```

## 1.2 编译


### cmake 
```bash
cd ~/opencv
mkdir build
cd build


# configuring
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
# without cuda 用CUDA可能会出现错误，并且编译时间较长。如果不是特别需要，关掉CUDA。
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_CUDA=OFF ..
# specify install directory
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/home/zhangxin/tools/opencv-3.3.1/release -D WITH_CUDA=OFF ..

```
很多时候我们用不多个不同版本的OpenCV，所以最好指定安装目录，与其他版本OpenCV避免混淆。

### build 
```
make -j8
```


### install 
```
make install
```


# 2 测试代码

## 2.1 C++代码
```c++
#include <iostream>
#include "opencv2/core/version.hpp"

int main(int argc, char ** argv)
{
  std::cout << "OpenCV version: "
            << CV_MAJOR_VERSION << "." 
            << CV_MINOR_VERSION << "."
            << CV_SUBMINOR_VERSION
            << std::endl;
  return 0;
}
```

## 2.2 Makefile
```makefile
CPP = g++

# OpenCV trunk
CPPFLAGS = -L/home/zhangxin/tools/opencv-3.3.1/release/libs \
	   -I/home/zhangxin/tools/opencv-3.3.1/release/include \
	   -Wl,-rpath=/home/zhangxin/tools/opencv-3.3.1/release/libs

# Opencv 2.4.8
#CPPFLAGS = -L/home/krystof/libs/opencv-2.4.8/release/installed/libs \
#            -I/home/krystof/libs/opencv-2.4.8/release/installed/include \
#	    -Wl,-rpath=/home/krystof/libs/opencv-2.4.8/release/installed/libs

all: test

# 注意Makefile里要用制表符
test: main.cpp
	$(CPP) $(CPPFLAGS) $^ -o $@
```

## 2.3 运行
```
make test
./test
```
