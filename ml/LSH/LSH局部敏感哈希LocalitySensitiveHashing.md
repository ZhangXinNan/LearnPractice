
In computer science, locality-sensitive hashing (LSH) is an algorithmic technique that hashes similar input items into the same "buckets" with high probability.[1] (The number of buckets is much smaller than the universe of possible input items.)[1] Since similar items end up in the same buckets, this technique can be used for data clustering and nearest neighbor search. It differs from conventional hashing techniques in that hash collisions are maximized, not minimized. Alternatively, the technique can be seen as a way to reduce the dimensionality of high-dimensional data; high-dimensional input items can be reduced to low-dimensional versions while preserving relative distances between items.

在计算机科学中，局部敏感散列 (LSH) 是一种算法技术，它以高概率将相似的输入项散列到相同的“桶”中。 [1] （桶的数量远小于可能的输入项目的个数。）[1] 由于相似的项目最终位于相同的桶中，因此该技术可用于数据聚类和最近邻搜索。 它与传统散列技术的不同之处在于散列冲突被最大化，而不是最小化。 或者，该技术可以被视为一种降低高维数据维数的方法； 高维输入项目可以减少到低维版本，同时保持项目之间的相对距离。

Hashing-based approximate nearest neighbor search algorithms generally use one of two main categories of hashing methods: either data-independent methods, such as locality-sensitive hashing (LSH); or data-dependent methods, such as locality-preserving hashing (LPH).

基于散列的近似最近邻搜索算法通常使用两种主要的散列方法之一：一种是数据无关的方法，例如局部敏感散列（LSH）； 或数据相关的方法，例如保持位置的散列 (LPH)。


哈希最开始是为了减少冲突方便快速增删改查，在这里LSH恰恰相反，它利用的正式哈希冲突加速检索，并且效果极其明显。

局部敏感哈希(Locality Sensitive Hashing，LSH)算法是我在前一段时间找工作时接触到的一种衡量文本相似度的算法。局部敏感哈希是近似最近邻搜索算法中最流行的一种，它有坚实的理论依据并且在高维数据空间中表现优异。它的主要作用就是从海量的数据中挖掘出相似的数据，可以具体应用到文本相似度检测、网页搜索等领域。

# 1 基本思想
　局部敏感哈希的基本思想类似于一种空间域转换思想，LSH算法基于一个假设，如果两个文本在原有的数据空间是相似的，那么分别经过哈希函数转换以后的它们也具有很高的相似度；相反，如果它们本身是不相似的，那么经过转换后它们应仍不具有相似性。

　　哈希函数，大家一定都很熟悉，那么什么样的哈希函数可以具有上述的功能呢，可以保持数据转化前后的相似性？当然，答案就是局部敏感哈希。

# 2 局部敏感哈希LSH

局部敏感哈希的最大特点就在于保持数据的相似性，我们通过一个反例来具体介绍一下。

　　假设一个哈希函数为Hash(x) = x%8，那么我们现在有三个数据分别为255、257和1023，我们知道255和257本身在数值上具有很小的差距，也就是说它们在三者中比较相似。我们将上述的三个数据通过Hash函数转换：

　　Hash(255) = 255%8 = 7;

　　Hash(257) = 257%8 = 1;

　　Hash(1023) = 1023%8 = 7;

　　我们通过上述的转换结果可以看出，本身很相似的255和257在转换以后变得差距很大，而在数值上差很多的255和1023却对应相同的转换结果。从这个例子我们可以看出，上述的Hash函数从数值相似度角度来看，它不是一个局部敏感哈希，因为经过它转换后的数据的相似性丧失了。

　　我们说局部敏感哈希要求能够保持数据的相似性，那么很多人怀疑这样的哈希函数是否真的存在。我们这样去思考这样一个极端的条件，假设一个局部敏感哈希函数具有10个不同的输出值，而现在我们具有11个完全没有相似度的数据，那么它们经过这个哈希函数必然至少存在两个不相似的数据变为了相似数据。从这个假设中，我们应该意识到局部敏感哈希是相对的，而且我们所说的保持数据的相似度不是说保持100%的相似度，而是保持最大可能的相似度。

　　对于局部敏感哈希“保持最大可能的相似度”的这一点，我们也可以从数据降维的角度去考虑。数据对应的维度越高，信息量也就越大，相反，如果数据进行了降维，那么毫无疑问数据所反映的信息必然会有损失。哈希函数从本质上来看就是一直在扮演数据降维的角色。

# 3 文档相似度计算





# 参考资料
* [[Algorithm] 局部敏感哈希算法(Locality Sensitive Hashing)](https://www.cnblogs.com/maybe2030/p/4953039.html)
* [Locality-sensitive hashing](https://en.wikipedia.org/wiki/Locality-sensitive_hashing)
* [局部敏感哈希 - MinHash](https://ansvver.github.io/lsh_minhash.html)
* [LSH-局部敏感哈希](https://zhuanlan.zhihu.com/p/225949044)


