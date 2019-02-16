
# 1 多GPU训练时，速度没有变得更快。

使用多GPU训练时，每个GPU都会运行一个 Caffe 模型的实例。比如当使用 nn 个GPU训练时，网络会有 nn 个分身分别在各自的GPU上运行，nn 个网络中有一个“本尊”叫root_net，root_net除了负责正常的前传反传还负责更新参数，而其它网络只负责前传和反传。大致流程是这样的，nn 个网络共享一个数据层，数据层读取 nn 个batch的数据分别送给 nn 个网络进行前传和反传，然后使用归约的方法将 nn 个网络计算的梯度累加在root_net上，取平均后由root_net更新网络参数，接着同步 nn 个网络的参数，数据层再取 nn 个batch的数据进行下一次迭代。在多个GPU之间实现归约和同步会很耗时，尤其是当两个GPU不在一个multiGpuBoardGroup上的情况，所以整体的时间并没有减少太多。

# 2 Batch_size 和 学习率 选择的问题 
这里的意思就是batchsize和学习率是相关的，如果batchsize减小了X倍，则理论上学习率应增大sqrt(X)倍（当然这是找到最好的batchsize的情况下的），不过Alex还是用了X倍。后面 https://arxiv.org/abs/1404.5997 这个链接的论文还没看，有时间的可以看一下，好像有专门讲到batchsize的设置的。

另外，batchsize最好设置为8的倍数，这样gpu的并行运算效率最高。

# 3 
现在的caffe版本已经支持多GPU并行了，原理比较简单，就是每个GPU分别算一个batch，n个GPU，实际的batchsize就是n*batch，比如原来用一个GPU，batchsize设置成256，现在用4个GPU，把batchsize设置成64，和原来的一个GPU的运算是等价的。

总batchsize为256时：
(1) 单GPU：iter_size没设置时，默认为1，batchsize=256；iter_size=4时，batch_size=64。
(2) 多GPU：假如4个GPU，iter_size没设置时，默认为1，batchsize=64；iter_size=4时，batch_size=16。如果显存能放得下，iter_size尽量设为1。

实际使用的时候基本不用设置，和原来一样编译好就可以用了。命令就是在-gpu 后面对多个GPU号用逗号隔开，比如-gpu 1,2,3,4 就是同时使用1-4共4个GPU，GPU编号可以不连续，或者直接用-gpu all，就是使用所有的GPU。

# 4
（1）solver中有一个iter size，iter size * batch size（train.prototxt中的）是真正的总的batch_size，如果显存放得下，尽量不设iter size，即默认为1。
（2）当多GPU训练时，总的batch_size等于 gpu数量 * iter size * batch size


# 参考资料
[Caffe 多GPU训练问题，以及batch_size 选择的问题](https://blog.csdn.net/calvinpaean/article/details/84063173)
[Caffe 是否支持多GPU并行训练？](http://www.caffecn.cn/?/question/85)

