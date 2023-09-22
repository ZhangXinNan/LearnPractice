import time
import threading


def hello_from_thread():
    # 输出当前线程的名称
    print("hello from thread {} !".format(threading.current_thread()))
    time.sleep(10)


# 创建新的线程来运行上边的函数
hello_thread = threading.Thread(target=hello_from_thread)
# 调用线程的start方法来启动
hello_thread.start()

# 正在进行的线程活动计数
total_threads = threading.active_count()
print("Python is currently running {} thread(s)".format(total_threads))

# 当前线程名称
thread_name = threading.current_thread().name
print("The current thread is {}".format(thread_name))

print(time.time())
# 让程序暂停，直到启动的线程完成
hello_thread.join()
print(time.time())


# 正在进行的线程活动计数
total_threads = threading.active_count()
print("Python is currently running {} thread(s)".format(total_threads))

