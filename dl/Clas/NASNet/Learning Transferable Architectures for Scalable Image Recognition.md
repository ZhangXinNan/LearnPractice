
# 1 Introduction

# 2 Related Work

# 3 Method

Our work makes use of search methods to find good convolutional architectures on a dataset of interest. The main search method we use in this work is the Neural Architecture Search (NAS) framework proposed by [71]. In NAS, a controller recurrent neural network (RNN) samples child networks with different architectures. The child networks are trained to convergence to obtain some accuracy on a held-out validation set. The resulting accuracies are used to update the controller so that the controller will generate better architectures over time. The controller weights are updated with policy gradient (see Figure 1).

我们的工作利用搜索方法在感兴趣的数据集上寻找合适的卷积架构。本文主要使用的搜索方法是 [71] 提出的神经架构搜索 (NAS) 框架。**在 NAS 中，控制器循环神经网络 (RNN) 对具有不同架构的子网络进行采样。** 子网络经过训练收敛，在保留的验证集上获得一定的准确率。得到的准确率用于更新控制器，使控制器随着时间的推移生成更优的架构。控制器权重通过策略梯度进行更新（见图 1）。


The main contribution of this work is the design of a novel search space, such that the best architecture found on the CIFAR-10 dataset would scale to larger, higherresolution image datasets across a range of computational settings. We name this search space the NASNet search space as it gives rise to NASNet, the best architecture found in our experiments. One inspiration for the NASNet search space is the realization that architecture engineering with CNNs often identifies repeated motifs consisting of combinations of convolutional filter banks, nonlinearities and a prudent selection of connections to achieve state-of-the-art results (such as the repeated modules present in the Inception and ResNet models [59, 20, 60, 58]). These observations suggest that it may be possible for the controller RNN to predict a generic convolutional cell expressed in terms of these motifs. This cell can then be stacked in series to handle inputs of arbitrary spatial dimensions and filter depth.

这项工作的主要贡献在于设计了一个新颖的搜索空间，使得在 CIFAR-10 数据集上找到的最佳架构能够扩展到更大、更高分辨率的图像数据集，并涵盖各种计算设置。我们将此搜索空间命名为 NASNet 搜索空间，因为它衍生出了 NASNet，这是我们在实验中发现的最佳架构。NASNet 搜索空间的设计灵感源于这样一个认识：CNN 的架构工程通常会识别出由卷积滤波器组、非线性函数和精心选择的连接组合而成的重复模体，从而实现最佳结果（例如 Inception 和 ResNet 模型中存在的重复模块 [59, 20, 60, 58]）。这些观察结果表明，**控制器 RNN 或许能够预测一个以这些模体为表达形式的通用卷积单元**。然后，该单元可以串联堆叠，以处理任意空间维度和滤波器深度的输入。

In our approach, the overall architectures of the convolutional nets are manually predetermined. They are composed of convolutional cells repeated many times where each convolutional cell has the same architecture, but different weights. To easily build scalable architectures for images of any size, we need two types of convolutional cells to serve two main functions when taking in a feature map as input: (1) convolutional cells that return a feature map of the same dimension, and (2) convolutional cells that return a feature map where the feature map height and width is reduced by a factor of two. We name the first type and second type of convolutional cells Normal Cell and Reduction Cell respectively. For the Reduction Cell, we make the initial operation applied to the cell’s inputs have a stride of two to reduce the height and width. All of our operations that we consider for building our convolutional cells have an option of striding.

在我们的方法中，卷积网络的整体架构是手动预先确定的。它们由多次重复的卷积单元组成，每个卷积单元具有相同的架构，但权重不同。为了轻松构建可扩展的架构以适应任意尺寸的图像，我们需要两种类型的卷积单元，在将特征图作为输入时实现两个主要功能：(1) 返回相同维度特征图的卷积单元；(​​2) 返回特征图高度和宽度减小一半的卷积单元。我们将第一类和第二类卷积单元分别命名为 **“普通单元”和“缩减单元”**。对于缩减单元，我们将应用于单元输入的初始操作的步长设为 2，以减小高度和宽度。我们用于构建卷积单元的所有操作都可选择步长。

Figure 2 shows our placement of Normal and Reduction Cells for CIFAR-10 and ImageNet. Note on ImageNet we have more Reduction Cells, since the incoming image size is 299x299 compared to 32x32 for CIFAR. The Reduction and Normal Cell could have the same architecture, but we empirically found it beneficial to learn two separate architectures. We use a common heuristic to double the number of filters in the output whenever the spatial activation size is reduced in order to maintain roughly constant hidden state dimension [32, 53]. Importantly, much like Inception and ResNet models [59, 20, 60, 58], we consider the number of motif repetitions N and the number of initial convolutional filters as free parameters that we tailor to the scale of an image classification problem.

