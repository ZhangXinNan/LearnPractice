
# 1 问题

ImportError: libGL.so.1: cannot open shared object file: No such file or directory

# 2 解决办法
sudo yum install mesa-libGL


# 3 新的问题

Error downloading packages:
  mesa-libGL-18.3.4-12.el7_9.x86_64: [Errno 256] No more mirrors to try.


# 4 解决办法
```bash
yum clean all
yum makecache
yum update -y
```

# 5 参考资料
[ImportError: libGL.so.1 on CentOS](https://stackoverflow.com/questions/60628083/importerror-libgl-so-1-on-centos)
[使用yum安装报错：[Errno 256] No more mirrors to try](https://www.cnblogs.com/python-wen/p/12360070.html)

