# 0 背景介绍
在 python 的 web 部署中，经常会使用 gunicorn 启动 web 服务，同时，为了并发效率更高，一般会使用 `-w` 指定**多个工作进程 (worker processes)** , 同时可以通过 `-k` 指定**工作进程的类型**，目前支持的工作进程的类型包括： `sync, eventlet, gevent, tornado, gthread`。具体选择工作进程类型可以参考此博客 。在我们的项目中，主要使用 gevent，本篇文章就希望能深入介绍 gevent 在 web 部署中是如何工作以及提升效率的。

gevent 是底层是依赖 greenlet 实现并发提升效率的，而 greenlet 是一个协程机制的实现。下面就从简单到复杂依次进行介绍。

# 1 协程
协程也被称为**微线程**，是一种比线程更轻量级的任务调度方式，一个线程内可以有多个协程。

协程是一种可以在子程序内部中断，转而执行其他子程序，之后再从中断点继续执行的机制。比如在 I/O 操作时就可以执行其他子程序，等 I/O 操作数据就绪时继续执行，就可以在单个线程内实现非阻塞式的复用，大大提升效率。

# 2 greenlet

在gevent中用到的主要模式是Greenlet, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

> 在任何时刻，只有一个协程在运行。

这与multiprocessing或threading等提供真正并行构造的库是不同的。 这些库轮转使用操作系统调度的进程和线程，是真正的并行。

greenlet 是一个轻量级的协程实现，使用的方法简单而清晰。创建 greenlet 实例执行方法，在方法内部可通过 greenlet.switch() 切换至其他 greenlet 实例进行执行。一个简单的例子如下所示：
```python
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    gr1.switch()
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
```
上面的代码执行的结果是:
```
12
56
34
```
可以看到上面创建了两个 greenlet 实例 gr1, gr2，首先最后一行调用gr1.switch() 启动执行 test1 方法，打印出 12，接着执行 gr2.switch() 从而启动执行 test2 方法，打印出 56，接着执行 gr1.swich() 方法执行 test1 方法， 从上次的断点出继续执行，打印出 34，之后就结束了，因此最终 78 不会被打印出来。

可以看到 gevent 实例的运行逻辑很简单，就是切换时保存现场，下一通过gevent.switch() 切换回来时，从切换点继续执行。但是并不是所有的 gevent 实例都能执行结束，比如上面的 gr2 就没有执行结束，因为没有切换回来。

## 2.1 父子关系
greenlet 实例之间存在父子关系，当子 greenlet 执行完毕后，父 greenlet 继续执行。在创建 greenlet 时，可以指定其父 greenlet，如果不指定父 greenlet， 那么其父 greenlet 就是主 greenlet(main greenlet)。下面介绍一个简单实例：
```python
from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2, parent=gr1)
gr1.switch()
```
可以看到上面的代码执行的结果如下所示：
```
12
56
78
34
```
可以看到建立了两个 greenlet gr1, gr2，其中 gr2 的父 greenlet 是 gr1，gr1 没有指定父 greenlet，因此默认是 主 greenlet。

实际执行时，首先启动 gr1，打印 12，之后切换为 gr2, 打印 56，78，之后 gr2 执行结束，切换为父greenlet gr1，从切换处继续执行，打印34，之后 gr1 执行结束，切换为主 greenlet，继续往下，主 greenlet 也执行结束。

## 2.2 greenlet 应用
可以看到 greenlet 思路很清晰，协程的切换接口很易用。但是对于实际的业务开发依旧存在一些不便之处：

greenlet 原始的执行方法都需要转换为 greenlet 实例，而且需要使用者管理 greenlet 实例之间的树形关系，对于业务开发而言并不友好；
greenlet 的切换需要调用 greenlet.switch() 方法进行切换，业务中需要充斥大量的 greenlet 管理代码；


# 3 gevent
gevent 基于 greenlet 库进行了封装，基于 libev 和 libuv 提供了高效的同步API。
gevent是一个基于libev的并发库。它为各种并发和网络相关的任务提供了整洁的API。

