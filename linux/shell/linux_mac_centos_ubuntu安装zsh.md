
# 0 安装zsh 和 oh-my-zsh
```bash
# 查看当前shell
echo $SHELL


# 安装zsh
## centos
sudo yum install zsh
## ubuntu
sudo apt install zsh

# 查看zsh
which zsh

# 更换sh
# chsh -s /usr/bin/zsh
chsh -s /bin/zsh

# clone from github
git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh
# 复制默认.zshrc
cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc

```



# 1 语法高亮插件
1. 安装
```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```
2. 配置
在~/.zshrc的plugins中加入zsh-syntax-highlighting

# 2 自动补全插件
1. 安装
```bash
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```
2. 配置
在~/.zshrc的plugins中加入zsh-autosuggestions



# 参考资料
[CentOS安装oh-my-zsh并配置语法高亮和命令自动补全](https://www.cnblogs.com/zhloong/archive/2020/06/21/installohmyzsh.html)



