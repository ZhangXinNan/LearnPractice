* [Installing and Configuring Your ROS Environment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)
* [安装并配置ROS环境](http://wiki.ros.org/cn/ROS/Tutorials/InstallingandConfiguringROSEnvironment)





# 1 安装ROS
在开始学习这些教程之前请先按照ROS安装说明完成安装。

> 注意: 如果你是使用类似apt这样的软件管理器来安装ROS的，那么安装后这些软件包将不具备写入权限，当前系统用户比如你自己也无法对这些软件包进行修改编辑。当你的开发涉及到ROS软件包源码层面的操作或者在创建一个新的ROS软件包时，你应该是在一个具备读写权限的目录下工作，就像在你当前系统用户的home目录下一样。

# 2 管理环境
在安装ROS期间，你会看到提示说需要 source 多个setup.*sh文件中的某一个，或者甚至提示添加这条'source'命令到你的启动脚本里面。这些操作是必须的，因为ROS是依赖于某种组合空间的概念，而这种概念就是通过配置脚本环境来实现的。这可以让针对不同版本或者不同软件包集的开发更加容易。

如果你在查找和使用ROS软件包方面遇到了问题，请确保你已经正确配置了脚本环境。一个检查的好方法是确保你已经设置了像ROS_ROOT和ROS_PACKAGE_PATH这样的环境变量，可以通过以下命令查看：

```
export | grep ROS
```
如果发现没有配置，那这个时候你就需要'source'某些'setup.*sh’文件了。

ROS会帮你自动生成这些‘setup.*sh’文件，通过以下方式生成并保存在不同地方：
* 通过类似apt的软件包管理器安装ROS软件包时会生成setup.*sh文件。
* 在rosbuild workspaces中通过类似rosws的工具生成。
* 在编译 或 安装 catkin 软件包时自动生成。


> 注意： 在所有教程中你将会经常看到分别针对rosbuild 和 catkin的不同操作说明，这是因为目前有两种不同的方法可以用来组织和编译ROS应用程序。一般而言，rosbuild比较简单也易于使用，而catkin使用了更加标准的CMake规则，所以比较复杂，但是也更加灵活，特别是对于那些想整合外部现有代码或者想发布自己代码的人。关于这些如果你想了解得更全面请参阅catkin or rosbuild。

如果你是通过ubuntu上的 apt 工具来安装ROS的，那么你将会在'/opt/ros/<distro>/'目录中看到setup.*sh文件，然后你可以执行下面的source命令：


# source /opt/ros/<distro>/setup.bash
请使用具体的ROS发行版名称代替<distro>。

比如你安装的是ROS Indigo，则上述命令改为：

```source /opt/ros/indigo/setup.bash```

在每次打开终端时你都需要先运行上面这条命令后才能运行ros相关的命令，为了避免这一繁琐过程，你可以事先在.bashrc文件（初学者请注意：该文件是在当前系统用户的home目录下。）中添加这条命令，这样当你每次登录后系统已经帮你执行这些命令配置好环境。这样做也可以方便你在同一台计算机上安装并随时切换到不同版本的ROS（比如fuerte和groovy）。

此外，你也可以在其它系统平台上相应的ROS安装目录下找到这些setup.*sh文件。

# 3 创建ROS工作空间


这些操作方法只适用于ROS Groovy及后期版本，对于ROS Fuerte及早期版本请选择rosbuild。

下面我们开始创建一个catkin 工作空间：
```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
```
即使这个工作空间是空的（在'src'目录中没有任何软件包，只有一个CMakeLists.txt链接文件），你依然可以编译它：

```bash
$ cd ~/catkin_ws/
$ catkin_make
```
catkin_make命令在catkin 工作空间中是一个非常方便的工具。如果你查看一下当前目录应该能看到'build'和'devel'这两个文件夹。在'devel'文件夹里面你可以看到几个setup.*sh文件。source这些文件中的任何一个都可以将当前工作空间设置在ROS工作环境的最顶层，想了解更多请参考catkin文档。接下来首先source一下新生成的setup.*sh文件：

```
$ source devel/setup.bash
```
要想保证工作空间已配置正确需确保ROS_PACKAGE_PATH环境变量包含你的工作空间目录，采用以下命令查看：

```
$ echo $ROS_PACKAGE_PATH
/home/<youruser>/catkin_ws/src:/opt/ros/indigo/share:/opt/ros/indigo/stacks
```



