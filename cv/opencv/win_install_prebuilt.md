参考文档：[Installation in Windows](https://docs.opencv.org/3.4.3/d3/d52/tutorial_windows_install.html)



# 安装预编译库流程：
1. 下载安装包（我下载的是3.4.3的版本，opencv-3.4.3-vc14_vc15.exe）
2. 确认你有admin权限，解压安装包
3. 设置OpenCV环境变量，并添加到系统变量里。




# 设置环境变量
（我是用的VS2017）
1. 命令行输入（以管理员身份运行）
```
# (suggested for Visual Studio 2015 - 64 bit Windows)
setx -m OPENCV_DIR D:\OpenCV\3.4.3\opencv\build\x64\vc15
```

【补充】vs与VC版本对应关系
```
Visual Studio 6 ： vc6 
Visual Studio 2003 ： vc7 
Visual Studio 2005 ： vc8 
Visual Studio 2008 ： vc9 
Visual Studio 2010 ： vc10 
Visual Studio 2012 ： vc11 
Visual Studio 2013 ： vc12 
Visual Studio 2015 ： vc14 
Visual Studio 2017 ： vc15
```

2. DLL
（1）如果编译静态库，这样就完成了。
（2）如果编译成动态库，需要将bin目录添加到系统路径里。因为你需要用OpenCV的动态链接库。在这里面存储了OpenCV包含的所有的算法和信息。操作系统在运行期间在需要时加载他们。然而操作系统需要知道他们在哪。系统PATH包含了一系列DLL的路径。


