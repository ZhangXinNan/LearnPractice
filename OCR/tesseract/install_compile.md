

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