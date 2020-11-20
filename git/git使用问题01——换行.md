
# 1 问题
```bash
fatal: LF would be replaced by CRLF in README.md
```



# 2 解决方法


The git config core.autocrlf command is used to change how Git handles line endings. It takes a single argument.

On Linux, you simply pass input to the configuration. For example:
```bash
git config --global core.autocrlf input
# Configure Git on Linux to properly handle line endings

git config --global core.autocrlf true
```


# 参考
[Dealing with line endings](https://help.github.com/en/articles/dealing-with-line-endings)

[Git diff ^M的消除](https://blog.csdn.net/csfreebird/article/details/10448493)

[git fatal: CRLF would be replaced by LF](https://blog.csdn.net/yhc166188/article/details/80340189)
[关于git提示"warning: LF will be replaced by CRLF"终极解答](https://www.jianshu.com/p/450cd21b36a4)