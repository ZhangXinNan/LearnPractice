


视频章节：
```
00:00 标题和作者
03:21 摘要
08:11 结论
10:05 导言
14:35 相关工作
16:34 模型
1:12:49 实验
1:21:46 讨论
```

Transformer 是（当前时间2021年10月29日）三年以来深度学习领域最重要的文章之一。
是继MLP、CNN、RNN之后第四大base模型。

# 1 标题和作者
Attention Is All You Need

作者后边都加了*号，代表“同样贡献”。

# 2 摘要 Abstract
【注】现在常见的模型结果是包含CNN和RNN的encoder-decoder结构，表现好的seq2seq模型都在encoder和decoder之前使用了attention机制。
我们的transformer模型是第一个仅仅使用了注意力机制的做encoder-decoder的模型，我们在其中使用了multi-head self attention结构等等...

The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.

主流的序列转录模型基于包括编码器和解码器的复杂递归或卷积神经网络。（转录模型：输入一个序列，生成另一个序列。）
性能最佳的模型还通过注意力机制连接编码器和解码器。
我们提出了一种新的简单网络架构，即 Transformer，它**完全基于注意力机制**，完全摒弃了循环和卷积。
对两项机器翻译任务的实验表明，这些模型在性能上更胜一筹，同时可并行化程度更高，并且需要的训练时间明显减少。
我们的模型在 WMT 2014 英德翻译任务中达到了 28.4 BLEU，比现有的最佳结果（包括集成）提高了超过 2 BLEU。
在 WMT 2014 英法翻译任务中，我们的模型在八个 GPU 上训练 3.5 天后建立了一个新的单模型最先进的 BLEU 分数 41.8，这是最好的训练成本的一小部分 来自文献的模型。
我们通过将 Transformer 成功应用于具有大量和有限训练数据的英语选区解析，证明 Transformer 可以很好地泛化到其他任务。

# 3 结论 Conclusion

In this work, we presented the Transformer, the first sequence transduction model based entirely on attention, replacing the recurrent layers most commonly used in encoder-decoder architectures with multi-headed self-attention.

For translation tasks, the Transformer can be trained significantly faster than architectures based on recurrent or convolutional layers. On both WMT 2014 English-to-German and WMT 2014 English-to-French translation tasks, we achieve a new state of the art. In the former task our best model outperforms even all previously reported ensembles.

We are excited about the future of attention-based models and plan to apply them to other tasks. We plan to extend the Transformer to problems involving input and output modalities other than text and to investigate local, restricted attention mechanisms to efficiently handle large inputs and outputs such as images, audio and video. Making generation less sequential is another research goals of ours.

The code we used to train and evaluate our models is available at https://github.com/tensorflow/tensor2tensor.

Acknowledgements We are grateful to Nal Kalchbrenner and Stephan Gouws for their fruitful comments, corrections and inspiration.

【简单】
在这项工作中，我们提出了 Transformer，这是第一个**完全基于注意力**的序列转录模型，用多头自注意力取代了编码器-解码器架构中最常用的循环层。

【快好】
对于翻译任务，Transformer 的训练速度明显快于基于循环层或卷积层的架构。 在 WMT 2014 英德和 WMT 2014 英法翻译任务中，我们都达到了新的水平。 在前一个任务中，我们最好的模型甚至优于所有先前报告的集成。

【预测】
我们对基于注意力的模型的未来感到兴奋，并计划将它们应用到其他任务中。 我们计划将 Transformer 扩展到涉及文本以外的输入和输出模式的问题，并研究局部的、受限的注意力机制，以有效处理图像、音频和视频等大型输入和输出。 减少生成顺序是我们的另一个研究目标。

我们用于训练和评估模型的代码可在 https://github.com/tensorflow/tensor2tensor 获得。

致谢 感谢 Nal Kalchbrenner 和 Stephan Gouws 富有成效的评论、更正和启发。

# 4 导言 Introduction

