
MobileNetV2: Inverted Residuals and Linear Bottlenecks
_____

Mark Sandler Andrew Howard Menglong Zhu Andrey Zhmoginov Liang-Chieh Chen

Google Inc.

fsandler, howarda, menglong, azhmogin, lccheng@google.com

# 0 Abstract

# 1. Introduction

Neural networks have revolutionized many areas of
machine intelligence, enabling superhuman accuracy for
challenging image recognition tasks. However, the drive
to improve accuracy often comes at a cost: modern state
of the art networks require high computational resources
beyond the capabilities of many mobile and embedded applications.

神经网络彻底改变了机器智能的诸多领域，使其在高难度图像识别任务中达到超越人类的准确率。然而，提升准确率的动力往往伴随着代价：现代最先进的神经网络需要大量的计算资源，这超出了许多移动和嵌入式应用的能力。

This paper introduces a new neural network architecture
that is specifically tailored for mobile and resource
constrained environments. Our network pushes the state
of the art for mobile tailored computer vision models,
by significantly decreasing the number of operations and
memory needed while retaining the same accuracy.

本文介绍了一种专为移动和资源受限环境量身定制的新型神经网络架构。我们的网络在保持相同准确率的同时，显著减少了所需的运算次数和内存，从而推动了移动定制计算机视觉模型的最新发展。

Our main contribution is a novel layer module: the
inverted residual with linear bottleneck. This module
takes as an input a low-dimensional compressed
representation which is first expanded to high dimension
and filtered with a lightweight depthwise convolution.
Features are subsequently projected back to a
low-dimensional representation with a linear convolution.
The official implementation is available as part of
TensorFlow-Slim model library in [4].

我们的主要贡献是一个新颖的层模块：带线性瓶颈的反向残差。该模块以低维压缩表示作为输入，首先将其扩展到高维，然后用轻量级的深度卷积进行滤波。然后，通过线性卷积将特征投影回低维表示。
官方实现可作为[4]中TensorFlow-Slim模型库的一部分获取。

This module can be efficiently implemented using
standard operations in any modern framework and allows
our models to beat state of the art along multiple
performance points using standard benchmarks. Furthermore,
this convolutional module is particularly suitable
for mobile designs, because it allows to significantly
reduce the memory footprint needed during inference
by never fully materializing large intermediate
tensors. This reduces the need for main memory access
in many embedded hardware designs, that provide small
amounts of very fast software controlled cache memory.


该模块可以使用任何现代框架中的标准操作高效实现，并使我们的模型在多个性能点上使用标准基准测试超越现有技术水平。此外，该卷积模块特别适用于移动设计，因为它无需完全实现大型中间张量，从而显著减少推理过程中所需的内存占用。这减少了许多嵌入式硬件设计中对主内存访问的需求，这些设计提供了少量非常快速的软件控制缓存。

# 2. Related Work

Tuning deep neural architectures to strike an optimal
balance between accuracy and performance has been
an area of active research for the last several years.
Both manual architecture search and improvements in
training algorithms, carried out by numerous teams has
lead to dramatic improvements over early designs such
as AlexNet [5], VGGNet [6], GoogLeNet [7]. , and
ResNet [8]. Recently there has been lots of progress
in algorithmic architecture exploration included hyperparameter
optimization [9, 10, 11] as well as various
methods of network pruning [12, 13, 14, 15, 16, 17] and
connectivity learning [18, 19]. A substantial amount of
work has also been dedicated to changing the connectivity
structure of the internal convolutional blocks such as
in ShuffleNet [20] or introducing sparsity [21] and others [22].

近年来，调整深度神经架构以在准确率和性能之间取得最佳平衡一直是一个活跃的研究领域。
众多团队通过手动架构搜索和训练算法的改进，取得了显著的改进，这些改进甚至超过了早期的设计，例如 AlexNet [5]、VGGNet [6]、GoogLeNet [7] 和 ResNet [8]。
最近，算法架构探索取得了许多进展，包括超参数优化 [9, 10, 11] 以及各种网络剪枝方法 [12, 13, 14, 15, 16, 17] 和连接学习 [18, 19]。
此外，还有大量工作致力于改变内部卷积块的连接结构，例如 ShuffleNet [20] 中的连接结构，或引入稀疏性 [21] 等 [22]。

Recently, [23, 24, 25, 26], opened up a new direction of bringing optimization methods including genetic algorithms and reinforcement learning to architectural search.
However one drawback is that the resulting networks end up very complex.
In this paper, we pursue the goal of developing better intuition about how neural networks operate and use that to guide the simplest possible network design.
Our approach should be seen as complimentary to the one described in [23] and related work.
In this vein our approach is similar to those taken by [20, 22] and allows to further improve the performance, while providing a glimpse on its internal operation.
Our network design is based on MobileNetV1 [27].
It retains its simplicity and does not require any special operators while significantly improves its accuracy, achieving state of the art on multiple image classification and detection tasks for mobile applications.


