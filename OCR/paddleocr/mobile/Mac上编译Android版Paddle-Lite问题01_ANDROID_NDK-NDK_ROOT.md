# 设置路径ANDROID_NDK 或者 NDK_ROOT
错误：
```bash
(py37_paddle) ➜  Paddle-Lite git:(zxdev) ./lite/tools/build_android.sh  --arch=armv8  --with_cv=ON --with_extra=ON
-- Found Paddle host system: macosx, version: 10.15.5
-- Found Paddle host system's CPU: 12 cores
CMake Error at cmake/cross_compiling/android.cmake:26 (message):
  Must set ANDROID_NDK or env NDK_ROOT
Call Stack (most recent call first):
  cmake/cross_compiling/preproject.cmake:47 (include)
  CMakeLists.txt:30 (include)
```

解决方法：
```bash
export NDK_ROOT=~/Library/Android/sdk/ndk/21.0.6113669
```