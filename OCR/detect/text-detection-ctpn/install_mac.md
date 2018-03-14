
```
python setup.py build_ext --include-dirs=/Users/zhangxin/anaconda2/lib/python2.7/site-packages/numpy/core/include
# or
python setup.py build
```


问题1：
```
35 warnings generated.
/usr/bin/gcc -bundle -undefined dynamic_lookup -L/Users/zhangxin/anaconda2/lib -arch x86_64 /Users/zhangxin/anaconda2/lib/python2.7/site-packages/numpy/core/include -arch x86_64 build/temp.macosx-10.6-x86_64-2.7/bbox.o -L/Users/zhangxin/anaconda2/lib -o build/lib.macosx-10.6-x86_64-2.7/bbox.so
ld: can't map file, errno=22 file '/Users/zhangxin/anaconda2/lib/python2.7/site-packages/numpy/core/include' for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
error: command '/usr/bin/gcc' failed with exit status 1
```

问题2：
```
➜  utils git:(zxdev_mac) ✗ python setup.py.zhao181 build
Traceback (most recent call last):
  File "setup.py.zhao181", line 11, in <module>
    ext_modules=cythonize(["bbox.pyx","cython_nms.pyx"], include_dirs=[numpy_include]),
  File "/Users/zhangxin/anaconda2/lib/python2.7/site-packages/Cython/Build/Dependencies.py", line 897, in cythonize
    c_options = CompilationOptions(**options)
  File "/Users/zhangxin/anaconda2/lib/python2.7/site-packages/Cython/Compiler/Main.py", line 559, in __init__
    raise ValueError(message)
ValueError: got unknown compilation option, please remove: include_dirs
```