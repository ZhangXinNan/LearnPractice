
# 1 说明
在conda创建的虚拟环境中使用pybind11时出现问题。

## 1.1 cmake ..
```bash
mkdir build
cd build
cmake ..
```
输出：
```bash
(py36_pytorch041) ➜  build git:(master) ✗ cmake ..
-- The C compiler identification is AppleClang 10.0.1.10010046
-- The CXX compiler identification is AppleClang 10.0.1.10010046
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PythonInterp: /Users/zhangxin/anaconda3/bin/python3.7 (found version "3.7") 
-- Found PythonLibs: /Users/zhangxin/anaconda3/lib/libpython3.7m.dylib
-- Performing Test HAS_CPP14_FLAG
-- Performing Test HAS_CPP14_FLAG - Success
-- pybind11 v2.3.dev0
-- Performing Test HAS_FLTO
-- Performing Test HAS_FLTO - Success
-- LTO enabled
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/zhangxin/github/pybind11_examples/01_py-list_cpp-vector/build
```

> 【注意】Found PythonInterp和Found PythonLibs这两行。

## 1.2 make 
```bash
make
```

输出：
```bash
(py36_pytorch041) ➜  build git:(master) ✗ make 
Scanning dependencies of target example
[ 50%] Building CXX object CMakeFiles/example.dir/example.cpp.o
[100%] Linking CXX shared module example.cpython-37m-darwin.so
[100%] Built target example
```

## 1.3 执行python测试

```bash
python ../test.py
```

输出：
```bash
(py36_pytorch041) ➜  build git:(master) ✗ python ../test.py 
Traceback (most recent call last):
  File "../test.py", line 2, in <module>
    import example
ModuleNotFoundError: No module named 'example'
```


# 2 解决方法

## 2. 1 在cmake 时设定python的路径。
```bash
cmake -DPYTHON_LIBRARY=/Users/zhangxin/anaconda3/envs/py36_pytorch041/lib/libpython3.6m.dylib \
    -DPYTHON_INCLUDE_DIR=/Users/zhangxin/anaconda3/envs/py36_pytorch041/include/python3.6 \
    -DPYTHON_EXECUTABLE=/Users/zhangxin/anaconda3/envs/py36_pytorch041/bin/python3.6 \
    ..
```

输出：
```bash
(py36_pytorch041) ➜  build git:(master) ✗ cmake -DPYTHON_LIBRARY=/Users/zhangxin/anaconda3/envs/py36_pytorch041/lib/libpython3.6m.dylib \
    -DPYTHON_INCLUDE_DIR=/Users/zhangxin/anaconda3/envs/py36_pytorch041/include/python3.6 \
    -DPYTHON_EXECUTABLE=/Users/zhangxin/anaconda3/envs/py36_pytorch041/bin/python3.6 \
    ..
-- The C compiler identification is AppleClang 10.0.1.10010046
-- The CXX compiler identification is AppleClang 10.0.1.10010046
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found PythonInterp: /Users/zhangxin/anaconda3/envs/py36_pytorch041/bin/python3.6 (found version "3.6.9") 
-- Found PythonLibs: /Users/zhangxin/anaconda3/envs/py36_pytorch041/lib/libpython3.6m.dylib
-- Performing Test HAS_CPP14_FLAG
-- Performing Test HAS_CPP14_FLAG - Success
-- pybind11 v2.3.dev0
-- Performing Test HAS_FLTO
-- Performing Test HAS_FLTO - Success
-- LTO enabled
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/zhangxin/github/pybind11_examples/01_py-list_cpp-vector/build
```

## 2.2 make

```bash
(py36_pytorch041) ➜  build git:(master) ✗ make 
Scanning dependencies of target example
[ 50%] Building CXX object CMakeFiles/example.dir/example.cpp.o
[100%] Linking CXX shared module example.cpython-36m-darwin.so
[100%] Built target example
```

## 2.3 测试
```bash
mv example.cpython-36m-darwin.so
cd ..
python test.py
```




# 3 代码

example.cpp
```c++
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

// ----------------
// Regular C++ code
// ----------------

// multiply all entries by 2.0
// input:  std::vector ([...]) (read only)
// output: std::vector ([...]) (new copy)
std::vector<double> modify(const std::vector<double>& input)
{
  std::vector<double> output;

  std::transform(
    input.begin(),
    input.end(),
    std::back_inserter(output),
    [](double x) -> double { return 2.*x; }
  );

  // N.B. this is equivalent to (but there are also other ways to do the same)
  //
  // std::vector<double> output(input.size());
  //
  // for ( size_t i = 0 ; i < input.size() ; ++i )
  //   output[i] = 2. * input[i];

  return output;
}

// ----------------
// Python interface
// ----------------

namespace py = pybind11;

PYBIND11_MODULE(example,m)
{
  m.doc() = "pybind11 example plugin";

  m.def("modify", &modify, "Multiply all entries of a list by 2.0");
}
```

test.py
```python
import example

A = [1.,2.,3.,4.]

B = example.modify(A)

print(B)
```

CMakeLists.txt
```makefile
cmake_minimum_required(VERSION 2.8.12)
project(example)

add_subdirectory(pybind11)
pybind11_add_module(example example.cpp)
```



# 4 参考
* [I have 2 versions of python installed, but cmake is using older version. How do I force cmake to use the newer version?](https://stackoverflow.com/questions/15291500/i-have-2-versions-of-python-installed-but-cmake-is-using-older-version-how-do)