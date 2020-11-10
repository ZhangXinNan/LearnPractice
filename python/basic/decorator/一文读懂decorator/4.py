def hint(func):
    def wrapper(*args, **kwargs):
        print('{} is running'.format(func.__name__))
        return func(*args, **kwargs)
    return wrapper

@hint
def hello():
    print("Hello!")

hello()
print(hello.__name__)