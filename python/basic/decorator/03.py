import logging

def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args, **kwargs)
        return wrapper

    return decorator

# @use_logging(level="warn")等价于@decorator
@use_logging(level="warn")
def foo(name, age=None, height=None):
    print("I am %s, age %s, height %s" % (name, age, height))

foo('zhangxin', 33, 171.5)