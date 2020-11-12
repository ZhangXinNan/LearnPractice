


# 1 什么是softmax

softmax把一个序列变成概率。

$S_j = \frac{e^{a_j}}{\sum_{k=1}^N{e^{a_k}}}$

从概念角度解释：
$S_j=P(y=j|a)$

代码：
```python
import numpy as np
def softmax(a):
    exps = np.exp(a)
    return exps / np.sum(exps)

a1 = [1.0, 2.0, 3.0]
result = softmax(a1)
print(result, type(result), result.shape)
# [0.09003057 0.24472847 0.66524096] <class 'numpy.ndarray'> (3,)
```

# 2 稳定的softmax

```python
def stable_softmax(x):
    """Compute the softmax of vector x in a numerically stable way."""
    shiftx = x - np.max(x)
    exps = np.exp(shiftx)
    return exps / np.sum(exps)

a2 = [-1000, 1, 10000]
result = stable_softmax(a2)
print(result)
```

# 3 LogSoftmax

$$
log(S_j) = log(\frac{e^{a_j}}{\sum_{k=1}^Ne^{a_k}})
= log(e^{a_j}) - log(\sum_{k=1}^Ne^{a_k})
= a_j - log(\sum_{k=1}^Ne^{a_k})

$$


```python

```