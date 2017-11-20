1. 用root帐号登录或者su到root。

2. 增加sudoers文件的写权限： 
```chmod u+w /etc/sudoers```

3. ```vim /etc/sudoers``` 找到 ```root ALL=(ALL) ALL``` 在这行下边添加 ```username ALL=(ALL) ALL```  (username代表是你要添加sudo权限的用户名)

4. 除去sudoers文件的写权限： chmod u-w /etc/sudoers