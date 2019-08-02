


# 1 方差和协方差
在统计学中，方差是用来度量单个随机变量的离散程度，而协方差则一般用来刻画两个随机变量的相似程度，其中，方差的计算公式为
## 方差
$$
\sigma_x^2 = \frac 1 {n-1} \Sigma_{i=1}^n (x_i - \bar{x})^2
$$

## 协方差


$$
\sigma(x,y) = \frac 1 {n-1}  \Sigma_{i=1}^n  (x_i - \bar{x}) (y_i - \bar{y})
$$

# 2 协方差矩阵


## 多个随机变量的方差
$$
\sigma(x_k,x_k) = \frac 1 {n-1}  \Sigma_{i=1}^n  (x_{ki} - \bar{x})^2
$$

## 两两之间的协方差

$$
\sigma(x_m,x_k) = \frac 1 {n-1}  \Sigma_{i=1}^n  (x_{mi} - \bar{x_m}) (x_{ki} - \bar{x_k})
$$


协方差矩阵
$$
\Sigma = \begin{bmatrix}
\sigma(x_1,x_1) & ... & \sigma(x_1, x_d)\\
... & ... & ... \\
\sigma(x_d,x_1) & ... & \sigma(x_d, x_d)
\end{bmatrix}
$$

对角线上的元素为各个随机变量的方差，非对角线上的元素为两两随机变量之间的协方差，根据协方差的定义，我们可以认定：矩阵 $\Sigma$ 为对称矩阵(symmetric matrix)，其大小为 $d \times d$

# 3 多元正态分布
假设一个向量$\vec x$ 服从均值向量为 $\vec\mu$，协方差矩阵为$\Sigma$ 的多元正态分布。

$$
p(x) = \frac{1}{\sqrt{2\pi \Sigma}} exp(-\frac12(x-\mu)^T\Sigma^{-1}(x-\mu))
$$

令$\mu$=0 ,
$$
p(x)\propto exp(-\frac12 x^T\Sigma^{-1}x)
$$

# 参考
* [如何直观地理解「协方差矩阵」？](https://zhuanlan.zhihu.com/p/37609917)
