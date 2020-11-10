一文看懂Python系列之装饰器(decorator)(工作面试必读)


Python的装饰器(decorator)可以说是Python的一个神器，它可以在不改变一个函数代码和调用方式的情况下给函数添加新的功能。Python的装饰器同时也是Python学习从入门到精通过程中必需要熟练掌握的知识。小编我当初学习Python时差点被装饰器搞晕掉，今天尝试用浅显的语言解释下Python装饰器的工作原理及如何编写自己的装饰器吧。



# 1 Python装饰器的本质

Python的装饰器本质上是一个嵌套函数，它接受被装饰的函数(func)作为参数，并返回一个包装过的函数。这样我们可以在不改变被装饰函数的代码的情况下给被装饰函数或程序添加新的功能。Python的装饰器广泛应用于缓存、权限校验(如django中的@login_required和@permission_required装饰器)、性能测试(比如统计一段程序的运行时间)和插入日志等应用场景。有了装饰器，我们就可以抽离出大量与函数功能本身无关的代码，增加一个函数的重用性。



试想你写了很多程序，一直运行也没啥问题。有一天老板突然让你统计每个程序都运行了多长时间并比较下运行效率。此时如果你去手动修改每个程序的代码一定会让你抓狂，而且还破坏了那些程序的重用性。聪明的程序员是绝不能干这种蠢事的。此时你可以编写一个@time_it的装饰器(代码如下所示)。如果你想打印出某个函数或程序运行时间，只需在函数前面@一下，是不是很帅?
```python
import time

def time_it(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('用时:{}秒'.format(end-start))
    return inner

@time_it
def func1():
    time.sleep(2)
    print("Func1 is running.")

if __name__ == '__main__':
    func1()
```
运行结果如下:
```bash
Func1 is running.

用时:2.0056326389312744
```


由于Python装饰器的工作原理主要依赖于嵌套函数和闭包，所以我们必须先对嵌套函数和闭包有深入的了解。嵌套函数和闭包几乎是Python工作面试必考题哦。



# 2 嵌套函数

