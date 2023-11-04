
# 0 准备
* [ubuntu 22.04.02 LTS](https://releases.ubuntu.com/22.04/ubuntu-22.04.2-desktop-amd64.iso)
* [pytorch 2.0.0](https://pytorch.org/) cuda 11.7 & 11.8
* [paddlepaddle 2.4](https://www.paddlepaddle.org.cn/) CUDA 11.7 & 11.6 & 11.2 & 10.2
* [CUDA 11.7]()
```bash
wget https://developer.download.nvidia.com/compute/cuda/11.7.0/local_installers/cuda_11.7.0_515.43.04_linux.run
sudo sh cuda_11.7.0_515.43.04_linux.run
```
* [nvidia driver]()
* paddlepaddle 与 cuda + cudnn 版本
```
CUDA 工具包 11.7 配合 cuDNN v8.4.1(如需多卡支持，需配合 NCCL2.7 及更高；如需使用 PaddleTensorRT 推理，需配合 TensorRT8.4.2.4)
```

# 1 安装显卡驱动
打开【软件和更新】。
点击附加驱动安装显卡驱动

# 2 安装gcc
新安装的Ubuntu22.04 没有安装gcc，需要安装gcc。在终端输入gcc -version 查看有没有gcc。

执行命令
```bash
sudo apt install gcc
```

# 3 安装无线网卡驱动
lspci是查看设备上pcie设备信息的命令。该命令的不同参数配合，在查看pcie设备和定位pcie问题时很有用。包括查看pcie设备中断号、查看配置空间内容、修改配置空间寄存器等操作。
```bash
lspci
```
在我的外星人笔记本上显示：
```bash
44:00.0 Ethernet controller: Qualcomm Atheros Killer E2500 Gigabit Ethernet Controller (rev 10)
45.00.0 Network controller: Intel Corporation Wireless-AC 9260 (rev 29)
```
其中 Ethernet Controller 后是以太网卡型号，Network controller 后面的就是无线网卡型号。





# 4 安装cuda


# 5 安装cudnn



# 参考资料
* [Ubuntu 22.04安装Cuda11.7和cudnn8.6](https://zhuanlan.zhihu.com/p/581720480) 到了安装显卡驱动时出错，无法继续。
* [Ubuntu18-22.04安装和干净卸载nvidia显卡驱动——超详细、最简单](https://blog.csdn.net/Perfect886/article/details/119109380) lightdm 安装失败，显卡安装失败。
* [Ubuntu 22.04 LTS下安装1030 GPU 的驱动(图文详解)](https://blog.csdn.net/weixin_38493195/article/details/124380112) 使用 sudo apt-get install nvidia-driver-515 安装显卡驱动成功。就是那么简单，无语了。
