
# [caffe的solver理解](https://blog.csdn.net/ying86615791/article/details/60134080)

average_loss: 40 官方解释是：Display the loss averaged over the last average_loss iterations，这里即显示最近40次iter的平均loss，

【这个跟源码中的UpdateSmoothedLoss函数有关？这个函数将历史过程中的loss求平均可以减少loss震荡】
--------------------- 
作者：美利坚节度使 
来源：CSDN 
原文：https://blog.csdn.net/ying86615791/article/details/60134080 
版权声明：本文为博主原创文章，转载请附上博文链接！




# [【Caffe细致入微】Solver_Step](https://blog.csdn.net/u012816621/article/details/53912425)
【Introduction】简单的说，这个函数就是核心的优化方法，不断通过前向和反向传播来更新参数的过程。
【Loss处理——均值滤波（广泛应用）】
```c++
template <typename Dtype>
void Solver<Dtype>::UpdateSmoothedLoss(Dtype loss, int start_iter, int average_loss)
```

每一次训练迭代都会进行前向传播，就会得到loss值。这个函数的作用就是把几次的loss进行平均化处理。

若average_loss为1：loss_容器里面只存当前获得的真实loss值，而smooth_loss_当然也是这个值

若average_loss为n：loss_容器里面就会存储前n个loss的值，而smooth_loss_相当于做了一个loss平均

【你可能会问】这么做好处是什么？

当然无论average_loss为多少，最终都是为了展示训练之后的loss，但是我们当然要从loss中得到一些信息和经验，比如，这一阶段的训练的效果等。平均值会比个体值更加客观的刻画整个集合。做这样的平均其实应用有很多，主要是去除掉一些噪音，让得到的值更加可信。caffe中默认average_loss为1。
--------------------- 
作者：DafuTT 
来源：CSDN 
原文：https://blog.csdn.net/u012816621/article/details/53912425 
版权声明：本文为博主原创文章，转载请附上博文链接！