如果在一个函数的内部还定义了另一个函数(注意: 是定义，不是引用!），这个函数就叫嵌套函数。外部的我们叫它外函数，内部的我们叫他内函数。



我们先来看一个最简单的嵌套函数的例子。我们在outer函数里又定义了一个inner函数，并调用了它。你注意到了吗? 内函数在自己作用域内查找局部变量失败后，会进一步向上一层作用域里查找。
```python
def outer():
    x = 1
    def inner():
        y = x + 1
        print(y)
    inner()

outer() #输出结果 2
```
如果我们在外函数里不直接调用内函数，而是通过return inner返回一个内函数的引用 这时会发生什么呢? 你将会得到一个内函数对象，而不是运行结果。
```python
def outer():
    x = 1
    def inner():
        y = x + 1
        print(y)
    return inner

outer() # 输出<function outer.<locals>.inner at 0x039248E8>
f1 = outer()
f1() # 输出2
```
上述这个案例比较简单，因为outer和inner函数都是没有参数的。我们现在对上述代码做点改动，加入参数。你可以看到外函数的参数或变量可以很容易传递到内函数。

```python
def outer(x):
    a = x

    def inner(y):
        b = y
        print(a+b)

    return inner

f1 = outer(1) # 返回inner函数对象
f1(10) # 相当于inner(10)。输出11
```
如果上例中外函数的变量x换成被装饰函数对象(func)，内函数的变量y换成被装饰函数的参数，我们就可以得到一个通用的装饰器啦(如下所示)。你注意到了吗? 我们在没对func本身做任何修改的情况下，添加了其它功能, 从而实现了对函数的装饰。

```python
def decorator(func):
    def inner(*args, **kwargs):
        add_other_actions()
        return func(*args, **kwargs)
    return inner
```
请你仔细再读读上面这段代码，我们的decorator返回的仅仅是inner函数吗? 答案是不。它返回的其实是个闭包(Closure)。整个装饰器的工作都依赖于Python的闭包原理。



# 3 闭包(Closure)

闭包是Python编程一个非常重要的概念。如果一个外函数中定义了一个内函数，且内函数体内引用到了体外的变量，这时外函数通过return返回内函数的引用时，会把定义时涉及到的外部引用变量和内函数打包成一个整体（闭包）返回。我们在看下之间案例。我们的outer方法返回的只是内函数对象吗? 错。我们的outer函数返回的实际上是一个由inner函数和外部引用变量(a)组成的闭包!

```python
def outer(x):
    a = x

    def inner(y):
        b = y
        print(a+b)

    return inner


f1 = outer(1) # 返回inner函数对象+局部变量1(闭包)
f1(10) # 相当于inner(10)。输出11
```
一般一个函数运行结束的时候，临时变量会被销毁。但是闭包是一个特别的情况。当外函数发现，自己的临时变量会在将来的内函数中用到，自己在结束的时候，返回内函数的同时，会把外函数的临时变量同内函数绑定在一起。这样即使外函数已经结束了，内函数仍然能够使用外函数的临时变量。这就是闭包的强大之处。



# 4 如何编写一个通用的装饰器

我们现在可以开始动手写个名为hint的装饰器了，其作用是在某个函数运行前给我们提示。这里外函数以hint命名，内函数以常用的wrapper(包裹函数)命名。
```python
def hint(func):
    def wrapper(*args, **kwargs):
        print('{} is running'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@hint
def hello():
    print("Hello!")
```
我们现在对hello已经进行了装饰，当我们调用hello()时，我们可以看到如下结果。
```bash
>>> hello()
hello is running.
Hello!
```
值得一提的是被装饰器装饰过的函数看上去名字没变，其实已经变了。当你运行hello()后，你会发现它的名字已经悄悄变成了wrapper，这显然不是我们想要的(如下图所示)。这一点也不奇怪，因为外函数返回的是由wrapper函数和其外部引用变量组成的闭包。
```bash
>>> hello.__name__
'wrapper'
```
为了解决这个问题保证装饰过的函数__name__属性不变，我们可以使用functools模块里的wraps方法，先对func变量进行wraps。下面这段代码可以作为编写一个通用装饰器的示范代码，注意收藏哦。

```python
from functools import wraps

def hint(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('{} is running'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


@hint
def hello():
    print("Hello!")
```
恭喜你，你已经学会写一个比较通用的装饰器啦，并保证装饰过的函数__name__属性不变啦。当然使用嵌套函数也有缺点，比如不直观。这时你可以借助Python的decorator模块(需事先安装)可以简化装饰器的编写和使用。如下所示。
```python
from decorator import decorator

@decorator
def hint(func, *args, **kwargs):
    print('{} is running'.format(func.__name__))
    return func(*args, **kwargs)
```

# 5 编写带参数的高级装饰器

前面几个装饰器一般是内外两层嵌套函数。如果我们需要编写的装饰器本身是带参数的，我们需要编写三层的嵌套函数，其中最外一层用来传递装饰器的参数。现在我们要对@hint装饰器做点改进，使其能通过@hint(coder="John")传递参数。该装饰器在函数运行前给出提示的时候还显示函数编写人员的名字。完整代码如下所示:
```python
from functools import wraps


def hint(coder):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print('{} is running'.format(func.__name__))
            print('Coder: {}'.format(coder))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@hint(coder="John")
def hello():
    print("Hello!")
```
下面这段代码是一段经典的Python装饰器代码，显示了@cache这个装饰器怎么编写和工作的。它需要使用缓存实例做为一个参数，所以也是三层嵌套函数。
```python
import time
from functools import wraps


# 装饰器增加缓存功能
def cache(instance):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            # 构建key: key => func_name::args::kwargs
            joint_args = ','.join((str(x) for x in args))
            joint_kwargs = ','.join('{}={}'.format(k, v) for k, v in sorted(kwargs.items()))
            key = '{}::{}::{}'.format(func.__name__,joint_args, joint_kwargs)
            # 根据key获取结果。如果key已存在直接返回结果，不用重复计算。
         result = instance.get(key)
            if result is not None:
                return result
            # 如果结果不存在，重新计算，缓存。
         result = func(*args, **kwargs)
            instance.set(key, result)
            return result
        return inner_wrapper
    return wrapper


# 创建字典构造函数，用户缓存K/V键值对
class DictCache:
    def __init__(self):
        self.cache = dict()

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value

    def __str__(self):
        return str(self.cache)

    def __repr__(self):
        return repr(self.cache)


# 创建缓存对象
cache_instance = DictCache()


# Python语法糖调用装饰器
@cache(cache_instance)
def long_time_func(x):
    time.sleep(x)
    return x

# 调用装饰过函数
long_time_func(3)
```

# 6 基于类实现的装饰器
Python的装饰器不仅可以用嵌套函数来编写，还可以使用类来编写。其调用__init__方法创建实例，传递参数，并调用__call__方法实现对被装饰函数功能的添加。
```python
from functools import wraps


#类的装饰器写法， 不带参数
class Hint(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('{} is running'.format(self.func.__name__))
        return self.func(*args, **kwargs)


#类的装饰器写法， 带参数
class Hint(object):
    def __init__(self, coder=None):
        self.coder = coder

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('{} is running'.format(func.__name__))
            print('Coder: {}'.format(self.coder))
            return func(*args, **kwargs)     # 正式调用主要处理函数
        return wrapper
```

# 7 小结

本文总结了什么是Python的装饰器及其工作原理，并重点介绍了嵌套函数和闭包原理。最后详细展示了如何编写一个通用装饰器及带参数的高级装饰器, 包括使用类来编写装饰器。大家要熟练掌握哦。看不懂的可以先加入微信收藏以后再反复阅读。



大江狗

2018.11.29



参考资料

https://www.cnblogs.com/Lin-Yi/p/7305364.html

http://python.jobbole.com/81683/

http://lib.csdn.net/article/python/62942

http://lib.csdn.net/article/python/64769

http://www.cnblogs.com/cicaday/p/python-decorator.html

