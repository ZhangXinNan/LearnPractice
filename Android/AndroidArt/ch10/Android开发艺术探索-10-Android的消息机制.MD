
# 10 Android 的消息机制
* Handler                   可以轻松的将一个任务切换到Handler所在的线程去执行。
* MessageQueue  消息队列。     
* Looper        消息循环。以无限循环的形式去查找是否有新消息。Handler创建的时候，会用当前线程的Looper来构造消息循环系统。
* ThreadLocal   Handler 内部

## 10.1 Android 的消息机制概述

## 10.2 Android 消息机制分析

### 10.2.1 ThreadLocal 的工作原理

ThreadLocal ： 线程的一个内部存储类，只有在指定线程中才能获取到存储的数据。


