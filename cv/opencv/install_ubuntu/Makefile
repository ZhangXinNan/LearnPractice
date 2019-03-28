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




