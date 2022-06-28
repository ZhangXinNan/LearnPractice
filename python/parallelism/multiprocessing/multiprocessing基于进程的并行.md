
multiprocessing ——基于进程的并行
________

# 0 概述

multiprocessing 是一个用于产生进程的包，具有与 threading 模块相似API。 multiprocessing 包同时提供本地和远程并发，使用子进程代替线程，有效避免 Global Interpreter Lock 带来的影响。因此， multiprocessing 模块允许程序员充分利用机器上的多核。可运行于 Unix 和 Windows 。

multiprocessing 模块还引入了在 threading 模块中没有的API。一个主要的例子就是 **Pool** 对象，它提供了一种快捷的方法，赋予函数并行化处理一系列输入值的能力，可以将输入数据分配给不同进程处理（数据并行）。下面的例子演示了在模块中定义此类函数的常见做法，以便子进程可以成功导入该模块。这个数据并行的基本例子使用了 Pool ，


# 1 Process类
在 multiprocessing 中，通过创建一个 Process 对象然后调用它的 start() 方法来生成进程。 Process 和 threading.Thread API 相同。 一个简单的多进程程序示例是:

# 2 上下文和启动方法
## 2.1 spawn
## 2.2 fork
## 2.3 forkserver

# 3 进程之间交换对象
## 3.1 Queue
Queue 对于一个进程向另一个进程或者多个进程发送消息非常有用。
队列是线程和进程安全的。


## 3.2 Pipe
Pipe() 函数返回一个由管道连接的连接对象，默认情况下是双工（双向）。

返回的两个连接对象 Pipe() 表示管道的两端。每个连接对象都有 send() 和 recv() 方法（相互之间的）。请注意，如果两个进程（或线程）同时尝试读取或写入管道的 同一 端，则管道中的数据可能会损坏。当然，在不同进程中同时使用管道的不同端的情况下不存在损坏的风险。


# 4 进程间同步

# 5 进程间共享状态
## 5.1 共享内存

## 5.2 服务进程



# 6 使用工作进程


