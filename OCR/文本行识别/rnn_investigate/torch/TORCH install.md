### seele ubuntu14.04 seele
```
 bash install-deps;


下列软件包有未满足的依赖关系：
 gfortran : 依赖: gfortran-4.8 (>= 4.8.2-5~) 但是它将不会被安装
 libqt4-dev : 依赖: libqt4-dbus (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-declarative (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-designer (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-dev-bin (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4)
              依赖: libqt4-help (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-network (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-qt3support (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是它将不会被安装
              依赖: libqt4-script (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-scripttools (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-sql (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-svg (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-test (= 4:4.8.5+git192-g085f851+dfsg-2ubuntu4) 但是 4:4.8.5+git192-g085f851+dfsg-2ubuntu4.1 正要被安装
              依赖: libqt4-xml (= 4:4.8.5+git192-g085f851+dfsg-2ubu
              
```



### 142
torch 安装 成功

```
[zhangxin0627@l22-240-142 src]$ sh build_cpp.sh
mkdir: cannot create directory ‘build’: File exists
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
LUAT_LIBRARY
    linked by target "crnn" in directory /data/zhangxin/github/crnn/src/cpp
THC_LIBRARY
    linked by target "crnn" in directory /data/zhangxin/github/crnn/src/cpp
THPP_LIBRARY
    linked by target "crnn" in directory /data/zhangxin/github/crnn/src/cpp
TH_LIBRARY
    linked by target "crnn" in directory /data/zhangxin/github/crnn/src/cpp

-- Configuring incomplete, errors occurred!
See also "/data/zhangxin/github/crnn/src/cpp/build/CMakeFiles/CMakeOutput.log".
make: *** No targets specified and no makefile found.  Stop.
cp: cannot stat ‘*.so’: No such file or directory
```