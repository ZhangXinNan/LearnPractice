
DEEP COMPRESSION: COMPRESSING DEEP NEURAL NETWORKS WITH PRUNING, TRAINED QUANTIZATION AND HUFFMAN CODING

Song Han
Stanford University, Stanford, CA 94305, USA
songhan@stanford.edu

Huizi Mao
Tsinghua University, Beijing, 100084, China
mhz12@mails.tsinghua.edu.cn

William J. Dally
Stanford University, Stanford, CA 94305, USA
NVIDIA, Santa Clara, CA 95050, USA
dally@stanford.edu


# 0 ABSTRACT
Neural networks are both computationally intensive and memory intensive, making
them difficult to deploy on embedded systems with limited hardware resources. To
address this limitation, we introduce “deep compression”, a three stage pipeline:
pruning, trained quantization and Huffman coding, that work together to reduce
the storage requirement of neural networks by $35 \times$  to $49 \times$  without affecting their
accuracy. Our method first prunes the network by learning only the important
connections. Next, we quantize the weights to enforce weight sharing, finally, we
apply Huffman coding. After the first two steps we retrain the network to fine
tune the remaining connections and the quantized centroids. Pruning, reduces the
number of connections by $9 \times$  to $13 \times$ ; Quantization then reduces the number of
bits that represent each connection from 32 to 5. On the ImageNet dataset, our
method reduced the storage required by AlexNet by $35 \times$ , from 240MB to 6.9MB,
without loss of accuracy. Our method reduced the size of VGG-16 by $49 \times$  from
552MB to 11.3MB, again with no loss of accuracy. This allows fitting the model
into on-chip SRAM cache rather than off-chip DRAM memory. Our compression
method also facilitates the use of complex neural networks in mobile applications
where application size and download bandwidth are constrained. Benchmarked on
CPU, GPU and mobile GPU, compressed network has $3 \times$  to $4 \times$  layerwise speedup
and $3 \times$  to $7 \times$  better energy efficiency.





in·ten·sive adj.   /ɪnˈtensɪv/ 
1.
involving a lot of work or activity done in a short time短时间内集中紧张进行的；密集的
• an intensive language course速成语言课程
• two weeks of intensive training两周的强化训练
• intensive diplomatic negotiations紧张的外交谈判
2.
extremely thorough; done with a lot of care彻底的；十分细致的
• His disappearance has been the subject of intensive investigation.他的失踪一直是大力调查的重点。



# 1 INTRODUCTION
Deep neural networks have evolved to the state-of-the-art technique for computer vision tasks
(Krizhevsky et al., 2012)(Simonyan & Zisserman, 2014). Though these neural networks are very
powerful, the large number of weights consumes considerable storage and memory bandwidth. For
example, the AlexNet Caffemodel is over 200MB, and the VGG-16 Caffemodel is over 500MB
(BVLC). This makes it difficult to deploy deep neural networks on mobile system.


First, for many mobile-first companies such as Baidu and Facebook, various apps are updated via
different app stores, and they are very sensitive to the size of the binary files. For example, App
Store has the restriction “apps above 100 MB will not download until you connect to Wi-Fi”. As a
result, a feature that increases the binary size by 100MB will receive much more scrutiny than one
that increases it by 10MB. Although having deep neural networks running on mobile has many great
features such as better privacy, less network bandwidth and real time processing, the large storage
overhead prevents deep neural networks from being incorporated into mobile apps.


The second issue is energy consumption. Running large neural networks require a lot of memory
bandwidth to fetch the weights and a lot of computation to do dot products— which in turn consumes
considerable energy. Mobile devices are battery constrained, making power hungry applications such
as deep neural networks hard to deploy.


Energy consumption is dominated by memory access. Under 45nm CMOS technology, a 32 bit floating point add consumes 0:9pJ, a 32bit SRAM cache access takes 5pJ, while a 32bit DRAM memory access takes 640pJ, which is 3 orders of magnitude of an add operation. Large networks do not fit in on-chip storage and hence require the more costly DRAM accesses. Running a 1 billion connection neural network, for example, at 20fps would require (20Hz)(1G)(640pJ) = 12:8W just for DRAM access - well beyond the power envelope of a typical mobile device.

