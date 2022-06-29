
# 出现问题
```bash
[ 50%] Building NVCC (Device) object CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o
/home/zhangxin/github/tensorrtx/yolov5/preprocess.cu:2:10: fatal error: opencv2/opencv.hpp: No such file or directory
    2 | #include <opencv2/opencv.hpp>
      |          ^~~~~~~~~~~~~~~~~~~~
compilation terminated.
CMake Error at yolov5_generated_preprocess.cu.o.Debug.cmake:220 (message):
  Error generating
  /home/zhangxin/github/tensorrtx/yolov5/build/CMakeFiles/yolov5.dir//./yolov5_generated_preprocess.cu.o


make[2]: *** [CMakeFiles/yolov5.dir/build.make:65: CMakeFiles/yolov5.dir/yolov5_generated_preprocess.cu.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:77: CMakeFiles/yolov5.dir/all] Error 2
make: *** [Makefile:84: all] Error 2
```

# 解决方法

编译安装opencv
```bash
# Install minimal prerequisites (Ubuntu 18.04 as reference)
sudo apt update && sudo apt install -y cmake g++ wget unzip
# Download and unpack sources
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.x.zip
unzip opencv.zip
# Create build directory
mkdir -p build && cd build
# Configure
cmake  ../opencv-4.x
# Build
cmake --build .
```

# 参考资料

![Installation in Linux](https://docs.opencv.org/4.x/d7/d9f/tutorial_linux_install.html)


