

[HKUST-Aerial-Robotics/VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)


# 1 安装OpenCV 3.3.1
参考我的博客：
[ubuntu安装opencv](https://blog.csdn.net/sdlypyzq/article/details/88852286)

# 2 安装Eigen
下载指定版本3.3.3，解压。无需安装。
或者
```
sudo apt-get install libeigen3-dev
```

# 3 ceres
[installation of ceres](http://ceres-solver.org/installation.html)


# 4 安装附加ROS包
**要先安装ROS**

```
sudo apt-get install ros-YOUR_DISTRO-cv-bridge ros-YOUR_DISTRO-tf ros-YOUR_DISTRO-message-filters ros-YOUR_DISTRO-image-transport

# kinetic
sudo apt-get install ros-kinetic-cv-bridge ros-kinetic-tf ros-kinetic-message-filters ros-kinetic-image-transport
```

# 5 安装catkin_make
检查ROS，是否未安装好
```
echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc
```


# 6 Build VINS-Mono on ROS
```
cd ~/catkin_ws/src
git clone https://github.com/HKUST-Aerial-Robotics/VINS-Mono.git
cd ../
catkin_make
source ~/catkin_ws/devel/setup.bash
```