最近，[23, 24, 25, 26] 开辟了将遗传算法和强化学习等优化方法引入架构搜索的新方向。
然而，其缺点是最终的网络会变得非常复杂。
在本文中，我们的目标是更好地理解神经网络的运作方式，并以此指导尽可能简单的网络设计。
我们的方法应被视为对 [23] 及相关工作中描述的方法的补充。
在这方面，我们的方法与 [20, 22] 中的方法类似，并且能够进一步提升性能，同时还能一窥其内部运作。
我们的网络设计基于 MobileNetV1 [27]。
它保留了其简单性，不需要任何特殊的算子，同时显著提高了准确率，在移动应用的多个图像分类和检测任务中达到了最佳水平。





# 3. Preliminaries, discussion and intuition
## 3.1. Depthwise Separable Convolutions

## 3.2 Linear Bottlenecks 线性瓶颈
Consider a deep neural network consisting of n layers
$L_i$ each of which has an activation tensor of dimensions
$h_i \times w_i \times di$. Throughout this section we will be discussing
the basic properties of these activation tensors,
which we will treat as containers of $h_i \times w_i$ “pixels”
with $d_i$ dimensions. Informally, for an input set of real
images, we say that the set of layer activations (for any
layer $L_i$) forms a “manifold of interest”. It has been long
assumed that manifolds of interest in neural networks
could be embedded in low-dimensional subspaces. In
other words, when we look at all individual d-channel
pixels of a deep convolutional layer, the information
encoded in those values actually lie in some manifold,
which in turn is embeddable into a low-dimensional subspace 2.

考虑一个由 n 层 $L_i$ 组成的深度神经网络，每层都有一个维度为 $h_i \times w_i \times di$ 的激活张量。本节将讨论这些激活张量的基本属性，我们将其视为维度为 $d_i$ 的 $h_i \times w_i$ 个“像素”的容器。
通俗地讲，对于一组真实图像的输入，我们称层激活值集合（对于任意层 $L_i$）构成一个“感兴趣流形”。
长期以来，人们一直认为神经网络中感兴趣的流形可以嵌入到低维子空间中。
换句话说，当我们观察深度卷积层的所有 d 通道像素时，这些值所编码的信息实际上位于某个流形中，而这个流形又可以嵌入到低维子空间 2 中。



At a first glance, such a fact could then be captured
and exploited by simply reducing the dimensionality of
a layer thus reducing the dimensionality of the operating
space. This has been successfully exploited by
MobileNetV1 [27] to effectively trade off between computation
and accuracy via a width multiplier parameter,
and has been incorporated into efficient model designs
of other networks as well [20]. Following that intuition,
the width multiplier approach allows one to reduce the
dimensionality of the activation space until the manifold
of interest spans this entire space. However, this
intuition breaks down when we recall that deep convolutional
neural networks actually have non-linear per coordinate
transformations, such as ReLU. For example,
ReLU applied to a line in 1D space produces a ’ray’,
where as in $R^n$ space, it generally results in a piece-wise
linear curve with n-joints.

乍一看，只需降低某一层的维数，即可捕捉并利用这一事实，从而降低操作空间的维数。MobileNetV1 [27] 已成功利用这一原理，通过宽度乘数参数有效地在计算量和准确率之间进行权衡，并且该原理也已被纳入其他网络的高效模型设计中 [20]。遵循这一直觉，宽度乘数方法可以降低激活空间的维数，直到目标流形覆盖整个空间。然而，当我们回想起深度卷积神经网络实际上具有非线性的坐标变换（例如 ReLU）时，这种直觉就站不住脚了。例如，在一维空间中，将 ReLU 应用于一条直线会产生一条“射线”，而在 $R^n$ 空间中，它通常会生成一条具有 n 个节点的分段线性曲线。

It is easy to see that in general if a result of a layer
transformation ReLU(Bx) has a non-zero volume S,
the points mapped to interior S are obtained via a linear
transformation B of the input, thus indicating that
the part of the input space corresponding to the full dimensional
output, is limited to a linear transformation.
In other words, deep networks only have the power of
a linear classifier on the non-zero volume part of the
output domain. We refer to supplemental material for
a more formal statement.

很容易看出，一般来说，如果层变换 ReLU(Bx) 的结果具有非零体积 S，则映射到内部 S 的点是通过对输入进行线性变换 B 获得的，这表明，输入空间中与全维输出对应的部分仅限于线性变换。
换句话说，深度网络仅在输出域的非零体积部分具有线性分类器的能力。有关更正式的表述，请参阅补充材料。

On the other hand, when ReLU collapses the channel,
it inevitably loses information in that channel. However
if we have lots of channels, and there is a a structure
in the activation manifold that information might still be
preserved in the other channels. In supplemental materials,
we show that if the input manifold can be embedded
into a significantly lower-dimensional subspace
of the activation space then the ReLU transformation
preserves the information while introducing the needed
complexity into the set of expressible functions.

