

# 1 问题
安装CUDA时出现
```bash
sudo sh cuda_10.1.105_418.39_linux.run

 Failed to verify gcc version. See log at /var/log/cuda-installer.log for details.
```

# 2 解决

我安装 的是CUDA10，对应要用的GCC是8，因此
```bash
sudo apt-get install gcc-8 g++-8
```