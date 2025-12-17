
An End-to-End Trainable Neural Network for Image-based Sequence Recognition and Its Application to Scene Text Recognition

用于基于图像的序列识别的端到端可训练神经网络及其在场景文本识别中的应用

Baoguang Shi, Xiang Bai and Cong Yao
School of Electronic Information and Communications
Huazhong University of Science and Technology, Wuhan, China
fshibaoguang,xbaig@hust.edu.cn, yaocong2010@gmail.com

_____

# 0 Abstract

Image-based sequence recognition has been a longstanding research topic in computer vision. In this paper, we investigate the problem of scene text recognition, which is among the most important and challenging tasks in image-based sequence recognition. A novel neural network architecture, which integrates feature extraction, sequence modeling and transcription into a unified framework, is proposed. Compared with previous systems for scene text recognition, the proposed architecture possesses four distinctive properties: (1) It is end-to-end trainable, in contrast to most of the existing algorithms whose components are separately trained and tuned. (2) It naturally handles sequences in arbitrary lengths, involving no character segmentation or horizontal scale normalization. (3) It is not confined to any predefined lexicon and achieves remarkable performances in both lexicon-free and lexicon-based scene text recognition tasks. (4) It generates an effective yet much smaller model, which is more practical for real-world application scenarios. The experiments on standard benchmarks, including the IIIT-5K, Street View Text and ICDAR datasets, demonstrate the superiority of the proposed algorithm over the prior arts. Moreover, the proposed algorithm performs well in the task of image-based music score recognition, which evidently verifies the generality of it.

基于图像的序列识别一直是计算机视觉领域的一个长期研究课题。 在本文中，我们研究了场景文本识别问题，这是基于图像的序列识别中最重要和最具挑战性的任务之一。 提出了一种新颖的神经网络架构，它将特征提取、序列建模和转录集成到一个统一的框架中。 与之前的场景文本识别系统相比，所提出的架构具有四个独特的特性：
(1) 它是端到端可训练的，而大多数现有算法的组件是单独训练和调整的。
(2) 它自然地处理任意长度的序列，不涉及字符分割或水平尺度标准化。
(3) 它不局限于任何预定义的词典，在无词典和基于词典的场景文本识别任务中都取得了显着的性能。
(4) 它生成了一个有效但小得多的模型，对于现实应用场景更实用。
 在标准基准（包括 IIIT-5K、街景文本和 ICDAR 数据集）上的实验证明了所提出的算法相对于现有技术的优越性。 此外，所提出的算法在基于图像的乐谱识别任务中表现良好，这显然验证了其通用性。


# 1. Introduction
Recently, the community has seen a strong revival of neural networks, which is mainly stimulated by the great success of deep neural network models, specifically Deep Convolutional Neural Networks (DCNN), in various vision tasks.
However, majority of the recent works related to deep neural networks have devoted to detection or classification of object categories [12, 25].
In this paper, we are concerned with a classic problem in computer vision: image-based sequence recognition.
In real world, a stable of visual objects, such as scene text, handwriting and musical score, tend to occur in the form of sequence, not in isolation.
Unlike general object recognition, recognizing such sequence-like objects often requires the system to predict a series of object labels, instead of a single label.
Therefore, recognition of such objects can be naturally cast as a sequence recognition problem. Another unique property of sequence-like objects is that their lengths may vary drastically.
For instance, English words can either consist of 2 characters such as “OK” or 15 characters such as “congratulations”.
Consequently, the most popular deep models like DCNN [25, 26] cannot be directly applied to sequence prediction, since DCNN models often operate on inputs and outputs with fixed dimensions, and thus are incapable of producing a variable-length label sequence.


最近，社区看到了神经网络的强劲复兴，这主要是受到深度神经网络模型，特别是深度卷积神经网络（DCNN）在各种视觉任务中取得巨大成功的刺激。
然而，最近与深度神经网络相关的大多数工作都致力于对象类别的检测或分类 [12, 25]。
在本文中，我们关注计算机视觉中的一个经典问题：基于图像的序列识别。
在现实世界中，稳定的视觉对象，例如场景文本、笔迹和乐谱，往往以序列的形式出现，而不是孤立的。
与一般的对象识别不同，识别此类序列对象通常需要系统预测一系列对象标签，而不是单个标签。
因此，此类物体的识别可以自然地转化为序列识别问题。
类序列对象的另一个独特属性是它们的长度可能变化很大。
例如，英语单词可以由 2 个字符（如“OK”）组成，也可以由 15 个字符（如“congratulations”）组成。
因此，像 DCNN [25, 26] 这样最流行的深度模型不能直接应用于序列预测，因为 DCNN 模型通常对固定维度的输入和输出进行操作，因此无法生成可变长度的标签序列。

总结：
- 过去 DCNN 致力于解决图像分类和目标检测，这篇论文涉及图像序列的识别。
- 序列识别需要预测一系列的标签，而不是单个标签。
- 另一个问题是序列长度变化大。