能耗主要体现在内存访问上。在 45nm CMOS 技术下，32 位浮点加法运算的功耗为 0.9pJ，32 位 SRAM 缓存访问功耗为 5pJ，而 32 位 DRAM 内存访问功耗为 640pJ，是加法运算的 3 个数量级。大型神经网络无法装入片上存储器，因此需要更昂贵的 DRAM 访问。例如，以 20fps 的速度运行一个拥有 10 亿个连接的神经网络，仅 DRAM 访问就需要 (20Hz)(1G)(640pJ) = 12.8W 的功耗——这远远超出了典型移动设备的功耗范围。

Our goal is to reduce the storage and energy required to run inference on such large networks so they
can be deployed on mobile devices. To achieve this goal, we present “deep compression”: a threestage
pipeline (Figure 1) to reduce the storage required by neural network in a manner that preserves
the original accuracy. First, we prune the networking by removing the redundant connections, keeping
only the most informative connections. Next, the weights are quantized so that multiple connections
share the same weight, thus only the codebook (effective weights) and the indices need to be stored.
Finally, we apply Huffman coding to take advantage of the biased distribution of effective weights.


Our main insight is that, pruning and trained quantization are able to compress the network without
interfering each other, thus lead to surprisingly high compression rate. It makes the required storage
so small (a few megabytes) that all weights can be cached on chip instead of going to off-chip DRAM
which is energy consuming. Based on “deep compression”, the EIE hardware accelerator Han et al.
(2016) was later proposed that works on the compressed model, achieving significant speedup and
energy efficiency improvement.


# 2 NETWORK PRUNING
Network pruning has been widely studied to compress CNN models. In early work, network pruning proved to be a valid way to reduce the network complexity and over-fitting (LeCun et al., 1989; Hanson & Pratt, 1989; Hassibi et al., 1993; Str¨om, 1997). Recently Han et al. (2015) pruned state-of-the-art CNN models with no loss of accuracy. We build on top of that approach. As shown on the left side of Figure 1, we start by learning the connectivity via normal network training. Next, we prune the small-weight connections: all connections with weights below a threshold are removed from the network. Finally, we retrain the network to learn the final weights for the remaining sparse connections. Pruning reduced the number of parameters by $9 \times$  and $13 \times$  for AlexNet and VGG-16 model.

网络剪枝已被广泛研究用于压缩 CNN 模型。在早期研究中，网络剪枝被证明是降低网络复杂度和过拟合的有效方法 (LeCun et al., 1989; Hanson & Pratt, 1989; Hassibi et al., 1993; Str¨om, 1997)。最近，Han et al. (2015) 对最先进的 CNN 模型进行了剪枝，且没有损失准确率。我们以此方法为基础进行构建。如图 1 左侧所示，我们首先通过常规网络训练来学习连接。接下来，我们剪枝小权重连接：所有权重低于阈值的连接都将从网络中删除。最后，我们重新训练网络以学习剩余稀疏连接的最终权重。剪枝使 AlexNet 和 VGG-16 模型的参数数量分别减少了 9 个和 13 个。



We store the sparse structure that results from pruning using compressed sparse row (CSR) or compressed sparse column (CSC) format, which requires $2a+n+1$ numbers, where a is the number of non-zero elements and n is the number of rows or columns.

我们使用压缩稀疏行 (CSR) 或压缩稀疏列 (CSC) 格式存储修剪产生的稀疏结构，这需要 $2a+n+1$ 个数字，其中 a 是非零元素的数量，n 是行数或列数。

To compress further, we store the index difference instead of the absolute position, and encode this difference in 8 bits for conv layer and 5 bits for fc layer. When we need an index difference larger than the bound, we the zero padding solution shown in Figure 2: in case when the difference exceeds 8, the largest 3-bit (as an example) unsigned number, we add a filler zero.

为了进一步压缩，我们存储索引差值而不是绝对位置，并将此差值编码为 8 位（卷积层）和 5 位（全连接层）。当我们需要的索引差值大于边界值时，我们采用图 2 所示的零填充方案：当差值超过 8 位（以最大的 3 位无符号数为例）时，我们添加一个零作为填充。


