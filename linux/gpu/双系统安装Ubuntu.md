
# 制作Ubuntu系统盘
0. 插入U盘。
1. 下载Ultraiso,Ubuntu。
2. 打开Ultraiso，并用其打开Ubuntu的iso文件。
3. 写入硬盘映像。
4. 格式化，写入。


[Ubuntu 16.04与Win10双系统双硬盘安装图解](https://blog.csdn.net/fesdgasdgasdg/article/details/54183577)
# 安装Ubuntu
1. 从U盘启动
2.【断网】安装
分区情况
20480MB     主分区      空间起始位置        Ext4日志文件系统        /
10240MB     逻辑分区    空间起始位置        交换空间
400MB       逻辑分区    空间起始位置        Ext4日志文件系统        /boot
128000      逻辑分区    空间起始位置        Ext4日志文件系统        /home

3. 【重点】【重点】【重点】安庄启动引导器的设备，先/boot分区所在的设备
遇到问题：
```
无法将grub-efi-amd64-signed软件包安装/target/中。如果没有GRUB启动引导器，所安装的系统将无法启动。
```

解决方法：
3.1 [安装Ubuntu时遇到“无法将grub-efi-amd64-signed软件包安装到/target/中”或“安装程序向硬盘复制文件时遇到错误”](https://blog.csdn.net/qq_37400312/article/details/77452626)
```
进入Chipset，在进入South Bridge，将onchip sata ytpe设置为AHCI，onchip ide mode设置为Legacy mode
```
新型UEFI，全称“统一的可扩展固件接口”(Unified Extensible Firmware Interface)， 是一种详细描述类型接口的标准。这种接口用于操作系统自动从预启动的操作环境，加载到一种操作系统上。


3.2 [提示“无法将 grub-efi 软件包安装到/target/中，如果没有 GRUB 启动引导期，所安装的系统无法启动。”](https://blog.csdn.net/qq_29985391/article/details/78663823)
```
2、(我的电脑是支持UEFI的)进入BIOS，找到BootMode，有三个选项Auto 、UEFI Only、Legacy Only。  选择Legacy      
Only（传统模式）。
```
# 参考资料



[win10+ubuntu双系统配置](https://blog.csdn.net/qq_31192383/article/details/78876905)
# 设置bios
boot->secure boot选disabled
boot->boot list option 选UEFI
U盘要选带UEFI的那个U盘项。

注：显卡和系统兼容问题。？？？

# 安装系统
选【其它选项】

## 不需要将系统引导器装在/boot分区，其实不需要，因为是UEFI安装，需要把引导器装到“保留BIOS启动区域”。
2049M   主分区      空间起始位置      保留BIOS启动区域
2049M   逻辑分区                    交换空间
40960M  逻辑分区                    /
50000M  逻辑分区                    /home


[Win10下UEFI环境安装Ubuntu 16.04双系统教程](https://blog.csdn.net/DeMonliuhui/article/details/77483523)
1. 进入BIOS设置后（正常都是开机秒按F2）
2. 关闭Security Boot
3. 选择UEFI下的U盘启动，所以整个过程根本不用改为Legacy启动（此种方式启动，又老又慢）

1.swap交换空间
这个也就是虚拟内存的地方。

大小：与电脑内存一致即可，最小不能低于电脑内存的一半。小了不够用，大了没用。
新分区的类型:主分区
新分区的位置：空间起始位置
用于：交换空间

2.efi系统分区
系统引导文件都会在里面

大小：大小最好不要小于256MB，系统引导文件都会在里面，我给的512MB。
新分区的类型:逻辑分区（这里不是主分区，请勿怀疑，老式的boot挂载才是主分区）
新分区的位置：空间起始位置
用于：efi系统分区
注意:它的作用和boot引导分区一样，但是boot引导是默认grub引导的，而efi显然是UEFI引导的。不要按照那些老教程去选boot引导分区，也就是最后你的挂载点里没有“/boot”这一项，否则你就没办法UEFI启动两个系统了。

3./home
这个相当于你的个人文件夹，类似Windows里的User，如果你是个娱乐向的用户，我建议最好能分配稍微大点，因为你的图片、视频、下载内容基本都在这里面，这些东西可不像在Win上面你想移动就能移动的。

大小：最好不要低于8GB，我Ubuntu分区的总大小是64GB，这里我给了30G给home。
新分区的类型:逻辑分区
新分区的位置：空间起始位置
用于：EXT4日志文件系统
挂载点：/home

4./
因为除了home和usr还有很多别的目录，但那些都不是最重要的，“/”就把除了之前你挂载的home和usr外的全部杂项囊括了。

大小：8G左右。
新分区的类型:逻辑分区
新分区的位置：空间起始位置
用于：EXT4日志文件系统
挂载点：/


5./usr
这个相当于你的软件安装位置，Linux下一般来说安装第三方软件你是没办法更改安装目录的，系统都会统一地安装到/usr目录下面。

大小：这个分区必须要大，把剩余的空间都给它就对了。
新分区的类型:逻辑分区
新分区的位置：空间起始位置
用于：EXT4日志文件系统
挂载点：/usr


6.设置安装引导的启动设置
找到类型为efi的设备，如图：/dev/sda7

