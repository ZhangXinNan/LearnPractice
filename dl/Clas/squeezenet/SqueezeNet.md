


# 2 RELATED WORK
## 2.1 MODEL COMPRESSION

The overarching goal of our work is to identify a model that has very few parameters while preserving accuracy. To address this problem, a sensible approach is to take an existing CNN model and compress it in a lossy fashion. In fact, a research community has emerged around the topic of model compression, and several approaches have been reported. A fairly straightforward approach by Denton et al. is to apply singular value decomposition (SVD) to a pretrained CNN model (Denton et al., 2014). Han et al. developed Network Pruning, which begins with a pretrained model, then replaces parameters that are below a certain threshold with zeros to form a sparse matrix, and finally performs a few iterations of training on the sparse CNN (Han et al., 2015b). Recently, Han et al. extended their work by combining Network Pruning with quantization (to 8 bits or less) and huffman encoding to create an approach called Deep Compression (Han et al., 2015a), and further designed a hardware accelerator called EIE (Han et al., 2016a) that operates directly on the compressed model, achieving substantial speedups and energy savings.

我们工作的首要目标是找到一个在保持准确率的同时具有极少参数的模型。为了解决这个问题，一个合理的方法是采用现有的 CNN 模型并以有损方式对其进行压缩。事实上，围绕模型压缩这一主题已经出现了一个研究社区，并且已经报道了几种方法。Denton 等人提出了一种相当简单的方法是将奇异值分解 (SVD) 应用于预训练的 CNN 模型（Denton 等人，2014）。Han 等人开发了网络剪枝，该方法从预训练模型开始，然后用零替换低于特定阈值的参数以形成稀疏矩阵，最后对稀疏 CNN 进行几次迭代训练（Han 等人，2015b）。最近，Han 等人通过将网络修剪与量化（至 8 位或更少）和哈夫曼编码相结合，扩展了他们的工作，以创建一种称为深度压缩（Han et al.，2015a）的方法，并进一步设计了一种称为 EIE（Han et al.，2016a）的硬件加速器，可直接在压缩模型上运行，从而实现显着的加速和节能。

