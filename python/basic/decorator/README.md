[理解 Python 装饰器看这一篇就够了](https://foofish.net/python-decorator.html)
[廖雪峰——python2.7教程-装饰器](https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000)
装饰器本身是一个python函数或类，可以让其他函数或者类不改任何代码的前提下增加额外功能。


# 简单装饰器
```python
#encoding=utf8
import logging

def use_logging(func):
    
    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()
```
use_logging 就是一个装饰器，它一个普通的函数，它把执行真正业务逻辑的函数 func 包裹在其中，看起来像 foo 被 use_logging 装饰了一样，use_logging 返回的也是一个函数，这个函数的名字叫 wrapper。在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。




# @语法糖
```python
import logging

def use_logging(func):
    
    def wrapper():
        logging.warn("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging
def foo():
    print("i am foo")

foo()
```

如上所示，有了 @ ，我们就可以省去foo = use_logging(foo)这一句了，直接调用 foo() 即可得到想要的结果。你们看到了没有，foo() 函数不需要做任何修改，只需在定义的地方加上装饰器，调用的时候还是和以前一样，如果我们有其他的类似函数，我们可以继续调用装饰器来修饰函数，而不用重复修改函数或者增加新的封装。这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。

装饰器在 Python 使用如此方便都要归因于 Python 的函数能像普通的对象一样能作为参数传递给其他函数，可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。


# *args、**kwargs


# 带参数的装饰器


# 类装饰器
没错，装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。


# functools.wraps

# 装饰器顺序
一个函数还可以同时定义多个装饰器
```python
@a
@b
@c
def f ():
    pass
```
它的执行顺序是从里到外，最先调用最里层的装饰器，最后调用最外层的装饰器，它等效于

f = a(b(c(f)))