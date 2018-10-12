# AlienWare
Service Tag: 1XVBSN2


# bios
(双硬盘主机)硬盘模式：RAID-->ACHI
secure boot --> disabled
legacy-->uefi

选中USB启动

注意：
* 不要勾选安装更新和第三方软件
* 不要选择与其他系统共存，选其他选项
* 启动windows10时硬盘模式RAID



# 分区
swap 主分区 空间起始位置 16G
efi系统分区 逻辑分区 空间起始位置  1000M efi 是uefi引导 
/home ext4日志文件系统 逻辑分区 空间起始位置 50G
/usr  ext4日志文件系统 逻辑分区 空间起始位置 32G  软件安装位置
/  ext4日志文件系统 逻辑分区 空间起始位置 16G



# 安装完后
改回Secure boot

# 查看网上驱动
```
lspci | grep -i net
```





[Alienware 17 R4安装windows10与ubuntu16.04双系统](https://blog.csdn.net/xiaohu50/article/details/78514564)

[Dell Alienware Aurora R6 （1080ti）安装Ubuntu17.04记录](https://blog.csdn.net/qq_17550379/article/details/78546850)


[亲测UEFI启动模式的电脑安装Win10和Ubuntu双系统(dell笔记本和hp笔记本)](https://blog.csdn.net/SeekN/article/details/69808288)

[UEFI模式下win10、Ubuntu双系统安装和问题集锦](https://blog.csdn.net/fangjin_kl/article/details/78676948)