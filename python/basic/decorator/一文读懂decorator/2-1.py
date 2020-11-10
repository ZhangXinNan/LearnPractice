def outer():
    x = 1
    def inner():
        y = x + 1
        print(y)
    return inner

outer() # 输出<function outer.<locals>.inner at 0x039248E8>
f1 = outer()
f1() # 输出2