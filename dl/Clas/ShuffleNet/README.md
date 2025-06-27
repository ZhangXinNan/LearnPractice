ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices

Xiangyu Zhang  Xinyu Zhou  Mengxiao Lin Jian Sun

Megvii Inc (Face++)


# 1 Introduction

# 2 Related Work

## Efficient Model Designs

## Group Convolution
The concept of group convolution, which was first introduced in AlexNet [21] for distributing the model over two GPUs, has been well demonstrated its effectiveness in ResNeXt [40]. Depthwise separable convolution proposed in Xception [3] generalizes the ideas of separable convolutions in Inception series [34, 32]. Recently, MobileNet [12] utilizes the depthwise separable convolutions and gains state-of-the-art results among lightweight models. Our work generalizes group convolution and depthwise separable convolution in a novel form.

组卷积的概念最早在 AlexNet [21] 中提出，用于将模型分布在两块 GPU 上，并在 ResNeXt [40] 中得到了充分的验证。Xception [3] 中提出的深度可分离卷积推广了 Inception 系列 [34, 32] 中可分离卷积的思想。最近，MobileNet [12] 利用深度可分离卷积，在轻量级模型中获得了最佳效果。我们的工作以一种新颖的形式推广了组卷积和深度可分离卷积。

## Channel Shuffle Operation
To the best of our knowledge, the idea of channel shuffle operation is rarely mentioned in previous work on efficient model design, although CNN library cuda-convnet [20] supports “random sparse convolution” layer, which is equivalent to random channel shuffle followed by a group convolutional layer. Such “random shuffle” operation has different purpose and been seldom exploited later. Very recently, another concurrent work[41] also adopt this idea for a two-stage convolution. However, [41] did not specially investigate the effectiveness of channel shuffle itself and its usage in tiny model design.

据我们所知，尽管 CNN 库 cuda-convnet [20] 支持“随机稀疏卷积”层（相当于先进行随机通道重排，然后再进行组卷积），但在先前关于高效模型设计的研究中，通道重排操作的思想却​​很少被提及。这种“随机重排”操作的用途不同，后来很少被利用。最近，另一项同期研究 [41] 也采用了这种思想，用于两阶段卷积。然而，[41] 并没有专门研究通道重排本身的有效性及其在微型模型设计中的应用。

## Model Acceleration
This direction aims to accelerate inference
while preserving accuracy of a pre-trained model.
Pruning network connections [6, 7] or channels [38] reduces
redundant connections in a pre-trained model while
maintaining performance. Quantization [31, 27, 39, 45, 44]
and factorization [22, 16, 18, 37] are proposed in literature
to reduce redundancy in calculations to speed up inference.
Without modifying the parameters, optimized convolution
algorithms implemented by FFT [25, 35] and other
methods [2] decrease time consumption in practice. Distilling
[11] transfers knowledge from large models into small
ones, which makes training small models easier.


# 3 Approach
## 3.1 Channel Shuffle for Group Convolutions

Modern convolutional neural networks [30, 33, 34, 32, 9, 10] usually consist of repeated building blocks with the same structure. Among them, state-of-the-art networks such as Xception [3] and ResNeXt [40] introduce efficient depthwise separable convolutions or group convolutions into the building blocks to strike an excellent trade-off between representation capability and computational cost. However, we notice that both designs do not fully take the $1 \times 1$ convolutions (also called pointwise convolutions in [12]) into account, which require considerable complexity. For example, in ResNeXt [40] only $3 \times 3$ layers are equipped with group convolutions. As a result, for each residual unit in ResNeXt the pointwise convolutions occupy 93.4% multiplication-adds (cardinality = 32 as suggested in [40]). In tiny networks, expensive pointwise convolutions result in limited number of channels to meet the complexity constraint, which might significantly damage the accuracy.

现代卷积神经网络 [30, 33, 34, 32, 9, 10] 通常由具有相同结构的重复构建块构成。其中，诸如 Xception [3] 和 ResNeXt [40] 等最先进的网络在构建块中引入了高效的深度可分离卷积或组卷积，以在表示能力和计算成本之间取得良好的平衡。然而，我们注意到，这两种设计都没有充分考虑 1 × 1 卷积（在 [12] 中也称为**逐点卷积**），这需要相当大的复杂度。例如，在 ResNeXt [40] 中，只有 3 × 3 层配备了组卷积。因此，对于 ResNeXt 中的每个残差单元，逐点卷积占用了 93.4% 的乘加运算（基数 = 32，如 [40] 中建议的）。在微型网络中，昂贵的逐点卷积会导致有限数量的通道满足复杂性约束，这可能会严重损害准确性。


