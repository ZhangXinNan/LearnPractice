

# 问题
```bash
(base) ➜  caffe git:(zxdev_mac) make
No receipt for 'com.apple.pkg.CLTools_Executables' found at '/'.
/bin/sh: line 0: [: -gt: unary operator expected
/bin/sh: line 0: [: -gt: unary operator expected
PROTOC src/caffe/proto/caffe.proto
make: protoc: No such file or directory
make: *** [.build_release/src/caffe/proto/caffe.pb.cc] Error 1
(base) ➜  caffe git:(zxdev_mac) xcode-select --install
xcode-select: note: install requested for command line developer tools
```

# 解决办法
