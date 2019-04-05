

开机时出现：
```
The system is running in low-graphics mode
Your screen, graphics card, and input device settings could not be detected correctly. You will need to configure these yourself.
[OK]
```

在我点了OK按钮后，出现如下画面：
```
What would you like to do ?
[*] Try running with default graphical mode
[ ] Reconfigure graphics
[ ] Troubleshoot the error
[ ] Exit to console login

[Cancel]   [OK]
```
点了OK后，并没有启动桌面。


## 解决方法
重新安装显卡驱动
```bash
sudo ./NVIDIA-Linux-x86_64-384.98.run --no-x-check
```
然后重启。

[Ubuntu16.04 报警"The system is running in low-graphics mode"](https://zhuanlan.zhihu.com/p/36087073)
[解决Ubuntu16.04 开机显示The system is running in low-graphics mode](https://blog.csdn.net/qq_26348877/article/details/79256277)