To address the issue, a straightforward solution is to apply channel sparse connections, for example group convolutions, also on $1 \times 1$ layers. By ensuring that each convolution operates only on the corresponding input channel group, group convolution significantly reduces computation cost. However, if multiple group convolutions stack together, there is one side effect: outputs from a certain channel are only derived from a small fraction of input channels. Fig 1 (a) illustrates a situation of two stacked group convolution layers. It is clear that outputs from a certain group only relate to the inputs within the group. This property blocks information flow between channel groups and weakens representation.

为了解决这个问题，一个直接的解决方案是应用通道稀疏连接，例如组卷积，同样应用于$1 \times 1$层。通过确保每个卷积仅作用于相应的输入通道组，组卷积显著降低了计算成本。然而，如果多个组卷积堆叠在一起，则会产生一个副作用：特定通道的输出仅来自一小部分输入通道。图 1 (a) 展示了两个堆叠的组卷积层的情况。很明显，特定组的输出仅与组内的输入相关。此属性阻碍了通道组之间的信息流动，并削弱了表征。




If we allow group convolution to obtain input data from
different groups (as shown in Fig 1 (b)), the input and output
channels will be fully related. Specifically, for the feature
map generated from the previous group layer, we can
first divide the channels in each group into several subgroups,
then feed each group in the next layer with different
subgroups. This can be efficiently and elegantly implemented
by a channel shuffle operation (Fig 1 (c)): suppose
a convolutional layer with g groups whose output has
$g \times n$ channels; we first reshape the output channel dimension
into $(g, n)$, transposing and then flattening it back as
the input of next layer. Note that the operation still takes
effect even if the two convolutions have different numbers
of groups. Moreover, channel shuffle is also differentiable,
which means it can be embedded into network structures for
end-to-end training.


如果我们允许组卷积从不同的组中获取输入数据（如图 1 (b) 所示），则输入和输出通道将完全相关。具体而言，对于前一个组层生成的特征图，我们可以首先将每个组中的通道划分为多个子组，然后将不同的子组输入到下一层的每个组中。这可以通过通道重排 (channel shuffle) 操作高效而优雅地实现（图 1 (c)）：假设一个卷积层包含 g 个组，其输出包含 $g \times n$ 个通道；我们首先将输出通道维度 reshape 为 $(g, n)$，然后进行转置，最后将其展平回原位作为下一层的输入。需要注意的是，即使两个卷积的组数不同，该操作仍然有效。此外，通道重排也是可微的，这意味着它可以嵌入到网络结构中进行端到端训练。


## 3.2. ShuffleNet Unit


Taking advantage of the channel shuffle operation, we propose a novel ShuffleNet unit specially designed for small networks. We start from the design principle of bottleneck unit [9] in Fig 2 (a). It is a residual block. In its residual branch, for the $3 \times 3$ layer, we apply a computational economical $3 \times 3$ depthwise convolution [3] on the bottleneck feature map. Then, we replace the first $1 \times 1$ layer with pointwise group convolution followed by a channel shuffle operation, to form a ShuffleNet unit, as shown in Fig 2 (b). The purpose of the second pointwise group convolution is to recover the channel dimension to match the shortcut path. For simplicity, we do not apply an extra channel shuffle operation after the second pointwise layer as it results in comparable scores. The usage of batch normalization (BN) [15] and nonlinearity is similar to [9, 40], except that we do not use ReLU after depthwise convolution as suggested by [3]. As for the case where ShuffleNet is applied with stride, we simply make two modifications (see Fig 2 (c)): (i) add a $3 \times 3$ average pooling on the shortcut path; (ii) replace the element-wise addition with channel concatenation, which makes it easy to enlarge channel dimension with little extra computation cost.

利用通道重排操作，我们提出了一种专为小型网络设计的新型 ShuffleNet 单元。我们从图 2 (a) 中瓶颈单元 [9] 的设计原理出发。它是一个残差块。在其残差分支中，对于 $3 \times 3$ 层，我们在瓶颈特征图上应用计算成本较低的 $3 \times 3$ 深度卷积 [3]。然后，我们将第一个 $1 \times 1$ 层替换为逐点组卷积，然后再进行通道重排操作，以形成 ShuffleNet 单元，如图 2 (b) 所示。第二个逐点组卷积的目的是恢复通道维度以匹配快捷路径。为简单起见，我们不在第二个逐点层之后应用额外的通道重排操作，因为这会导致类似的得分。批量归一化 (BN) [15] 和非线性的使用与 [9, 40] 类似，只是我们没有像 [3] 建议的那样在深度卷积后使用 ReLU。对于使用步幅的 ShuffleNet 的情况，我们只需做两处修改（见图 2（c））：（i）在捷径上添加一个 $3 \times 3$ 平均池化；（ii）用通道连接代替逐元素加法，这样可以轻松扩大通道维度，且几乎不会增加计算成本。




