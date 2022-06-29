

# 问题
```bash
(base) ➜  build git:(zxdev_mac) pwd
/Users/zhangxin/github/caffe/build
(base) ➜  build git:(zxdev_mac) cmake ..
-- Boost 1.54 found.
-- Found Boost components:
   system;thread;filesystem
-- Found gflags  (include: /usr/local/include, library: /usr/local/lib/libgflags.dylib)
-- Found glog    (include: /usr/local/include, library: /usr/local/lib/libglog.dylib)
CMake Error at /usr/local/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:137 (message):
  Could NOT find Protobuf (missing: Protobuf_INCLUDE_DIR)
Call Stack (most recent call first):
  /usr/local/share/cmake-3.10/Modules/FindPackageHandleStandardArgs.cmake:378 (_FPHSA_FAILURE_MESSAGE)
  /usr/local/share/cmake-3.10/Modules/FindProtobuf.cmake:543 (FIND_PACKAGE_HANDLE_STANDARD_ARGS)
  cmake/ProtoBuf.cmake:4 (find_package)
  cmake/Dependencies.cmake:43 (include)
  CMakeLists.txt:49 (include)


-- Configuring incomplete, errors occurred!
See also "/Users/zhangxin/github/caffe/build/CMakeFiles/CMakeOutput.log".
```

# 解决办法：

安装protobuf
```bash
(base) ➜  build git:(zxdev_mac) brew install protobuf boost
# Warning: protobuf 3.13.0 is already installed, it's just not linked
# You can use `brew link protobuf` to link this version.
# Warning: boost 1.73.0 is already installed and up-to-date
# To reinstall 1.73.0, run `brew reinstall boost`

(base) ➜  build git:(zxdev_mac) brew link protobuf
Linking /usr/local/Cellar/protobuf/3.13.0... 
Error: Could not symlink share/emacs/site-lisp/protobuf
/usr/local/share/emacs/site-lisp is not writable.
```

解决办法：
```bash
sudo chown zhangxin /usr/local/share/emacs/site-lisp
```
再次
```bash
cmake ..
```
就可以了。




