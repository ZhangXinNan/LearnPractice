
- 第一章 asyncio简介
    - 1.1 什么是asyncio
    - 1.2 什么是I/O密集型和CPU密集型
    - 1.3 了解并发、并行和多任务
    - 1.4 了解进程、线程和多线程和多处理
        - 1-2.py 简单python应用程序中的进程和线程
        - 1-3.py 创建多线程python应用程序
    - 1.5 理解全局解释器锁
    - 1.6 单线程并发
    - 1.7 事件循环的工作原理
    - 1.8 本章小节

# 第一章 asyncio简介

## 1.1 什么是asyncio
asyncio 是异步I/O的缩写。
asyncio 是一个库，使用**称为单线程事件循环的并发模型以异步方式**执行这些**协程**。


## 1.2 什么是I/O密集型和CPU密集型
* 1-1.py I/O密集型和CPU密集型操作

## 1.3 了解并发、并行和多任务
### 1.3.1 并发
### 1.3.2 并行
并发意味着多个任务同时进行，但并不意味着并行。
并行：有两个或多个任务同时发生，而且同时执行。
### 1.3.3 并行与并发的区别
### 1.3.4 什么是多任务
* 抢占式多任务处理
* 协同多任务处理
### 1.3.5 协同多任务处理的优势 

## 1.4 了解进程、线程和多线程和多处理
### 1.4.1 进程
进程：具有其他应用程序无法访问的内存空间的应用程序运行状态。

### 1.4.2 线程
线程共享进程的内存。
* 1-2.py 简单python应用程序中的进程和线程
```python
import os
import threading

# os.getpid()：获取进程ID
print(f'Python process running with process id : {os.getpid()}')

# 正在进行的线程活动计数
total_threads = threading.active_count()
print("Python is currently running {} thread(s)".format(total_threads))

# 当前线程名称
thread_name = threading.current_thread().name
print("The current thread is {}".format(thread_name))
```

* 1-3.py 创建多线程python应用程序

线程的start方法开始运行它。
线程的join方法让程序暂停，直到启动的线程完成。
多线程仅对I/O密集型 工作有用，因为它受到全局解释器锁的限制。

* 1-4.py 创建多个进程


## 1.5 理解全局解释器锁
GIL 阻止一个python进程在任何给定的时间执行多个python字节码指令。
即使在多核机器上有多个线程，python进程也只能有一个线程运行python代码。

* 1-5.py 生成斐波那契数列并计算时间
* 1-6.py 多线程的斐波那契数列

### 1.5.1 GIL会释放吗
* 1-7.py 同步读取状态码
* 1-8.py 通过多线程读取状态码

### 1.5.2 asyncio 和 GIL
当使用asyncio 时，创建了名为协程的对象。协程可被认为是在执行一个轻量级线程。

## 1.6 单线程并发
## 1.7 事件循环的工作原理
## 1.8 本章小节

