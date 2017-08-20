
# 0 准备
现在有ubuntu14+cuda8的docker容器。

# 1 安装pytorch
这里我用pip安装，其他情况可以参考 [pytorch](http://pytorch.org/)。
```
pip install http://download.pytorch.org/whl/cu80/torch-0.1.12.post2-cp27-none-linux_x86_64.whl 
pip install torchvision
```

## 1.1 没有安装pip
```
apt-get install python-pip
```

## 1.2 安装yaml
### 问题
```
build/temp.linux-x86_64-2.7/check_libyaml.c:2:18: fatal error: yaml.h: No such file or directory
```
### 解决方法
```
pip install pyyaml
```

## 1.3 测试pytorch安装是否成功

## 1.4 SystemError: Cannot compile 'Python.h'. Perhaps you need to install python-dev|python-devel.
```
apt-get install python-dev
```

# 2 安装crnn.pytorch
## 2.1 下载crnn.pytorch
参见项目地址 [meijieru/crnn.pytorch](https://github.com/meijieru/crnn.pytorch)

## 2.2 下载模型放到data目录下
```
apt-get install lrzsz
apt-get install unzip

```

## 2.3 测试
```
python demo.py
```


### 2.3.1 问题1 
```
root@ubuntu14cuda8-22cmp:/data/crnn.pytorch-master# python demo.py 
Traceback (most recent call last):
  File "demo.py", line 1, in <module>
    import torch
  File "/usr/local/lib/python2.7/dist-packages/torch/__init__.py", line 53, in <module>
    from torch._C import *
ImportError: libpython2.7.so.1.0: cannot open shared object file: No such file or directory
```
解决方法：
First, install some dependencies:
```
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
```
Then download using the following command:
```
version=2.7.13
cd ~/Downloads/
wget https://www.python.org/ftp/python/$version/Python-$version.tgz
```
Extract and go to the directory:
```
tar -xvf Python-$version.tgz
cd Python-$version
```
Now, install using the command you just tried, using checkinstall instead to make it easier to uninstall if needed:
```
./configure
make
sudo checkinstall
```
Change version to whichever version you need (version=2.7.1 or version=3.6.0, for example).

