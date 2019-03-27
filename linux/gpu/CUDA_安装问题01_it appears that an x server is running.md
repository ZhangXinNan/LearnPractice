

安装CUDA时
```
sudo sh ./cuda_9.0.176_384.81_linux.run
```
出现如下问题：
```
It appears that an X server is running . Please exit X before installation. If you're sure that X is not running, but are getting this error, please delete any X lock files in /tmp.
```


删除tmp文件夹下的X lock，这是最先搜到的方法，最后就是要求重启.




# 参考
[How to install NVIDIA.run?](https://askubuntu.com/questions/149206/how-to-install-nvidia-run)

[MxNet Ubuntu Desktop 16.04 安装教程（我遇到的坑）经验总结在帖子最下方](https://discuss.gluon.ai/t/topic/1129)