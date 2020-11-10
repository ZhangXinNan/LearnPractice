from functools import wraps


def hint(coder):
    def wrapper(func):
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            print('{} is running'.format(func.__name__))
            print('Coder: {}'.format(coder))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper


@hint(coder="John")
def hello():
    print("Hello!")

hello()
print(hello.__name__)