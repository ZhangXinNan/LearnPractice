# Linux添加/删除用户和用户组
本文总结了Linux添加或者删除用户和用户组时常用的一些命令和参数。
1、建用户：
```bash
adduser phpq                             //新建phpq用户
passwd phpq                               //给phpq用户设置密码
# 为用户添加sudo权限
sudo usermod -a -G sudo phpq
```
2、建工作组
```
groupadd test                          //新建test工作组
```
3、新建用户同时增加工作组
```
useradd -g test phpq                      //新建phpq用户并增加到test工作组
```
注：：-g 所属组 -d 家目录 -s 所用的SHELL


4、给已有的用户增加工作组
```
usermod -G groupname username  （这个会把用户从其他组中去掉）

usermod -a groupname username

或者：gpasswd -a user group
```
如果添加了用户，添加了组，然后使这个组里的人都可以sudo 到公共账号下

可以/etc/sudoers.d 下面建立一个文件内容如下 ，就可以是etl组的所有用户都可以无密码的切到etl用户下。
```
%etl ALL=(ALL) NOPASSWD: /bin/su etl
%etl ALL=(ALL) NOPASSWD: /bin/su - etl
```
sudo 具体参考 http://www.cnblogs.com/xd502djj/p/6641475.html

5、临时关闭：在/etc/shadow文件中属于该用户的行的第二个字段（密码）前面加上*就可以了。想恢复该用户，去掉*即可。

或者使用如下命令关闭用户账号：
```
passwd peter –l
```
重新释放：
```
passwd peter –u
```
6、永久性删除用户账号
```
userdel peter

groupdel peter

usermod –G peter peter   （强制删除该用户的主目录和主目录下的所有文件和子目录）
```
7、从组中删除用户
编辑/etc/group 找到GROUP1那一行，删除 A
或者用命令
```
gpasswd -d A GROUP
```
8、显示用户信息
```
id user
cat /etc/passwd
```
更详细的用户和用户组的解说请参考
Linux 用户和用户组详细解说
本文主要讲述在Linux 系统中用户(user)和用户组(group)管理相应的概念；用户(user)和用户组(group)相关命令的列举；其中也对单用户多任务，多用户多任务也做以解说。

本篇文章来源于 PHP资讯 原文链接：http://www.phpq.net/linux/linux-add-delete-user-group.html

 

Linux 用户（user）和用户组（group）管理概述

 

、理解Linux的单用户多任务，多用户多任务概念；

Linux 是一个多用户、多任务的操作系统；我们应该了解单用户多任务和多用户多任务的概念；


1、Linux 的单用户多任务；

单用户多任务；比如我们以beinan 登录系统，进入系统后，我要打开gedit 来写文档，但在写文档的过程中，我感觉少点音乐，所以又打开xmms 来点音乐；当然听点音乐还不行，MSN 还得打开，想知道几个弟兄现在正在做什么，这样一样，我在用beinan 用户登录时，执行了gedit 、xmms以及msn等，当然还有输入法fcitx ；这样说来就有点简单了，一个beinan用户，为了完成工作，执行了几个任务；当然beinan这个用户，其它的人还能以远程登录过来，也能做其它的工作。


2、Linux 的多用户、多任务；

有时可能是很多用户同时用同一个系统，但并不所有的用户都一定都要做同一件事，所以这就有多用户多任务之说；

举个例子，比如LinuxSir.Org 服务器，上面有FTP 用户、系统管理员、web 用户、常规普通用户等，在同一时刻，可能有的弟兄正在访问论坛；有的可能在上传软件包管理子站，比如luma 或Yuking 兄在管理他们的主页系统和FTP ；在与此同时，可能还会有系统管理员在维护系统；浏览主页的用的是nobody 用户，大家都用同一个，而上传软件包用的是FTP用户；管理员的对系统的维护或查看，可能用的是普通帐号或超级权限root帐号；不同用户所具有的权限也不同，要完成不同的任务得需要不同的用户，也可以说不同的用户，可能完成的工作也不一样；

值得注意的是：多用户多任务并不是大家同时挤到一接在一台机器的的键盘和显示器前来操作机器，多用户可能通过远程登录来进行，比如对服务器的远程控制，只要有用户权限任何人都是可以上去操作或访问的；


3、用户的角色区分；

用户在系统中是分角色的，在Linux 系统中，由于角色不同，权限和所完成的任务也不同；值得注意的是用户的角色是通过UID和识别的，特别是UID；在系统管理中，系统管理员一定要坚守UID 唯一的特性；

root 用户：系统唯一，是真实的，可以登录系统，可以操作系统任何文件和命令，拥有最高权限；
虚拟用户：这类用户也被称之为伪用户或假用户，与真实用户区分开来，这类用户不具有登录系统的能力，但却是系统运行不可缺少的用户，比如bin、daemon、adm、ftp、mail等；这类用户都系统自身拥有的，而非后来添加的，当然我们也可以添加虚拟用户；
普通真实用户：这类用户能登录系统，但只能操作自己家目录的内容；权限有限；这类用户都是系统管理员自行添加的；


