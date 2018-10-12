

# 1 修改远程仓库地址
方法有三种：
## 1.1 修改命令
```
git remote set-url origin [url]
```
## 1.2 先删后加
```
git remote rm origin
git remote add origin [url]
```
## 1.3 直接修改config文件

# 2 删除分支
## 2.0 查看分支
```
# 查看所有分支，包括本地分支和远程分支
git branch -a

# 查看远程分支
git branch -r
```

## 2.1 删除本地分支
```
git branch -d dev_a
```

## 2.2 删除远程分支
```
git branch -r -d origin/branch-name
git push origin :branch-name
```

# 3 参考资料：
[git修改远程仓库地址](https://ddnode.com/2015/04/14/git-modify-remote-responsity-url.html)
[git命令行删除远程分支](https://blog.csdn.net/furzoom/article/details/53002699)