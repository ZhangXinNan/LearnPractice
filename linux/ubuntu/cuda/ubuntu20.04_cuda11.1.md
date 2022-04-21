
# 1 手动安装
## 1.1 安装驱动
编辑文件 blacklist.conf
```bash
sudo gedit /etc/modprobe.d/blacklist.conf
```

在文件最后部分插入以下两行内容
```bash
blacklist nouveau
options nouveau modeset=0
```

更新系统
```bash
sudo update-initramfs -u
```
重启系统（一定要重启）

在英伟达的官网上查找你自己电脑的显卡型号然后下载相应的驱动。网址：http://www.nvidia.cn/page/home.html

先安装一些依赖库
```bash
sudo apt install build-essential libglvnd-dev pkg-config
```

停止桌面管理器，进入命令行模式
```bash
sudo telinit 3
```

删除已安装的 nvidia 驱动
```bash
sudo apt purge "nvidia*"
```

手动安装下载下来的显卡驱动，不一定是什么名字，以下为示例
```bash
sudo bash NVIDIA-Linux-x86_64-440.82.run
```
> 提示没有gcc


重启
```bash
sudo reboot
```
## 1.2 问题1
开机启动失败：
```bash
ucsi_acpi USBC000:00: con2: failed to register alternate modes
ucsi_acpi USBC000:00: PPM init failed (-110)
```

## 1.3 问题2
```bash
drm:lspcon_init i915 ERROR failed to probe lspcon
lspcon init failed on port D
```



# 2 自动安装


# 参考资料
* [Ubuntu 20.04 手动安装 Nvidia 驱动](https://www.jianshu.com/p/aff231e4ac72)