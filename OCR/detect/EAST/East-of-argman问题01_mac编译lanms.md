
# 1 问题

```bash
(py36_tf) ➜  EAST git:(zxdev) ✗ python eval.py \      
        --test_data_path=/Users/zhangxin/data_md/crop \
        --gpu_list=0 \
        --checkpoint_path=models/east_icdar2015_resnet_v1_50_rbox/ \
        --output_dir=tmp/
find: -xtype: unknown primary or operator
c++ -o adaptor.so -I include  -std=c++11 -O3 -I/Users/zhangxin/anaconda3/envs/py36_tf/include/python3.6m -I/Users/zhangxin/anaconda3/envs/py36_tf/include/python3.6m -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/zhangxin/anaconda3/envs/py36_tf/include -arch x86_64 -I/Users/zhangxin/anaconda3/envs/py36_tf/include -arch x86_64 -L/Users/zhangxin/anaconda3/envs/py36_tf/lib/python3.6/config-3.6m-darwin -lpython3.6m -ldl -framework CoreFoundation -Wl,-stack_size,1000000 -framework CoreFoundation adaptor.cpp include/clipper/clipper.cpp --shared -fPIC
adaptor.cpp:53:1: warning: 'pybind11_init' is deprecated: PYBIND11_PLUGIN is deprecated, use PYBIND11_MODULE [-Wdeprecated-declarations]
PYBIND11_PLUGIN(adaptor) {
^
include/pybind11/common.h:232:20: note: expanded from macro 'PYBIND11_PLUGIN'
            return pybind11_init();                                            \
                   ^
adaptor.cpp:53:1: note: 'pybind11_init' has been explicitly marked deprecated here
include/pybind11/common.h:216:5: note: expanded from macro 'PYBIND11_PLUGIN'
    PYBIND11_DEPRECATED("PYBIND11_PLUGIN is deprecated, use PYBIND11_MODULE")  \
    ^
include/pybind11/common.h:80:54: note: expanded from macro 'PYBIND11_DEPRECATED'
#  define PYBIND11_DEPRECATED(reason) __attribute__((deprecated(reason)))
                                                     ^
1 warning generated.
include/clipper/clipper.cpp:3665:13: warning: unused variable 'firstLeft' [-Wunused-variable]
    OutRec* firstLeft = ParseFirstLeft(outRec->FirstLeft);
            ^
1 warning generated.
ld: -stack_size option can only be used when linking a main executable
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make: *** [adaptor.so] Error 1
Traceback (most recent call last):
  File "eval.py", line 9, in <module>
    import lanms
  File "/Users/zhangxin/github/EAST/lanms/__init__.py", line 8, in <module>
    raise RuntimeError('Cannot compile lanms: {}'.format(BASE_DIR))
RuntimeError: Cannot compile lanms: /Users/zhangxin/github/EAST/lanms
```


# 2 解决
通过
```bash
python3-config --ldflags
```
打印出结果，然后将结果删掉不用的部分-Wl,-stack_size,1000000
，然后手工填入LDFLAGS。
```bash
# LDFLAGS = $(shell python3-config --ldflags)
LDFLAGS = -L/Users/zhangxin/anaconda3/envs/py36_tf/lib/python3.6/config-3.6m-darwin -lpython3.6m -ldl -framework CoreFoundation -framework CoreFoundation
```

# 3 参考
* [pyenv: compiling a module](https://stackoverflow.com/questions/54114773/pyenv-compiling-a-module)
* [installed on Mac but failed to compile the lanms #174](https://github.com/argman/EAST/issues/174)