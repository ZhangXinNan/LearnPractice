
# 问题
```bash
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

# 解决方法
## 方法1 
ubuntu
```bash
apt install libgl1-mesa-glx
```

```bash
RUN apt-get update ##[edited]
RUN apt-get install 'ffmpeg'\
    'libsm6'\ 
    'libxext6'  -y
# 或者
sudo apt-get update
sudo apt-get install -y libgl1-mesa-dev
```

centos
```bash
yum install mesa-libGL.x86_64
```

## 方法2
```bash
# docker
pip uninstall opencv-python
pip install opencv-python-headless
```




# 参考
[ImportError: libGL.so.1: cannot open shared object file: No such file or directory](https://stackoverflow.com/questions/55313610/importerror-libgl-so-1-cannot-open-shared-object-file-no-such-file-or-directo)