
Autograd: 自动微分
_________


# 1 旧版本中的Variable
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

# 2 新版本中的Tensor
* 使用 .requires_grad 追踪操作。梯度记录在.grad里。
* 完成计算后，使用 .backward 来自动计算梯度。
* .detach() 
* torch.no_grad() 阻止追踪历史。
* .grad_fn 关联一个 Function 

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


# 3 神经网络
torch.nn用来定义和运行神经网络。
nn.Module看作是一个网络的封装，包含各层定义及forward方法，调用forward(input)，可返回前向传播的结果。

## 3.1 定义网络
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


# 4 参考资料
* [What is PyTorch?](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py)
* [深度学习框架PyTorch入门与实践]

