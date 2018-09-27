
# 安装
```
sudo apt-get install docker-ce
```

# 启动
```
sudo service docker start
```
## 问题：
```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.35/containers/json: dial unix /var/run/docker.sock: connect: permission denied
```
## 解决方法
[免sudo使用docker命令](https://www.jianshu.com/p/95e397570896)
