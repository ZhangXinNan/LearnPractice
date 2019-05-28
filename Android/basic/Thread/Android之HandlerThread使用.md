

HandlerThread可以创建一个带有looper的线程,looper对象可以用于创建Handler类来进行来进行调度，而且start()方法必须被调用。

在Android开发中，不熟悉多线程开发的人一想到要使用线程，可能就用new Thread(){…}.start()这样的方式。实质上在只有单个耗时任务时用这种方式是可以的，但若是有多个耗时任务要串行执行呢？那不得要多次创建多次销毁线程，这样导致的代价是很耗系统资源，容易存在性能问题。那么，怎么解决呢？



# 参考
* [Android多线程开发之HandlerThread的使用](https://blog.csdn.net/isee361820238/article/details/52589731)



