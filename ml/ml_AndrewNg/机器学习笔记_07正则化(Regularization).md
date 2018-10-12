# 七、正则化
## 7.1 过拟合的问题
参考视频: 7 - 1 - The Problem of Overfitting (10 min).mkv

过拟合如何处理：
1. 丢弃不能帮助我们正确预测的特征。
2. 正则化。保留所有的特征，但是减少参数的大小。

## 7.2 代价函数
参考视频: 7 - 2 - Cost Function (10 min).mkv
正则化的基本方法：在一定程度上减小参数$\theta$的值。
修改后的代价函数：
$$J(\theta)= \frac 1 {2m}[\sum^m_{i=1}((h_\theta(x^i)-y^i)^2 + \lambda\sum^n_{j=1}\theta_j^2)]$$
$\lambda$ : 正则化参数 regularization parameter

如果选择的正则化参数$\lambda$过大，则会把所有的参数都最小化了，导致模型变成$h_\theta(x)=\theta_0$，是一条红线，造成欠拟合。

## 7.3 正则化线性回归
参考视频: 7 - 3 - Regularized Linear Regression (11 min).mkv

对于线性回归的求解，我们之前推导了两种学习算法：一种基于梯度下降，一种基于正规方程。
正则化线性回归的代价函数为：
$$J(\theta) = \frac1{2m}[\sum^m_{i=1}(h_\theta(x^i)-y^i)^2 + \lambda\sum^n_{j=1}\theta^2_j]$$

如果我们要使用**梯度下降**令这个函数最小化，$\theta_0$不需要正则化，所以梯度下降算法将分为两种情形：
Repeat until convergence {
$$\theta_0 := \theta_0 - \alpha\frac1m\sum((h_\theta(x^i)-y^i)*x_0^i)$$
$$\theta_j := \theta_j - \alpha\frac1m\sum((h_\theta(x^i)-y^i)*x_j^i + \frac \lambda m \theta_j) $$   (for j = 1, 2, ... , n)
}

对上面的算法中j = 1, 2, ..., n时的更新式子进行调整可得：
$$\theta_j := \theta_j(1-\alpha\frac\lambda m) - \alpha \frac 1 m \sum^m_{i=1}(h_\theta(x^i) - y^i) x_j^i$$

用**正规方程**来求解正则化线性模型：
$$\theta = (X_TX+\lambda\begin{bmatrix}
 0&  &  &  &  & \\ 
 &1  &  &  &  & \\ 
 &  &1  &  &  & \\ 
 &  &  &.  &  & \\ 
 &  &  &  &.  & \\ 
 &  &  &  &  &1 
\end{bmatrix})^-1 X^Ty$$
图中的矩阵尺寸为(n+1)*(n+1)。

7.4 正则化的逻辑回归模型
参考视频: 7 - 4 - Regularized Logistic Regression (9 min).mkv
逻辑回归增加一个正则化的表达式后的代价函数：
$$J(\theta)=-[\frac1m\sum^m_{i=1}(y^i*\log(h_\theta(x^i))+(1-y^i)*\log(1-h_\theta(x^i)))]+\frac\lambda{2m}\sum^n_{j=1}\theta_j^2$$

要最小化该代价函数，通过求导，得出梯度下降算为：
Repeat until convergence{
$$\theta_0 := \theta_0 - \alpha\frac1m\sum^n_{i=1}((h_\theta(x^i)-y^i)*x_0^i)$$
$$\theta_j := \theta_j - \alpha\frac1m\sum^n_{i=1}((h_\theta(x^i)-y^i)*x_0^j + \frac\lambda m \theta_j)$$ 
for j = 1, 2, ..., n
}
***注***：
看上去同线性回归一样，但是知道$h_\theta(x)=g(\theta^TX)$，所以与线性回归不同。
***注意***:
1.虽然正则化的逻辑回归中的梯度下降和正则化的线性回归中的表达式看起来一样,但 由于两者的 h(x)不同所以还是有很大差别。
2. θ0 不参与其中的任何一个正则化。
