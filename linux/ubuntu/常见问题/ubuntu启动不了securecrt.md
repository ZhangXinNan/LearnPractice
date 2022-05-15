
[Ubuntu16.04下安装破解secureCRT和secureFX的操作记录](https://www.cnblogs.com/kevingrace/p/9353963.html)
[关于使用ubuntu，无法用securecrt的问题的解决](https://blog.csdn.net/LittleDream_of_wzj/article/details/81323255)
[linuxmint14 安装完SecureCRT，无法启动。](http://blog.sina.com.cn/s/blog_891a78160101c9sv.html)

# 安装
```bash
sudo dpkg -i scrt-sfx-8.3.4-1699.ubuntu16-64.x86_64.deb
sudo apt-get install openssh-server 
ps -e |grep ssh
```

## 问题１
安装好SecureCRT后启动不了，在命令行中执行：
```bash
zhangxin@zhangxin-Alienware-17-R5:~/Downloads$ sudo SecureCRT
SecureCRT: error while loading shared libraries: libpng16.so.16: cannot open shared object file: No such file or directory
```


解决方法　：
```bash
sudo apt install libpng16-16
```
并不解决问题，又出现　问题２

## 问题２
```bash
zhangxin@zhangxin-Alienware-17-R5:~/Downloads$ sudo SecureCRT
SecureCRT: /usr/lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.22' not found (required by SecureCRT)
```


## 解决　办法　：卸载新版本，安装旧版本
```
sudo dpkg -r scrt
sudo dpkg -i scrt-sfx-8.3.4-1699.ubuntu16-64.x86_64.deb
```


# 破解
```bash
sudo perl securecrt_linux_crack.pl /usr/bin/SecureCRT
```