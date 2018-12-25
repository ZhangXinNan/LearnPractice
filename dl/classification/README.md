


[Multi-class, Multi-label 以及 Multi-task 问题](https://blog.csdn.net/golden1314521/article/details/51251252)



## Multiclass classification 
就是多分类问题，比如年龄预测中把人分为小孩，年轻人，青年人和老年人这四个类别。Multiclass classification 与 binary classification相对应，性别预测只有男、女两个值，就属于后者。


## Multilabel classification 
是多标签分类，比如一个新闻稿A可以与{政治，体育，自然}有关，就可以打上这三个标签。而新闻稿B可能只与其中的{体育，自然}相关，就只能打上这两个标签。


## Multioutput-multiclass classification 和 multi-task classification 
指的是同一个东西。仍然举前边的新闻稿的例子，定义一个三个元素的向量，该向量第1、2和3个元素分别对应是否（分别取值1或0）与政治、体育和自然相关。那么新闻稿A可以表示为[1,1,1]，而新闻稿B可以表示为[0,1,1]，这就可以看成是multi-task classification 问题了。 从这个例子也可以看出，Multilabel classification 是一种特殊的multi-task classification 问题。之所以说它特殊，是因为一般情况下，向量的元素可能会取多于两个值，比如同时要求预测年龄和性别，其中年龄有四个取值，而性别有两个取值。