对 greenlet 在业务开发中的不便之处，提供了很好的解决方案：
1. 对于 greenlet 实例的管理，不使用树形关系进行组织，隐藏不必要的复杂性；
2. 采用 monkey patching 与第三方库协作，不需要重写原因方法，也不需要手工通过greenlet.switch() 切换；
基本使用类似如下所示：

```python
import gevent
from gevent import socket

urls = ['www.google.com', 'www.example.com', 'www.python.org']
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
gevent.joinall(jobs, timeout=2)

print([job.value for job in jobs])
```
上面的示例中使用了 gevent 中两个基础接口：
* `gevent.spawn()` 此方法用于创建一个 greenlet 实例，用于执行特定的方法
* `gevent.joinall()` 用于等待所有的 greenlet 实例执行完毕
上面的例子中创建了三个 greenlet 实例，执行socket.gethostbyname 方法，全部执行结束后获取请求的结果。可以看到业务代码使用 gevent 时，不需要关心 greenlet 实例组织的逻辑，由 gevent 统一组织调度起来。

## 3.1 monkey patching
通过之前的介绍，gevent 是利用协程实现线程的复用，在子任务出现 I/O 操作时，切换去执行其他子任务，但是在业务代码中，不会手工触发 `greenlet.switch()` 去触发切换到另一个子任务，甚至默认的网络库进行网络请求时是阻塞式地请求网络，完全没有办法切换子任务去实现复用，那么 gevent 是如何实现的呢？

答案是 monkey patching，gevent.monkey 模块提供了大量的方法与类去替换第三方阻塞式的库的行为，比如替换 socket 库中的行为从而支持非阻塞式的网络请求。

比如希望引入非阻塞式的网络请求，可以实现的方式如下：
1. 直接从 gevent 中引入 socket 库进行使用，代码如下所示
```python
from gevent import socket
```
2. 使用系统的 socket 库，并使用 gevent 的 monkey.patch_socket() 对其打补丁
```python
from gevent import monkey; monkey.patch_socket()
```
如果希望直接用 gevent 对其所支持的第三方库打补丁，使其转换为非阻塞的操作，可以使用如下所示的代码
```python
from gevent import monkey; monkey.patch_all()
```

## 3.2 gevent 应用
通过上面的介绍可以看到，gevent 通过接口的封装，让使用者不需要关心 greenlet 实例的调度，易用性得到提升，同时利用 monkey patching，让使用者不用关心任务的切换，从而让业务代码写起来更加方便

## 3.3 同步和异步执行
并发的核心思想在于，大的任务可以分解成一系列的子任务，后者可以被调度成 同时执行或异步执行，而不是一次一个地或者同步地执行。两个子任务之间的 切换也就是上下文切换。

在gevent里面，上下文切换是通过yielding来完成的. 在下面的例子里， 我们有两个上下文，通过调用gevent.sleep(0)，它们各自yield向对方。
```python
import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
])
```

当我们在受限于网络或IO的函数中使用gevent，这些函数会被协作式的调度， gevent的真正能力会得到发挥。Gevent处理了所有的细节， 来保证你的网络库会在可能的时候，隐式交出greenlet上下文的执行权。 这样的一种用法是如何强大，怎么强调都不为过。或者我们举些例子来详述。

下面例子中的select()函数通常是一个在各种文件描述符上轮询的阻塞调用。

```python
import time
import gevent
from gevent import select

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time() - start)

def gr1():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: %s' % tic())
    select.select([], [], [], 2)
    print('Ended Polling: %s' % tic())

def gr2():
    # Busy waits for a second, but we don't want to stick around...
    print('Started Polling: %s' % tic())
    select.select([], [], [], 2)
    print('Ended Polling: %s' % tic())

def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)

gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])
```

下面是另外一个多少有点人造色彩的例子，定义一个非确定性的(non-deterministic) 的task函数(给定相同输入的情况下，它的输出不保证相同)。 此例中执行这个函数的副作用就是，每次task在它的执行过程中都会随机地停某些秒。

