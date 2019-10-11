
### 2.2.1 Tensor
Tensor 特点： 
1. Tensor和numpy的ndarrays类似，但是**Tensor可以使用GPU加速**。
2. 函数名后面带下划线的函数会修改Tensor本身。
3. Tensor和numpy对象共享内存。



定义一个tensor
```python
from __future__ import print_function
import torch as t
# 构建一个5x3的矩阵
x = t.Tensor(5, 3)              # torch.Tensor 是 torch.FloatTensor的别名。
# 查看形状
print(x.shape)                  # torch.Size([5, 3])
print(x.size())
# 使用[0,1]随机初始化二维数组
x = t.rand(5, 3)
print(x)

# 全0的tensor, dtype指定数值类型
x = t.zeros(5, 3, dtype=t.long)
print(x)
y = t.ones(3,4)
print(y)

# 直接从数组数据构建 tensor
x = t.tensor([5, 5.3])
```

加法的三种写法：
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

Tensor不支持的操作，可以先转为numpy数组处理，再转回Tensor
```python
# tensor -> numpy
b = a.numpy()
# Numpy -> tensor
b = t.from_numpy(a)
# 通过.cuda方法转为GPU的Tensor
if t.cuda.is_available():
    # x = x.cuda()
    # print(x)
    device = t.device("cuda")
    y = t.ones_like(x, device=device)
    x = x.to(device)
    z = x + y
    print(z)
    print(z.to("cpu", t.double))
```

使用torch.view 重设尺寸
```python
x = t.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)
print(x.size(), y.size(), z.size())
# torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])
```

使用item()将tensor类型转为python类型
```python
x = t.randn(1)
print(x, x.item())
```

### 2.2.2 Autograd: 自动微分
#### 旧版本中的Variable
> 【注意】在新版本的PyTorch中，Variable和Tensor已经合并。

Autograd.Variable 是Autograd的核心类，封装了Tensor。
* Variable 才具有自动求导功能。

Variable的三个属性：
* data 保存了Variable的Tensor。
* grad 保存data对应的梯度，grad也是一个Variable ?
* grad_fn 指向一个Function对象，这个Function用来计算反向传播计算输入的梯度。

```python
import torch as t
from torch.autograd import Variable
x = Variable(t.ones(2,2), requires_grad=True)
y = x.sum()
```

#### 新版本中的Tensor
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


### 2.2.3 神经网络
torch.nn用来定义和运行神经网络。
nn.Module看作是一个网络的封装，包含各层定义及forward方法，调用forward(input)，可返回前向传播的结果。

#### 定义网络
可学习的层放到__init__中。
nn.Module子类的构造函数必须在构造函数中执行父类的构造函数。
定义网络时，继承nn.Module，实现它的forward方法。
```
nn.Module.__init__(self)
# or
super(Net, self).__init__()
```


网络可学习参数通过net.parameters()返回。 

如果只想输入一个样本，则用input.unsqueeze(0)将bacth_size设为1。


