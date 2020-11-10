from decorator import decorator

@decorator
def hint(func, *args, **kwargs):
    print('{} is running'.format(func.__name__))
    return func(*args, **kwargs)

@hint
def hello():
    print("Hello!")


hello()
print(hello.__name__)