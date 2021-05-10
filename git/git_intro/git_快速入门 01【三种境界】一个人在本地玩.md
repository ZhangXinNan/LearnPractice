
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

# 2 Git 工作区、暂存区和版本库概念
* 工作区：就是你在电脑里能看到的目录。
* 暂存区：英文叫 stage 或 index。一般存放在 .git 目录下的 index 文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）。
* 版本库：工作区有一个隐藏目录 .git，这个不算工作区，而是 Git 的版本库。

![](工作区暂存区.jpeg)
* 图中左侧为工作区，右侧为版本库。在版本库中标记为 "index" 的区域是暂存区（stage/index），标记为 "master" 的是 master 分支所代表的目录树。

* 图中我们可以看出此时 "HEAD" 实际是指向 master 分支的一个"游标"。所以图示的命令中出现 HEAD 的地方可以用 master 来替换。

* 图中的 objects 标识的区域为 Git 的对象库，实际位于 ".git/objects" 目录下，里面包含了创建的各种对象及内容。

* 当对工作区修改（或新增）的文件执行 git add 命令时，暂存区的目录树被更新，同时工作区修改（或新增）的文件内容被写入到对象库中的一个新的对象中，而该对象的ID被记录在暂存区的文件索引中。

* 当执行提交操作（git commit）时，暂存区的目录树写到版本库（对象库）中，master 分支会做相应的更新。即 master 指向的目录树就是提交时暂存区的目录树。

* 当执行 git reset HEAD 命令时，暂存区的目录树会被重写，被 master 分支指向的目录树所替换，但是工作区不受影响。

* 当执行 git rm --cached <file> 命令时，会直接从暂存区删除文件，工作区则不做出改变。

* 当执行 git checkout . 或者 git checkout -- <file> 命令时，会用暂存区全部或指定的文件替换工作区的文件。这个操作很危险，会清除工作区中未添加到暂存区的改动。

* 当执行 git checkout HEAD . 或者 git checkout HEAD <file> 命令时，会用 HEAD 指向的 master 分支中的全部或者部分文件替换暂存区和以及工作区中的文件。这个命令也是极具危险性的，因为不但会清除工作区中未提交的改动，也会清除暂存区中未提交的改动。



# 参考资料
* [Git 工作区、暂存区和版本库](https://www.runoob.com/git/git-workspace-index-repo.html)