
# 1 问题
```
Got permission denied while trying to connect to the Docker daemon socket
```

# 2 解决方法

Create the docker group.
创建docker组。
```bash
sudo groupadd docker
```

添加用户到docker组里。
Add your user to the docker group.
```bash
sudo usermod -aG docker ${USER}
```

先退出再登录
You would need to loog out and log back in so that your group membership is re-evaluated or type the following command:
```
su -s ${USER}
```

测试
Verify that you can run docker commands without sudo.
```
docker run hello-world
```