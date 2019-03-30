

## 2.1 ROS图
* ROS图中的节点：　一个发送和接收消息的软件模块。
* ROS图中的边：   两个节点之间传递的消息。



## 2.2 roscore
roscore　是一个向节点提供连接信息，以便节点间互相传递信息的服务程序。每个节点在启动时连接到roscore，并注册该节点发布和订阅的消息。


## 2.3 catkin 工作区 ROS程序包
### 2.3.1 catkin

### 2.3.2 工作区
* 可以创建多个ROS工作区，但是任何时刻只能在其中一个工作区中工作。
* 首先需要确认ROS全局设置的脚本加入.bashrc中。
```bash 
source /opt/ros/kinetic/setup.bash
```

创建一个catkin工作区并初始化
```bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
catkin_init_workspace
```


创建工作区文件。build是使用C++时catkin存放库和可执行程序的地方。devel。
```bash
cd ~/catkin_ws
catkin_make
```

添加使用的工作区的setup.bash，否则无法找到代码。
```bash
source ~/catkin_ws/devel/setup.bash
```


### 2.3.3 ROS程序包
创建一个包，依赖于rospy
```bash
cd ~/catkin_ws/src
catkin_create_pkg my_awesome_code rospy
```
结果：
```bash
catkin_ws
    build
    devel
    src
        CMakeLists.txt
        my_awesome_code
            CMakeLists.txt
            package.xml         # 描述包的内容及catkin如何与之交互
            src
```




## 2.4 rosrun

启动roscore实例
```bash
roscore
```

在另一个终端中运行。
* rosrun  寻找程序包中的可执行程序并且向这个程序传递任何参数。
```bash
rosrun rospy_tutorials talker
```

在第三个终端上运行
```bash
rosrun rospy_tutorials listener
```

在第四个终端，启动基于QT的ROS图可视化工具rqt_graph
```bash
rqt_graph
```
![](rosgraph.png)



## 2.5 命名 命名空间 重映射
### 2.5.1 命名

### 2.5.2 命名空间

### 2.5.3 重映射


## 2.6 roslauch
roslauch  自动启动一系列ROS节点的命令行工具。roslauch操作lauch文件，而不是节点。
lauch文件是描述一组节点以及它们的话题。



## 2.7 tab键
自动补全命令。

## 2.8 tf: 坐标系转换


## 2.9 小结



