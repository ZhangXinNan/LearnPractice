Spyder是一个挺好用的python IDE。
如果想在虚拟环境中用Spyder，或者 说是Spyder中用虚拟环境中的库，则需要在虚拟环境中安装并启动，可以通过命令的方式，也可以通过Anaconda来操作。
1. 创建虚拟环境myenv，再安装spyder，最后启动。
```
conda create -n myenv python=3.6
conda activate myenv
conda install spyder
spyder
```
2. 打开Anaconda，创建一个环境，切换到创建好的环境，然后再安装spyder，最后启动即可。

参考资料：
[How to run Spyder in virtual environment?](https://stackoverflow.com/questions/30170468/how-to-run-spyder-in-virtual-environment)
