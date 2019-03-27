

[HKUST-Aerial-Robotics/VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)


# 1 安装OpenCV 3.3.1
[tutorial_linux_install](https://docs.opencv.org/3.3.1/d7/d9f/tutorial_linux_install.html)

## 1.1 安装依赖包
```
# [compiler] 
sudo apt-get install build-essential

# [required] 
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev

# [optional] 
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```


## 1.2 编译


### cmake 
```
cd ~/opencv
mkdir build
cd build


# configuring
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..


# without cuda
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


