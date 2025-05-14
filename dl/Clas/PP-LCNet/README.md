
# Abstract
We propose a lightweight CPU network based on the MKLDNN acceleration strategy, named PP-LCNet, which improves the performance of lightweight models on multiple tasks. This paper lists technologies which can improve network accuracy while the latency is almost constant. With these improvements, the accuracy of PP-LCNet can greatly surpass the previous network structure with the same inference time for classification. As shown in Figure 1, it outperforms the most state-of-the-art models. And for downstream tasks of computer vision, it also performs very well, such as object detection, semantic segmentation, etc. All our experiments are implemented based on PaddlePaddle1. Code and pretrained models are available at PaddleClas2.

我们提出了一种基于 MKLDNN 加速策略的轻量级 CPU 网络 PP-LCNet，该网络能够提升轻量级模型在多个任务上的性能。本文列举了一些能够在延迟几乎保持不变的情况下提升网络准确率的技术。凭借这些改进，PP-LCNet 的准确率在相同的分类推理时间下能够大幅超越之前的网络结构。如图 1 所示，它的表现超越了最先进的模型。此外，在目标检测、语义分割等计算机视觉的下游任务中，PP-LCNet 也表现出色。我们所有的实验均基于 PaddlePaddle1 实现。代码和预训练模型可在 PaddleClas2 获取。

