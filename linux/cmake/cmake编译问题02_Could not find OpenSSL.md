

# 1 问题
```bash
(base) zhangxin@zx:~/tools/cmake/cmake-3.19.0-rc3$ ./bootstrap 
---------------------------------------------
CMake 3.19.0-rc3, Copyright 2000-2020 Kitware, Inc. and Contributors
Found GNU toolchain
C compiler on this system is: gcc   
C++ compiler on this system is: g++    
Makefile processor on this system is: make
g++ has setenv
g++ has unsetenv
g++ does not have environ in stdlib.h
g++ has stl wstring
g++ has <ext/stdio_filebuf.h>
---------------------------------------------
make: 'cmake' is up to date.
loading initial cache file /home/zhangxin/tools/cmake/cmake-3.19.0-rc3/Bootstrap.cmk/InitialCacheFlags.cmake
-- Could NOT find OpenSSL, try to set the path to OpenSSL root folder in the system variable OPENSSL_ROOT_DIR (missing: OPENSSL_CRYPTO_LIBRARY OPENSSL_INCLUDE_DIR) 
CMake Error at Utilities/cmcurl/CMakeLists.txt:505 (message):
  Could not find OpenSSL.  Install an OpenSSL development package or
  configure CMake with -DCMAKE_USE_OPENSSL=OFF to build without OpenSSL.


-- Configuring incomplete, errors occurred!
See also "/home/zhangxin/tools/cmake/cmake-3.19.0-rc3/CMakeFiles/CMakeOutput.log".
See also "/home/zhangxin/tools/cmake/cmake-3.19.0-rc3/CMakeFiles/CMakeError.log".
---------------------------------------------
Error when bootstrapping CMake:
Problem while running initial CMake
---------------------------------------------
```

# 2 解决办法

```bash
# cmake . -DCMAKE_USE_OPENSSL=OFF
cmake .
make      
make install
```


