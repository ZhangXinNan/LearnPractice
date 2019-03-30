



## 参考
* [ROS 不能再详细的安装教程](https://www.cnblogs.com/liu-fa/p/5779206.html)
* [Ubuntu16.04安装ROS kinetic](https://blog.csdn.net/softimite_zifeng/article/details/78632211)
* [Ubuntu install of ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu)


## 1.1 配置Ubuntu库

Configure your Ubuntu repositories to allow "restricted," "universe," and "multiverse." 

## 1.2 设置sources.list

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

## 1.3 设置keys
```bash
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA11
```


## 1.4 安装

```bash
sudo apt-get update
```
输出：
```bash
Err:10 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main amd64 Packages
  404  Not Found
Ign:11 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main i386 Packages
Ign:12 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main all Packages
Ign:13 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main Translation-en_US
Ign:14 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main Translation-en
Ign:15 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main amd64 DEP-11 Metadata
Ign:16 http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial/main DEP-11 64x64 Icons
Fetched 325 kB in 25s (12.8 kB/s)
Duplicate sources.list entry http://mirrors.tuna.tsinghua.edu.cn/ubuntu xenial Release
Reading package lists... Done
W: The repository 'http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu xenial Release' does not have a Release file.
N: Data from such a repository can't be authenticated and is therefore potentially dangerous to use.
N: See apt-secure(8) manpage for repository creation and user configuration details.
E: Failed to fetch http://ppa.launchpad.net/bzindovic/suitesparse-bugfix-1319687/ubuntu/dists/xenial/main/binary-amd64/Packages  404  Not Found
E: Some index files failed to download. They have been ignored, or old ones used instead.
W: Duplicate sources.list entry http://mirrors.tuna.tsinghua.edu.cn/ubuntu xenial Release

```


安装
```bash
# Desktop-Full Install: (Recommended) 
sudo apt-get install ros-kinetic-desktop-full
```
输出：
```bash
zhangxin@zhangxin-Alienware-17-R5:~/tools$ sudo apt-get install ros-kinetic-desktop-full
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ros-kinetic-desktop-full is already the newest version (1.3.2-0xenial-20190320-232543-0800).
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 apt-utils : Depends: apt (= 1.2.27) but 1.2.29ubuntu0.1 is to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).
```


## 1.5 初始化rosdep
```bash
sudo rosdep init
rosdep update
```


## 1.6 环境设置
```bash
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```


## 1.7 安装创建时的包
```bash
sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
```
输出：
```bash
zhangxin@zhangxin-Alienware-17-R5:~/tools$ sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
Reading package lists... Done
Building dependency tree       
Reading state information... Done
build-essential is already the newest version (12.1ubuntu2).
python-rosinstall is already the newest version (0.7.8-1).
python-wstool is already the newest version (0.1.17-1).
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 apt-utils : Depends: apt (= 1.2.27) but 1.2.29ubuntu0.1 is to be installed
 python-rosinstall-generator : Depends: python-rosdistro (>= 0.7.3) but 0.7.2-100 is to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).
```

## 1.8 Build farm status

```
略
```


# 2 测试
## 2.1 打开Termial，输入以下命令，初始化ROS环境：
```bash
roscore
```

输出：
```bash
zhangxin@zhangxin-Alienware-17-R5:~/tools/catkin_ws$ roscore
The program 'roscore' is currently not installed. You can install it by typing:
sudo apt install python-roslaunch
```

解决办法：
可能是ROS环境变量没设置，可以将以下代码加入~/.bashrc中。
```bash
source /opt/ros/kinetic/setup.bash
```


## 2.2 打开新的Termial，输入以下命令，弹出一个小乌龟窗口：
```bash
rosrun turtlesim turtlesim_node
```


## 2.3 打开新的Termial，输入以下命令，可以在Termial中通过方向键控制小乌龟的移动：
```bash
rosrun turtlesim turtle_teleop_key
```

## 2.4 打开新的Termial，输入以下命令，弹出新的窗口查看ROS节点信息：
```bash
rosrun rqt_graph rqt_graph
```