4、多用户操作系统的安全；

多用户系统从事实来说对系统管理更为方便。从安全角度来说，多用户管理的系统更为安全，比如beinan用户下的某个文件不想让其它用户看到，只是设置一下文件的权限，只有beinan一个用户可读可写可编辑就行了，这样一来只有beinan一个用户可以对其私有文件进行操作，Linux 在多用户下表现最佳，Linux能很好的保护每个用户的安全，但我们也得学会Linux 才是，再安全的系统，如果没有安全意识的管理员或管理技术，这样的系统也不是安全的。

从服务器角度来说，多用户的下的系统安全性也是最为重要的，我们常用的Windows 操作系统，它在系纺权限管理的能力只能说是一般般，根本没有没有办法和Linux或Unix 类系统相比；


二、用户(user）和用户组（group）概念；


1、用户（user）的概念；

通过前面对Linux 多用户的理解，我们明白Linux 是真正意义上的多用户操作系统，所以我们能在Linux系统中建若干用户（user）。比如我们的同事想用我的计算机，但我不想让他用我的用户名登录，因为我的用户名下有不想让别人看到的资料和信息（也就是隐私内容）这时我就可以给他建一个新的用户名，让他用我所开的用户名去折腾，这从计算机安全角度来说是符合操作规则的；

当然用户（user）的概念理解还不仅仅于此，在Linux系统中还有一些用户是用来完成特定任务的，比如nobody和ftp 等，我们访问LinuxSir.Org 的网页程序，就是nobody用户；我们匿名访问ftp 时，会用到用户ftp或nobody ；如果您想了解Linux系统的一些帐号，请查看 /etc/passwd ；


2、用户组（group）的概念；

用户组（group）就是具有相同特征的用户（user）的集合体；比如有时我们要让多个用户具有相同的权限，比如查看、修改某一文件或执行某个命令，这时我们需要用户组，我们把用户都定义到同一用户组，我们通过修改文件或目录的权限，让用户组具有一定的操作权限，这样用户组下的用户对该文件或目录都具有相同的权限，这是我们通过定义组和修改文件的权限来实现的；

举例：我们为了让一些用户有权限查看某一文档，比如是一个时间表，而编写时间表的人要具有读写执行的权限，我们想让一些用户知道这个时间表的内容，而不让他们修改，所以我们可以把这些用户都划到一个组，然后来修改这个文件的权限，让用户组可读，这样用户组下面的每个用户都是可读的；

用户和用户组的对应关系是：一对一、多对一、一对多或多对多；

一对一：某个用户可以是某个组的唯一成员；
多对一：多个用户可以是某个唯一的组的成员，不归属其它用户组；比如beinan和linuxsir两个用户只归属于beinan用户组；
一对多：某个用户可以是多个用户组的成员；比如beinan可以是root组成员，也可以是linuxsir用户组成员，还可以是adm用户组成员；
多对多：多个用户对应多个用户组，并且几个用户可以是归属相同的组；其实多对多的关系是前面三条的扩展；理解了上面的三条，这条也能理解；


三、用户（user）和用户组（group）相关的配置文件、命令或目录；


1、与用户（user）和用户组（group）相关的配置文件；


1）与用户（user）相关的配置文件；

/etc/passwd 注：用户（user）的配置文件；
/etc/shadow 注：用户（user）影子口令文件；


2）与用户组（group）相关的配置文件；

/etc/group 注：用户组（group）配置文件；
/etc/gshadow 注：用户组（group）的影子文件；


2、管理用户（user）和用户组（group）的相关工具或命令；


1）管理用户（user）的工具或命令；

useradd    注：添加用户 
adduser    注：添加用户
passwd     注：为用户设置密码
usermod  注：修改用户命令，可以通过usermod 来修改登录名、用户的家目录等等；
pwcov       注：同步用户从/etc/passwd 到/etc/shadow 
pwck         注：pwck是校验用户配置文件/etc/passwd 和/etc/shadow 文件内容是否合法或完整；
pwunconv  注：是pwcov 的立逆向操作，是从/etc/shadow和 /etc/passwd 创建/etc/passwd ，然后会删除 /etc/shadow 文件；
finger        注：查看用户信息工具
id              注：查看用户的UID、GID及所归属的用户组
chfn          注：更改用户信息工具
su             注：用户切换工具
sudo         注：sudo 是通过另一个用户来执行命令（execute a command as another user），su 是用来切换用户，然后通过切换到的用户来完成相应的任务，但sudo 能后面直接执行命令，比如sudo 不需要root 密码就可以执行root 赋与的执行只有root才能执行相应的命令；但得通过visudo 来编辑/etc/sudoers来实现；
visudo      注：visodo 是编辑 /etc/sudoers 的命令；也可以不用这个命令，直接用vi 来编辑 /etc/sudoers 的效果是一样的；
sudoedit  注：和sudo 功能差不多；


2）管理用户组（group）的工具或命令；

groupadd  注：添加用户组；
groupdel         注：删除用户组；
groupmod        注：修改用户组信息
groups     注：显示用户所属的用户组
grpck
grpconv   注：通过/etc/group和/etc/gshadow 的文件内容来同步或创建/etc/gshadow ，如果/etc/gshadow 不存在则创建；
grpunconv   注：通过/etc/group 和/etc/gshadow 文件内容来同步或创建/etc/group ，然后删除gshadow文件；
 


3、/etc/skel 目录；

/etc/skel目录一般是存放用户启动文件的目录，这个目录是由root权限控制，当我们添加用户时，这个目录下的文件自动复制到新添加的用户的家目录下；/etc/skel 目录下的文件都是隐藏文件，也就是类似.file格式的；我们可通过修改、添加、删除/etc/skel目录下的文件，来为用户提供一个统一、标准的、默认的用户环境；
```
[root@localhost beinan]# ls -la /etc/skel/
总用量 92
drwxr-xr-x    3 root root  4096  8月 11 23:32 .
drwxr-xr-x  115 root root 12288 10月 14 13:44 ..
-rw-r--r--    1 root root    24  5月 11 00:15 .bash_logout
-rw-r--r--    1 root root   191  5月 11 00:15 .bash_profile
-rw-r--r--    1 root root   124  5月 11 00:15 .bashrc
-rw-r--r--    1 root root  5619 2005-03-08  .canna
-rw-r--r--    1 root root   438  5月 18 15:23 .emacs
-rw-r--r--    1 root root   120  5月 23 05:18 .gtkrc
drwxr-xr-x    3 root root  4096  8月 11 23:16 .kde
-rw-r--r--    1 root root   658 2005-01-17  .zshrc
``` 

/etc/skel 目录下的文件，一般是我们用useradd 和adduser 命令添加用户（user）时，系统自动复制到新添加用户（user）的家目录下；如果我们通过修改 /etc/passwd 来添加用户时，我们可以自己创建用户的家目录，然后把/etc/skel 下的文件复制到用户的家目录下，然后要用chown 来改变新用户家目录的属主；

4、/etc/login.defs 配置文件；

/etc/login.defs 文件是当创建用户时的一些规划，比如创建用户时，是否需要家目录，UID和GID的范围；用户的期限等等，这个文件是可以通过root来定义的；

比如Fedora 的 /etc/logins.defs 文件内容；
```
# *REQUIRED*
#   Directory where mailboxes reside, _or_ name of file, relative to the
#   home directory.  If you _do_ define both, MAIL_DIR takes precedence.
#   QMAIL_DIR is for Qmail
#
#QMAIL_DIR      Maildir
MAIL_DIR        /var/spool/mail  注：创建用户时，要在目录/var/spool/mail中创建一个用户mail文件；
#MAIL_FILE      .mail

# Password aging controls:
#
#       PASS_MAX_DAYS   Maximum number of days a password may be used.
#       PASS_MIN_DAYS   Minimum number of days allowed between password changes.
#       PASS_MIN_LEN    Minimum acceptable password length.
#       PASS_WARN_AGE   Number of days warning given before a password expires.
#
PASS_MAX_DAYS   99999   注：用户的密码不过期最多的天数；
PASS_MIN_DAYS   0       注：密码修改之间最小的天数；
PASS_MIN_LEN    5       注：密码最小长度；
PASS_WARN_AGE   7       注：

#
# Min/max values for automatic uid selection in useradd
#
UID_MIN                   500  注：最小UID为500 ，也就是说添加用户时，UID 是从500开始的；
UID_MAX                 60000   注：最大UID为60000；

#
# Min/max values for automatic gid selection in groupadd
#
GID_MIN                   500   注：GID 是从500开始；
GID_MAX                 60000

#
# If defined, this command is run when removing a user.
# It should remove any at/cron/print jobs etc. owned by
# the user to be removed (passed as the first argument).
#
#USERDEL_CMD    /usr/sbin/userdel_local

#
# If useradd should create home directories for users by default
# On RH systems, we do. This option is ORed with the -m flag on
# useradd command line.
#
CREATE_HOME     yes   注：是否创用户家目录，要求创建；
 
```

5、/etc/default/useradd 文件；

通过useradd 添加用户时的规则文件；
```
# useradd defaults file
GROUP=100
HOME=/home  注：把用户的家目录建在/home中；
INACTIVE=-1  注：是否启用帐号过期停权，-1表示不启用；
EXPIRE=   注：帐号终止日期，不设置表示不启用；
SHELL=/bin/bash  注：所用SHELL的类型；
SKEL=/etc/skel   注： 默认添加用户的目录默认文件存放位置；也就是说，当我们用adduser添加用户时，用户家目录下的文件，都是从这个目录中复制过去的；
```


后记：

关于用户（user）和用户组（group）管理内容大约就是这么多；只要把上面所说的内容了解和掌握，用户（user）和用户组（group）管理就差不多了；由于用户（user）和用户组（group）是和文件及目录权限联系在一起的，所以文件及目录权限的操作也会独立成文来给大家介绍；
