

# ABSTRACT

Deep neural networks (DNNs) continue to make significant advances, solving tasks from image classification to translation or reinforcement learning. One aspect of the field receiving considerable attention is efficiently executing deep models in resource-constrained environments, such as mobile or embedded devices. This paper focuses on this problem, and proposes two new compression methods, which jointly leverage weight quantization and distillation of larger networks, called “teachers,” into compressed “student” networks. The first method we propose is called quantized distillation and leverages distillation during the training process, by incorporating distillation loss, expressed with respect to the teacher network, into the training of a smaller student network whose weights are quantized to a limited set of levels. The second method, differentiable quantization, optimizes the location of quantization points through stochastic gradient descent, to better fit the behavior of the teacher model. We validate both methods through experiments on convolutional and recurrent architectures. We show that quantized shallow students can reach similar accuracy levels to state-of-the-art full-precision teacher models, while providing up to order of magnitude compression, and inference speedup that is almost linear in the depth reduction. In sum, our results enable DNNs for resource-constrained environments to leverage architecture and accuracy advances developed on more powerful devices.

深度神经网络 (DNN) 持续取得重大进展，解决了从图像分类到翻译或强化学习等各种任务。该领域备受关注的一个方面是如何在资源受限的环境中高效地执行深度模型，例如移动或嵌入式设备。本文重点关注这一问题，并提出了两种新的压缩方法，它们将较大的网络（称为“教师”）的权重量化和蒸馏结合起来，压缩成“学生”网络。我们提出的第一种方法称为量化蒸馏，该方法在训练过程中利用蒸馏，将相对于教师网络表示的蒸馏损失合并到较小的学生网络的训练中，该学生网络的权重被量化到有限的级别。第二种方法称为可微量化，它通过随机梯度下降优化量化点的位置，以更好地拟合教师模型的行为。我们通过在卷积和循环架构上的实验验证了这两种方法。我们证明了，量化浅层学生模型可以达到与最先进的全精度教师模型相当的准确率水平，同时提供高达数量级的压缩，以及与深度缩减几乎呈线性关系的推理加速。总而言之，我们的研究结果使资源受限环境下的深度神经网络 (DNN) 能够充分利用在性能更强大的设备上开发的架构和准确率方面的进步。




