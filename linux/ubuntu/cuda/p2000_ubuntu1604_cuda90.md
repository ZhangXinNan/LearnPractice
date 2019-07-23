
# 1 安装ssh
参考 ubuntu_使用问题04_ssh.md



# 2 挂载机械硬盘，设置为新的home目

## 2.1 自动挂载硬盘

```bash
# 查看硬盘
sudo fdisk -l

# 查看分区的uuid
sudo blkid

# 配置开机自动挂载，先备份/etc/fstab
sudo vim /etc/fstab
# 添加
UUID=db30df2c-7b8a-4999-9f8f-f65a1c1d840e       /home   ext4    defaults        0       2
```

# 3 安装显卡驱动

## 3.1 
```bash
sudo sh NVIDIA-Linux-x86_64-378.13.run
# 报错
 ERROR: You appear to be running an X server; please exit X before installing.  For further details, please see the section INSTALLING THE NVIDIA DRIVER in the README available on the Linux  
         driver download page at www.nvidia.com.



 ERROR: Installation has failed.  Please see the file '/var/log/nvidia-installer.log' for details.  You may find suggestions on fixing installation problems in the README available on the    
         Linux driver download page at www.nvidia.com.
```


## 3.2 问题2
```bash
sudo sh NVIDIA-Linux-x86_64-378.13.run　--no-x-check
# 报错
The distributeion-provided pre-install scrpt failed! Are your sure you want continue?

ERROR: The Nouveau kernal driver is currently in use by your system. This driver is incompatible with NVIDIA driver, and must be disabled before proceeding. Plesase consult the NVIDIA driver README and your linux distribution's documentation for details on how to correctly disable the Nouveau kernel driver.


ERROR: Installation has failed. Please see the file '/var/log/nvidia-install.log' for details. You may find suggestions on fixing installation problems in the README available on the Linux driver download page at www.nvidia.com.
```

## 3.3Create a file: /etc/modprobe.d/blacklist-nouveau.conf
### 3.3.1
```
sudo vi /etc/modprobe.d/blacklist-nouveau.conf
```

Put the following in the file
```
blacklist nouveau
options nouveau modeset=0
```

### 3.3.2 update-initramfs
```
sudo update-initramfs –u
```

### 3.3.3 reboot
```
sudo reboot
```
### 3.3.4 After reboot
```
lsmod | grep nouveau
```
And there is nothing output. If you output something, you need to check the step.


### 3.3.5 安装显卡驱动
```bash
sudo sh NVIDIA-Linux-x86_64-378.13.run　--no-x-check
# 报错
Error: An error occurred while performing the step : "building kernel modules". See /var/log/nvidia-installer.log for details.
```




