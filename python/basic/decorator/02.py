
import logging

def use_logging(func):
    
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper

# 有了@，可以省去foo = use_logging(foo)这句。
@use_logging
def foo():
    print("i am foo")

foo()