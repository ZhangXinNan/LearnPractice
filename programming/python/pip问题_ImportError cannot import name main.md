

在我安装升级完pip后，pip不能使用了。
```bash
zhangxin@zhangxin-ThinkPad-L480:/media/zhangxin/DATA/gitlab/documents/DL/ksyun/caffe$ pip -V
Traceback (most recent call last):
  File "/usr/bin/pip", line 9, in <module>
    from pip import main
ImportError: cannot import name main

```




## 解决办法：
```bash
# 打开/usr/bin/pip
sudo vim /usr/bin/pip

# 修改
from pip import main
# 为
from pip._internal import main
```



