# Tesseract OCR 历史

# 1. 介绍
Tesseract 是一个开源系统，最初由HP在1985到1995年间开发，搁置了10年后，于2006年开源，目前主要由Google维护。


除了别的事情除外，Tesseract的历史就是统计和非统计分类方法争论的缩影。

# 2. 系统架构
Addaapptitvivee Thhreshold
->Page Layout Analysis
->Recognize Word Pass 1->Recognize Word Pass 2
->X-Height Fix->Fuzzy Space Fix->Word Bigram Fix![](1.png =600x)
Figure 1. Block diagram of the overall architecture of Tesseract.

这是整体架构，已经多年未变，以传统OCR流程展示了它的起源。实际的字符识别组件有双通格式，用于识别单词过程1和过程2，过程1训练了个即时自适应分类器，过程二重新访问对识别不满意的单词。

处理复杂的任务，需要在一个合适的整体架构下。文章一开始，就按细节的处理，将OCR的架构分成了4类：


	• Traditional, naive. Traditional pipelined “feed forward” systems start as a series of steps that make hard decisions in one domain, and pass the results on to the next part of the pipeline.	• Traditional, mature. Matured pipelined systems are characterized by additional steps that revisit some of the earlier decisions with additional information from other parts of the pipeline. Examples include adaptive character classification, adaptive font spacing/character size models, and document dictionaries.	• Modern, naive. More recent approaches try to avoid premature decision-making by pushing all the hard problems into a monolithic statistical module, such as a Hidden Markov Model (HMM) and expect it to resolve everything at once. These systems began with segmentation-free, also-known-as sliding window classification, in which decisions over character boundaries are made in parallel with character classification. Between-word spacing falls out naturally from such systems, but it is more difficult to incorporate knowledge such as words tend to use only a single font. The pioneering work in this area is the Document Image Decoding(DID) system, and more recently, the BBN system.	• Modern, mature. It would be against the principles of an HMM-based OCR system to patch it with post- processing modules that re-visit earlier decisions, so mature modern systems will be characterized by increasingly complex models that take into account all the structure of printed information, much as the original DID system did, but without requiring a hand-coded model for each type of page layout.
（1）传统的，简单的。传统的流水线正向系统，一系列步骤，每一步的结果作会给下一个部分。项目初期，为了方便定义问题、分工协作，传统的方式就是将问题拆分，快速搭建出pipeline，而pipeline中确实可能有些环节一直在『make hard decisions』，成为效果的瓶颈。

（2）传统的，成熟的。成熟的流水线系统有额外的操作，使用来自其他部分的额外信息重新访问早期的决策。例如包括自适应的字符分类，自适应的字体分隔或者字符尺寸模型，文档字典。

对于传统流程的项目（如Tesseract这样有悠久历史的项目），就只有获得更多信息后，反复重跑之前的流程直到获得满意结果（传统观点是鄙视这种ad-hoc的架构的）。

（3）现代的，简单的。现在的方法尽量避免不成熟的决定，把所有难以解决的难题放到一个整体统计模型里。

随着基于统计的机器学习的兴起，大家开始倾向于用更多的数据去减缓这个瓶颈，就是文中所说的，将难题都推给一个模块，然后用大量的数据去解决。

（4）现代的，成熟的。使用后处理模块重新访问早期决定，因此成熟的现代系统将以越来越多的复杂模型为特点，考虑了打印信息的所有结构。

对于没有历史包袱的项目，则可以考虑在模型上就能支持更复杂的信息输入、输出，当然，但这样的代价是『increasingly complex model』。总之，这样的架构作者才认为是成熟的架构。从趋势来看，后者应该是将来的主流（虽然目前我还不知道有哪个项目真的是这样做的）。

![](2.png =700x)

**Tesseract 单词识别器，如图2所示，寻找一个单词的最佳分割为孤立字符，喂给字符分类器。根据Casey 和 Lecolinet 对于分割的研究，Tesseract是一个用经典方法和基于识别的分割的混合物，不过没有使用过分割算法在里边。** 过度分割的字识别器将最大限度地分割单词（或文本行），然后应用波束搜索以通过所得到的格子来选择最佳的几个分割路径。从初始的基于连接分量的分割开始，当该单词不令人满意时，它从字符分类器中分离出具有差信度的分量。 在每个步骤中，波束搜索将字符分类器结果与语言模型相结合，如Sec7。如果斩波不能产生令人满意的结果，则根据分类器和语言模型的提示，通过连接相邻的字符片段来搜索分割格子，例如词典搜索死亡词的哪个位置。 对于每个分割假设，波束搜索重新运行，直到产生满意的词。

# 3. feature space 特征空间

# 4. 分类器

# 5. 测试

# 6. 语言

# 7. 语言模型和单词识别

