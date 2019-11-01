```python
%matplotlib inline
```


What is PyTorch?
================

It’s a Python-based scientific computing package targeted at two sets of
audiences:

-  A replacement for NumPy to use the power of GPUs
-  a deep learning research platform that provides maximum flexibility
   and speed

Getting Started
---------------

Tensors
^^^^^^^

Tensors are similar to NumPy’s ndarrays, with the addition being that
Tensors can also be used on a GPU to accelerate computing.




```python
from __future__ import print_function
import torch
print('version : ', torch.__version__)
```

    version :  1.3.0


<div class="alert alert-info"><h4>Note</h4><p>An uninitialized matrix is declared,
    but does not contain definite known
    values before it is used. When an
    uninitialized matrix is created,
    whatever values were in the allocated
    memory at the time will appear as the initial values.</p></div>



Construct a 5x3 matrix, uninitialized:




```python
x = torch.empty(5, 3)
print(x)
print(x.shape)
y = torch.Tensor(5, 3)
print(y)
print(y.size())
```

    tensor([[ 0.0000e+00, -1.5846e+29,  0.0000e+00],
            [-1.5846e+29,  1.8361e+25,  1.4603e-19],
            [ 1.6795e+08,  4.7423e+30,  4.7393e+30],
            [ 9.5461e-01,  4.4377e+27,  1.7975e+19],
            [ 4.6894e+27,  7.9463e+08,  3.2604e-12]])
    torch.Size([5, 3])
    tensor([[ 0.0000e+00,  0.0000e+00,  0.0000e+00],
            [ 0.0000e+00,  1.5417e-16,  1.4013e-45],
            [        nan,  6.8609e+22,  1.4013e-45],
            [ 0.0000e+00,  1.5716e-22,  2.8629e-42],
            [ 1.5646e-16,  1.4013e-45, -1.0471e-07]])
    torch.Size([5, 3])


Construct a randomly initialized matrix:




```python
x = torch.rand(5, 3)
print(x)
```

    tensor([[0.9999, 0.8515, 0.9452],
            [0.7062, 0.6893, 0.7615],
            [0.7981, 0.0418, 0.5584],
            [0.3330, 0.1955, 0.5286],
            [0.3754, 0.1722, 0.1421]])


Construct a matrix filled zeros and of dtype long:




```python
x = torch.zeros(5, 3, dtype=torch.long)
print(x)
y = torch.ones(5, 3, dtype=torch.float)
print(y)
```

    tensor([[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]])
    tensor([[1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.]])


Construct a tensor directly from data:




```python
x = torch.tensor([5.5, 3])
print(x)
```

    tensor([5.5000, 3.0000])


or create a tensor based on an existing tensor. These methods
will reuse properties of the input tensor, e.g. dtype, unless
new values are provided by user




```python
x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
print(x)

x = torch.randn_like(x, dtype=torch.float)    # override dtype!
print(x)                                      # result has the same size
```

    tensor([[1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.],
            [1., 1., 1.]], dtype=torch.float64)
    tensor([[ 0.3378,  0.7459,  0.0819],
            [ 1.6458, -0.0619, -0.8104],
            [-0.5626,  0.4126,  0.2850],
            [-0.5534, -0.4418,  1.2075],
            [ 0.4447,  0.6673,  0.7059]])


Get its size:




```python
print(x.size())
```

    torch.Size([5, 3])


<div class="alert alert-info"><h4>Note</h4><p>``torch.Size`` is in fact a tuple, so it supports all tuple operations.</p></div>

Operations
^^^^^^^^^^
There are multiple syntaxes for operations. In the following
example, we will take a look at the addition operation.

Addition: syntax 1




```python
y = torch.rand(5, 3)
print(x + y)
```

    tensor([[ 1.0878,  1.1113,  0.4764],
            [ 2.3734,  0.8463, -0.6719],
            [-0.0860,  0.5396,  1.0508],
            [ 0.0848,  0.3724,  1.4067],
            [ 0.5138,  0.7496,  1.1881]])


Addition: syntax 2




```python
print(torch.add(x, y))
```

    tensor([[ 1.0878,  1.1113,  0.4764],
            [ 2.3734,  0.8463, -0.6719],
            [-0.0860,  0.5396,  1.0508],
            [ 0.0848,  0.3724,  1.4067],
            [ 0.5138,  0.7496,  1.1881]])


Addition: providing an output tensor as argument




```python
result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)
```

    tensor([[ 1.0878,  1.1113,  0.4764],
            [ 2.3734,  0.8463, -0.6719],
            [-0.0860,  0.5396,  1.0508],
            [ 0.0848,  0.3724,  1.4067],
            [ 0.5138,  0.7496,  1.1881]])


Addition: in-place




```python
# adds x to y
y.add_(x)
print(y)
```

    tensor([[ 1.0878,  1.1113,  0.4764],
            [ 2.3734,  0.8463, -0.6719],
            [-0.0860,  0.5396,  1.0508],
            [ 0.0848,  0.3724,  1.4067],
            [ 0.5138,  0.7496,  1.1881]])


<div class="alert alert-info"><h4>Note</h4><p>Any operation that mutates a tensor in-place is post-fixed with an ``_``.
    For example: ``x.copy_(y)``, ``x.t_()``, will change ``x``.</p></div>

You can use standard NumPy-like indexing with all bells and whistles!




```python
print(x[:, 1])
```

    tensor([ 0.7459, -0.0619,  0.4126, -0.4418,  0.6673])


Resizing: If you want to resize/reshape tensor, you can use ``torch.view``:




```python
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())
```

    torch.Size([4, 4]) torch.Size([16]) torch.Size([2, 8])


If you have a one element tensor, use ``.item()`` to get the value as a
Python number




```python
x = torch.randn(1)
print(x)
print(x.item())
```

    tensor([-1.0126])
    -1.012573003768921


**Read later:**


  100+ Tensor operations, including transposing, indexing, slicing,
  mathematical operations, linear algebra, random numbers, etc.,
  are described
  `here <https://pytorch.org/docs/torch>`_.

NumPy Bridge
------------

Converting a Torch Tensor to a NumPy array and vice versa is a breeze.

The Torch Tensor and NumPy array will share their underlying memory
locations (if the Torch Tensor is on CPU), and changing one will change
the other.

Converting a Torch Tensor to a NumPy Array
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




```python
a = torch.ones(5)
print(a)
```

    tensor([1., 1., 1., 1., 1.])



```python
b = a.numpy()
print(b)
```

    [1. 1. 1. 1. 1.]


See how the numpy array changed in value.




```python
a.add_(1)
print(a)
print(b)
```

    tensor([2., 2., 2., 2., 2.])
    [2. 2. 2. 2. 2.]


Converting NumPy Array to Torch Tensor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See how changing the np array changed the Torch Tensor automatically




```python
import numpy as np
a = np.ones(5)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)
```

    [2. 2. 2. 2. 2.]
    tensor([2., 2., 2., 2., 2.], dtype=torch.float64)


All the Tensors on the CPU except a CharTensor support converting to
NumPy and back.

CUDA Tensors
------------

Tensors can be moved onto any device using the ``.to`` method.




```python
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
