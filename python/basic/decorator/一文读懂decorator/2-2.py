def outer(x):
    a = x

    def inner(y):
        b = y
        print(a+b)

    return inner

f1 = outer(1) # 返回inner函数对象
f1(10) # 相当于inner(10)。输出11