```python
import gevent
import random

def task(pid):
    """
    Some non-deterministic task
    """
    gevent.sleep(random.randint(0,2)*0.001)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
```

上例中，在同步的部分，所有的task都同步的执行， 结果当每个task在执行时主流程被阻塞(主流程的执行暂时停住)。

程序的重要部分是将task函数封装到Greenlet内部线程的gevent.spawn。 初始化的greenlet列表存放在数组threads中，此数组被传给gevent.joinall 函数，后者阻塞当前流程，并执行所有给定的greenlet。执行流程只会在 所有greenlet执行完后才会继续向下走。

要重点留意的是，异步的部分本质上是随机的，而且异步部分的整体运行时间比同步 要大大减少。事实上，同步部分的最大运行时间，即是每个task停0.002秒，结果整个 队列要停0.02秒。而异步部分的最大运行时间大致为0.002秒，因为没有任何一个task会 阻塞其它task的执行。

一个更常见的应用场景，如异步地向服务器取数据，取数据操作的执行时间 依赖于发起取数据请求时远端服务器的负载，各个请求的执行时间会有差别。

```python
import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json

def fetch(pid):
    response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
```

# 3.4 确定性
就像之前所提到的，greenlet具有确定性。在相同配置相同输入的情况下，它们总是 会产生相同的输出。下面就有例子，我们在multiprocessing的pool之间执行一系列的 任务，与在gevent的pool之间执行作比较。

即使gevent通常带有确定性，当开始与如socket或文件等外部服务交互时， 不确定性也可能溜进你的程序中。因此尽管gevent线程是一种“确定的并发”形式， 使用它仍然可能会遇到像使用POSIX线程或进程时遇到的那些问题。

涉及并发长期存在的问题就是竞争条件(race condition)。简单来说， 当两个并发线程/进程都依赖于某个共享资源同时都尝试去修改它的时候， 就会出现竞争条件。这会导致资源修改的结果状态依赖于时间和执行顺序。 这是个问题，我们一般会做很多努力尝试避免竞争条件， 因为它会导致整个程序行为变得不确定。

最好的办法是始终避免所有全局的状态。全局状态和导入时(import-time)副作用总是会 反咬你一口！

# 4 gunicorn 与 gevent
在实际的 web 部署中，我们的使用 gevent 比前面介绍得要更加简单一些，我们甚至都不需要显示去执行 monkey.patch_all() 去给第三方库打补丁，直接在 gunicorn 启动 web 服务时，通过 -k gevent 去指定工作进程类型即可，后续不需要任何的开发。看起来 gunicorn 帮助我们做了该做的初始化，具体代码是怎么呢 ？ 在 github 的项目的 gunicorn/workers/ggevent.py 可以看到相关的实现：
```python
def patch(self):
    monkey.patch_all()

    # monkey patch sendfile to make it none blocking     
    patch_sendfile()

    # patch sockets     
    sockets = []
    for s in self.sockets:
        sockets.append(socket.socket(s.FAMILY, socket.SOCK_STREAM, fileno=s.sock.fileno()))
    self.sockets = sockets


def init_process(self):
    self.patch()
    super().init_process()
```
可以看到 gunicorn 的初始化工作进程中，调用self.patch() 方法，执行了monkey.patch_all() 给第三方库加上了补丁，从而保证在使用 gevent 时，可以将支持的第三方的阻塞方法转换为非阻塞方法，从而充分利用协程提供的并发效率。

# 5 总结
从协程的基础概念，到 greenlet 的协程实现，再到 gevent 的二次封装，再到 gunicorn 与 gevent 的联合使用，最终将一个复杂的协程复用变成一个只需要一个参数 -k gevent 就能协作起来大大提升效率的方案，不得不说让人佩服。


# 6 参考资料
* [深入了解 gevent](https://hustyichi.github.io/2019/04/14/dive-into-gevent/)
* [gevent程序员指南](http://hhkbp2.com/gevent-tutorial/)
