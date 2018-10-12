

# 2 使用git的三种境界之二——一个人到外地玩
## 2.1 git clone 
```
git clone <repository> [<directory>]
```
使用 git clone 拷贝一个 Git 仓库到本地，让自己能够查看该项目，或者进行修改。
```
git clone git@github.com:schacon/simplegit.git
```
默认情况下，Git 会按照你提供的 URL 所指示的项目的名称创建你的本地项目目录。 通常就是该 URL 最后一个 / 之后的项目名称。如果你想要一个不一样的名字， 你可以在该命令后加上你想要的名称。
```
git clone git@github.com:schacon/simplegit.git my_simplegit
```

## 2.2 git remote
```
git remote
```
查看有哪些远程仓库

```
git remote -v
```
执行时加上 -v 参数，你还可以看到每个别名的实际链接地址。

增加远程仓库
```
git remote add [alias] [repo]
```

删除远程仓库
```
git remote rm [alias]
```

## 2.3 git fetch
从远程仓库下载新分支与数据


## 2.4 git push
推送到远程仓库
```
git push [alias] [branch]
```

## 2.5 删除远程分支和tag
```
git push origin --delete <branchName>
git push origin --delete tag <tagName>
```
或者：
```
git push origin :dev
```

## 2.6 修改远程的URL
```
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git
```