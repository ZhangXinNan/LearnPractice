
# 概述
PCA（Principal Componnet Analysis）是一种常用的数据表示方法。PCA将通过线性变换将原始数据变换为一组各维度线性无关的表示，可用于提取数据的主要特征分量，学用于高维数据的降维。

# 内积
$(a_1, a_2, a_n)^T \cdot  (b_1, b_2, b_n)^T = a_1b_1 + a_2b_2 + a_nb_n$

$A\cdot{B} = |A||B|\cos(\alpha)$

上述两公式相等证明的提示：$\cos(\alpha) = \cos (A-B) = \cos A \cos B + \sin A \sin B$

A与B的内积等于A到B的投影长度乘以B的模。
设B的模为1，则A与B的内积值等于A向B所在直线投影的矢量长度。

要准确描述向量，首先要确定一组基，然后给出在基所在的各个直线上的投影值 。

# 基变换的矩阵表示 
两个矩阵相乘的意义：将右边矩阵中的每一列列向量变换到左边矩阵每一行行向量为*基*所表示的空间中去。

# 协方差矩阵及其优化
方差：寻找一个一维基，使得所有数据变换为这个基上的坐标表示后，方差值最大。

协方差：$Cov(a,b)=\frac{1}{m}\Sigma^m_{i=1}a_ib_i$

降维问题的优化目标：将一组N维向量降为K维，基目标是选择K个单位正交基，使得原始数据变换到这组基上后，各字段两两协方差为0，而字段的方差则尽可能大。（在正交的约束下，取最大的K个方差）


# 参考资料
[PCA的数学原理](http://blog.codinglabs.org/articles/pca-tutorial.html)

[PCA（主成分分析）](https://yoyoyohamapi.gitbooks.io/mit-ml/content/%E7%89%B9%E5%BE%81%E9%99%8D%E7%BB%B4/articles/PCA.html)