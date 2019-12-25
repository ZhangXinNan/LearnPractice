
# 1 问题
```bash
(py36_pytorch13) ➜  lanms git:(zxdev) ✗ python setup.py build_ext --inplace
running build_ext
building 'adaptor' extension
creating build
creating build/temp.macosx-10.7-x86_64-3.6
creating build/temp.macosx-10.7-x86_64-3.6/include
creating build/temp.macosx-10.7-x86_64-3.6/include/clipper
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/zhangxin/anaconda3/envs/py36_pytorch13/include -arch x86_64 -I/Users/zhangxin/anaconda3/envs/py36_pytorch13/include -arch x86_64 -Iinclude -I/Users/zhangxin/anaconda3/envs/py36_pytorch13/include/python3.6m -c adaptor.cpp -o build/temp.macosx-10.7-x86_64-3.6/adaptor.o
warning: include path for stdlibc++ headers not found; pass '-stdlib=libc++' on the command line to use the libc++ standard library instead
      [-Wstdlibcxx-not-found]
In file included from adaptor.cpp:1:
In file included from include/pybind11/pybind11.h:43:
In file included from include/pybind11/attr.h:13:
In file included from include/pybind11/cast.h:13:
In file included from include/pybind11/pytypes.h:12:
include/pybind11/common.h:126:10: fatal error: 'cstddef' file not found
#include <cstddef>
         ^~~~~~~~~
1 warning and 1 error generated.
error: command 'gcc' failed with exit status 1
```


# 2 解决方法



