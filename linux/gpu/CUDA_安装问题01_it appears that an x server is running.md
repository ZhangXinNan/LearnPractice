

安装CUDA时
```
sudo sh ./cuda_9.0.176_384.81_linux.run
```
1. 出现如下问题：
```
It appears that an X server is running . Please exit X before installation. If you're sure that X is not running, but are getting this error, please delete any X lock files in /tmp.
```


删除tmp文件夹下的X lock，这是最先搜到的方法，最后就是要求重启.


2. 又出现新的问题：
```bash
Installing the NVIDIA display driver...
The driver installation is unable to locate the kernel source. Please make sure that the kernel source packages are installed and set up correctly.
If you know that the kernel source packages are installed and set up correctly, you may pass the location of the kernel source with the '--kernel-source-path' flag.
```

3. 安装显卡驱动时，
```
sudo sh NVIDIA---.run
```
出现如下错误：
```bash
ERROR: Installation has failed. Please see the file '/var/log/nvidia-installer.log' for details. You may find suggestions on fixing installation problems in the README available on the Linux driver download page at www.nvidia.com
```

加了--no-x-check后
```bash
The distribution-provided pre-install script failed! Are you sure want to continue?
[Continue installation]  [Abort installation]
```

中间出现如下信息：
```bash
WRANING: Unable to find a suitable destination to install 32-bit
```



# 参考
[How to install NVIDIA.run?](https://askubuntu.com/questions/149206/how-to-install-nvidia-run)

[MxNet Ubuntu Desktop 16.04 安装教程（我遇到的坑）经验总结在帖子最下方](https://discuss.gluon.ai/t/topic/1129)