Recurrent neural networks, long short-term memory [13] and gated recurrent [7] neural networks in particular, have been firmly established as state of the art approaches in sequence modeling and transduction problems such as language modeling and machine translation [35, 2, 5]. Numerous efforts have since continued to push the boundaries of recurrent language models and encoder-decoder architectures [38, 24, 15].

【回顾RNN】
循环神经网络，特别是LSTM(长短期记忆) [13] 和GRU（门控循环） [7] 神经网络，已被牢固地确立为序列建模和转换问题（例如语言建模和机器翻译）的最先进方法 [35, 2, 5]。
此后，许多努力继续推动循环语言模型和编码器-解码器架构的边界 [38、24、15]。

Recurrent models typically factor computation along the symbol positions of the input and output sequences. Aligning the positions to steps in computation time, they generate a sequence of hidden states $h_t$, as a function of the previous hidden state $h_{t−1}$ and the input for position $t$ . This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples. Recent work has achieved significant improvements in computational efficiency through factorization tricks [21] and conditional computation [32], while also improving model performance in case of the latter. The fundamental constraint of sequential computation, however, remains.

【RNN的缺点：无法并行/内存开销大】
循环模型通常沿着输入和输出序列的符号位置对计算进行因子计算。
将位置与计算时间的步骤对齐，它们生成一系列隐藏状态 $h_t$，作为先前隐藏状态 $h_{t−1}$ 和位置$t$的输入的函数。 
这种固有的顺序性质排除了训练示例中的并行化，这在较长的序列长度下变得至关重要，因为内存限制限制了跨示例的批处理。 最近的工作通过分解技巧 [21] 和条件计算 [32] 显着提高了计算效率，同时在后者的情况下也提高了模型性能。 然而，顺序计算的基本限制仍然存在。
【注】RNN无法并行，而Transformer可以并行。

Attention mechanisms have become an integral part of compelling sequence modeling and transduction models in various tasks, allowing modeling of dependencies without regard to their distance in the input or output sequences [2, 19]. In all but a few cases [27], however, such attention mechanisms are used in conjunction with a recurrent network.

【Attention在RNN中的应用】
注意力机制已成为各种任务中令人信服的序列建模和转导模型不可或缺的一部分，允许依赖性建模而不考虑它们在输入或输出序列中的距离 [2, 19]。 然而，在除少数情况外的所有情况下 [27]，这种注意机制都与循环网络结合使用。

In this work we propose the Transformer, a model architecture eschewing recurrence and instead relying entirely on an attention mechanism to draw global dependencies between input and output. The Transformer allows for significantly more parallelization and can reach a new state of the art in translation quality after being trained for as little as twelve hours on eight P100 GPUs.

【Transformer可并行】
在这项工作中，我们提出了 Transformer，这是一种避免重复出现的模型架构，而是完全依赖注意力机制来绘制输入和输出之间的全局依赖关系。 Transformer 允许显着提高并行化，并且在八个 P100 GPU 上经过短短 12 小时的训练后，可以达到翻译质量的新水平。

【注】RNN存在的缺点：1、只能串行计算；2、长序列的早期的信息可能会丢失，每一步的历史信息都需要存储，内存开销大；
attention在RNN上的应用：attention作用是怎么把encoder有效的信息传递给decoder，允许建模 input or output sequence 与距离无关的 dependencies。
transformer不再使用循环结果，纯attention结构，并行效率高，训练时间短等等...

# 5 相关工作 Background

The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU [16], ByteNet [18] and ConvS2S [9], all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions [12]. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention as described in section 3.2.

减少顺序计算的目标也构成了扩展神经 GPU [16]、ByteNet [18] 和 ConvS2S [9] 的基础，所有这些都使用卷积神经网络作为基本构建块，并行计算所有输入的隐藏表示和输出位置。
在这些模型中，将来自两个任意输入或输出位置的信号相关联所需的操作数量随着位置之间的距离而增加，ConvS2S 呈线性增长，ByteNet 呈对数增长。
这使得学习远距离位置之间的依赖关系变得更加困难 [12]。
在 Transformer 中，这被减少到恒定数量的操作，尽管由于平均注意力加权位置而导致有效分辨率降低为代价，我们用(多头注意力机制)Multi-Head Attention 抵消了这种效果，如第 3.2 节所述。

