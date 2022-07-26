
Spatial Dual-Modality Graph Reasoning for Key Information Extraction

关键信息提取的空间双模态图推理

_____

# 0 摘要

Abstract—Key information extraction from document images is of paramount importance in office automation. Conventional template matching based approaches fail to generalize well to document images of unseen templates, and are not robust against text recognition errors. In this paper, we propose an end-to-end Spatial Dual-Modality Graph Reasoning method (SDMGR) to extract key information from unstructured document images. We model document images as dual-modality graphs, nodes of which encode both the visual and textual features of detected text regions, and edges of which represent the spatial relations between neighboring text regions. The key information extraction is solved by iteratively propagating messages along graph edges and reasoning the categories of graph nodes. In order to roundly evaluate our proposed method as well as boost the future research, we release a new dataset named WildReceipt, which is collected and annotated tailored for the evaluation of key information extraction from document images of unseen templates in the wild. It contains 25 key information categories, a total of about 69000 text boxes, and is about 2 times larger than the existing public datasets. Extensive experiments validate that all information including visual features, textual features and spatial relations can benefit key information extraction. It has been shown that SDMGR can effectively extract key information from document images of unseen templates, and obtain new state-of-the-art results on the recent popular benchmark SROIE and our WildReceipt. Our code and dataset will be publicly released.

摘要：
从文档图像中提取关键信息在办公自动化中至关重要。
传统的基于模板匹配的方法不能很好地泛化到未见过模板的文档图像，并且对文本识别错误也没有鲁棒性。
在本文中，我们提出了一种端到端的空间双模态图推理方法（SDMGR）来从非结构化文档图像中提取关键信息。
我们将文档图像建模为**双模态图**，其**节点**编码检测到的文本区域的视觉和文本特征，其**边缘**表示相邻文本区域之间的空间关系。
关键信息提取是通过沿图边迭代传播消息并推理图节点的类别来解决的。
为了全面评估我们提出的方法并促进未来的研究，我们发布了一个名为 WildReceipt 的新数据集，该数据集是为评估从野外看不见的模板的文档图像中提取关键信息而量身定制的。
它包含 25 个关键信息类别，总共约 69000 个文本框，比现有公共数据集大约 2 倍。
大量实验验证了包括视觉特征、文本特征和空间关系在内的所有信息都可以有益于关键信息的提取。
已经表明，SDMG-R 可以有效地从不可见模板的文档图像中提取关键信息，并在最近流行的基准 SROIE 和我们的 WildReceipt 上获得新的最先进的结果。
我们的代码和数据集将公开发布。

- paramount
  - adj. 至为重要的，首要的；至高无上的，权力最大的
  - n. 最高统治者
- modality
  - n. 形式，形态；程序；物理疗法；主要的感觉

Index Terms—Key information extraction, Document images, Graph reasoning, Dual modality.

索引词——关键信息提取、文档图像、图形推理、双模态。

# 1 介绍



# 2 相关工作

# 3 方法

# 4 WildReceipt

# 5 实验

# 6 总结



