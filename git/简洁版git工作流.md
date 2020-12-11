![在这里插入图片描述](https://img-blog.csdnimg.cn/20201211101817589.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NkbHlweXpx,size_16,color_FFFFFF,t_70#pic_center)

1. 现在gitlab上有一个项目，例如叫作 Project。不考虑使用fork，直接将项目拉到本地。
```bash
git clone https://gitlab.com/my-group/Project.git
```
2. 进入文件夹里，开一个新的分支，然后进行开发。
```bash
cd Project
git checkout -b dev
# 在对代码进行了一些修改后，保存
git add .
git commit -m '添加新功能'
```
3. 现在本地已经在dev分支上把新功能开发完成了，这时可以提交到远程仓库里。然后看右图，push上去后，远程仓库里也有了这个新分支了。
```bash
git push origin dev
```
4. 这时如果想将代码合并 至master，需要在gitlab/github上提一个merge request的申请，将代码合并至master。
5. 别人或者自己合并后，还需要再拉一次代码。fetch 后，更新会保存至本地版本库，但是当前的代码还是旧的哦。
```bash
git fetch origin
```
6. 切换至master分支，把远程仓库里的master合并至当前master。这样，现在本地的master分支就和远程的master代码是一样的了。
```bash
git checkout master
git merge origin/master
```

7. dev的使命已经完成，为以后不混淆，就可以把dev分支删掉了。每个分支的名字最好有特定的意义。
```bash
# 删除本地dev
git branch -d dev
# 删除远程dev
git push origin :dev
```
