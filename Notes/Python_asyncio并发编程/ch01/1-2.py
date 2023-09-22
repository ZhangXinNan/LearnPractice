# 1-4-2

import os
import threading

# 进程ID
print(f'Python process running with process id : {os.getpid()}')

# 正在进行的线程活动计数
total_threads = threading.active_count()
print("Python is currently running {} thread(s)".format(total_threads))

# 当前线程名称
thread_name = threading.current_thread().name
print("The current thread is {}".format(thread_name))


