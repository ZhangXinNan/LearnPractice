

# 1 问题
```bash
(base) zhangxin@zx:~/tools/cmake/cmake-3.19.0-rc3$ cmake .
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
Modules directory not found in
/usr/local/share/cmake-3.10
CMake Error: Error executing cmake::LoadCache(). Aborting.

(base) zhangxin@zx:~/tools/cmake/cmake-3.19.0-rc3$ cmake --version
CMake Error: Could not find CMAKE_ROOT !!!
CMake has most likely not been installed correctly.
Modules directory not found in
/usr/local/share/cmake-3.10
cmake version 3.10.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).

```

# 2 解决办法
```bash
# 清除缓存
hash -r
```