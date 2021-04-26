
# 0 security boot 关掉

# 1 安装ubuntu 18.04
安装界面点E，在linux行最后添加
```bash
 nomodeset
```
再按F10。

# 2 安装显卡驱动


1. 更新ubuntu源。
```bash
cd /etc/apt/
sudo zip sources.list.zip sources.list
sudo gedit sources.list

sudo apt update
```
2. 安装gcc/g++。
```bash
sudo apt install gcc g++
# 安装网络工具
sudo apt install net-tools
sudo apt install cmake
```

3. 安装显卡。
使用【软件和更新】（siftware & Updates）安装开源显卡驱动。

```bash
# 若执行以下命令打印内容，则Nouveau驱动程序被加载
lsmod | grep nouveau
# Nouveau驱动程序被加载时，执行如下；否则到此为止
sudo vim /etc/modprobe.d/blacklist-nouveau.conf
# 创建包含以下内容的文件/etc/modprobe.d/blacklist-nouveau.conf
blacklist nouveau
options nouveau modeset=0
# 重新生成kernel initramfs
sudo update-initramfs -u
```

# 3 安装cuda

