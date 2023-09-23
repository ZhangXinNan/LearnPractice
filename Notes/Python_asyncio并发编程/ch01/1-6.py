import threading
import time


def print_fib(number: int) -> None:
    def fib(n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    print("fib({}) is {}".format(number, fib(number)))


def fibs_with_threading():
    forieth_thread = threading.Thread(target=print_fib(40))
    forty_first_thread = threading.Thread(target=print_fib(41))
    forieth_thread.start()
    forty_first_thread.start()
    forieth_thread.join()
    forty_first_thread.join()


start = time.time()
fibs_with_threading()
end = time.time()

print("completed in {:.4f} seconds".format(end - start))
