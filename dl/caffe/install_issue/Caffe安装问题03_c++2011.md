
## 问题
```
PROTOC src/caffe/proto/caffe.proto
CXX .build_release/src/caffe/proto/caffe.pb.cc
In file included from /usr/include/c++/5/mutex:35:0,
                 from /usr/local/include/google/protobuf/stubs/mutex.h:33,
                 from /usr/local/include/google/protobuf/stubs/common.h:52,
                 from .build_release/src/caffe/proto/caffe.pb.h:9,
                 from .build_release/src/caffe/proto/caffe.pb.cc:4:
/usr/include/c++/5/bits/c++0x_warning.h:32:2: error: #error This file requires compiler and library support for the ISO C++ 2011 standard. This support must be enabled with the -std=c++11 or -std=gnu++11 compiler options.
 #error This file requires compiler and library support \
  ^
In file included from /usr/local/include/google/protobuf/stubs/common.h:52:0,
                 from .build_release/src/caffe/proto/caffe.pb.h:9,
                 from .build_release/src/caffe/proto/caffe.pb.cc:4:
/usr/local/include/google/protobuf/stubs/mutex.h:58:8: error: ‘mutex’ in namespace ‘std’ does not name a type
   std::mutex mu_;
        ^
/usr/local/include/google/protobuf/stubs/mutex.h: In member function ‘void google::protobuf::internal::WrappedMutex::Lock()’:
/usr/local/include/google/protobuf/stubs/mutex.h:51:17: error: ‘mu_’ was not declared in this scope
   void Lock() { mu_.lock(); }
                 ^
/usr/local/include/google/protobuf/stubs/mutex.h: In member function ‘void google::protobuf::internal::WrappedMutex::Unlock()’:
/usr/local/include/google/protobuf/stubs/mutex.h:52:19: error: ‘mu_’ was not declared in this scope
   void Unlock() { mu_.unlock(); }
                   ^
/usr/local/include/google/protobuf/stubs/mutex.h: At global scope:
/usr/local/include/google/protobuf/stubs/mutex.h:61:7: error: expected nested-name-specifier before ‘Mutex’
 using Mutex = WrappedMutex;
       ^
/usr/local/include/google/protobuf/stubs/mutex.h:66:28: error: expected ‘)’ before ‘*’ token
   explicit MutexLock(Mutex *mu) : mu_(mu) { this->mu_->Lock(); }
                            ^
/usr/local/include/google/protobuf/stubs/mutex.h:69:3: error: ‘Mutex’ does not name a type
   Mutex *const mu_;
   ^
/usr/local/include/google/protobuf/stubs/mutex.h: In destructor ‘google::protobuf::internal::MutexLock::~MutexLock()’:
/usr/local/include/google/protobuf/stubs/mutex.h:67:24: error: ‘class google::protobuf::internal::MutexLock’ has no member named ‘mu_’
   ~MutexLock() { this->mu_->Unlock(); }
                        ^
/usr/local/include/google/protobuf/stubs/mutex.h: At global scope:
/usr/local/include/google/protobuf/stubs/mutex.h:80:33: error: expected ‘)’ before ‘*’ token
   explicit MutexLockMaybe(Mutex *mu) :
                                 ^
In file included from /usr/local/include/google/protobuf/arena.h:48:0,
                 from .build_release/src/caffe/proto/caffe.pb.h:23,
                 from .build_release/src/caffe/proto/caffe.pb.cc:4:
/usr/include/c++/5/typeinfo:39:37: error: expected ‘}’ before end of line
/usr/include/c++/5/typeinfo:39:37: error: expected unqualified-id before end of line
/usr/include/c++/5/typeinfo:39:37: error: expected ‘}’ before end of line
/usr/include/c++/5/typeinfo:39:37: error: expected ‘}’ before end of line
/usr/include/c++/5/typeinfo:39:37: error: expected ‘}’ before end of line
/usr/include/c++/5/typeinfo:39:37: error: expected declaration before end of line
Makefile:598: recipe for target '.build_release/src/caffe/proto/caffe.pb.o' failed
make: *** [.build_release/src/caffe/proto/caffe.pb.o] Error 1

```

## 解决方法
```

```


## 参考
[Build Caffe and pycaffe ](https://github.com/BVLC/caffe/issues/5078)

```
We have the same problem...and it is because of the wrong version of protobuf
首先你要卸载，并重装其要求的protobuf版本（2.6.1），之后重新编译就好了
我卸载了protobuf3.0，重新安装了很多次的protobuf2.6.1，但都不行
重装后：protoc --version 结果还是3.0
如果你也这样，你需要的工作是：
1。sudo find / -name protoc
2。将2.6.1版本生成的protoc，替换掉找到的3.0版本的protoc
然后就ok了
我整整搞了两天
good luck
```


```
First remove the protobuf in Anaconda.
Then, sudo apt-get install libprotobuf-dev protobuf-compiler.
Problem solved somehow.
```