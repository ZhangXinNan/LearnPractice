
# 出现问题
/usr/bin/ld: cannot find -lnvinfer
collect2: error: ld returned 1 exit status


# 解决方法
背景：
首先：这个问题的出现的前提是，你安装的tensorRT是zip或者tar版本，不需要root权限。
其次：出现这个问题是在使用tensorrtx github库时候，跑lenet的demo的时候出现的。使用make编译的时候报的错。
在github的tensorrtx/tutorials/faq.md中说过如何解决这个问题：

然后按照说明的改cmakelist.txt文件就行。改动如下：
将下面两行注释掉，这两个指向的是系统环境下tensorrt的那几个头文件的位置。

# tensorrt
```make
include_directories(/usr/include/x86_64-linux-gnu/)
link_directories(/usr/lib/x86_64-linux-gnu/)
```
然后添加如下两行
```make
include_directories(/home/xxxx/TensorRT-6.0.1.5/include/)
link_directories(/home/xxxx/TensorRT-6.0.1.5/targets/x86_64-linux-gnu/lib/)
#TensorRT-6.0.1.5是我解压后的文件夹名称
```




# 参考资料
![部署tensorRT时，解决可能出现的问题。](https://blog.csdn.net/qq_41375609/article/details/109972482)


