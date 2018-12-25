

# SWIG和SIP
都定义了一种接口描述语言。先写一个接口描述文件，用于描述我要导出的C++函数和类，然后通过一个翻译器，将接口描述文件翻译成C++程序。最后编译连接生成的C++程序 来生成扩展库。

## SWIG
适合包装C程序。

# Boost.Python
用于导出C++函数和类的时候，需要添加的也是C++的代码。

缺点：
使用了大量的模板技巧，导出元素多时，编译较慢 。


# 参考
[用 Boost.Python 写扩展库(1 简介)](https://blog.csdn.net/bz201/article/details/523624)

[Boost.Python](https://www.boost.org/doc/libs/1_61_0/libs/python/doc/html/index.html)