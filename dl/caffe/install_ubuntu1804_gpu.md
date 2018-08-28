
# 自动安装
```
sudo apt install caffe-cuda
```

# 源码安装

```
sudo apt  build-dep caffe-cuda
```
## could not get lock /var/lib/dpkg/lock-open

解决办法：
```
# 搜索运行的进程
ps -A | grep apt-get

# 杀死
sudo kill 2098

# 打开一个新的终端
```

## Error: you must put some 'source' URIs in your sources.list

解决办法：
```
# 打开software & updates -> Ubuntu Software -> source code 打勾
```

