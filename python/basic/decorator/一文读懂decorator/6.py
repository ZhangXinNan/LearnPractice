from functools import wraps


#类的装饰器写法， 不带参数
class Hint(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('{} is running'.format(self.func.__name__))
        return self.func(*args, **kwargs)


#类的装饰器写法， 带参数
class Hint(object):
    def __init__(self, coder=None):
        self.coder = coder

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('{} is running'.format(func.__name__))
            print('Coder: {}'.format(self.coder))
            return func(*args, **kwargs)     # 正式调用主要处理函数
        return wrapper
