

# 问题
安装双系统后，想从ubuntu下访问windows的硬盘，出现
```bash
ubuntu read-only file system
```

# 解决方法
```bash
sudo ntfsfix /dev/sda1


# 或者
# 不知道是否好使
sudo mount -o remount -o rw /dev/sda1 /media/zhangxin/DATA
```


# 参考
1. [Ubuntu 下不能访问 Windows 文件系统](https://wenzhixin.net.cn/2014/11/20/ubuntu_unable_to_access_windows)


