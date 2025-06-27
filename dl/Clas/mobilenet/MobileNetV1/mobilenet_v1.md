# 0 摘要

- depthwise separable convolutions
  - 大大减少运算量和参数数量
- two simple global hyperparameters
  - width
  - depth

# 1 介绍

## 1.1 背景
1. CNN越来越流行
2. 倾向于越来越深和越来越复杂的结构来提升准确率，没有考虑模型大小和速度
3. 现实世界中有些应用需要小且快的模型

## 1.2 怎么做的
1. 高效的网络结构
2. 两个超参数使模型更小、更低延迟


# 2 早先工作

MobileNets是第一个关注低延迟且小尺寸的模型。


# 3 MobileNet Architecture
## 3.1 Depthwise Separable Convolution
## 3.2 Network Structure and Training

The MobileNet structure is built on depthwise separable convolutions as mentioned in the previous section except for the first layer which is a full convolution. By defining the network in such simple terms we are able to easily explore network topologies to find a good network. The MobileNet architecture is defined in Table 1. All layers are followed by a batchnorm [13] and ReLU nonlinearity with the exception of the final fully connected layer which has no nonlinearity and feeds into a softmax layer for classification. Figure 3 contrasts a layer with regular convolutions, batchnorm and ReLU nonlinearity to the factorized layer with depthwise convolution, 1x1 pointwise convolution as well as batchnorm and ReLU after each convolutional layer. Down sampling is handled with strided convolution in the depthwise convolutions as well as in the first layer. A final average pooling reduces the spatial resolution to 1 before the fully connected layer. Counting depthwise and pointwise convolutions as separate layers, MobileNet has 28 layers.

MobileNet 结构建立在深度可分离卷积之上，如上文所述，但第一层除外，它是全卷积。通过用如此简单的术语定义网络，我们能够轻松探索网络拓扑以找到良好的网络。MobileNet 架构定义如表 1 所示。所有层后都跟有批量归一化 [13] 和 ReLU 非线性，但最后的全连接层除外，该层没有非线性，并输入到 softmax 层进行分类。图 3 对比了具有常规卷积、批量归一化和 ReLU 非线性的层与具有深度卷积、1x1 逐点卷积以及每个卷积层后的批量归一化和 ReLU 的分解层。在深度卷积和第一层中，使用步幅卷积进行下采样。最终的平均池化在全连接层之前将空间分辨率降低到 1。将深度卷积和逐点卷积算作单独的层，MobileNet 共有 28 层。


It is not enough to simply define networks in terms of a small number of Mult-Adds. It is also important to make sure these operations can be efficiently implementable. For instance unstructured sparse matrix operations are not typically faster than dense matrix operations until a very high level of sparsity. Our model structure puts nearly all of the computation into dense 1x1 convolutions. This can be implemented with highly optimized general matrix multiply (GEMM) functions. Often convolutions are implemented by a GEMM but require an initial reordering in memory called im2col in order to map it to a GEMM. For instance, this approach is used in the popular Caffe package [15]. 1x1 convolutions do not require this reordering in memory and can be implemented directly with GEMM which is one of the most optimized numerical linear algebra algorithms. MobileNet spends 95% of it’s computation time in 1x1 convolutions which also has 75% of the parameters as can be seen in Table 2. Nearly all of the additional parameters are in the fully connected layer.

仅仅用少量的 Mult-Adds 来定义网络是不够的。确保这些操作能够高效实现也很重要。例如，非结构化稀疏矩阵运算通常不比密集矩阵运算更快，除非稀疏度非常高。我们的模型结构将几乎所有的计算都放入密集的 1x1 卷积中。这可以通过高度优化的通用矩阵乘法 (GEMM) 函数来实现。卷积通常由 GEMM 实现，但需要在内存中进行初始重新排序（称为 im2col）才能将其映射到 GEMM。例如，流行的 Caffe 包 [15] 中就使用了这种方法。1x1 卷积不需要在内存中进行这种重新排序，可以直接用 GEMM 实现，GEMM 是最优化的数值线性代数算法之一。 MobileNet 将 95% 的计算时间花在 1x1 卷积上，并且该卷积也具有 75% 的参数，如表 2 所示。几乎所有附加参数都在完全连接层中。

MobileNet models were trained in TensorFlow [1] using RMSprop [33] with asynchronous gradient descent similar to Inception V3 [31]. However, contrary to training large models we use less regularization and data augmentation techniques because small models have less trouble with overfitting. When training MobileNets we do not use side heads or label smoothing and additionally reduce the amount image of distortions by limiting the size of small crops that are used in large Inception training [31]. Additionally, we found that it was important to put very little or no weight decay (l2 regularization) on the depthwise filters since their are so few parameters in them. For the ImageNet benchmarks in the next section all models were trained with same training parameters regardless of the size of the model.




## 3.3 Width Multiplier: Thinner Models

Although the base MobileNet architecture is already small and low latency, many times a specific use case or application may require the model to be smaller and faster. In order to construct these smaller and less computationally expensive models we introduce a very simple parameter  $\alpha$ called width multiplier. The role of the width multiplier $\alpha$  is to thin a network uniformly at each layer. For a given layer and width multiplier $\alpha$ , the number of input channels $M$ becomes  $\alpha M$ and the number of output channels $N$ becomes $\alpha N$.

## 3.4 Resolution Multiplier: Reduced Representation

The second hyper-parameter to reduce the computational cost of a neural network is a resolution multiplier $\rho$. We apply this to the input image and the internal representation of every layer is subsequently reduced by the same multiplier. In practice we implicitly set $\rho$ by setting the input resolution.

