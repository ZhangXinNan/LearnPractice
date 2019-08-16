
# 1 问题
电脑上安装了双系统，在windows上格掉一个分区后，启动不了ubuntu，出现
```
error : unknown filesystem
grub rescue
```


# 2 解决
## 2.1 查看有哪些分区
```bash
ls
```


## 2.2 寻找ubuntu在哪个分区
```bash
# 我的是hd1,msdos5
ls (hd1,msdos5)/grub
```

## 2.3 修改启动分区
```bash
# grub rescue
root=hd1,msdos5
prefix=(hd1,msdos5)/grub
# set root=(hd1,msdos5)
# nromal
insmod normal
normal
```

## 2.4 按C进入命令行模式
```bash
# set root=(hd1,msdos5)
# set prefix=(hd1,msdos5)/grub
# linux /vmlinuz root=/dev/sda5
```

## 2.5 进入ubuntu 进行修复
```bash
sudo update-grub
sudo grub-install /dev/sda
```
