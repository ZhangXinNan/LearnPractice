
Centos 7默认gcc版本为4.8，有时需要更高版本的，这里以升级至8.3.1版本为例，分别执行下面三条命令即可，无需手动下载源码编译

# 1 安装centos-release-scl
```bash
sudo yum install centos-release-scl
```

# 2 安装devtoolset
注意，如果想安装7.*版本的，就改成devtoolset-7-gcc*，以此类推
```bash
sudo yum install devtoolset-8-gcc*

sudo yum install devtoolset-7-gcc*
```

# 3 激活对应的devtoolset
所以你可以一次安装多个版本的devtoolset，需要的时候用下面这条命令切换到对应的版本
```bash
scl enable devtoolset-8 bash

scl enable devtoolset-7 bash
```
大功告成，查看一下gcc版本
```bash
gcc -v
```
显示为 gcc version 8.3.1 20190311 (Red Hat 8.3.1-3) (GCC)

补充：这条激活命令只对本次会话有效，重启会话后还是会变回原来的4.8.5版本，要想随意切换可按如下操作。

首先，安装的devtoolset是在 /opt/sh 目录下的，如图



 每个版本的目录下面都有个 enable 文件，如果需要启用某个版本，只需要执行
```bash
source ./enable
```
所以要想切换到某个版本，只需要执行
```bash
source /opt/rh/devtoolset-8/enable

source /opt/rh/devtoolset-7/enable
```
可以将对应版本的切换命令写个shell文件放在配了环境变量的目录下，需要时随时切换，或者开机自启

# 4 直接替换旧的gcc

旧的gcc是运行的 /usr/bin/gcc，所以将该目录下的gcc/g++替换为刚安装的新版本gcc软连接，免得每次enable
```bash
mv /usr/bin/gcc /usr/bin/gcc-4.8.5

ln -s /opt/rh/devtoolset-8/root/bin/gcc /usr/bin/gcc

mv /usr/bin/g++ /usr/bin/g++-4.8.5

ln -s /opt/rh/devtoolset-8/root/bin/g++ /usr/bin/g++

gcc --version

g++ --version
```

# 参考
1. 不好使的。[2020.11.20(记录一次gcc升级和cmake安装)](https://blog.csdn.net/m0_48758256/article/details/109852311)
2. 好使的。[CentOS 7升级gcc版本](https://www.cnblogs.com/jixiaohua/p/11732225.html)

