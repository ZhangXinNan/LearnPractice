# 1 安装
## 1.1 安装命令
```
pip install paddlepaddle -i https://pypi.douban.com/simple
```


## 1.2 问题在mac上安装paddle后：
```
➜  深度学习-用PaddlePaddle调戏邮件诈骗犯 git:(master) ✗ python hello.py
Fatal Python error: PyThreadState_Get: no current thread
[1]    1758 abort      python hello.py
```

## 1.3 解决办法
1、运行otool，可以看到pip安装之后的_swig_paddle.so依赖/usr/local/opt/python/Frameworks/Python.framework/Versions/2.7/Python，但实际系统中不存在该路径
```
➜  深度学习-用PaddlePaddle调戏邮件诈骗犯 git:(master) ✗ otool -L ~/anaconda2/lib/python2.7/site-packages/py_paddle/_swig_paddle.so
/Users/zhangxin/anaconda2/lib/python2.7/site-packages/py_paddle/_swig_paddle.so:
	/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 1445.12.0)
	/System/Library/Frameworks/Security.framework/Versions/A/Security (compatibility version 1.0.0, current version 58286.20.16)
	/usr/local/opt/python/Frameworks/Python.framework/Versions/2.7/Python (compatibility version 2.7.0, current version 2.7.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 400.9.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.0.0)
```

2、利用install_name_tool来替换依赖
```
install_name_tool -change /usr/local/opt/python/Frameworks/Python.framework/Versions/2.7/Python ~/anaconda2/lib/libpython2.7.dylib ~/anaconda2/lib/python2.7/site-packages/py_paddle/_swig_paddle.so
```

3、 替换成功后，可以看到第五条已经成功的换成anaconda下的路径了
```
➜  深度学习-用PaddlePaddle调戏邮件诈骗犯 git:(master) ✗ otool -L ~/anaconda2/lib/python2.7/site-packages/py_paddle/_swig_paddle.so
/Users/zhangxin/anaconda2/lib/python2.7/site-packages/py_paddle/_swig_paddle.so:
	/System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation (compatibility version 150.0.0, current version 1445.12.0)
	/System/Library/Frameworks/Security.framework/Versions/A/Security (compatibility version 1.0.0, current version 58286.20.16)
	/Users/zhangxin/anaconda2/lib/libpython2.7.dylib (compatibility version 2.7.0, current version 2.7.0)
	/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 400.9.0)
	/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.0.0)

```