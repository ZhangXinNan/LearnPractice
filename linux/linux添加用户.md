1.添加用户
(username代表是你要添加sudo权限的用户名)
```bash
新建username用户
sudo adduser username
# 给username设置密码
passwd username
```

2.添加sudo权限
```bash
sudo usermod -G sudo username 
```

3.添加root权限

如果需要让此用户有root权限，执行命令：
```bash
sudo chmod u+w /etc/sudoers

sudo vim /etc/sudoers
```

修改文件如下：
```bash
# User privilege specification
root ALL=(ALL) ALL
username ALL=(ALL) ALL
```
保存退出，username 用户就拥有了root权限。

4. 除去sudoers文件的写权限： 
```bash
chmod u-w /etc/sudoers
```




3.切换用户 

```bash
# 切换用户的命令
su username 
# 从普通用户切换到root用户，还可以使用命令 
sudo su
# 在切换用户时，如果想在切换用户之后使用新用户的工作环境，可以在su和username之间加-
su - root
# 提示符$表示普通用户，#表示超级用户，即root用户。
```

# 参考资料
* [Ubuntu添加用户并赋sudo权限](https://blog.csdn.net/breeze5428/article/details/52837768)

* [Ubuntu用户管理（创建用户、切换用户、修改密码等）](https://blog.csdn.net/ezhchai/article/details/79273741)