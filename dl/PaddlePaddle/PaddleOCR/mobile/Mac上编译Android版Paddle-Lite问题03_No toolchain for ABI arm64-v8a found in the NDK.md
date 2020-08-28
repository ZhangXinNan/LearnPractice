


## 遇到错误
```bash
(py37_paddle) ➜  Paddle-Lite git:(zxdev) ./lite/tools/build_android.sh  --arch=armv8  --with_cv=ON --with_extra=ON         
-- Found Paddle host system: macosx, version: 10.15.5
-- Found Paddle host system's CPU: 12 cores
-- Found host C compiler: /usr/bin/gcc
-- Found host CXX compiler: /usr/bin/g++
-- Lite ARM Compile android with armv8 
-- Android: Targeting API '23' with architecture 'arm64', ABI 'arm64-v8a', and processor 'aarch64'
CMake Error at /usr/local/share/cmake-3.10/Modules/Platform/Android/Determine-Compiler-NDK.cmake:97 (message):
  Android: No toolchain for ABI 'arm64-v8a' found in the NDK:

    /Users/zhangxin/Library/Android/sdk/ndk/21.0.6113669

Call Stack (most recent call first):
  /usr/local/share/cmake-3.10/Modules/Platform/Android/Determine-Compiler.cmake:39 (include)
  /usr/local/share/cmake-3.10/Modules/Platform/Android-Determine-CXX.cmake:1 (include)
  /usr/local/share/cmake-3.10/Modules/CMakeDetermineCXXCompiler.cmake:26 (include)
  CMakeLists.txt:32 (project)


CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "/Users/zhangxin/github/Paddle-Lite/build.lite.android.armv8.gcc/CMakeFiles/CMakeOutput.log".
make: *** No rule to make target `publish_inference'.  Stop.
```



## 解决办法

使用paddle-lite推荐的ndk就可以了。原来我安装的是NDK 21，然后通过 Tools->SDK Manager -> SDK Tools，安装17的NDK即可，然后配置环境变量
```bash
export NDK_ROOT=/Users/zhangxin/Library/Android/sdk/ndk/17.2.4988734
```
