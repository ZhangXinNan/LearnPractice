# 1 同一个邮箱

由于邮箱是识别的唯一手段，那么自然的，这两者采用同一个邮箱，生成的 public key 也会是同一个，上传到 Github 或者 Gitlab 上面，在 Git 的配置中 ，设置好 Global 的配置 ：
```
git config --global user.name 'ZhangXinNan'
git config --global user.email 'zhangxin19870504@163.com' 
git config --global core.editor vim
```
进行日常的开发是没有问题的。
一个邮箱使用github参考[github使用入门](http://blog.csdn.net/sdlypyzq/article/details/75051033)，写得比简单，如果有细节 不明白可以留言，我会补充或者 回答 。
实际生活中采用同一个邮箱的可能性并不是太大，这就引出了方案二.

 

# 2 不同邮箱

## 2.1 生成ssh-key

 
### 生成默认，Github使用
```
ssh-keygen -t rsa -b 4096 -C "zhangxin19870504@163.com"
```
此命令创建了~/.ssh文件夹，同时生成了
```
id_rsa     
id_rsa.pub
```

### 生成公钥、密钥的同时指定文件名，Gitlab使用
```
ssh-keygen -t rsa -f ~/.ssh/id_rsa.gitlab -C "zhangxin0627@autohome.com.cn"
ssh-keygen -t rsa -f ~/.ssh/id_rsa -C "zhangxin19870504@163.com"
```
上传public key 到github或者gitlab
 
以Github为例，过程如下：
```
登录github
点击右上方的Accounting settings图标
选择 SSH key
点击 Add SSH key
 
在出现的界面中填写SSH key的名称，填一个你自己喜欢的名称即可，然后将上面拷贝的~/.ssh/id_rsa.pub文件内容粘帖到key一栏，在点击“add key”按钮就可以了。
添加过程github会提示你输入一次你的github密码 ，确认后即添加完毕。 上传Gitlab的过程一样，请自己操作。
```
 
## 2.2 配置config文件
 
在 ~/.ssh目录下，如果不存在，则新建 touch ~/.ssh/config文件 ，文件内容添加如下：
```
# Default github user(first@mail.com),注意User项直接填git，不用填在github的用户名
Host github.com
 HostName github.com
 User git
 IdentityFile ~/.ssh/id_rsa

# second user(second@mail.com)
# 建一个gitlab别名，新建的帐号使用这个别名做克隆和更新
Host git.corpautohome.com
 HostName git.corpautohome.com
 User zhangxin0627
 IdentityFile ~/.ssh/id_rsa.gitlab
```

配置完成后，符合 *.corp.xxx.com后缀的 Git 仓库，均采取~/.ssh/id_rsa.gitlab 密钥进行验证，其它的采取默认的。

 
## 2.3 难证是否OK
 
由于每个托管商的仓库都有唯一的后缀，比如 Github的是 git@github.com:*，所以可以这样测试：
```
➜  ~ ssh -T git@github.com
The authenticity of host 'github.com (192.30.255.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'github.com,192.30.255.112' (RSA) to the list of known hosts.
Hi ZhangXinNan! You've successfully authenticated, but GitHub does not provide shell access.

➜  ~ ssh -T git@git.corpautohome.com
The authenticity of host 'git.corpautohome.com (10.168.100.80)' can't be established.
RSA key fingerprint is SHA256:SufpdWzsO0cdXqgj0/h141fs+7RjQamTq8so25Y60WI.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'git.corpautohome.com,10.168.100.80' (RSA) to the list of known hosts.
Welcome to GitLab, zhangxin0627!
```

看到这些 Welcome 信息，说明就是 OK的了。
配置
## 2.4 全局配置，Github仓库中默认使用此配置
```
git config --global user.name 'ZhangXinNan'
git config --global user.email 'zhangxin19870504@163.com'
```
## 2.5 团队项目配置，每次新创建一个项目，需要执行下
```
git config --local user.name 'ZhangXinNan'
git config --local user.email 'zhangxin0627@autohome.com.cn'
```


# 3 参考资料：
[一台机器上Github/Gitlab多账户管理SSH Key切换解决push冲突](http://www.ixirong.com/2015/07/29/how-to-use-github-gitlab-together/)