【注】卷积只能看局部，如果想看到距离很远的地方之间的关联，需要很多层。但是卷积网络可以做多个输出通道，一个输出通道可以认为是识别不同的模式。作者也想使用多通道，所以提出了Multi-head Attention。
self attention：不是transformer首先提出来的理论，但是我们是第一个只依赖self attention来实现encoder-decoder架构的模型；

Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations [4, 27, 28, 22].

自注意力，有时称为内部注意力，是一种将单个序列的不同位置相关联以计算序列表示的注意力机制。
自注意力已成功用于各种任务，包括阅读理解、抽象摘要、文本蕴含和学习与任务无关的句子表示 [4、27、28、22]。

End-to-end memory networks are based on a recurrent attention mechanism instead of sequence-aligned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks [34].

端到端记忆网络基于循环注意力机制而不是序列对齐循环，并且已被证明在简单语言问答和语言建模任务上表现良好 [34]。

To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence-aligned RNNs or convolution. In the following sections, we will describe the Transformer, motivate self-attention and discuss its advantages over models such as [17, 18] and [9].

然而，据我们所知，Transformer 是第一个完全依靠自注意力来计算其输入和输出表示而不使用序列对齐 RNN 或卷积的转导模型。
在接下来的部分中，我们将描述 Transformer，激发自注意力并讨论它相对于 [17、18] 和 [9] 等模型的优势。

# 6 模型架构 Model Architecture

Most competitive neural sequence transduction models have an encoder-decoder structure [5, 2, 35].
Here, the encoder maps an input sequence of symbol representations $(x_1, ..., x_n)$ to a sequence of continuous representations$z = (z_1, ..., z_n)$.
Given z, the decoder then generates an output sequence $(y_1, ..., y_m)$ of symbols one element at a time.
At each step the model is auto-regressive [10], consuming the previously generated symbols as additional input when generating the next.

The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.

大多数有竞争力的神经序列转导模型都具有编码器-解码器结构 [5、2、35]。
这里，**编码器**将输入的符号表示序列$(x_1, ..., x_n)$映射到连续表示序列$z = (z_1, ..., z_n)$。
给定 z，**解码器**然后一次生成一个符号的输出序列$(y_1, ..., y_m)$。
在每个步骤中，模型都是自回归的(auto-regressive) [10]，在生成下一步时将先前生成的符号作为附加输入使用。

Transformer 遵循这种整体架构，为编码器和解码器使用堆叠式自注意力层和逐点全连接层，分别如图 1 的左半部分和右半部分所示。

![](fig1.png)
左边是encoder，右边是decoder。
Outputs (shifted right)是decoder的输入，decoder在做预测时没有输入，实际是decoder在之前时刻的一些输出作为输入。

## 6.1 Encoder and Decoder Stacks
Encoder: The encoder is composed of a stack of $N = 6$ identical layers. Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network. We employ a residual connection [11] around each of the two sub-layers, followed by layer normalization [1]. That is, the output of each sub-layer is $LayerNorm(x + Sublayer(x))$, where $Sublayer(x)$ is the function implemented by the sub-layer itself. To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension $d_model = 512$.

![](batch-norm_layer-norm.png)
编码器：
编码器由 $N = 6$ 个相同层的堆栈组成。 每一层都有两个子层。 第一个是多头自注意力机制（Multi-Head self-attention），第二个是简单的、按位置的全连接前馈网络（MLP）。 我们在两个子层中的每一个周围都使用了一个残差连接[11]，然后是层归一化[1]。 即每个子层的输出是$LayerNorm(x + Sublayer(x))$，其中$Sublayer(x)$是子层自己实现的函数。 为了促进这些残差连接，模型中的所有子层以及嵌入层都产生维度 $d_model = 512$ 的输出。

