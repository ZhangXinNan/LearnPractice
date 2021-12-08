
# 1 查看磁盘信息
```bash
sudo fdisk -l
```


```bash
Disk /dev/nvme0n1: 953.89 GiB, 1024209543168 bytes, 2000409264 sectors
Disk model: KXG60ZNV1T02 NVMe KIOXIA 1024GB         
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: E12E300F-A0FA-45B2-BC6B-773E8BFDEECB

Device              Start        End    Sectors   Size Type
/dev/nvme0n1p1       2048    1023999    1021952   499M EFI System
/dev/nvme0n1p2    1024000    1286143     262144   128M Microsoft reserved
/dev/nvme0n1p3    1286144  625516543  624230400 297.7G Microsoft basic data
/dev/nvme0n1p4 1982097408 2000408575   18311168   8.7G Windows recovery environment
/dev/nvme0n1p5  625516544 1982097407 1356580864 646.9G Linux filesystem

Partition table entries are not in disk order.


Disk /dev/sda: 7.28 TiB, 8001563222016 bytes, 15628053168 sectors
Disk model: HGST HUS728T8TAL
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: gpt
Disk identifier: BD84688B-45A2-4D89-AEB3-9F51076B38E5

Device      Start         End     Sectors  Size Type
/dev/sda1    2048      264191      262144  128M Microsoft reserved
/dev/sda2  264192 15628052479 15627788288  7.3T Microsoft basic data
```


# 2 查看UUID
```bash
sudo blkid
```


```
/dev/sda1: PARTLABEL="Microsoft reserved partition" PARTUUID="217b8118-216b-4522-a759-511146e35e0b"
/dev/sda2: LABEL="DATA" UUID="B602D16302D128DF" TYPE="ntfs" PARTLABEL="Basic data partition" PARTUUID="01e747c8-7c0c-4f5d-a737-9145478d60a0"
```

# 3 创建挂载点
```bash
sudo mkdir /data
```

# 4 永远挂载分区
```bash
sudo vi /etc/fstab

# 自动挂载
# 需要注意是ext4还是ntfs
echo UUID="B602D16302D128DF" /data ext4 defaults 0 0 >> /etc/fstab
```

# 5 参考资料
* [Ubuntu挂载硬盘](https://blog.csdn.net/qq_37858386/article/details/109028537)
* [Linux——Ubuntu系统挂载硬盘方法总结（开机自动挂载）](https://cloud.tencent.com/developer/article/1746763)
* [格式化云硬盘-linux](https://docs.ucloud.cn/udisk/userguide/format/linux)



