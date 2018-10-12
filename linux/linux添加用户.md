1.添加用户

sudo adduser username 

2.添加sudo权限

sudo usermod -G sudo username 

3.添加root权限

如果需要让此用户有root权限，执行命令：

 sudo vim /etc/sudoers


修改文件如下：
# User privilege specification
root ALL=(ALL) ALL
username ALL=(ALL) ALL
保存退出，username 用户就拥有了root权限。

[Ubuntu添加用户并赋sudo权限](https://blog.csdn.net/breeze5428/article/details/52837768)


1.修改用户密码 
修改root密码（默认root无密码，第一次执行时创建密码）： 
sudo passwd root 
修改开机登录密码（用户名为username）： 
sudo passwd username

2.创建用户 
创建用户，同时创建该用户主目录，创建用户同名的组（用户名为username）。 
sudo adduser username 
会提示设置密码，其他提示一路回车即可。

如果需要让此用户有root权限，执行命令： 
root@ubuntu:~# sudo vim /etc/sudoers 
修改文件如下：

# User privilege specification
root ALL=(ALL) ALL
username ALL=(ALL) ALL
1
2
3
保存退出，username用户就拥有了root权限。

3.切换用户 
切换用户的命令 
su username 
从普通用户切换到root用户，还可以使用命令 
sudo su

在终端输入exit或logout或使用快捷方式ctrl+d，可以退回到原来用户 
在切换用户时，如果想在切换用户之后使用新用户的工作环境，可以在su和username之间加-，例如 
su - root 
提示符$表示普通用户，#表示超级用户，即root用户。

[Ubuntu用户管理（创建用户、切换用户、修改密码等）](https://blog.csdn.net/ezhchai/article/details/79273741)