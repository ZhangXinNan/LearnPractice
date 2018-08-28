
参考此文章：
[Mahedi-61/cuda_installation_on_ubuntu_18.04](https://gist.github.com/Mahedi-61/2a2f1579d4271717d421065168ce6a73)

[Ubuntu 18.04上CUDA 9.0、cuDNN7.0及Tensorflow 1.8的安装](https://www.cnblogs.com/ArrowKeys/p/9007437.html)

# 安装显卡驱动
```
sudo ubuntu-drivers autoinstall
```
然后重启


# 安装cuda
从NVIDIA官网Legacy Releases下载CUDA 9.0版本的.run安装包 
[cuda 9.0](https://developer.nvidia.com/cuda-90-download-archive)。

## 安装gcc-6/g++-6
由于CUDA 9.0仅支持GCC 6.0及以下版本，而Ubuntu 18.04预装GCC版本为7.3，故手动安装gcc-6与g++-6：
```
sudo apt-get install gcc-6 g++-6
```

之后切换至/usr/bin目录修改符号链接，使GCC 6成为默认使用版本：
```
cd /usr/bin
sudo rm gcc
sudo ln -s gcc-6 gcc
sudo rm g++
sudo ln -s g++-6 g++
```
## 安装cuda 9.0
为CUDA 9.0安装包赋予运行权限并运行之：
```
chmod 775 cuda_9.0.176_384.81_linux.run
sudo ./cuda_9.0.176_384.81_linux.run --no-opengl-libs
```
安装过程中选择不安装驱动，仅安装CUDA与Samples。若提示"You are attempting to install on an unsupported configuration."选择y强制安装（如果前面修改了GCC版本，此处应不报该错误）。
安装完成后若提示安装失败，可参考错误提示增加--override参数重新安装。

## 测试
进入Samples所在目录（默认为~/NVIDIA_CUDA-9.0_Samples），运行命令（所需时间较长）
```
make
```
（若不愿等候太长时间也可进入子目录单独make一些示例程序）
若编译成功（可能有warning）则可以进入bin目录运行其中的程序。以上皆成功时，则CUDA安装成功。


# 安装cudnn
```
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-9.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-9.0/lib64/
sudo chmod a+r /usr/local/cuda-9.0/lib64/libcudnn*
```
