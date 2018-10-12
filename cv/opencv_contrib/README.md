## 编译
```
mkdir release
cd release
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D INSTALL_C_EXAMPLES=OFF \
      -D OPENCV_EXTRA_MODULES_PATH=/Users/zhangxin/github/opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON \
      ..

make
sudo make install
```

## 问题
### 问题1
```
/usr/local/include/tesseract/publictypes.h:33:1: error: unknown type name 'constexpr'
```
解决方法：
```
sudo vim /usr/local/include/tesseract/publictypes.h
//add this line
#define constexpr const
```

### 问题2
```

```