Some attempts have been made to address this problem for a specific sequence-like object (e.g. scene text). For example, the algorithms in [35, 8] firstly detect individual characters and then recognize these detected characters with DCNN models, which are trained using labeled character images. Such methods often require training a strong character detector for accurately detecting and cropping each character out from the original word image. Some other approaches (such as [22]) treat scene text recognition as an image classification problem, and assign a class label to each English word (90K words in total). It turns out a large trained model with a huge number of classes, which is difficult to be generalized to other types of sequencelike objects, such as Chinese texts, musical scores, etc., because the numbers of basic combinations of such kind of sequences can be greater than 1 million. In summary, current systems based on DCNN can not be directly used for image-based sequence recognition.

已经进行了一些尝试来解决特定的类序列对象（例如场景文本）的这个问题。 例如，[35, 8]中的算法首先检测单个字符，然后使用 DCNN 模型识别这些检测到的字符，该模型使用标记的字符图像进行训练。 此类方法通常需要训练强大的字符检测器，以准确地检测并从原始单词图像中裁剪出每个字符。 其他一些方法（例如[22]）将场景文本识别视为图像分类问题，并为每个英文单词（总共 90K 个单词）分配一个类别标签。 结果是一个具有大量类的大型训练模型，很难推广到其他类型的类序列对象，例如中文文本、乐谱等，因为此类序列的基本组合的数量可以 大于100万。 综上所述，当前基于DCNN的系统不能直接用于基于图像的序列识别。


Recurrent neural networks (RNN) models, another important branch of the deep neural networks family, were mainly designed for handling sequences. One of the advantages of RNN is that it does not need the position of each element in a sequence object image in both training and testing. However, a preprocessing step that converts an input object image into a sequence of image features, is usually essential. For example, Graves et al. [16] extract a set of geometrical or image features from handwritten texts, while Su and Lu [33] convert word images into sequential HOG features. The preprocessing step is independent of the subsequent components in the pipeline, thus the existing systems based on RNN can not be trained and optimized in an end-to-end fashion.

递归神经网络（RNN）模型是深度神经网络家族的另一个重要分支，主要用于处理序列。 RNN 的优点之一是在训练和测试时都不需要序列对象图像中每个元素的位置。 然而，将输入对象图像转换为图像特征序列的预处理步骤通常是必不可少的。 例如，格雷夫斯等人。 [16]从手写文本中提取一组几何或图像特征，而Su和Lu[33]将文字图像转换为顺序HOG特征。 预处理步骤独立于流程中的后续组件，因此基于 RNN 的现有系统无法以端到端的方式进行训练和优化。


Several conventional scene text recognition methods that are not based on neural networks also brought insightful ideas and novel representations into this field. For example, Almaza`n et al. [5] and Rodriguez-Serrano et al. [30] proposed to embed word images and text strings in a common vectorial subspace, and word recognition is converted into a retrieval problem. Yao et al. [36] and Gordo et al. [14] used mid-level features for scene text recognition. Though achieved promising performance on standard benchmarks, these methods are generally outperformed by previous algorithms based on neural networks [8, 22], as well as the approach proposed in this paper.

几种不基于神经网络的传统场景文本识别方法也为该领域带来了富有洞察力的想法和新颖的表示。 例如，Almaza`n 等人。 [5] 和罗德里格斯·塞拉诺等人。 [30]提出将单词图像和文本字符串嵌入到公共向量子空间中，并将单词识别转化为检索问题。 姚等人。 [36] 和戈多等人。 [14]使用中级特征进行场景文本识别。 尽管在标准基准上取得了有希望的性能，但这些方法通常优于以前基于神经网络的算法 [8, 22] 以及本文提出的方法。


The main contribution of this paper is a novel neural network model, whose network architecture is specifically designed for recognizing sequence-like objects in images. The proposed neural network model is named as Convolutional Recurrent Neural Network (CRNN), since it is a combination of DCNN and RNN. For sequence-like objects, CRNN possesses several distinctive advantages over conventional neural network models: 1) It can be directly learned from sequence labels (for instance, words), requiring no detailed annotations (for instance, characters); 2) It has the same property of DCNN on learning informative representations directly from image data, requiring neither hand-craft features nor preprocessing steps, including binarization/segmentation, component localization, etc.; 3) It has the same property of RNN, being able to produce a sequence of labels; 4) It is unconstrained to the lengths of sequence-like objects, requiring only height normalization in both training and testing phases; 5) It achieves better or highly competitive performance on scene texts (word recognition) than the prior arts [23, 8]; 6) It contains much less parameters than a standard DCNN model, consuming less storage space.

本文的主要贡献是一种新颖的神经网络模型，其网络架构是专门为识别图像中的序列状对象而设计的。 所提出的神经网络模型被命名为卷积循环神经网络（CRNN），因为它是 DCNN 和 RNN 的组合。 对于类似序列的对象，CRNN 比传统的神经网络模型具有几个独特的优势：1）它可以直接从序列标签（例如单词）中学习，不需要详细的注释（例如字符）； 2）它具有与DCNN相同的特性，可以直接从图像数据中学习信息表示，不需要手工制作特征，也不需要预处理步骤，包括二值化/分割、组件定位等； 3）具有与RNN相同的性质，能够产生标签序列； 4）不受类序列对象长度的限制，只需要在训练和测试阶段进行高度归一化； 5）在场景文本（单词识别）上取得了比现有技术更好或极具竞争力的性能[23, 8]； 6）它包含的参数比标准 DCNN 模型少得多