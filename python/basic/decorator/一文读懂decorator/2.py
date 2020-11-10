

def outer():
    x = 1
    def inner():
        y = x + 1
        print(y)
    inner()

outer() #输出结果 2


