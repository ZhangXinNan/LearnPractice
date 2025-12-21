
- 模块列表
  - 模块概述
  - 文档图像方向分类模块
  - 文档类视觉语言模型模块
  - 公式识别模块
  - 版面区域检测模块
  - 版面分析模块
  - 印章文本检测模块
  - 表格单元格检测模块
  - 表格分类模块
  - 表格结构识别模块
  - 文本检测模块
  - 文本图像矫正模块
  - 文本行方向分类模块
  - 文本识别模块
  - 图表解析模块



# 0 模块概述
模块是实现基本功能的最小单位。模块通常使用单个模型去完成特定的任务，比如文本检测、图像分类等基本功能。模块作为基础构建单元，为更复杂的应用场景提供了必要的功能支持。这种设计方式使得用户可以根据需要灵活选择和组合不同的模块，从而简化了开发流程，并提高了开发的灵活性和效率。

# 1 文档图像方向分类模块使用教程
一、概述

文档图像方向分类模块主要是将文档图像的方向区分出来，并使用后处理将其矫正。在诸如文档扫描、证照拍摄等过程中，有时为了拍摄更清晰，会将拍摄设备进行旋转，导致得到的图片也是不同方向的。此时，标准的OCR流程无法很好地应对这些数据。利用图像分类技术，可以预先判断含文字区域的文档或证件的方向，并将其进行方向调整，从而提高OCR处理的准确性。

二、支持模型列表

推理耗时仅包含模型推理耗时，不包含前后处理耗时。

模型 | 模型下载链接 | Top-1 Acc（%） | GPU推理耗时（ms）[常规模式 / 高性能模式] | CPU推理耗时（ms） [常规模式 / 高性能模式] | 模型存储大小（MB）| 介绍
---|---|---|---|---|---|---
PP-LCNet_x1_0_doc_ori | 推理模型/训练模型 | 99.06 | 2.62 / 0.59 | 3.24 / 1.19 | 7 | 基于PP-LCNet_x1_0的文档图像分类模型，含有四个类别，即0度，90度，180度，270度

# 2 文档类视觉语言模型模块使用教程
一、概述

文档类视觉语言模型是当前一种前沿的多模态处理技术，旨在解决传统文档处理方法的局限性。传统方法往往局限于处理特定格式或预定义类别的文档信息，而文档类视觉语言模型能够融合视觉与语言信息，理解并处理多样化的文档内容。通过结合计算机视觉与自然语言处理技术，模型可以识别文档中的图像、文本及其相互关系，甚至能理解复杂版面结构中的语义信息。这使得文档处理更加智能化、灵活化，具备更强的泛化能力，在自动化办公、信息提取等领域展现出广阔的应用前景。

> 测试不成功，并且模型很大。

# 3 Formula Recognition Module Tutorial
I. Overview

The formula recognition module is a key component of an OCR (Optical Character Recognition) system, responsible for converting mathematical formulas in images into editable text or computer-readable formats. The performance of this module directly affects the accuracy and efficiency of the entire OCR system. The formula recognition module typically outputs LaTeX or MathML code of the mathematical formulas, which will be passed as input to the text understanding module for further processing.

# 4 Layout Detection Module Tutorial
I. Overview

The core task of structure analysis is to parse and segment the content of input document images. By identifying different elements in the image (such as text, charts, images, etc.), they are classified into predefined categories (e.g., pure text area, title area, table area, image area, list area, etc.), and the position and size of these regions in the document are determined.

II. Supported Model List

The inference time only includes the model inference time and does not include the time for pre- or post-processing.

The layout detection model includes 20 common categories: document title, paragraph title, text, page number, abstract, table, references, footnotes, header, footer, algorithm, formula, formula number, image, table, seal, figure_table title, chart, and sidebar text and lists of references

