

遇到错误：
```bash
(py37_paddle) ➜  Paddle-Lite git:(zxdev) ./lite/tools/build_android.sh  --arch=armv8  --with_cv=ON --with_extra=ON
-- Found Paddle host system: macosx, version: 10.15.5
-- Found Paddle host system's CPU: 12 cores
-- Found host C compiler: /usr/bin/gcc
-- Found host CXX compiler: /usr/bin/g++
-- Lite ARM Compile android with armv8 
-- Android: Targeting API '23' with architecture 'arm64', ABI 'arm64-v8a', and processor 'aarch64'
-- Android: Selected unified Clang toolchain
-- The CXX compiler identification is Clang 9.0.8
-- The C compiler identification is Clang 9.0.8
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /Users/zhangxin/Library/Android/sdk/ndk/21.0.6113669/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /Users/zhangxin/Library/Android/sdk/ndk/21.0.6113669/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- CXX compiler: /Users/zhangxin/Library/Android/sdk/ndk/21.0.6113669/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang++, version: Clang 9.0.8
-- C compiler: /Users/zhangxin/Library/Android/sdk/ndk/21.0.6113669/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang, version: Clang 9.0.8
-- AR tools: /Users/zhangxin/Library/Android/sdk/ndk/21.0.6113669/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android-ar
-- Found Git: /usr/bin/git (found version "2.24.3 (Apple Git-128)") 
-- Looking for pthread.h
-- Looking for pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - not found
-- Check if compiler accepts -pthread
-- Check if compiler accepts -pthread - yes
-- Found Threads: TRUE  
-- Performing Test MMX_FOUND
-- Performing Test MMX_FOUND - Failed
-- Performing Test SSE2_FOUND
-- Performing Test SSE2_FOUND - Failed
-- Performing Test SSE3_FOUND
-- Performing Test SSE3_FOUND - Failed
-- Performing Test AVX_FOUND
-- Performing Test AVX_FOUND - Failed
-- Performing Test AVX2_FOUND
-- Performing Test AVX2_FOUND - Failed
-- Performing Test AVX512F_FOUND
-- Performing Test AVX512F_FOUND - Failed
-- CMAKE_BUILD_TYPE: Release
-- `lite/model_parser/flatbuffers/framework.fbs`: add generation of C++ code with '--no-includes;--gen-compare;--force-empty'
-- SRC_FBS_DIR: lite/model_parser/flatbuffers
-- `lite/model_parser/flatbuffers/param.fbs`: add generation of C++ code with '--no-includes;--gen-compare;--force-empty'
-- SRC_FBS_DIR: lite/model_parser/flatbuffers
-- Building the mobile framework
-- Performing Test out_var
-- Performing Test out_var - Failed
-- Found OpenMP_C: -fopenmp=libomp (found version "3.1") 
CMake Error at /usr/local/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:165 (message):
  Could NOT find OpenMP_CXX (missing: OpenMP_CXX_FLAGS OpenMP_CXX_LIB_NAMES)
Call Stack (most recent call first):
  /usr/local/share/cmake-3.18/Modules/FindPackageHandleStandardArgs.cmake:458 (_FPHSA_FAILURE_MESSAGE)
  /usr/local/share/cmake-3.18/Modules/FindOpenMP.cmake:529 (find_package_handle_standard_args)
  cmake/cross_compiling/postproject.cmake:95 (find_package)
  CMakeLists.txt:179 (include)


-- Configuring incomplete, errors occurred!
See also "/Users/zhangxin/github/Paddle-Lite/build.lite.android.armv8.gcc/CMakeFiles/CMakeOutput.log".
See also "/Users/zhangxin/github/Paddle-Lite/build.lite.android.armv8.gcc/CMakeFiles/CMakeError.log".
make: *** No rule to make target `publish_inference'.  Stop.
```



解决办法：重新编译安装camke 3.10.3版本。
安装cmake：
```bash
./bootstrap
make -j4
sudo make install
```

