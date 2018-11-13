# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

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



print(d[p, q])
print(d[q, p])