【注】为什么在序列模型里，使用layernorm，因为每个样本的序列长度是不一样的。

Decoder: The decoder is also composed of a stack of $N = 6$ identical layers. In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization. We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position $i$ can depend only on the known outputs at positions less than $i$.

解码器：
解码器也由一堆$N = 6$个相同的层组成。
除了每个编码器层中的两个子层之外，解码器还插入了第三个子层，它对编码器堆栈的输出执行多头注意力。
与编码器类似，我们在每个子层周围使用残差连接，然后进行层归一化。
我们还修改了解码器堆栈中的自我注意子层，以防止位置关注后续位置。
这种掩蔽与输出嵌入偏移一个位置的事实相结合，确保了位置 $i$ 的预测只能依赖于位置小于 $i$ 的已知输出。

## 6.2 Attention

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.

注意力函数可以描述为将查询和一组键值对映射到输出，其中查询、键、值和输出都是向量。
输出计算为值的加权和，其中分配给每个值的权重由查询与相应键的兼容性函数计算。

![](fig2.png)

### 6.2.1 Scaled Dot-Product Attention

We call our particular attention "Scaled Dot-Product Attention" (Figure 2).
The input consists of queries and keys of dimension $d_k$, and values of dimension $d_v$.
We compute the dot products of the query with all keys, divide each by $\sqrt{d_k}$, and apply a softmax function to obtain the weights on the values.

我们将我们的特殊注意力称为“缩放点积注意力”（图 2）。
输入由维度 $d_k$ 的queries和keys以及维度 $d_v$ 的values组成。
我们计算查询与所有键的点积，每个键除以 $\sqrt{d_k}$，然后应用 softmax 函数来获得值的权重。

In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix $Q$.
The keys and values are also packed together into matrices $K$ and $V$ .
We compute the matrix of outputs as:

在实践中，我们同时计算一组查询的注意力函数，并将它们打包到一个矩阵 $Q$ 中。
键和值也一起打包到矩阵 $K$ 和 $V$ 中。
我们将输出矩阵计算为：

$$
Attention(Q, K, V ) = softmax(\frac {QK^T} {\sqrt{d_k}})V
$$


The two most commonly used attention functions are additive attention [2], and dot-product (multi-plicative) attention.
Dot-product attention is identical to our algorithm, except for the scaling factor of $\face 1 {\sqrt{d_k}}$.
Additive attention computes the compatibility function using a feed-forward network with a single hidden layer.
While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.

两种最常用的注意功能是加法注意 [2] 和点积（多重）注意。
点积注意力与我们的算法相同，除了 $\face 1 {\sqrt{d_k}}$ 的比例因子。
附加注意使用具有单个隐藏层的前馈网络计算兼容性函数。
虽然两者在理论上的复杂性相似，但点积注意力在实践中速度更快且空间效率更高，因为它可以使用高度优化的矩阵乘法代码来实现。

While for small values of $d_k$ the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of $d_k$ [3].
We suspect that for large values of $d_k$, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients.
To counteract this effect, we scale the dot products by $\frac 1 {\sqrt{d_k}}$.

虽然对于较小的 $d_k$ 值，这两种机制的表现相似，但加法注意力优于点积注意力，而无需缩放更大的 $d_k$ 值 [3]。
我们怀疑对于较大的 $d_k$ 值，点积的幅度会变大，将 softmax 函数推入梯度极小的区域。
为了抵消这种影响，我们将点积缩放 $\frac 1 {\sqrt{d_k}}$。

### 6.2.2 Multi-Head Attention

### 6.2.3 Applications of Attention in our Model

## 6.3 Position-wise Feed-Forward Networks

## 6.4 Embeddings and Softmax

## 6.5 Positional Encoding




# 7 实验

# 8 讨论


# 参考资料
* [一文浅析transformer--李沐带你深入浅出transformer - 新一的文章 - 知乎](https://zhuanlan.zhihu.com/p/452663865)






