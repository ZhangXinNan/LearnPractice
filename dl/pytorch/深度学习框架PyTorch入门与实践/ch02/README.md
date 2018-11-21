
### 2.2.1 Tensor
Tensor和numpy的ndarrays类似，但是Tensor可以使用GPU加速。
函数名后面带下划线的函数会修改Tensor本身。
Tensor和numpy对象共享内存。
```python
# tensor -> numpy
b = a.numpy()
# Numpy -> tensor
b = t.from_numpy(a)
# 通过.cuda方法转为GPU的Tensor
x = x.cuda()
```

### 2.2.2 Autograd: 自动微分
Autograd.Variable 是Autograd的核心类，封装了Tensor。
Variable的三个属性：
* data 保存了Variable的Tensor。
* grad 保存data对应的梯度，grad也是一个Variable ?
* grad_fn 指向一个Function对象，这个Function用来计算反向传播计算输入的梯度。


### 2.2.3 神经网络
torch.nn用来定义和运行神经网络。
nn.Module看作是一个网络的封装，包含各层定义及forward方法，调用forward(input)，可返回前向传播的结果。

#### 定义网络
可学习的层放到__init__中。
nn.Module子类的构造函数必须在构造函数中执行父类的构造函数。
```
nn.Module.__init__(self)
# or
super(Net, self).__init__()
```


网络可学习参数通过net.parameters()返回。 


