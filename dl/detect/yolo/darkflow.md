[darkflow](https://github.com/thtrieu/darkflow)

安装
```
virtualenv --no-site-packages -p /usr/local/bin/python3 venv
source venv/bin/activate
pip3 install Cython
pip3 install numpy
python3 setup.py build_ext --inplace
```

问题1
```
/usr/bin/gcc -bundle -undefined dynamic_lookup -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk /usr/local/opt/openssl/lib /usr/local/opt/openssl/include build/temp.macosx-10.13-x86_64-3.6/darkflow/cython_utils/nms.o -lm -o build/lib.macosx-10.13-x86_64-3.6/darkflow/cython_utils/nms.cpython-36m-darwin.so
ld: can't map file, errno=22 file '/usr/local/opt/openssl/lib' for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
error: command '/usr/bin/gcc' failed with exit status 1
```

解决方法：
```

```