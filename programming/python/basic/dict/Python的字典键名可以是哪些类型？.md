

今天看别人代码时发现一个事，就是把对象当作字典的键名，并且把两个对象（类的实例）当作键名，然后去查了下：

> 键必须是不可变的，如字符串，数字或元组。


# 1 键的类型，列表/字典不可以，~~其它都可以~~ 
但是网上却没有说其他类型可不可以，怎么用的。我写代码试了下：
```python
class Person:
    def __init__(self, name):
        self.name = name


i = 5
s = 'abc'
t = (5,'a')
p = Person('Lily')
q = Person('xiao')
m = {'a':1, 'b':10}
lst = [1,2,3]

d = {}
d[i] = 'five'
d[s] = 'ABC'
d[t] = 'five-a'
d[p] = 'name:Lily'
# d[lst] = 'list : 1,2,3'
# TypeError: unhashable type: 'list'
d[p, q] = 'two people: Lily and xiao'
d[i,s,t,p,q] = 'all in key'

for k, v in d.items():
    print(k, '=>', v)

```


输出结果：
```
5 => five
abc => ABC
(5, 'a') => five-a
<__main__.Person object at 0x000001803EEF27F0> => name:Lily
(<__main__.Person object at 0x000001803EEF27F0>, <__main__.Person object at 0x000001803EEF28D0>) => two people: Lily and xiao
(5, 'abc', (5, 'a'), <__main__.Person object at 0x000001803EEF27F0>, <__main__.Person object at 0x000001803EEF28D0>) => all in key
```

# 2 多个对象可当作键名，顺序不同时是不同的键
```
print(d[p, q])
print(d[q, p])
```

### 输出：
```
two people: Lily and xiao
Traceback (most recent call last):

  File "<ipython-input-15-12aff481ab93>", line 1, in <module>
    runfile('C:/Users/Xpeng/.spyder-py3/temp.py', wdir='C:/Users/Xpeng/.spyder-py3')

  File "D:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_64\lib\site-packages\spyder\utils\site\sitecustomize.py", line 705, in runfile
    execfile(filename, namespace)

  File "D:\Program Files (x86)\Microsoft Visual Studio\Shared\Anaconda3_64\lib\site-packages\spyder\utils\site\sitecustomize.py", line 102, in execfile
    exec(compile(f.read(), filename, 'exec'), namespace)

  File "C:/Users/Xpeng/.spyder-py3/temp.py", line 37, in <module>
    print(d[q, p])

KeyError: (<__main__.Person object at 0x000001803EF58940>, <__main__.Person object at 0x000001803EF58668>)
```

# 3 结论【有误】：
（1）**除了列表不能当作键名，其它都 可以，还可以放多个**。
（2）我是这样理解的，列表是可变的，其他类型都是不可变的。对象作为键名时，实际传入的是对象的地址，也是不可变的。
（3）放多个时不同顺序时键不同。

------2020.04.07更新-----
感谢两次网友的提醒。
（1）**准确的说是列表、字典这种不可哈希（unhashable）的类型不可当做键值，可哈希的类型才可当作键。**
