### 1 在本机安装git
### 2 注册一个github账户
### 3 生成ssh-key，并添加到github账户
[Generating a new SSH key and adding it to the ssh-agent](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/)
#### 3.1 Generating a new SSH key
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

#### 3.2 adding your ssh to the ssg-agent


1. Start the ssh-agent in the background.
```
eval "$(ssh-agent -s)"
```
2. If you're using macOS Sierra 10.12.2 or later, you will need to modify your ~/.ssh/config file to automatically load keys into the ssh-agent and store passphrases in your keychain.
```
Host *
 AddKeysToAgent yes
 UseKeychain yes
 IdentityFile ~/.ssh/id_rsa
```
3. Add your SSH private key to the ssh-agent and store your passphrase in the keychain. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_rsa in the command with the name of your private key file.
```
ssh-add -K ~/.ssh/id_rsa
```

#### 3.3 复制

```
# win
clip < ~/.ssh/id_rsa.pub

# mac
pbcopy < ~/.ssh/id_rsa.pub
```

### 4 运行前的配置
```
git config --global user.name "your_name"
git config --global user.email "your_email@example.com"
git config --global core.editor vim
# git status时中文文件夹或者文件名不正常显示时
git config --global core.quotepath false
```