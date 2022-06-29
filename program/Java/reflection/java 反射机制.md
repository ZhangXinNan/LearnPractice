

反射机制 Reflection 入门
____________________

# 1
* ClassLoader
* Class

## 1.1 程序运行过程：
1. ClassLoad将xxx.class  Load 到其内存中CodeSegment
2. 运行环境找到main方法开始执行
3. 运行过程中会有更多的class被load到内存。

## 1.2 ClassLoader的类加载机制
* 并非一次性加载，需要的时候加载（运行期间动态加载）
* 例：
（1）TestDynamicLoading.java -verbose:class 可以观察类的具体载过程。Run Configurations -->> Arguments -->> VM arguments , 添加-verbose:class。
```
[Loaded A from file:/D:/gitlab/documents/Java/reflection/ReflectionTest/bin/]
**---------------------------**
[Loaded B from file:/D:/gitlab/documents/Java/reflection/ReflectionTest/bin/]
[Loaded C from file:/D:/gitlab/documents/Java/reflection/ReflectionTest/bin/]
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCc
[Loaded D from file:/D:/gitlab/documents/Java/reflection/ReflectionTest/bin/]
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
```

* static语句块在加载后执行一次
* dynamic语句块每次new新的对象都会执行
（1）等同于构造方法中语句
（2）用的较少


## 1.3 JDK内置 ClassLoader
1. bootstrap class loader
最顶层的 class loader。专门管理一些核心类。
不能动。
* implemented by native language
* load core classes of jdk

2. extesion class loader
* loader the class from jre/lib/ext

3. application class loader
* load user-define classes
* ClassLoader.getSystemClassLoader()

4. other class loaders
* SecureClassLoader
* URLClassLoader

## 1.4 JDK Class Loader 的层次关系（不是继承）
classloader在load class的时候首先找上一层loader是不是load过了。如果已经load了，就不会再次load。

安全性好，自己写的String.class永远没有机会执行。


ClassLoader.getParent() 

# 2 反射机制
站在ClassLoader的角度看CodeSegment
一个一个的Class对象。
java.lang.Class
* 代表了Load到内存中的Class对象
* Object的getClass()可以拿 到该类对象（等同于类名.class)
* Class的getClassLoader可以拿到装载这个class的ClassLoader



