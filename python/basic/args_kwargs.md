
*args 和 **kwargs 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。
这里的不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。

# *args 
用来发送一个非键值对的可变数量的参数列表给一个函数.

```
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```
这会产生如下输出:
```
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

## **kwargs 
允许你将不定长度的键值对, 作为参数传递给一个函数。 如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。
```
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


>>> greet_me(name="yasoob")
name == yasoob
```

# 使用 *args 和 **kwargs 来调用函数
```
# 首先使用 *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# 现在使用 **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```

# 标准参数与*args、**kwargs在使用时的顺序
那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
```
some_func(fargs, *args, **kwargs)
```

# 参考资料：
[*args 和 **kwargs](https://eastlakeside.gitbooks.io/interpy-zh/content/args_kwargs/)