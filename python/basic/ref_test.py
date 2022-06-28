

a = [1, 2, 3]
b = [11, 22, 33]
c = [100, 200, 300]

def fun1(a):
    print("a : {}, id(a): {}".format(a, id(a)))
    a = a + [5]
    print("a : {}, id(a): {}".format(a, id(a)))

def fun2(a):
    print("a : {}, id(a): {}".format(a, id(a)))
    a += [5]
    print("a : {}, id(a): {}".format(a, id(a)))

def fun3(a):
    print("a : {}, id(a): {}".format(a, id(a)))
    a.append(55)
    print("a : {}, id(a): {}".format(a, id(a)))

fun1(a)
print(a)
fun2(b)
print(b)
fun3(c)
print(c)


'''
[1, 2, 3]
[11, 22, 33, 5]
[100, 200, 300, 55]
'''

aa = a
a.append(aa) 
print(a)
print(aa)
print(a[-1])
'''
[1, 2, 3, [...]]
[1, 2, 3, [...]]
[1, 2, 3, [...]]

'''
