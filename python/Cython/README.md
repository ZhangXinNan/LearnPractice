# 1 基础教程
## 1.1 Cython的基础
Cython是包含C数据类型的Python。
Cython的编译器会转化Python代码为C代码，这些C代码可以调用Python/C的API。
Cython中的参数和变量还可以从C数据类型来声明。


## 1.2 Cython的Hello World

1. 新建文件helloworld.pyx

2. 创建 setup.py

3. 构建
```
python setup.py build_ext --inplace
```
运行后会得到 helloworld.so。（Windows得到helloworld.pyd）

4. 打开Python的解释器
```
➜  Cython git:(master) ✗ python 
Python 2.7.14 |Anaconda custom (64-bit)| (default, Dec  7 2017, 11:07:58) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import helloworld
Hello World
```


## 1.3 pyximport Cython简单编译

## 1.4 Fibonacci 函数

## 1.5 质数 Primes
cdef 来定义 C 语言的局部变量
