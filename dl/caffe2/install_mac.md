

```
Performing C++ SOURCE FILE Test CAFFE2_LONG_IS_INT32_OR_64 failed with the following output:
Change Dir: /Users/zhangxin/github/caffe2/build/CMakeFiles/CMakeTmp

Run Build Command:"/usr/bin/make" "cmTC_bd401/fast"
/Applications/Xcode.app/Contents/Developer/usr/bin/make -f CMakeFiles/cmTC_bd401.dir/build.make CMakeFiles/cmTC_bd401.dir/build
Building CXX object CMakeFiles/cmTC_bd401.dir/src.cxx.o
/Applications/Xcode.app/Contents/Developer/usr/bin/g++    -DCAFFE2_LONG_IS_INT32_OR_64 -std=c++11 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk   -o CMakeFiles/cmTC_bd401.dir/src.cxx.o -c /Users/zhangxin/github/caffe2/build/CMakeFiles/CMakeTmp/src.cxx
Linking CXX executable cmTC_bd401
/usr/local/Cellar/cmake/3.10.2/bin/cmake -E cmake_link_script CMakeFiles/cmTC_bd401.dir/link.txt --verbose=1
/Applications/Xcode.app/Contents/Developer/usr/bin/g++   -DCAFFE2_LONG_IS_INT32_OR_64 -std=c++11 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk -Wl,-search_paths_first -Wl,-headerpad_max_install_names   CMakeFiles/cmTC_bd401.dir/src.cxx.o  -o cmTC_bd401 
Undefined symbols for architecture x86_64:
  "void Foo<long>()", referenced from:
      _main in src.cxx.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[1]: *** [cmTC_bd401] Error 1
make: *** [cmTC_bd401/fast] Error 2

Source file was:
#include <cstdint>

    template <typename T> void Foo();
    template<> void Foo<int32_t>() {}
    template<> void Foo<int64_t>() {}
    int main(int argc, char** argv) {
      Foo<long>();
      return 0;
    }

```