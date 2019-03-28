



## 参考
* [ROS 不能再详细的安装教程](https://www.cnblogs.com/liu-fa/p/5779206.html)
* [Ubuntu16.04安装ROS kinetic](https://blog.csdn.net/softimite_zifeng/article/details/78632211)
* [Ubuntu install of ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu)


## 1.1 配置Ubuntu库

Configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse." 

## 1.2 设置sources.list

```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

## 1.3 设置keys
```
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA11
```


## 1.4 安装
```
sudo apt-get update

# Desktop-Full Install: (Recommended) 
sudo apt-get install ros-kinetic-desktop-full
```


## 1.5 初始化rosdep
```
sudo rosdep init
rosdep update
```


## 1.6 环境设置
```
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```


## 1.7 安装创建时的包
```
sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```


## 1.8 Build farm status

```
略
```


# 2 测试
## 2.1 打开Termial，输入以下命令，初始化ROS环境：
```
roscore
```


## 2.2 打开新的Termial，输入以下命令，弹出一个小乌龟窗口：
```
rosrun turtlesim turtlesim_node
```


## 2.3 打开新的Termial，输入以下命令，可以在Termial中通过方向键控制小乌龟的移动：
```
rosrun turtlesim turtle_teleop_key
```

## 2.4 打开新的Termial，输入以下命令，弹出新的窗口查看ROS节点信息：
```
rosrun rqt_graph rqt_graph
```


