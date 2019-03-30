

github地址：[HKUST-Aerial-Robotics/VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)


# 1 安装OpenCV 3.3.1
参考我的博客：
[ubuntu安装opencv](https://blog.csdn.net/sdlypyzq/article/details/88852286)

其他参考：
[error：cv_bridge---opencv和ros连接起来的桥](http://www.cnblogs.com/Jessica-jie/p/6959309.html)



# 2 安装Eigen
下载指定版本3.3.3，解压。无需安装。
或者
```bash
sudo apt-get install libeigen3-dev
```

# 3 ceres
安装文档：[installation of ceres](http://ceres-solver.org/installation.html)


# 4 安装附加ROS包
**要先安装ROS**

```bash
# sudo apt-get install ros-YOUR_DISTRO-cv-bridge ros-YOUR_DISTRO-tf ros-YOUR_DISTRO-message-filters ros-YOUR_DISTRO-image-transport

# kinetic
sudo apt-get install ros-kinetic-cv-bridge ros-kinetic-tf ros-kinetic-message-filters ros-kinetic-image-transport
```

# 5 安装catkin_make
检查ROS，是否未安装好
```bash
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```


# 6 Build VINS-Mono on ROS
```bash
cd ~/catkin_ws/src
git clone https://github.com/HKUST-Aerial-Robotics/VINS-Mono.git
cd ../
catkin_make
# source ~/catkin_ws/devel/setup.bash
source /home/zhangxin/tools/catkin_ws/devel/setup.bash
```


# 7 Visual-Inertial Odometry and Pose Graph Reuse on Public datasets
```bash
roslaunch vins_estimator euroc.launch
roslaunch vins_estimator vins_rviz.launch
# rosbag play YOUR_PATH_TO_DATASET/MH_01_easy.bag 
rosbag play /media/zhangxin/DATA/data_public/SLAM/EuRoC/MH_01_easy.bag
```