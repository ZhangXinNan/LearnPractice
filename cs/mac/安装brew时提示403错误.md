
homebrew是mac下最常用的软件包管理工具，我们经常要用brew命令来安装各种命令行工具。
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
安装brew时出现403错误，如下：
```
curl: (7) Failed to connect to raw.githubusercontent.com port 443 after 19 ms: Couldn't connect to server
```

解决办法，使用国内的进行替换：
```bash
/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)"
```
安装时根据提示进行操作即可，别忘了在安装后重启终端（建议）或者`source ${HOME}/.zprofile`。
