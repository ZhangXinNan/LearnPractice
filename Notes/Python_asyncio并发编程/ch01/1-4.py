
import os
import multiprocessing


def hello_from_process():
    print("Hello from child process {}".format(os.getpid()))


if __name__ == '__main__':
    hello_process = multiprocessing.Process(target=hello_from_process)
    hello_process.start()
    print("Hello from parent process {}".format(os.getpid()))
    hello_process.join()