# 3 TRAINED QUANTIZATION AND WEIGHT SHARING
Network quantization and weight sharing further compresses the pruned network by reducing the number of bits required to represent each weight. We limit the number of effective weights we need to store by having multiple connections share the same weight, and then fine-tune those shared weights.

网络量化和权重共享通过减少表示每个权重所需的位数，进一步压缩了剪枝后的网络。我们通过让多个连接共享相同的权重来限制需要存储的有效权重数量，然后对这些共享的权重进行微调。

Weight sharing is illustrated in Figure 3. Suppose we have a layer that has 4 input neurons and 4 output neurons, the weight is a $4 \times 4$ matrix. On the top left is the $4 \times 4$ weight matrix, and on the bottom left is the $4 \times 4$ gradient matrix. The weights are quantized to 4 bins (denoted with 4 colors), all the weights in the same bin share the same value, thus for each weight, we then need to store only a small index into a table of shared weights. During update, all the gradients are grouped by the color and summed together, multiplied by the learning rate and subtracted from the shared centroids from last iteration. For pruned AlexNet, we are able to quantize to 8-bits (256 shared weights) for each CONV layers, and 5-bits (32 shared weights) for each FC layer without any loss of accuracy.

图 3 展示了权重共享。假设我们有一个包含 4 个输入神经元和 4 个输出神经元的层，权重是一个 $4 \times 4$ 矩阵。左上角是 $4 \times 4$ 权重矩阵，左下角是 $4 \times 4$ 梯度矩阵。权重被量化为 4 个 bin（用 4 种颜色表示），同一 bin 中的所有权重共享相同的值，因此对于每个权重，我们只需将一个小的索引存储在共享权重表中。在更新过程中，所有梯度按颜色分组并相加，乘以学习率，并从上次迭代的共享质心减去。对于剪枝后的 AlexNet，我们能够将每个卷积层量化为 8 位（256 个共享权重），将每个全连接层量化为 5 位（32 个共享权重），而不会造成任何精度损失。


To calculate the compression rate, given k clusters, we only need $\log_{2}{k}$ bits to encode the index. In
general, for a network with n connections and each connection is represented with b bits, constraining
the connections to have only k shared weights will result in a compression rate of:
$$
$$

For example, Figure 3 shows the weights of a single layer neural network with four input units and four output units. There are $4 \times 4 = 16$ weights originally but there are only 4 shared weights: similar weights are grouped together to share the same value. Originally we need to store 16 weights each has 32 bits, now we need to store only 4 effective weights (blue, green, red and orange), each has 32 bits, together with 16 2-bit indices giving a compression rate of $16 * 32 / (4 * 32 + 2 * 16) = 3.2$

为了计算压缩率，给定 k 个簇，我们只需要 $\log_{2}{k}$ 位来编码索引。一般来说，对于具有 n 个连接且每个连接用 b 位表示的网络，将连接限制为仅具有 k 个共享权重，将导致压缩率为：





# 4 HUFFMAN CODING
A Huffman code is an optimal prefix code commonly used for lossless data compression(Van Leeuwen, 1976). It uses variable-length codewords to encode source symbols. The table is derived from the occurrence probability for each symbol. More common symbols are represented with fewer bits.

Figure 5 shows the probability distribution of quantized weights and the sparse matrix index of the last fully connected layer in AlexNet. Both distributions are biased: most of the quantized weights are distributed around the two peaks; the sparse matrix index difference are rarely above 20. Experiments show that Huffman coding these non-uniformly distributed values saves 20% - 30% of network storage.

霍夫曼码是一种常用于无损数据压缩的最佳前缀码（Van Leeuwen，1976）。它使用可变长度的码字对源符号进行编码。该表基于每个符号的出现概率得出。更常见的符号用更少的比特表示。

图 5 展示了 AlexNet 中量化权重的概率分布以及最后一个全连接层的稀疏矩阵索引。这两个分布都存在偏差：大多数量化权重分布在两个峰值附近；稀疏矩阵索引差很少超过 20。实验表明，对这些非均匀分布的值进行霍夫曼编码可以节省 20% 到 30% 的网络存储。