图 2 展示了我们在 CIFAR-10 和 ImageNet 中常规单元和缩减单元的布局。需要注意的是，在 ImageNet 中，缩减单元的数量更多，因为输入图像尺寸为 299x299，而 CIFAR 为 32x32。缩减单元和常规单元可以采用相同的架构，但我们根据经验发现，学习两种不同的架构更为有益。我们使用一种通用的启发式方法，每当空间激活尺寸减小时，将输出中的滤波器数量加倍，以保持隐藏状态维度大致恒定 [32, 53]。重要的是，与 Inception 和 ResNet 模型 [59, 20, 60, 58] 非常相似，我们将模体重复次数 N 和初始卷积滤波器数量视为自由参数，并根据图像分类问题的规模进行调整。


What varies in the convolutional nets is the structures of the Normal and Reduction Cells, which are searched by the controller RNN. The structures of the cells can be searched within a search space defined as follows (see Appendix, Figure 7 for schematic). In our search space, each cell receives as input two initial hidden states $h_i$ and $h_{i-1}$ which are the outputs of two cells in previous two lower layers or the input image. The controller RNN recursively predicts the rest of the structure of the convolutional cell, given these two initial hidden states (Figure 3). The predictions of the controller for each cell are grouped into $\Beta$ blocks, where each block has 5 prediction steps made by 5 distinct softmax classifiers corresponding to discrete choices of the elements of a block:

卷积网络的不同之处在于常规单元和约简单元的结构，这些单元由控制器 RNN 搜索。单元结构可以在定义如下的搜索空间内进行搜索（参见附录，图 7 中的示意图）。在我们的搜索空间中，每个单元接收两个初始隐藏状态 $h_i$ 和 $h_{i-1}$ 作为输入，它们是前两个较低层中两个单元的输出或输入图像。控制器 RNN 根据这两个初始隐藏状态递归地预测卷积单元的其余结构（图 3）。控制器对每个单元的预测被分组为 $\Beta$ 个块，其中每个块有 5 个预测步骤，由 5 个不同的 softmax 分类器做出，对应于块元素的离散选择：

Step 1. Select a hidden state from $h_i$; $h_{i-1}$ or from the set of hidden states created in previous blocks.
Step 2. Select a second hidden state from the same options as in Step 1.
Step 3. Select an operation to apply to the hidden state selected in Step 1.
Step 4. Select an operation to apply to the hidden state selected in Step 2.
Step 5. Select a method to combine the outputs of Step 3 and 4 to create a new hidden state.


In step 5 the controller RNN selects a method to combine the two hidden states, either (1) element-wise addition between two hidden states or (2) concatenation between two hidden states along the filter dimension. Finally, all of the unused hidden states generated in the convolutional cell are concatenated together in depth to provide the final cell output.

在步骤 5 中，控制器 RNN 选择一种方法来合并两个隐藏状态：(1) 两个隐藏状态之间逐元素相加，或 (2) 两个隐藏状态沿滤波器维度连接。最后，将卷积单元中生成的所有未使用的隐藏状态进行深度连接，以提供最终的单元输出。

To allow the controller RNN to predict both Normal Cell and Reduction Cell, we simply make the controller have $2 \times 5B$ predictions in total, where the first $5B$ predictions are for the Normal Cell and the second $5B$ predictions are for the Reduction Cell.

为了让控制器 RNN 能够预测 Normal Cell 和 Reduction Cell，我们只需让控制器总共具有 $2 \times 5B$ 个预测，其中前 $5B$ 个预测针对 Normal Cell，后 $5B$ 个预测针对 Reduction Cell。


Finally, our work makes use of the reinforcement learning
proposal in NAS [71]; however, it is also possible to
use random search to search for architectures in the NASNet
search space. In random search, instead of sampling
the decisions from the softmax classifiers in the controller
RNN, we can sample the decisions from the uniform distribution.
In our experiments, we find that random search is
slightly worse than reinforcement learning on the CIFAR-
10 dataset. Although there is value in using reinforcement
learning, the gap is smaller than what is found in the original
work of [71]. This result suggests that 1) the NASNet search
space is well-constructed such that random search can perform
reasonably well and 2) random search is a difficult
baseline to beat. We will compare reinforcement learning
against random search in Section 4.4.


最后，我们的工作利用了 NAS [71] 中的强化学习方案；然而，也可以使用随机搜索在 NASNet 搜索空间中搜索架构。在随机搜索中，我们不是从控制器 RNN 中的 softmax 分类器中采样决策，而是从均匀分布中采样决策。在我们的实验中，我们发现随机搜索在 CIFAR-10 数据集上的表现略逊于强化学习。虽然使用强化学习有其价值，但差距小于 [71] 的原始工作中发现的差距。这一结果表明：1) NASNet 搜索空间构造良好，使得随机搜索能够表现得相当好；2) 随机搜索是一个难以超越的基准。我们将在 4.4 节中比较强化学习和随机搜索。




