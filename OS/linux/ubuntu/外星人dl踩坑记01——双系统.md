

2016年曾经在京东上配了一个带GTX 1070的主机，主机共花费8500元。去年实在受不了主机太大太占空间太麻烦扯线，于是卖掉，卖了6600元。
念叨了一年多，2018在自己31岁生日前买个外星人笔记本（17寸，gtx1070），这三年一直用macbook pro，实在是被AlienWare的重量震撼了————太大太重了！

# 一、安装双系统 win10 + ubuntu 16.04
自带win10系统，想着搞深度学习，还是用ubuntu吧。于是下载好了ubuntu16.04，并刻录到U盘，这个一般没什么问题。
从网上找了一些教程安装 双系统，操作如下：
1. 修改bios设置，开机按F2，修改bios
```
(双硬盘主机)硬盘模式：RAID-->ACHI
secure boot --> disabled
legacy-->uefi 
```

注意：
* 不要勾选安装更新和第三方软件
* 不要选择与其他系统共存，选其他选项

2. 安装过程中分区
```
# 分区
swap 主分区 空间起始位置 16G
efi系统分区 逻辑分区 空间起始位置  1000M efi 是uefi引导 
/home ext4日志文件系统 逻辑分区 空间起始位置 50G
/usr  ext4日志文件系统 逻辑分区 空间起始位置 32G  软件安装位置
/  ext4日志文件系统 逻辑分区 空间起始位置 16G
```

3. 安装完成后，ubuntu可以正常启动，按说这时应该继续安装 显卡驱动 、无线网卡驱动 、cuda、cudnn、tensorflow-gpu等等。但是我发现windows启动不了了。需要修改硬盘模式为RAID，才可以启动win10，但是这样ubuntu又启动不了了。

# 参考资料
[Alienware 17 R4安装windows10与ubuntu16.04双系统](https://blog.csdn.net/xiaohu50/article/details/78514564)

[Dell Alienware Aurora R6 （1080ti）安装Ubuntu17.04记录](https://blog.csdn.net/qq_17550379/article/details/78546850)


[亲测UEFI启动模式的电脑安装Win10和Ubuntu双系统(dell笔记本和hp笔记本)](https://blog.csdn.net/SeekN/article/details/69808288)

[UEFI模式下win10、Ubuntu双系统安装和问题集锦](https://blog.csdn.net/fangjin_kl/article/details/78676948)