另一方面，当 ReLU 折叠通道时，
它不可避免地会丢失该通道中的信息。然而，
如果我们有很多通道，并且激活流形中存在一个结构，
那么信息可能仍然保留在其他通道中。在补充材料中，
我们证明了，如果输入流形可以嵌入到
激活空间中一个维度明显较低的子空间中，
那么 ReLU 变换
就能保留信息，同时为可表达函数集引入所需的
复杂性。

To summarize, we have highlighted two properties
that are indicative of the requirement that the manifold
of interest should lie in a low-dimensional subspace of
the higher-dimensional activation space:
1. If the manifold of interest remains non-zero volume
after ReLU transformation, it corresponds to
a linear transformation.
2. ReLU is capable of preserving complete information
about the input manifold, but only if the input
manifold lies in a low-dimensional subspace of the
input space.

总而言之，我们强调了两个属性，它们表明目标流形应该位于高维激活空间的低维子空间中：
1. 如果目标流形在 ReLU 变换后仍然保持非零体积，则它对应于线性变换。
2. ReLU 能够保留关于输入流形的完整信息，但前提是输入流形位于输入空间的低维子空间中。

These two insights provide us with an empirical hint
for optimizing existing neural architectures: assuming
the manifold of interest is low-dimensional we can capture
this by inserting linear bottleneck layers into the
convolutional blocks. Experimental evidence suggests
that using linear layers is crucial as it prevents nonlinearities
from destroying too much information. In
Section 6, we show empirically that using non-linear
layers in bottlenecks indeed hurts the performance by
several percent, further validating our hypothesis 3. We
note that similar reports where non-linearity was helped
were reported in [29] where non-linearity was removed
from the input of the traditional residual block and that
lead to improved performance on CIFAR dataset.

这两个洞见为我们优化现有神经架构提供了经验提示：假设我们感兴趣的流形是低维的，我们可以通过在卷积块中插入线性瓶颈层来捕捉这一点。实验证据表明，使用线性层至关重要，因为它可以防止非线性层破坏过多信息。在第六部分，我们通过经验证明，在瓶颈层中使用非线性层确实会使性能降低几个百分点，这进一步验证了我们的假设3。我们注意到，[29] 中也报告了类似的报告，报告指出非线性层有助于提升性能，即从传统残差块的输入中移除非线性层，从而提升了 CIFAR 数据集上的性能。

For the remainder of this paper we will be utilizing
bottleneck convolutions. We will refer to the ratio between
the size of the input bottleneck and the inner size
as the expansion ratio.

在本文的其余部分，我们将使用瓶颈卷积。我们将输入瓶颈的大小与内部大小的比率称为扩展率。


## 3.3. Inverted residuals

The bottleneck blocks appear similar to residual
block where each block contains an input followed
by several bottlenecks then followed by expansion [8].
However, inspired by the intuition that the bottlenecks
actually contain all the necessary information, while an
expansion layer acts merely as an implementation detail
that accompanies a non-linear transformation of the tensor,
we use shortcuts directly between the bottlenecks.

瓶颈块看起来类似于残差块，其中每个块包含一个输入，后跟多个瓶颈，然后是扩展 [8]。
然而，受瓶颈实际上包含所有必要信息的直觉启发，
而扩展层仅仅是伴随张量非线性变换的实现细节，
因此，我们直接在瓶颈之间使用快捷方式。



Figure 3 provides a schematic visualization of the difference in the designs. The motivation for inserting shortcuts is similar to that of classical residual connections: we want to improve the ability of a gradient to propagate across multiplier layers. However, the inverted design is considerably more memory efficient (see Section 5 for details), as well as works slightly better in our experiments.

图 3 以示意图的形式展示了两种设计之间的差异。插入快捷方式的动机与经典残差连接类似：我们希望提升梯度在乘法器层间的传播能力。然而，反向设计的内存效率更高（详情请参阅第 5 节），并且在我们的实验中效果也略胜一筹。


**Running time and parameter count for bottleneck convolution**

The basic implementation structure is illustrated
in Table 1. For a block of size $h \times w$, expansion
factor t and kernel size $k$ with $d'$ input channels
and $d''$ output channels, the total number of multiply
add required is $h \cdot  w \cdot d' \cdot t(d' + k^2 + d'')$. Compared
with (1) this expression has an extra term, as indeed
we have an extra $1 \times 1$ convolution, however the
nature of our networks allows us to utilize much smaller
input and output dimensions. In Table 3 we compare the
needed sizes for each resolution between MobileNetV1,
MobileNetV2 and ShuffleNet.

**瓶颈卷积的运行时间和参数数量**

表 1 展示了其基本实现结构。对于一个大小为 $h \times w$、扩展因子为 t、核大小为 $k$ 且输入通道数为 $d'$ 个、输出通道数为 $d''$ 个的块，所需的乘加运算次数为 $h \cdot  w \cdot d' \cdot t(d' + k^2 + d'')$。与 (1) 式相比，该表达式多了一个项，因为我们确实多了一个 $1 \times 1$ 卷积，但是，由于我们网络的特性，我们可以使用更小的输入和输出维度。表 3 比较了 MobileNetV1、MobileNetV2 和 ShuffleNet 在不同分辨率下所需的尺寸。

