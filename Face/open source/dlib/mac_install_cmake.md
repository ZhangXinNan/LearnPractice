
```
cmake .. -DUSE_AVX_INSTRUCTIONS=1
```

报错：
```
-- The C compiler identification is AppleClang 9.1.0.9020039
-- The CXX compiler identification is AppleClang 9.1.0.9020039
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/usr/bin/gcc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/usr/bin/gcc -- broken
CMake Error at /usr/local/Cellar/cmake/3.10.2/share/cmake/Modules/CMakeTestCCompiler.cmake:52 (message):
  The C compiler

    "/Applications/Xcode.app/Contents/Developer/usr/bin/gcc"

  is not able to compile a simple test program.

  It fails with the following output:

    Change Dir: /Users/zhangxin/github/dlib/build/CMakeFiles/CMakeTmp
    
    Run Build Command:"/usr/bin/make" "cmTC_03a90/fast"
    /Applications/Xcode.app/Contents/Developer/usr/bin/make -f CMakeFiles/cmTC_03a90.dir/build.make CMakeFiles/cmTC_03a90.dir/build
    Building C object CMakeFiles/cmTC_03a90.dir/testCCompiler.c.o
    /Applications/Xcode.app/Contents/Developer/usr/bin/gcc   -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk   -o CMakeFiles/cmTC_03a90.dir/testCCompiler.c.o   -c /Users/zhangxin/github/dlib/build/CMakeFiles/CMakeTmp/testCCompiler.c
    Linking C executable cmTC_03a90
    /usr/local/Cellar/cmake/3.10.2/bin/cmake -E cmake_link_script CMakeFiles/cmTC_03a90.dir/link.txt --verbose=1
    /Applications/Xcode.app/Contents/Developer/usr/bin/gcc   -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk -Wl,-search_paths_first -Wl,-headerpad_max_install_names /usr/local/opt/openssl/lib  CMakeFiles/cmTC_03a90.dir/testCCompiler.c.o  -o cmTC_03a90 
    ld: can't map file, errno=22 file '/usr/local/opt/openssl/lib' for architecture x86_64
    clang: error: linker command failed with exit code 1 (use -v to see invocation)
    make[1]: *** [cmTC_03a90] Error 1
    make: *** [cmTC_03a90/fast] Error 2
    

  

  CMake will not be able to correctly generate this project.
Call Stack (most recent call first):
  CMakeLists.txt


-- Configuring incomplete, errors occurred!
See also "/Users/zhangxin/github/dlib/build/CMakeFiles/CMakeOutput.log".
See also "/Users/zhangxin/github/dlib/build/CMakeFiles/CMakeError.log".
```

