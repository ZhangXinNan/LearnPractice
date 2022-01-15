

# 1 问题
安装完 ubuntu 20.04LTS 和 cuda 后无法启动图形界面。


# 2 解决办法
如果你没有瞎卸载很多东西的话，先在字符界面输入你的用户名和密码， 先尝试这个命令：
```bash
sudo systemctl isolate graphical.target
```
不行的话，我的解决办法：安装图形化界面ubuntu-desktop 或者unity
```bash
sudo apt-get install ubuntu-desktop
sudo apt-get install unity
```
然后再用命令行命令进入图形化界面

```bash
sudo service gdm3 start
```
没有1111号这个插件的话，可以下载安装，命令如下：

```
sudo apt-get install lightdm
```
输入上述命令后，会让你选gdm3或者lightdm。建议选择gdm3，因为我ubuntu18.04开始选的是lightdm，结果3天没进去图形化界面，眼睛都哭瞎了。
然后再输入如下命令：

sudo service gdm3 start


# 3 参考资料
1. [ubuntu18.04在安装CUDA并更新显卡驱动后无法进入图形界面的解决办法_m0_48284265的博客-程序员资料_ubuntu安装cuda后进不了图形界面](https://www.its304.com/article/m0_48284265/118359080)
2. [ubuntu20.04内核自动升级之后，nvidia-smi显示NVIDIA-SMI has failed because it couldn’t communicate with the NIVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.重装驱动之后无法正常进去图形化界面](https://www.cxybb.com/article/m0_54258455/112211576)
3. [ubuntu 18.04安装NVIDIA驱动失败经历 --- 不能进入图形界面](https://blog.csdn.net/Rachelint/article/details/104173376)
4. [nvidia-smi指令报错：Failed to initialize NVML: Driver解决](https://zhuanlan.zhihu.com/p/94378201)



