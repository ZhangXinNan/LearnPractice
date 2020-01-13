


# 1 问题
在MAC使用readlink命令时，会提示
```bash
++++ readlink -f ./bin/startup.sh
readlink: illegal option -- f
usage: readlink [-n] [file ...]
+++ dirname
usage: dirname path
++ readlink -f /..
readlink: illegal option -- f
usage: readlink [-n] [file ...]
+ __base__=
```

# 2 解决
安装greadlink 进行替代readlink

```bash
brew install coreutils

greadlink -f file.txt
```

# 3 参考
1. [How can I get the behavior of GNU's readlink -f on a Mac?](https://stackoverflow.com/questions/1055671/how-can-i-get-the-behavior-of-gnus-readlink-f-on-a-mac)

