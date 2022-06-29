

# 1 定义一个java类


编译生成Hello.class
```bash
javac Hello.java
```



# 2 生成本地链接库
```bash
javah Hello
```
生成Hello.h后，创建一个Hello.cpp



# 3 编译生成共享库


```bash
# -c                       Compile and assemble, but do not link
# -fPIC  作用于编译阶段，告诉编译器产生与位置无关代码(Position-Independent Code)，
#        则产生的代码中，没有绝对地址，全部使用相对地址，故而代码可以被加载器加载到内存的任意
#        位置，都可以正确的执行。这正是共享库所要求的，共享库被加载时，在内存的位置不是固定的。
g++ -I/home/zhangxin/Android/Sdk/ndk-bundle/sysroot/usr/include/ -c -fPIC Hello.cpp
```

```bash
g++ -shared -Wl,-soname,libhello.so.1 -o libhello.so.1.0 Hello.o
cp libhello.so.1.0 libhello.so

g++ -shared -Wl,-soname,libhello.so -o libhello.so Hello.o
```

# 4 测试
```bash
javac ToSay.java
java ToSay
```




# 参考
* [gcc编译参数-fPIC的一些问题](http://blog.sina.com.cn/s/blog_54f82cc201011op1.html)
* [Android：JNI 与 NDK到底是什么？（含实例教学）](https://blog.csdn.net/carson_ho/article/details/73250163)