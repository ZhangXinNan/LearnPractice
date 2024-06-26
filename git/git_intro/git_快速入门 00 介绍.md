# 0 前言
## git的历史
Linus在1991年创建了开源的Linux，从此，Linux系统不断发展，已经成为最大的服务器系统软件了。

Linus虽然创建了Linux，但Linux的壮大是靠全世界热心的志愿者参与的，这么多人在世界各地为Linux编写代码，那Linux的代码是如何管理的呢？

事实是，在2002年以前，世界各地的志愿者把源代码文件通过diff的方式发给Linus，然后由Linus本人通过手工方式合并代码！

你也许会想，为什么Linus不把Linux代码放到版本控制系统里呢？不是有CVS、SVN这些免费的版本控制系统吗？因为Linus坚定地反对CVS和SVN，这些集中式的版本控制系统不但速度慢，而且必须联网才能使用。有一些商用的版本控制系统，虽然比CVS、SVN好用，但那是付费的，和Linux的开源精神不符。

不过，到了2002年，Linux系统已经发展了十年了，代码库之大让Linus很难继续通过手工方式管理了，社区的弟兄们也对这种方式表达了强烈不满，于是Linus选择了一个商业的版本控制系统BitKeeper，BitKeeper的东家BitMover公司出于人道主义精神，授权Linux社区免费使用这个版本控制系统。

安定团结的大好局面在2005年就被打破了，原因是Linux社区牛人聚集，不免沾染了一些梁山好汉的江湖习气。开发Samba的Andrew试图破解BitKeeper的协议（这么干的其实也不只他一个），被BitMover公司发现了（监控工作做得不错！），于是BitMover公司怒了，要收回Linux社区的免费使用权。

Linus可以向BitMover公司道个歉，保证以后严格管教弟兄们，嗯，这是不可能的。实际情况是这样的：

Linus花了两周时间自己用C写了一个分布式版本控制系统，这就是Git！一个月之内，Linux系统的源码已经由Git管理了！牛是怎么定义的呢？大家可以体会一下。

## 注意
* git使用方法非常灵活，每个操作可能都有很多写法，我这里不会讨论一个“回”字有几种写法，只提及一种，目的是尽快上手入门。

## Git比其他版本控制系统分支性能更好的原因。
1. 其他版本控制系统（如：SVN）的分支是通过文件复制创建的，如果文件过多，创建分支时间就慢，并且占用大量的磁盘空间。
2. Git 的分支是通过当前文件的一个快照指针创建的，无论文件多还是少，创建分支时间快，不占用大量的磁盘空间。


# 1 git基础知识
## 1.1 版本管理
版本管理就是管理更新的历史记录。它为我们提供了一些在软件开发过程中必不可少的功能，例如记录一款软件添加或者更改源代码的过程，回滚到特定阶段，恢复误删的文件等。

## 1.2 基本概念
* 工作区：就是你在电脑里能看到的目录。
* 暂存区：英文叫stage, 或index。一般存放在 ".git目录下" 下的index文件（.git/index）中，所以我们把暂存区有时也叫作索引（index）。
* 版本库：工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库。

![](work_index_ver.jpg)

## 1.3 原理
Git 利用底层数据结构，通过指向索引对象的可变指针，保存文件快照。Git 是对象数据库，把Git仓库里面被跟踪的文件（源码，图片，声音等文件）转化成一个对象数据，并用 SHA-1 哈希值计算引用显示文件，当提交更新的时候，就会生成当前所有文件的快照与增删改操作记录，保存到Git仓库里面.git目录中。

## 1.4 git核心文件
### .git文件夹
操作系统默认隐藏此目录，目的是以防止意外删除或修改，如果.git目录被删除，就会导致Git仓库版本记录丢失。
### .gitignore文件
指定忽略git跟踪文件。


# 参考资料
* [git - 简明指南](http://www.runoob.com/manual/git-guide/)
* [Git 教程](http://www.runoob.com/git/git-tutorial.html)
* [寥雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/)
* [git版本控制管理](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B00U42VM7Y/ref=sr_1_1?ie=UTF8&qid=1501466981&sr=8-1&keywords=git)
* [Git工具水很深，你根本把握不住（一）](https://zhuanlan.zhihu.com/p/376488061)