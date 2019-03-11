
# 1 使用git的三种境界之一——一个人在本地玩
一个人在本地玩：一个人在自己的一个电脑上，不需要网络连接，使用git来做代码的管理。
## 1.1 git init
git init 创建一个新的仓库或者重新初始化一个现有的。
git init 命令创建了一个.git的目录，里边有所有版本信息。
```bash
mkdir ~/public_html
cd ~/public_html
echo 'My website is alive!' > index.html

git init
```


## 1.2 git add
git add 命令可将该文件添加到缓存
```bash
git add index.html
```
git add . 让git把当前目录及子目录中的文件都添加到版本库里。
git add 只是暂存（staged）了这个文件。

## 1.3 git status
git status 查看当前中间状态，查看上次提交之后是否有修改。
```
git status
```

## 1.4 git commit
使用 git add 命令将想要快照的内容写入缓存区， 而执行 git commit 将缓存区内容添加到仓库中。

## 1.5 git rm
git rm file 会将文件从缓存区和你的硬盘中（工作目录）删除。
如果你要在工作目录中留着该文件，可以使用 git rm --cached

## 1.6 git mv
git mv 命令用于移动或重命名一个文件、目录、软连接。

## 1.7 git diff
git diff 命令显示已写入缓存与已修改但尚未写入缓存的改动的区别。
* 尚未缓存的改动：git diff
* 查看已缓存的改动： git diff --cached
* 查看已缓存的与未缓存的所有改动：git diff HEAD
* 显示摘要而非整个 diff：git diff --stat

## 1.8 git branch
git branch 用来列出、创建、删除分支
```
git branch -a
git branch dev
git branch -d dev
```

## 1.9 git checkout
git checkout 切换分支或者更恢复工作树。
当你切换分支的时候，Git 会用该分支的最后提交的快照替换你的工作目录的内容， 所以多个分支不需要多个目录。
```
git checkout dev
```
创建并切的到新分支
```
git checkout -b dev
```

## 1.10 git log
查看提交日志

## 1.11 git merge
合并分支

## 1.12 git reset 
回溯历史版本

## 1.13 git rebase -i
压缩历史
