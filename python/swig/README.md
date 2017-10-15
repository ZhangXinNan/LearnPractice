## 建立Python模块

转换编码C成Python模块很简单，只需要按如下做即可（请见其他操作系统的SWIG共享库帮助手册）:
```
swig -python example.i
gcc -c example.c example_wrap.c \
        -I/usr/include/python2.7/
ld -shared example.o example_wrap.o -o _example.so
```
我们现在可以使用如下Python模块 :
```
 >>> import example
 >>> example.fact(5)
 120
 >>> example.my_mod(7,3)
 1
 >>> example.get_time()
 'Sun Feb 11 23:01:07 1996'
 >>>
```