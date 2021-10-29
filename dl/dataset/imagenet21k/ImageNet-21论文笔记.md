
ImageNet-21K Pretrainging for the Masses

______


# 0 摘要

ImageNet-1K serves as the primary dataset for pretraining deep learning models for computer vision tasks. ImageNet-21K dataset, which is bigger and more diverse, is used less frequently for pretraining, mainly due to its complexity, low accessibility, and underestimation of its added value. This paper aims to close this gap, and make high-quality efficient pretraining on ImageNet-21K available for everyone. Via a dedicated preprocessing stage, utilization of WordNet hierarchical structure, and a novel training scheme called semantic softmax, we show that various models significantly benefit from ImageNet-21K pretraining on numerous datasets and tasks, including small mobile-oriented models. We also show that we outperform previous ImageNet-21K pretraining schemes for prominent new models like ViT and Mixer. Our proposed pretraining pipeline is efficient, accessible, and leads to SoTA reproducible results, from a publicly available dataset. The training code and pretrained models are available at: https://github.com/Alibaba-MIIL/ImageNet21K


ImageNet-1K 作为用于计算机视觉任务预训练深度学习模型的主要数据集。 ImageNet-21K 数据集更大、更多样化，用于预训练的频率较低，主要是由于其复杂性、低可访问性以及对其附加值的低估。本文旨在缩小这一差距，并为所有人提供 ImageNet-21K 上的高质量高效预训练。通过专用的预处理阶段、WordNet 分层结构的利用和称为语义 softmax 的新型训练方案，我们表明各种模型显着受益于 ImageNet-21K 对众多数据集和任务的预训练，包括面向移动的小型模型。我们还表明，对于 ViT 和 Mixer 等著名的新模型，我们的性能优于之前的 ImageNet-21K 预训练方案。我们提出的预训练管道高效、易于访问，并且可以从公开可用的数据集中获得 SoTA 可重现的结果。训练代码和预训练模型见：https://github.com/Alibaba-MIIL/ImageNet21K