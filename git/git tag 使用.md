


1. 查看tag
```bash
git tag
```

2. 在某个commit上打tag
```bash
git tag test_tag c809ddbf83939a89659e51dc2a5fe183af384233
```

3. 本地tag推送到线上
```bash
git push origin test_tag
```
4. 本地删除tag
```bash
git tag -d test_tag
```


5. 删除线上tag
本地tag删除了，再执行该句，删除线上tag
```bash
git push origin :refs/tags/test_tag
```

【注意】
> 只要在打标签时添加-m”xxxx”，都可以添加标签说明，并在git show 显示的信息中显示打标签者、打标签日期和标签说明。而git tag -a应该只是声明要打一个含附注的标签，你可以用-m添加，又或者是使用它跳转的文本编辑软件添加，总之加上-a的标签必须要有标签说明，而git tag不会强制要求。当使用git tag -m时，效果其实和git tag -a -m是一样的。




# 参考
1. [git 创建tag , 查看tag ， 删除tag](https://www.cnblogs.com/pansidong/p/7773873.html)
2. [git tag与git tag -a的不同](https://blog.csdn.net/RMaple_Qiu/article/details/78362076)