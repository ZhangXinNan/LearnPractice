# 1 从0到1（使用几个命令来训练手写数字数据集）
## 1.1 下载数据、转换数据格式
设CAFFE_ROOT为caffe的安装路径。
```
cd $CAFFE_ROOT
./data/mnist/get_mnist.sh
./examples/mnist/create_mnist.sh
```
上述脚本中的内容完成的工作就是下载并转换数据，暂不做详细介绍。

## 1.2 训练
```
cd $CAFFE_ROOT
./examples/mnist/train_lenet.sh
```
### 训练命令：
```
caffe train -solver lenet_solver.prototxt -gpu 0 -log_dir ./
```
### 参数解释：
gpu : 指定用哪块GPU训练
log_dir : 指定log文件输出的路径。（这个路径必须事先存在）


# 2 训练过程
## 2.1 lenet_solver.prototxt
查看训练脚本：
```
➜  caffe git:(zxdev_mac) cat ./examples/mnist/train_lenet.sh
#!/usr/bin/env sh
set -e

./build/tools/caffe train --solver=examples/mnist/lenet_solver.prototxt $@
```

查看solver.prototxt
```
➜  caffe git:(zxdev_mac) cat examples/mnist/lenet_solver.prototxt
# The train/test net protocol buffer definition
net: "examples/mnist/lenet_train_test.prototxt"
# test_iter specifies how many forward passes the test should carry out.
# In the case of MNIST, we have test batch size 100 and 100 test iterations,
# covering the full 10,000 testing images.
# test_iter 指定test执行的时候迭代次数
test_iter: 100
# Carry out testing every 500 training iterations.
# 每训练多少次执行一次test
test_interval: 500
# The base learning rate, momentum and the weight decay of the network.
base_lr: 0.01
momentum: 0.9
weight_decay: 0.0005
# The learning rate policy
# inv 的学习策略，lr = base_lr * (1 + gamma * iter) ^ (-power)
lr_policy: "inv"
gamma: 0.0001
power: 0.75
# Display every 100 iterations
# 每迭代多少次显示 一次当前训练的信息，主要是loss和学习率
display: 100
# The maximum number of iterations
# 指定最大迭代次数
max_iter: 10000
# snapshot intermediate results
# 每迭代多少次保存一次模型的参数和训练状态。
snapshot: 5000
snapshot_prefix: "examples/mnist/lenet"
# solver mode: CPU or GPU
solver_mode: GPU
```

## 2.2 定义网络结构 lenet_train_val.prototxt
网络结构定义在examples/mnist/lenet_train_test.prototxt中。
```
➜  caffe git:(zxdev_mac) cat examples/mnist/lenet_train_test.prototxt
name: "LeNet"
layer {
  # 这一层的名字是mnist
  name: "mnist"
  # 这一层的类型是Data
  type: "Data"
  # 这一层产生两个blobs，分别是data blob和label blob
  top: "data"
  top: "label"
  include {
    phase: TRAIN
  }
  transform_param {
    # 此处还可添加mean_value，数据先减mean_value，再乘scale
    # mean_value: 128
    # 1/256.0 = 0.00390625，像素值控制在0到1之间。
    scale: 0.00390625
  }
  data_param {
    source: "examples/mnist/mnist_train_lmdb"
    # 指定训练阶段，每次迭代用50个。
    batch_size: 64
    backend: LMDB
  }
}
layer {
  name: "mnist"
  type: "Data"
  top: "data"
  top: "label"
  include {
    phase: TEST
  }
  transform_param {
    scale: 0.00390625
  }
  data_param {
    source: "examples/mnist/mnist_test_lmdb"
    batch_size: 100
    backend: LMDB
  }
}
layer {
  name: "conv1"
  type: "Convolution"
  bottom: "data"
  top: "conv1"
  # 卷积核学习率为基础学习率乘以 lr_mult
  param {
    lr_mult: 1
  }
  # 偏置学习率为基础学习率乘以 lr_mult
  param {
    lr_mult: 2
  }
  convolution_param {
    # 输出20个通道
    num_output: 20
    # 卷积核尺寸是5
    kernel_size: 5
    # 步长是1
    stride: 1
    # 随机初始化权重，用xavier算法，自动根据输入输出的数量来定初始化的比例
    weight_filler {
      type: "xavier"
    }
    # bais使用常数，默认用0填充。
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool1"
  type: "Pooling"
  bottom: "conv1"
  top: "pool1"
  pooling_param {
    pool: MAX
    # 池化核尺寸为2，步长为2
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "conv2"
  type: "Convolution"
  bottom: "pool1"
  top: "conv2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  convolution_param {
    num_output: 50
    kernel_size: 5
    stride: 1
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "pool2"
  type: "Pooling"
  bottom: "conv2"
  top: "pool2"
  pooling_param {
    pool: MAX
    kernel_size: 2
    stride: 2
  }
}
layer {
  name: "ip1"
  type: "InnerProduct"
  bottom: "pool2"
  top: "ip1"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 500
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
layer {
  name: "relu1"
  type: "ReLU"
  bottom: "ip1"
  top: "ip1"
}
layer {
  name: "ip2"
  type: "InnerProduct"
  bottom: "ip1"
  top: "ip2"
  param {
    lr_mult: 1
  }
  param {
    lr_mult: 2
  }
  inner_product_param {
    num_output: 10
    weight_filler {
      type: "xavier"
    }
    bias_filler {
      type: "constant"
    }
  }
}
# Accuracy层只用在验证、测试阶段，用于计算分类的准确率
layer {
  name: "accuracy"
  type: "Accuracy"
  bottom: "ip2"
  bottom: "label"
  top: "accuracy"
  include {
    phase: TEST
  }
}
layer {
  name: "loss"
  type: "SoftmaxWithLoss"
  # 没有输出，只是计算loss
  bottom: "ip2"
  bottom: "label"
  top: "loss"
}
```

# 3 查看训练过程中的准确率和loss
将log_dir指定路径下的日志重命名后缀为log，例如mnist_train.log。
在log_dir下生成准确率图片：
```
../tools/extra/plot_training_log.py.example 0 test_acc_vs_iters.png mnist_train.log
../tools/extra/plot_training_log.py.example 2 test_loss_vs_iters.png mnist_train.log
../tools/extra/plot_training_log.py.example 6 train_acc_vs_iters.png mnist_train.log
../tools/extra/plot_training_log.py.example 4 lr_vs_iters.png mnist_train.log
```