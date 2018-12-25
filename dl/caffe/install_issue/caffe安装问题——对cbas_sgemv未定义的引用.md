## 问题
```
CXX/LD -o .build_release/tools/caffe.bin
.build_release/lib/libcaffe.so：对‘cblas_sgemv’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_dgemm’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_sscal’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_dgemv’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_dasum’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_dscal’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_scopy’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_daxpy’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_dcopy’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_saxpy’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_ddot’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_sgemm’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_sasum’未定义的引用
.build_release/lib/libcaffe.so：对‘cblas_sdot’未定义的引用
collect2: error: ld returned 1 exit status
Makefile:635: recipe for target '.build_release/tools/caffe.bin' failed
make: *** [.build_release/tools/caffe.bin] Error 1

```


## 解决方法：
原因说起来搞笑
```
BLAS := open
BLAS_INCLUDE := /usr/include/openblas
BLAS_LIB := /usr/lib
```
问题在于我open后面多了个空格，去掉就可以了
