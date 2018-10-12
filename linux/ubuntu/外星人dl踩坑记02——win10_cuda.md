
# 1. 确保windows正常使用
# 2. 下载安装cuda，并安装
win10下安装就特别简单了，双击exe，其他默认就可以了。
安装完成后命令行执行```nvcc -V ```看是否安装成功。

问题：
1. 这里存在一个疑问，安装 cuda前需要不需要卸载所有nvidia的东西？？？

2. 如果出现 不兼容，则参考 [Win10 安装Tensorflow-GPU版教程（附CUDA安装 could not fine compatible graphic hardware问题解答）](https://blog.csdn.net/ygjustgo/article/details/78883981)
```
补充： 
我在安装CUDA8.0的时候遇到了如下问题：The graphics driver could not find compatible graphics hardware。这个问题的主要原因是你本机的显卡驱动版本比CUDA8.0中自带的驱动版本高（实际上，不论CUDA装的哪个版本，只要本机驱动比CUDA自带驱动版本高，都可能出现这个问题）。 
解决办法： 
直接点击继续—>同意并继续—>自定义（高级）—>只选择CUDA进行安装，最后安装成功。 
在自定义界面可以看到CUDA自带驱动版本号以及目前本机驱动版本号，如果本机版本号高于CUDA自带版本号，就不要再勾选安装了。 
```


# 3. 下载cudnn，并安装
注意cudnn的版本一定要与cuda的版本相匹配。
cudnn下载后解压，复制到```C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0```即可。

# 4. 下载anaconda，并安装
这个也不用多说。

# 5. 使用anaconda安装tensorflow-gpu

## 5.1 打开Anaconda Navigator，创建Tensorflow环境
根据自己的需要选择python2.7或者3.6
```
conda create -n tensorflow python=3.6
# 这里又有一个坑，tensorflow在windows下不支持2.7版本了，只能用3.5或者3.6
conda create -n tf_py2 python=2.7
```

## 5.2 打开Anaconda Prompt，输入
```activate Tensorflow```

## 5.3 安装tensorflow
```
pip install --ignore-installed --upgrade tensorflow-gpu 
```




# 官方地址：
cuda下载地址：
[CUDA Toolkit 9.0 Downloads](https://developer.nvidia.com/cuda-90-download-archive?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal)

tensorflow 安装文档：
[在 Windows 上安装 TensorFlow](https://www.tensorflow.org/install/install_windows?hl=zh-cn)

# 参考：
[Win10环境+ CUDA9.0 +CUDNN7.0+TensorFlow1.7/1.6/1.5配置](https://blog.csdn.net/xuefengyang666/article/details/79422012)

[win10+cuda8.0+cudnn+Tensorflow（GPU）安装](https://blog.csdn.net/weixin_36368407/article/details/54177380)


[CUDA】CUDA9.0+VS2017+win10详细配置](https://blog.csdn.net/u013165921/article/details/77891913)
