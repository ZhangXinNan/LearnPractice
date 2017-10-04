下面演示在macbookpro上安装Anaconda。其他平台上安装类同。首先需要先把系统平台，是windows还是linux,还是mac, 再次选择python的版本2还是3，最后就是选择安装图形界面的还是命令行的。比如我是mac、python2、command，则下载的软件为[https://repo.continuum.io/archive/Anaconda2-4.4.0-MacOSX-x86_64.sh](https://repo.continuum.io/archive/Anaconda2-4.4.0-MacOSX-x86_64.sh)
# Anaconda的卸载
## 删除原有软件
```
rm -rf ~/anaconda
```
## 去掉原有环境变量
在~/.bash_profile是去除原来的环境变量
## 去掉原来的隐藏文件
```
rm -rf ~/.condarc ~/.conda ~/.continuum
```

# 安装
```
bash Anaconda2-4.4.0-MacOSX-x86_64.sh 
```

参考资料：
[OS X Anaconda install](https://conda.io/docs/install/full.html#os-x-anaconda-install)
[下载地址](https://www.continuum.io/downloads)