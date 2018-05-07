### 1 在本机安装git
### 2 注册一个github账户
### 3 生成ssh-key，并添加到github账户
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

### 4 运行前的配置
```
git config --global user.name "your_name"
git config --global user.email "your_email@example.com"
git config --global core.editor vim
# git status时中文文件夹或者文件名不正常显示时
git config --global core.quotepath false
```