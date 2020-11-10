import time

def time_it(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('用时:{}秒'.format(end-start))
    return inner

@time_it
def func1():
    time.sleep(2)
    print("Func1 is running.")

if __name__ == '__main__':
    func1()