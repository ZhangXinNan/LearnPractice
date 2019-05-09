
# 1 错误描述
在执行
```bash
make runtest -j8
```
出现如下错误
```bash
root@test02_tianv_1:~/github/caffe# make runtest -j8
.build_release/tools/caffe
.build_release/tools/caffe: error while loading shared libraries: libcudnn.so.7: cannot open shared object file: No such file or directory
Makefile:542: recipe for target 'runtest' failed
make: *** [runtest] Error 127
```

# ldconfig
参考：[ldconfig命令](http://man.linuxde.net/ldconfig)

ldconfig命令的用途主要是在默认搜寻目录/lib和/usr/lib以及动态库配置文件/etc/ld.so.conf内所列的目录下，搜索出可共享的动态链接库（格式如lib*.so*）,进而创建出动态装入程序(ld.so)所需的连接和缓存文件。缓存文件默认为/etc/ld.so.cache，此文件保存已排好序的动态链接库名字列表，为了让动态链接库为系统所共享，需运行动态链接库的管理命令ldconfig，此执行程序存放在/sbin目录下。

ldconfig通常在系统启动时运行，而当用户安装了一个新的动态链接库时，就需要手工运行这个命令。

执行
```bash
sudo ldconfig
```
出现如下提示：
```bash
root@test02_tianv_1:~/github/caffe# sudo ldconfig
/sbin/ldconfig.real: /usr/local/cuda-10.1/targets/x86_64-linux/lib/libcudnn.so.7 is not a symbolic link
```


# 2 解决方法
```bash
rm libcudnn.so
rm libcudnn.so.7
sudo ln libcudnn.so.7.5.0 libcudnn.so.7
sudo ln libcudnn.so.7 libcudnn.so
sudo ldconfig
```

# 3 参考：
* [Why do I get “/sbin/ldconfig.real: /usr/local/cuda/lib64/libcudnn.so.7 is not a symbolic link”?](https://askubuntu.com/questions/1025928/why-do-i-get-sbin-ldconfig-real-usr-local-cuda-lib64-libcudnn-so-7-is-not-a)


