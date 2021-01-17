
有时用conda安装开源软件特别慢 ，可以 把源换成清华的源。

清华大学开源软件镜像站[Anaconda 镜像使用帮助](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/)


Anaconda 是一个用于科学计算的 Python 发行版，支持 Linux, Mac, Windows, 包含了众多流行的科学计算、数据分析的 Python 包。

Anaconda 安装包可以到 https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/ 下载。

TUNA 还提供了 Anaconda 仓库与第三方源（conda-forge、msys2、pytorch等，查看完整列表）的镜像，各系统都可以通过修改用户目录下的 .condarc 文件:
```bash
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
即可添加 Anaconda Python 免费仓库。Windows 用户无法直接创建名为 .condarc 的文件，可先执行 conda config --set show_channel_urls yes 生成该文件之后再修改。
```
运行 conda create -n myenv numpy 测试一下吧。


# 一、conda换国内源
## 1.1 查看源

```bash
conda config --show-sources
# 显示结果
==> /home/xxx/.condarc <==
channels:

- https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
- defaults
```
这里有两个源，一个是清华的源，另一个是默认的源

## 1.2 添加源（这里以添加清华源为例，当然也可以选择其他的源）
```bash
# conda config --add channels
#添加清华的源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# 运行成果后，使用显示源查看是否添加成功（conda config --show-sources）
```

## 1.3 其他可选的源（还有更多的可以网上搜索，这里不一一列举）
```bash
# 中科大的源
conda config –add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/ 
# 阿里云的源
conda config --add channels http://mirrors.aliyun.com/pypi/simple/
```

## 1.4 移除源
```bash
# conda config --remove channels
conda config --remove channels 'https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/'
```

# 参考：
* [conda安装的国内镜像配置，实现快速下载](https://juejin.cn/post/6844903988324728840)
