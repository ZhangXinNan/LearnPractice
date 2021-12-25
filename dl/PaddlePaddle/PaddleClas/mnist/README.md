
# MLP

```
download training data and load training data
load finished
---------------------------------------------------------------------------
 Layer (type)       Input Shape          Output Shape         Param #
===========================================================================
   Flatten-1      [[1, 1, 28, 28]]         [1, 784]              0
   Linear-1          [[1, 784]]            [1, 100]           78,500
    ReLU-1           [[1, 100]]            [1, 100]              0
   Linear-2          [[1, 100]]            [1, 100]           10,100
    ReLU-2           [[1, 100]]            [1, 100]              0
   Linear-3          [[1, 100]]            [1, 10]             1,010
===========================================================================
Total params: 89,610
Trainable params: 89,610
Non-trainable params: 0
---------------------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.01
Params size (MB): 0.34
Estimated Total Size (MB): 0.35
---------------------------------------------------------------------------

The loss value printed in the log is the current step, and the metric is the average value of previous steps.
Epoch 1/5
/opt/anaconda3/envs/py37_paddle/lib/python3.7/site-packages/paddle/fluid/layers/utils.py:77: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working
  return (isinstance(seq, collections.Sequence) and
step 938/938 [==============================] - loss: 0.2819 - acc: 0.8935 - 10ms/step
Epoch 2/5
step 938/938 [==============================] - loss: 0.1411 - acc: 0.9473 - 10ms/step
Epoch 3/5
step 938/938 [==============================] - loss: 0.0362 - acc: 0.9599 - 10ms/step
Epoch 4/5
step 938/938 [==============================] - loss: 0.0216 - acc: 0.9649 - 10ms/step
Epoch 5/5
step 938/938 [==============================] - loss: 0.2609 - acc: 0.9706 - 11ms/step
Eval begin...
step 10000/10000 [==============================] - loss: 1.0181e-04 - acc: 0.9687 - 2ms/step
Eval samples: 10000
{'loss': [0.000101809914], 'acc': 0.9687}
```

# LeNet
```
2.2.1
Running verify PaddlePaddle program ...
PaddlePaddle works well on 1 CPU.
W1225 22:08:42.012818 354143680 fuse_all_reduce_op_pass.cc:76] Find all_reduce operators: 2. To make the speed faster, some all_reduce ops are fused during training, after fusion, the number of all_reduce ops is 2.
PaddlePaddle works well on 2 CPUs.
PaddlePaddle is installed successfully! Let's start deep learning with PaddlePaddle now.
None
download training data and load training data
load finished
---------------------------------------------------------------------------
 Layer (type)       Input Shape          Output Shape         Param #
===========================================================================
   Conv2D-1       [[1, 1, 28, 28]]      [1, 6, 28, 28]          156
  MaxPool2D-1     [[1, 6, 28, 28]]      [1, 6, 14, 14]           0
   Conv2D-2       [[1, 6, 14, 14]]     [1, 16, 10, 10]         2,416
  MaxPool2D-2    [[1, 16, 10, 10]]      [1, 16, 5, 5]            0
   Linear-1          [[1, 400]]            [1, 120]           48,120
   Linear-2          [[1, 120]]            [1, 84]            10,164
   Linear-3          [[1, 84]]             [1, 10]              850
===========================================================================
Total params: 61,706
Trainable params: 61,706
Non-trainable params: 0
---------------------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.06
Params size (MB): 0.24
Estimated Total Size (MB): 0.30
---------------------------------------------------------------------------

The loss value printed in the log is the current step, and the metric is the average value of previous steps.
Epoch 1/5
/opt/anaconda3/envs/py37_paddle/lib/python3.7/site-packages/paddle/fluid/layers/utils.py:77: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3,and in 3.9 it will stop working
  return (isinstance(seq, collections.Sequence) and
step 938/938 [==============================] - loss: 0.0596 - acc: 0.9486 - 22ms/step
Epoch 2/5
step 938/938 [==============================] - loss: 0.0134 - acc: 0.9815 - 22ms/step
Epoch 3/5
step 938/938 [==============================] - loss: 0.0033 - acc: 0.9873 - 21ms/step
Epoch 4/5
step 938/938 [==============================] - loss: 0.1117 - acc: 0.9892 - 21ms/step
Epoch 5/5
step 938/938 [==============================] - loss: 0.0149 - acc: 0.9915 - 21ms/step
Eval begin...
step 10000/10000 [==============================] - loss: 3.5763e-06 - acc: 0.9881 - 2ms/step
Eval samples: 10000
{'loss': [3.576285e-06], 'acc': 0.9881}
```


