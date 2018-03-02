原文地址: [初学python者自学anaconda的正确姿势是什么？](https://www.zhihu.com/question/58033789)

# 1 Anaconda 是什么
你可能已经安装了 Python，那么为什么还需要 Anaconda？有以下3个原因：1）Anaconda 附带了一大批常用数据科学包，它附带了 conda、Python 和 150 多个科学包及其依赖项。因此你可以立即开始处理数据。2）管理包Anaconda 是在 conda（一个包管理器和环境管理器）上发展出来的。在数据分析中，你会用到很多第三方的包，而conda（包管理器）可以很好的帮助你在计算机上安装和管理这些包，包括安装、卸载和更新包。3）管理环境为什么需要管理环境呢？比如你在A项目中用了 Python 2，而新的项目B老大要求使用Python 3，而同时安装两个Python版本可能会造成许多混乱和错误。这时候 conda就可以帮助你为不同的项目建立不同的运行环境。还有很多项目使用的包版本不同，比如不同的pandas版本，不可能同时安装两个 Numpy 版本，你要做的应该是，为每个 Numpy 版本创建一个环境，然后项目的对应环境中工作。这时候conda就可以帮你做到。


# 2 如何安装
如果计算机上已经安装了 Python，安装不会对你有任何影响。实际上，脚本和程序使用的默认 Python 是 Anaconda 附带的 Python。

> 注意：如果你是windows 10系统，注意在安装Anaconda软件的时候，右击安装软件→选择以管理员的身份运行。


## 2.1 查看安装的内容
```
conda list
```
PS:如果按上面操作后在Anaconda Prompt中都无法使用Conda命令，按以下顺序的解决办法来尝试（正常使用的朋友忽略这一步，继续往下）：
* 1）检查你是否原来安装过Python，如果安装过请彻底删除Python（同时要删除环境变量）后重装Anaconda
* 2）检查自己是否将Conda命令添加到了环境变量，操作方法如下：[数据分析之第一坑解决-- conda不是内部或者外部命令报错](https://zhuanlan.zhihu.com/p/32446675)
另外，如果path中有任何关于anaconda、python的其他路径，都要删除，否则电脑识别不了两个路径，就会出现上述的错误。就好像有两个人给你各指了一条路，然而你并不知道哪条路是对的。

* 3）确保你的Anaconda安装路径不包含中文或其他非英语常用字符；

* 4）经过以上步骤还是没有任何改善，请卸载Anaconda重装一遍；

## 2.2 更新所有包，避免后面使用报错
```
conda upgrade --all
```

> 什么是你的“notebook工作文件夹”呢？默认情况下，是你启动Anaconda Prompt终端中的那个文件夹，比如我电脑上是下面这个文件夹（Windows为C://Users/username/.condarc，Linux/Mac为~/.condarc）：


# 3 如何管理包
## 3.1 安装包
可以安装多个，还可以添加版本号
```
conda install package_name
conda install pandas numpy
conda install numpy=1.10
```

## 3.2 卸载包
```
conda remove package_name
```

## 3.3 更新包
```
conda update package_name
```

## 3.4 列出所有包
```
conda list
```

## 3.5 搜索
```
conda search num
```



# 4 如何管理环境

## 4.0 安装nb_conda用于notebook自动关联nb_conda的环境。
```
conda install nb_conda
```
## 4.1 创建环境
```
conda create -n env_name package_names
```
* env_name 设置环境的名称（-n 是指该命令后面的env_name是你要创建环境的名称）
* package_names 是你要安装在创建环境中的包名称。

例如：要创建环境名称为 py3 的环境并在其中安装 numpy，在终端中输入 conda create -n py3 pandas。
```
conda create -n py3 pandas
```

## 4.2 创建环境时指定要安装在环境中的python版本
```
conda create -n py3 python=3 
conda create -n py2 python=2
```

## 4.3 进入/离开环境
```
# windows
activate my_env
deactivate

# OSX/Linux
source activate my_env
source deactivate
```

## 4.4 共享环境
将当前环境保存为YAML文件
```
conda env export > envrionment.yaml
```

> 在 GitHub 上共享代码时，最好同样创建环境文件并将其包括在代码库中。这能让其他人更轻松地安装你的代码的所有依赖项。

### 4.4.1 导出的环境在其他电脑上如何使用？
* 1 在conda中进入你的环境
```
activate py3
```
* 2 更新环境
```
#其中-f表示你要导出文件在本地的路径，所以/path/to/environment.yml要换成你本地的实际路径
conda env update -f=/path/to/environment.yml
```

### 4.4.2 
```
pip freeze > environment.txt
pip install -r /path/requirements.txt
```

## 4.5 列出环境
```
conda env list
```

## 4.6 删除环境
```
conda env remove -n env_name
```

# 5 Jupyter notebook 如何快速上手


