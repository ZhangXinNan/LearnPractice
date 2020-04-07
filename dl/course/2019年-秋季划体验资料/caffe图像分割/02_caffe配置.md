

# 1 英伟达环境配置

进入命令行界面 ctrl + alt + F1
```bash
# 关闭图形界面
sudo service lightdm  stop

sudo ./NVIDIA*.run

# 重新开启图像界面
sudo service lightdm start

# 查看驱动安装结果
nvidia-smi
```

# 2 nvidia驱动安装问题
## 2.1 笔记本双显卡系统，登录界面无限循环，无法进入桌面。


普通笔记本一般默认采用集显作为视频输出，此时没有关闭opengl文件的安装，会继续使用ubuntu默认的nouveau驱动，而后者已经被禁掉。

```bash
sudo ./NVIDIA*.run -no-opengl-files 只安装驱动文件，不安装OpenGL文件。
# 或者
sudo ./cuda*.run --no-opengl-libs
```

## 2.2 The Nouveau kernel driver is currently in use by your system

1. 禁用ubuntu默认的驱动nouveau
2. vim /etc/modprobe.d/blacklist.conf
3. blacklist nouveau 禁用nouveau驱动
4. sudo update-initramfs -u 更新新kernel
5. lsmod | grep nouveau 查看是否更新


# 3 CUDA 环境配置
```bash
sudo dpkg -i cuda-repo-ubuntu*.deb

sudo apt-key add /var/cuda-repo-<version>/*.pub

sudo apt-get update

sudo apt-get install cuda

cd /usr/local/cuda-8.0/samples/1_Utilities/deviceQuery 
sudo make 
./deviceQuery
```
注意在最后选择是否安装cuda自带的driver时，选择否，因为前面已经安装好驱动。




