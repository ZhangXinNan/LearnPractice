

我的电脑安装了win10+ubuntu14，原来是安装的win7，没想到可以直接从win7安装win10，方便简单很多。而安装了win10之后，需要分出一个区用来安装ubuntu。具体可以参考 [Windows10+Ubuntu双系统安装[多图]](http://www.jianshu.com/p/2eebd6ad284d)。

在ubuntu下安装cuda和cudnn。
### 1. 安装 ubuntu 14.04 
### 2. 下载cuda, cudnn
### 3. 关掉图形界面
```
sudo service lightdm stop
```
### 4. 直接运行安装cuda，里边已经包含显卡驱动 ，**不需要单独安装显卡驱动** 。
```
chmod +x cuda_8.0.61_375.26_linux.run
./cuda_8.0.61_375.26_linux.run 
 sudo service lightdm start   
```
### 5. 安装 cudnn
解压
```
tar -xvf cudnn-8.0-linux-x64-v5.0-ga.tgz_ubuntu
```
拷贝文件
```
sudo mv cuda/include/cudnn.h /usr/local/cuda/include/
sudo mv cuda/lib64/libcudnn.so.5.0.5 cuda/lib64/libcudnn_static.a /usr/local/cuda/lib64/
```
创建软链接 
```
sudo ln -s libcudnn.so.5.0.5 libcudnn.so.5    
sudo ln -s libcudnn.so.5 libcudnn.so
```


### 6. 配置环境变量

```
export CUDA=/usr/local/cuda
export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:$CUDA/include
export LD_LIBRARY_PATH=$CUDA/lib:$LD_LIBRARY_PATH
export PATH=$CUDA/bin:$PATH
export CUDA_TOOLKIT_ROOT_DIR=$CUDA/bin
export MANPATH=$CUDA/doc/man:$MANPATH
```

有经验 的同事提示，把环境变量单独写个脚本，比如把如下环境变量写到~/shell/cuda.sh里，然后添加~/shell/linux.sh，写入
```
source /home/zhangxin/shell/cuda.sh
```
再在~/.bashrc最后添加
```
source ~/shell/linux.sh
```
，这样来管理环境变量，就不需要再改.bashrc，避免改乱。







参考资料：
[安装配置 Ubuntu 14.04 + CUDA8.0 + cuDNN v5 + caffe](http://www.jianshu.com/p/69a10d0a24b9)