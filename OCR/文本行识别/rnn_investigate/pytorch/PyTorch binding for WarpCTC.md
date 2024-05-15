# seele
## 问题1
```
zhangxin@seele:~/github/torch/warp-ctc/build$ make
[ 14%] Linking CXX shared library libwarpctc.so
[ 42%] Built target warpctc
[ 57%] Linking CXX executable test_cpu
[ 71%] Built target test_cpu
[ 85%] Linking CXX executable test_gpu
/usr/bin/ld: /usr/local/cuda-8.0/lib64/libcudart_static.a(libcudart_static.a.o): undefined reference to symbol 'shm_unlink@@GLIBC_2.2.5'
//lib/x86_64-linux-gnu/librt.so.1: error adding symbols: DSO missing from command line
collect2: error: ld returned 1 exit status
make[2]: *** [test_gpu] 错误 1
make[1]: *** [CMakeFiles/test_gpu.dir/all] 错误 2
make: *** [all] 错误 2
```

# mac
[pytorch bindings](https://github.com/SeanNaren/warp-ctc/tree/pytorch_bindings/pytorch_binding)

## error: invalid argument '-std=c++11' not allowed with 'C/ObjC'
```
pytorch_binding git:(zxdev_pytorch) python setup.py install
CUDA_HOME not found in the environment so building without GPU support. To build with GPU support please define the CUDA_HOME environment variable. This should be a path which contains include/cuda.h
generating build/_warp_ctc.c
regenerated: 'build/_warp_ctc.c'
running install
running build
running build_py
creating build/lib.macosx-10.11-x86_64-2.7
creating build/lib.macosx-10.11-x86_64-2.7/warpctc_pytorch
copying warpctc_pytorch/__init__.py -> build/lib.macosx-10.11-x86_64-2.7/warpctc_pytorch
running build_ext
building 'warpctc_pytorch._warp_ctc' extension
creating build/temp.macosx-10.11-x86_64-2.7
creating build/temp.macosx-10.11-x86_64-2.7/build
creating build/temp.macosx-10.11-x86_64-2.7/Users
creating build/temp.macosx-10.11-x86_64-2.7/Users/zhangxin
creating build/temp.macosx-10.11-x86_64-2.7/Users/zhangxin/github
creating build/temp.macosx-10.11-x86_64-2.7/Users/zhangxin/github/warp-ctc
creating build/temp.macosx-10.11-x86_64-2.7/Users/zhangxin/github/warp-ctc/pytorch_binding
creating build/temp.macosx-10.11-x86_64-2.7/Users/zhangxin/github/warp-ctc/pytorch_binding/src
clang -fno-strict-aliasing -fno-common -dynamic -g -O2 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/usr/local/lib/python2.7/site-packages/torch/utils/ffi/../../lib/include -I/usr/local/lib/python2.7/site-packages/torch/utils/ffi/../../lib/include/TH -I/Users/zhangxin/github/warp-ctc/include -I/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/include/python2.7 -c build/_warp_ctc.c -o build/temp.macosx-10.11-x86_64-2.7/build/_warp_ctc.o -std=c++11 -fPIC
error: invalid argument '-std=c++11' not allowed with 'C/ObjC'
error: command 'clang' failed with exit status 1
```
解决方法：去掉-std=c++11后编译没报错

```
➜  tests git:(zxdev_pytorch) ✗ python test.py 
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    from warpctc_pytorch import CTCLoss
  File "/usr/local/lib/python2.7/site-packages/warpctc_pytorch/__init__.py", line 7, in <module>
    from ._warp_ctc import lib as _lib, ffi as _ffi
ImportError: dlopen(/usr/local/lib/python2.7/site-packages/warpctc_pytorch/_warp_ctc.so, 2): Library not loaded: @rpath/libwarpctc.dylib
  Referenced from: /usr/local/lib/python2.7/site-packages/warpctc_pytorch/_warp_ctc.so
  Reason: image not found
```


# mac virutalenv
## ImportError: torch.utils.ffi requires the cffi package
```
(venv_pytorch) ➜  pytorch_binding git:(zxdev_pytorch) ✗ python setup.py install
Traceback (most recent call last):
  File "setup.py", line 7, in <module>
    from torch.utils.ffi import create_extension
  File "/Users/zhangxin/tools/venv_pytorch/lib/python2.7/site-packages/torch/utils/ffi/__init__.py", line 14, in <module>
    raise ImportError("torch.utils.ffi requires the cffi package")
ImportError: torch.utils.ffi requires the cffi package
```
解决方法：
```
pip install cffi
```

# docker 容器
## ImportError: libwarpctc.so
```
root@a38c0b8807a0:/data/crnn.pytorch-master# python crnn_main.py --trainroot /data/lmdb/plate --valroot /data/lmdb/plate_test/
Traceback (most recent call last):
  File "crnn_main.py", line 10, in <module>
    from warpctc_pytorch import CTCLoss
  File "/usr/local/lib/python2.7/dist-packages/warpctc_pytorch/__init__.py", line 7, in <module>
    from ._warp_ctc import lib as _lib, ffi as _ffi
ImportError: libwarpctc.so: cannot open shared object file: No such file or directory
```

解决方法：
```
export LD_LIBRARY_PATH=/usr/local/lib:/usr/lib:$LD_LIBRARY_PATH
```

# version `GOMP_4.0' not found
```
root@a38c0b8807a0:/data/crnn.pytorch-master# python crnn_main.py --trainroot /data/lmdb/plate --valroot /data/lmdb/plate_test/
Traceback (most recent call last):
  File "crnn_main.py", line 10, in <module>
    from warpctc_pytorch import CTCLoss
  File "/usr/local/lib/python2.7/dist-packages/warpctc_pytorch/__init__.py", line 7, in <module>
    from ._warp_ctc import lib as _lib, ffi as _ffi
ImportError: /usr/local/lib/python2.7/dist-packages/torch/lib/libgomp.so.1: version `GOMP_4.0' not found (required by /data/warp-ctc-pytorch_bindings/build/libwarpctc.so)
```
解决方法：
```
 mv /usr/local/lib/python2.7/dist-packages/torch/lib/libgomp.so.1 /usr/local/lib/python2.7/dist-packages/torch/lib/libgomp.so.1.bak
```

# 143 virtualenv
```
(venv_pytorch)[zhangxin0627@l22-240-143 pytorch_binding]$ python setup.py install
ImportError: numpy.core.multiarray failed to import
Traceback (most recent call last):
  File "setup.py", line 7, in <module>
    from torch.utils.ffi import create_extension
  File "/data/home/zhangxin0627/venv_pytorch/lib/python2.7/site-packages/torch/__init__.py", line 53, in <module>
    from torch._C import *
ImportError: numpy.core.multiarray failed to import
You have mail in /var/spool/mail/root
```
解决方法：
```
pip install numpy
```

# 142 conda
```
[zhangxin0627@l22-240-142 build]$ ./test_cpu
./test_cpu: error while loading shared libraries: libwarpctc.so: cannot open shared object file: No such file or directory
```
解决方法：在环境变量里添加
```
WARP_CTC_PATH=/data/zhangxin/github/warp-ctc/build
export WARP_CTC_PATH
export LD_LIBRARY_PATH=$WARP_CTC_PATH:$LD_LIBRARY_PATH
```