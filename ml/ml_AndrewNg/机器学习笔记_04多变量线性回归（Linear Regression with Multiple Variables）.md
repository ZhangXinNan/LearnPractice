# 四、多变量线性回归
## 4.1 多维特征
$x^i$代表第i个训练实例，是特征矩阵中的第i行，是一个向量（vector）。
$x^i_j$代表特征矩阵中第i行的第j个特征，也就是第i个训练实例的第j的特征。
支持多变量的假设h表示为：$h_\theta(x)=\theta_0+\theta_1 x_1+\theta_2 x_2 + ... + \theta_n x_n$
这个公式中有n+1个参数和n个变量，为了简化公式，引入$x_0=1$，则公式转化为：$h_\theta(x)=\theta^T X$。
参数是一个n+1维的向量，任何一个训练实例也都是n+1维的向量，特征矩阵的维度是m*(n=1）。
## 4.2  多变量梯度下降
参考视频：4-2 Gradient Descent for Multiple Variables


## 4.3 梯度下降实践1-特征缩放
参考视频: 4 - 3 - Gradient Descent in Practice I - Feature Scaling (9 min).mkv
最简单的方法：令$$x_n = \frac{x_n-\mu_n}{s_n}$$
其中，$\mu_n$是平均值，$s_n$是标准差。

## 4.4 梯度下降法实践2-学习率
## 4.5 特征和多项式回归
## 4.6 正规方程
【参考视频: 4 - 6 - Normal Equation (16 min).mkv】
正规方程求解下面的方程来找出使得代价函数最小的参数：$$\frac\partial\partial \theta_j J(\theta_j)=0$$
假设我们的训练集特征矩阵为X（包含了$x_0=1$），并且我们的训练结果为向量y，则利用正规方程解出向量$\theta=(X^TX)^{-1}X^Ty$。

|梯度下降 | 正规方程 |
|:------:|:------:|
|需要选择学习率 α|不需要|
|需要多次迭代|一次运算得出|
|当特征数量 n 大时也能较好适用|需要计算(XTX)-1|
|如果特征数量 n 较大则运算代价大,因 为矩阵逆的计算时间复杂度为 O(n3),通常 来说当 n 小于 10000 时还是可以接受的|适用于各种类型的模型|
|只适用于线性模型,不适合逻辑回归模|型等其他模型|

## 4.7 正规方程及不可逆性
参考视频: 4 - 7 - Normal Equation Noninvertibility (Optional) (6 min).mkv

**正规方程（normal equation）**
 $$\theta = (X^TX)^{-1}X^Ty$$
我们称那些不可逆矩阵为**奇异矩阵**或者**退化矩阵**。
在Octave里，pinv()求伪逆，inv()求逆。