
# 11章 Android 的线程和线程池

* AsyncThread 封装了线程和Handler，方便开发者在子线程中更新UI。
* Handler 是一个具有消息循环的线程。在它的内部可以使用Handler。
* IntentService 是一个服务，系统对其进行了封装，可以更方便的执行后台任务。IntentService 内部采用HandlerThread 来执行任务。执行完毕后IntentService自动退出。


## 11.1 主线程和子线程
主线程主要处理界面交互相关的逻辑。也叫UI线程。

## 11.2 Android线程形态

### 11.2.1 AsyncTask
### 11.2.2 AsyncTask的工作原理
### 11.2.3 HandlerThread

继承了Thread，是一种可以 使用 Handler 的Thread。

HandlerThread 在内部创建了消息队列，外界需要通过 Handler 的消息方式来通知 HandlerThread 执行一个具体的任务。

### 11.2.4 IntentService



## 11.3 Android 中的线程池

