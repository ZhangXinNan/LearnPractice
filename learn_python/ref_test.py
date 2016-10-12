

a = [1, 2, 3]
b = [11, 22, 33]
c = [100, 200, 300]

def fun1(a):
    a = a + [5]
def fun2(a):
    a += [5]
def fun3(a):
    a.append(55)
fun1(a)
fun2(b)
fun3(c)
print a
print b
print c
'''
[1, 2, 3]
[11, 22, 33, 5]
[100, 200, 300, 55]

'''
aa = a
a.append(aa) 
print a
print aa
print a[-1]
'''
[1, 2, 3, [...]]
[1, 2, 3, [...]]
[1, 2, 3, [...]]

'''
