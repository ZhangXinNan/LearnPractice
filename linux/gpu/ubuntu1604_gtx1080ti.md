# 查看显卡型号
查看显卡型号：lspci |grep VGA （lspci是linux查看硬件信息的命令），屏幕会打印出主机的集显几独显信息

查看nvidia芯片信息：lspci |grep -i nvidia，会打印出nvidia系列的硬件信息，如果主机安装了没有视频输出的GPU（如tesla系列），这个命令会很有用
[ubuntu查看显卡型号以及查看主机安装的nvidia芯片信息](https://blog.csdn.net/cdw_FstLst/article/details/49861957)

# 查看操作系统版本
查看内核版本命令：
```
cat /proc/version
```

# 安装显卡驱动
到官网下载显卡驱动
```
sudo apt install gcc
sudo apt install make
sudo sh NVIDIA-Linux-x86_64-410.78.run
nvidia-smi
```

# 安装cuda
```
sudo sh cuda_9.0.176_384.81_linux.run
```
显示：
```
Installing the CUDA Toolkit in /usr/local/cuda-9.0 ...
Missing recommended library: libGLU.so
Missing recommended library: libX11.so
Missing recommended library: libXi.so
Missing recommended library: libXmu.so

Installing the CUDA Samples in /home/ubuntu ...
Copying samples to /home/ubuntu/NVIDIA_CUDA-9.0_Samples now...
Finished copying samples.

===========
= Summary =
===========

Driver:   Not Selected
Toolkit:  Installed in /usr/local/cuda-9.0
Samples:  Installed in /home/ubuntu, but missing recommended libraries

Please make sure that
 -   PATH includes /usr/local/cuda-9.0/bin
 -   LD_LIBRARY_PATH includes /usr/local/cuda-9.0/lib64, or, add /usr/local/cuda-9.0/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run the uninstall script in /usr/local/cuda-9.0/bin

Please see CUDA_Installation_Guide_Linux.pdf in /usr/local/cuda-9.0/doc/pdf for detailed information on setting up CUDA.

***WARNING: Incomplete installation! This installation did not install the CUDA Driver. A driver of version at least 384.00 is required for CUDA 9.0 functionality to work.
To install the driver using this installer, run the following command, replacing <CudaInstaller> with the name of this run file:
    sudo <CudaInstaller>.run -silent -driver

Logfile is /tmp/cuda_install_5474.log

```

# 安装cudnn
实际就是解压，然后把include和lib下的文件拷贝过去 。

# 安装caffe
```
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libopenblas-dev

```

## 安装nccl
```
git clone https://github.com/NVIDIA/nccl.git
cd nccl
sudo make install -j4
sudo ldconfig
```


