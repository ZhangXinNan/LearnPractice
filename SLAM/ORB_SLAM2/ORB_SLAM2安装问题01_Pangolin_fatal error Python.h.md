问题：

cmake ..
```
zhangxin@zhangxin-Alienware-17-R5:~/tools/Pangolin/build$ cmake ..
-- The C compiler identification is GNU 5.4.0
-- The CXX compiler identification is GNU 5.4.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
Build type not set (defaults to release)
-DCMAKE_BUILD_TYPE=Debug for debug
-- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1") 
-- Found PythonInterp: /usr/bin/python3.5 (found version "3.5.2") 
-- Found PythonLibs: python3.5m
-- pybind11 v2.3.dev0
-- Python Found and Enabled (with pybind11)
-- Eigen Found and Enabled
-- libdc1394 Found and Enabled
-- V4L Found and Enabled
-- OpenNI Found and Enabled
-- libpng Found and Enabled
-- libjpeg Found and Enabled
-- libtiff Found and Enabled
-- libopenexr Found and Enabled
-- liblz4 Found and Enabled
-- Performing Test HAS_FLTO
-- Performing Test HAS_FLTO - Success
-- LTO enabled
-- Could NOT find Doxygen (missing:  DOXYGEN_EXECUTABLE) 
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zhangxin/tools/Pangolin/build
```

then, cmake --build .
```
[ 25%] Building CXX object src/CMakeFiles/pangolin.dir/display/display.cpp.o
In file included from /home/zhangxin/tools/Pangolin/src/display/display.cpp:31:0:
/home/zhangxin/tools/Pangolin/include/pangolin/python/pyinterpreter.h:30:20: fatal error: Python.h: No such file or directory
compilation terminated.
src/CMakeFiles/pangolin.dir/build.make:998: recipe for target 'src/CMakeFiles/pangolin.dir/display/display.cpp.o' failed
make[2]: *** [src/CMakeFiles/pangolin.dir/display/display.cpp.o] Error 1
CMakeFiles/Makefile2:139: recipe for target 'src/CMakeFiles/pangolin.dir/all' failed
make[1]: *** [src/CMakeFiles/pangolin.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2
```


解决方法：
```
```





