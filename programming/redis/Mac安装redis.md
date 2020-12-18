

# 使用brew安装redis
```bash
brew update
brew install redis
```


# 启动redis
```bash
brew services start redis
# 后台运行
redis-server /usr/local/etc/redis.conf
```

# 终止
```bash
brew services stop redis
```

# 测试是否运行
```bash
redis-cli ping
```


# 配置文件路径
```bash
/usr/local/etc/redis.conf
```

# 卸载
```bash
brew uninstall redis
rm ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
```