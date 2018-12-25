## 问题
```
NVCC src/caffe/layers/absval_layer.cu
nvcc fatal   : Unsupported gpu architecture 'compute_20'
Makefile:604: recipe for target '.build_release/cuda/src/caffe/layers/absval_layer.o' failed
make: *** [.build_release/cuda/src/caffe/layers/absval_layer.o] Error 1

```


## 解决方法
去掉这两行：
```
-gencode arch=compute_20,code=sm_20 \
-gencode arch=compute_20,code=sm_21 \
```
