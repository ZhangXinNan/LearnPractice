

# mac
## 问题1
```
➜  tesseract git:(zxdev_mac) ✗ tesseract
dyld: Library not loaded: /usr/local/opt/gcc/lib/gcc/6/libgomp.1.dylib
  Referenced from: /usr/local/bin/tesseract
  Reason: image not found
[1]    31187 trace trap  tesseract
```


解决方法
```
ln -s /usr/local/opt/gcc/lib/gcc/7/libgomp.1.dylib /usr/local/lib/libgomp.1.dylib
```

## 问题2
```
➜  tesseract git:(zxdev_mac) ./configure CC=gcc-6 CXX=g++-6 CPPFLAGS=-I/usr/local/opt/icu4c/include LDFLAGS=-L/usr/local/opt/icu4c/lib
checking whether the C++ compiler works... no
configure: error: in `/Users/zhangxin/github/tesseract':
configure: error: C++ compiler cannot create executables
See `config.log' for more details

```

解决办法：
```
# 去掉CC和CXX部分。

省略。。。
Configuration is done.
You can now build and install tesseract by running:

$ make
$ sudo make install

Training tools can be built and installed with:

$ make training
$ sudo make training-install

```

