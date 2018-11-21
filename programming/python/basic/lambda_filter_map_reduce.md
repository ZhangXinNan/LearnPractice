[python之lambda、filter、map、reduce的用法说明](https://www.cnblogs.com/yufeihlf/p/6179982.html)

```
#coding=utf-8
'''
Created on 2016-12-14
@author: Jennifer
项目：Python中filter、map、reduce、lambda 的用法
'''
#1.lambda用法，冒号之前的是入参，冒号之后的是表达式，返回的值，最简单的函数
print [(lambda x:x*x)(x)for x in range(11)]
#结果：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print (lambda x:x*x)(3)
#结果：9
g=lambda x:x*x
print g(4)
#结果：16

#2.filter用法:返回执行结果为TRUE的入参（入参是列表字符元组）
print filter(lambda x:x*x-4,range(10))
#结果：[0, 1, 3, 4, 5, 6, 7, 8, 9]

#3.map的用法：对列表入参依次执行函数。入参为列表，有多少个列表，就应该有多少个入参。
print map(lambda x:x*x-4,range(10))
#结果：[-4, -3, 0, 5, 12, 21, 32, 45, 60, 77]
print map(lambda x,y:x*y-4,range(3),[8,9,10])
#结果：[-4, 5, 16]

#4.reduce用法：先把sequence中第一个值和第二个值当参数传给function，再把function的返回值和第三个值当参数传给fuction,最终返回一个结果值
#接收的入参个数只能为2
print reduce(lambda x,y:x*y-4,range(4))
#结果：-40
#计算0到100的和
print reduce(lambda x,y:x+y, range(101))
#结果：5050
print reduce(lambda x,y:x+y, range(101),100)
#结果：5150
```