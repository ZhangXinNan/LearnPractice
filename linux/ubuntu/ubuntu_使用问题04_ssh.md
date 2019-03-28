
```
# 查看是否安装ssh-server服务
dpkg -l | grep ssh
# 安装ssh-server
sudo apt-get install openssh-server
# 再次查看是否安装ssh-server服务
dpkg -l | grep ssh

# 确认ssh-server是否启动
ps -e | grep ssh

# 然后重启SSH服务： 
sudo /etc/init.d/ssh stop 
sudo /etc/init.d/ssh start

```



# 参考
[ubuntu开启SSH服务远程登录](https://blog.csdn.net/jackghq/article/details/54974141)




