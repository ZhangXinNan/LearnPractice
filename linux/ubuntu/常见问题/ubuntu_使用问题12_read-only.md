
在安装双系统后，启动了windows，再启动ubuntu后，其他盘无法创建文件夹，提示
```bash
Read-only file system
```

解决办法

```bash
# 查询你想修复权限的分区id
sudo fdisk -l
# 进行修复
sudo ntfsfix /dev/sda3
```
然后重启，进入ubuntu后就好了。
