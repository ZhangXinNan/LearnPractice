
# 1 Tensor
Tensor 特点： 
1. Tensor和numpy的ndarrays类似，但是**Tensor可以使用GPU加速**。
2. 函数名后面带下划线的函数会修改Tensor本身。
3. Tensor和numpy对象共享内存。

## 1.1 查看pytorch 版本，cuda是否可用
```python
from __future__ import print_function
import torch as t
print(t.__version__)
print('cuda : ', t.cuda.is_available())
```
输出结果
```bin
1.3.0
cuda :  False
```


## 1.2 定义一个tensor
```python
import torch as t
# 构建一个5x3的矩阵，未初始化值
x = t.Tensor(5, 3)              # torch.Tensor 是 torch.FloatTensor的别名。
y = t.empty(5, 3)
# 查看形状
print(x.shape)                  # torch.Size([5, 3])
print(y.size())
# 使用[0,1]随机初始化二维数组
z = t.rand(5, 3)
print(z)
print(z.size())

# 全0的tensor, dtype指定数值类型
x = t.zeros(5, 3, dtype=t.long)
print(x)
# 构建全为1的tensor
y = t.ones(3,4)
print(y)

# 直接从数组数据构建 tensor
x = t.tensor([5, 5.3])

# 使用已有的tensor的性质创建tensor
x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)
x = torch.randn_like(x, dtype=torch.float)    # override dtype!
print(x)                                      # result has the same size
```

## 1.3 加法的三种写法
```python
y = t.rand(5, 3)
z = x + y
t.add(x, y)
result = t.Tensor(5,3)
t.add(x, y, out=result)
print(result)
```

函数名后面带下划线的函数会修改Tensor本身。
```python
y.add(x)
print(y)
y.add_(x)
print(y)
```

## 1.4 tensor与numpy数组转化
Tensor不支持的操作，可以先转为numpy数组处理，再转回Tensor
```python
# tensor -> numpy
b = a.numpy()
# Numpy -> tensor
b = t.from_numpy(a)
# 通过.cuda方法转为GPU的Tensor
# let us run this cell only if CUDA is available
# We will use ``torch.device`` objects to move tensors in and out of GPU
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!
```

使用item()将tensor类型转为python类型
```python
x = t.randn(1)
print(x, x.item())
```

## 1.5 使用torch.view 重设尺寸
```python
x = t.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())
# torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])
```



## 1.6 新版本中的Tensor
* 使用 .requires_grad 追踪操作。
* 使用 .backward 来自动计算梯度。
* torch.no_grad() 阻止追踪历史。
```python
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x + 2
print(y)

z = y * y * 3
out = z.mean()
print(z, out)
```

```python
a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)
print(a.requires_grad)
b = (a * a).sum()
print(b.grad_fn)
```



# 4 参考资料
* [What is PyTorch?](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py)
* [深度学习框架PyTorch入门与实践]

