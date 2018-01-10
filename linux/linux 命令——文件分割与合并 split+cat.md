有时文件太大，而上传下载会有限制，所以分割与合并。
例如一部电影guizi.rmvb，分割为100M一个的文件，
```
split -b 100m guizi.rmvb 
# 指定前缀名，指定用数字后缀、后缀长度
split -b 100m guizi.rmvb guizi -d -a 3
```

可以看到很多xa*的文件，将其合并为guizi_.rmvb，命令为
```
cat xa* > guizi_.rmvb
```

新生成的文件电影可播放，没有问题。