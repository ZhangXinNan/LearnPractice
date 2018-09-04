1. 安装 ubuntu 14.04 
2. 下载cuda, cudnn
3. 关掉图形界面
```
sudo service lightdm stop
```
4. 直接运行安装cuda，里边已经包含显卡驱动 ，不需要单独安装显卡驱动 。
```
chmod +x cuda_8.0.61_375.26_linux.run
./cuda_8.0.61_375.26_linux.run 
 sudo service lightdm start   
```
5. 安装 cudnn
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