# 六、逻辑回归Logistic Regression
## 6.1 分类问题
参考视频: 6 - 1 - Classification (8 min).mkv
**因变量 dependent variable**：**负向类 negative class**；**正向类 positive class**。
因变量$y\in{0,1}$，其中0表示负向类，1表示正向类。

## 6.2 假说表示 Hypothesis Representation
参考视频: 6 - 2 - Hypothesis Representation (7 min).mkv
逻辑回归模型的假设：
$$h_\theta(x)=g(\theta^T X)$$
其中：
X代表特征向量。
g 代表逻辑函数（logistic function）是一个常用的逻辑函数为S形函数（sigmoid function），公式为：
$$g(z)=\frac1{1+e^{-z}}$$
合起来得到逻辑模型的假设：
$$g(z)=\frac1{1+e^{-\theta^T X}}$$

$h_\theta(x)$的作用是，对于给定的输入变量，根据选择的参数计算输出变量=1的可能性（estimated probability），即$$h_\theta(x)=P(y=1|x;\theta)$$


## 6.3 判定边界
参考视频: 6 - 3 - Decision Boundary (15 min).mkv
决策边界 decision boundary

## 6.4 代价函数
参考视频: 6 - 4 - Cost Function (11 min).mkv
* 线性回归的代价函数：$J(\theta)=\frac1m\sum^m_{i=1}\frac12(h_\theta(x^i)-y^i)^2$ (非凸函数non-convex function)
* 重新定义逻辑回归的代价函数：
$$J(\theta)=\frac1 m\sum^m_{i=1}Cost(h_\theta(x^i),y^i)$$
其中：
$$Cost(h_\theta(x), y) = \left\{
\begin{aligned}
&-\log(h\theta(x)) &if \quad y = 1 \\
&-\log(1-h\theta(x)) & if  \quad y = 0
\end{aligned}
\right.$$

$Cost(h_\theta(x^i),y^i)$简化如下：
$$Cost(h_\theta(x^i),y^i)=-y\log(h_\theta(x))-(1-y)\log(1-h_\theta(x))$$

代入代价函数得到：
$$J(\theta)=-\frac1 m\sum^m_{i=1}[y^i\log h_\theta(x^i) + (1 - y^i)\log(1-h_\theta(x^i))]$$

在得到这样一个代价函数后，我们便可以用梯度下降算法求得能使代价函数最小的参数了。算法为：
Repeat {
  $$\theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}J(\theta)$$  simultaneously update all
}
求导后得到：
Repeat {
  $$\theta_j := \theta_j - \alpha\frac{\partial}{\partial\theta_j}(h_\theta(x^i)-y^i)x^i_j$$  simultaneously update all
}


## 6.5 简化的成本函数和梯度下降
参考视频: 6 - 5 - Simplified Cost Function and Gradient Descent (10 min).mkv
线性回归假设函数：$h_\theta(x)=\theta^TX$
逻辑回归假设函数：$h_\theta(x)=\frac1{1 + e ^{-\theta^TX}}$

## 6.6 高级优化
参考视频: 6 - 6 - Advanced Optimization (14 min).mkv

## 6.7 多类别分类：一对多
选择一个让$h_\theta^i(x)$最大的i，即$$\max_i h^i_\theta(x)$$
