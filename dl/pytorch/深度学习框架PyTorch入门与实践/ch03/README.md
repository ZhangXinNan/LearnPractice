《深度学习框架PyTorch入门与实践》
# 3 Tensor和autograd

## 3.1 Tensor
PyTorch的tensor支持GPU加速。

### 3.1.1 基础操作
从接口角度，对tensor的操作分为:
(1) torch.function
(2) tensor.function

从存储角度：
(1) a.add(b)
(2) a.add_(b)

以_结尾的都 是inplace操作，即会修改调用者自己的数据。

## 3.2 autograd

### 3.2.1 Variable
Variable 封装了Tensor，包括三个属性：
(1) data
(2) grad
(3) grad_fn

