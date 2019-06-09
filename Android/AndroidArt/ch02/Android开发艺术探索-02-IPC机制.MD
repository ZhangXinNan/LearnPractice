
## 2.1 Android IPC简介
IPC ： Inter-Process Communication，进程间通信或者跨进程通信。
在安卓里面主线程也叫UI线程，在UI线程里才能操作界面。如果耗时任务放在主线程中会造成界面无法响应，即应用无响应（Application Not Responding）。



## 2.2 Android中的多进程模式

### 2.2.1 开启多进程模式
在AndroidManifest中指定android:process属性。
process值：
（1）冒号开头表示要在当前的进程名前面附加上当前的包名。
（2）进程名以冒号开头的进程属于当前应用的**私有进程**。否则是**全局进程**。


Android系统为每个应用分配一个唯一的UID，具有相同UID的应用才能共享数据。



### 2.2.2 多进程模式的运行机制

Android 为每个应用分配了一个独立的虚拟机。

使用多进程会造成以下问题：
* （1）静态成员和单例模式完全失效；
* （2）线程同步机制完全失效；
* （3）SharedPreferences 可靠性下降；
* （4）Application 会多次创建。


## 2.3 IPC基础概念介绍

Serializable 是Java中的序列化接口，使用起来简单但是开销大，序列化和反序列化过程需要大量IO操作。
Parcelable 是Android中的序列化方式，使用麻烦，但是效率高。


### 2.3.1 Serializable接口

### 2.3.2 Parcelable接口

### 2.3.3 Binder



