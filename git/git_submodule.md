


## 1 在一个已存在的git仓库添加子模块。
```
git submodule add url地址 [其他路径或者名称]
```
执行此命令后会增加一个.gitmoduls文件和子项目文件夹。

## 2 克隆含有子模块的项目
克隆项目：
```
git clone pro_url
```
默认包含子模块目录，但是没有任何文件。
初始化本地配置文件：
```
git submodule init
```

从该项目中抓取所有数据并检出父项目中列出的合适的提交：
更新项目内子模块到最新版本
```
git submodule update
```

# 3 删除子模块
有时子模块的项目维护地址发生了变化，或者需要替换子模块，就需要删除原有的子模块。

删除子模块较复杂，步骤如下：
```bash
rm -rf 子模块目录 删除子模块目录及源码
vi .gitmodules 删除项目目录下.gitmodules文件中子模块相关条目
vi .git/config 删除配置项中子模块相关条目
rm .git/module/* 删除模块下的子模块目录，每个子模块对应一个目录，注意只删除对应的子模块目录即可
```

# 问题：
```bash
zhangxin@zhangxin-ThinkPad-L480:/media/zhangxin/Data/github/slambook2$ git submodule init
error: chmod on /media/zhangxin/Data/github/slambook2/.git/config.lock failed: Operation not permitted
Failed to register url for submodule path '3rdparty/DBoW3'
```

解决方法：
挂载磁盘权限问题


# 参考
[git中submodule子模块的添加、使用和删除](https://blog.csdn.net/guotianqing/article/details/82391665)

