

# 错误
```bash
(base) ➜  caffe git:(zxdev_mac) make
No receipt for 'com.apple.pkg.CLTools_Executables' found at '/'.
/bin/sh: line 0: [: -gt: unary operator expected
/bin/sh: line 0: [: -gt: unary operator expected
PROTOC src/caffe/proto/caffe.proto
CXX .build_release/src/caffe/proto/caffe.pb.cc
In file included from .build_release/src/caffe/proto/caffe.pb.cc:4:
In file included from .build_release/src/caffe/proto/caffe.pb.h:23:
In file included from /usr/local/include/google/protobuf/io/coded_stream.h:141:
In file included from /usr/local/include/google/protobuf/stubs/common.h:46:
In file included from /usr/local/include/google/protobuf/stubs/macros.h:34:
/usr/local/include/google/protobuf/stubs/port.h:114:2: error: "Protobuf requires at least C++11."
#error "Protobuf requires at least C++11."
 ^
/usr/local/include/google/protobuf/stubs/port.h:120:26: warning: alias declarations are a C++11 extension [-Wc++11-extensions]
using ConstStringParam = const std::string &;
                         ^
In file included from .build_release/src/caffe/proto/caffe.pb.cc:4:
In file included from .build_release/src/caffe/proto/caffe.pb.h:23:
In file included from /usr/local/include/google/protobuf/io/coded_stream.h:141:
In file included from /usr/local/include/google/protobuf/stubs/common.h:49:
/usr/local/include/google/protobuf/stubs/stringpiece.h:315:3: warning: explicit conversion functions are a C++11 extension [-Wc++11-extensions]
  explicit operator std::string() const { return ToString(); }
  ^~~~~~~~
/usr/local/include/google/protobuf/stubs/stringpiece.h:464:3: warning: explicit conversion functions are a C++11 extension [-Wc++11-extensions]
  explicit operator std::string() const { return ToString(); }
  ^~~~~~~~
In file included from .build_release/src/caffe/proto/caffe.pb.cc:4:
In file included from .build_release/src/caffe/proto/caffe.pb.h:23:
In file included from /usr/local/include/google/protobuf/io/coded_stream.h:141:
/usr/local/include/google/protobuf/stubs/common.h:167:3: warning: 'auto' type specifier is a C++11 extension [-Wc++11-extensions]
```


# 解决办法


在Makefile或者CMakeLists.txt中增加 -std=c++11
```bash
# CMakeLists.txt
if(UNIX OR APPLE)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -Wall -std=c++11")
endif()
```