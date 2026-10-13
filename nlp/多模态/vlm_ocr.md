# VLM 是否已经超越传统 OCR？VLM OCR 的原理是什么？

先说结论：截至 2026 年，VLM 在复杂文档解析、表格理解、语义抽取等任务上，已经表现出很强的优势；但是在纯文本检测与识别方面，还不能说全面超越了 DBNet + CRNN/SVTR 等传统 OCR 方法。

尤其是你熟悉的身份证、护照、多国证件 OCR，如果目标是字符级准确率高、推理速度快、结果可控，传统 OCR 仍然有很强的竞争力。

我建议把这个问题分成四个层次：

1. 传统 OCR 与 VLM OCR 有什么本质区别？
2. VLM 究竟如何识别图像中的文字？
3. 哪些任务 VLM 已经更强，哪些仍适合传统 OCR？
4. 如果你现在重新做 OCR 项目，应该采用什么技术方案？

## 一、传统 OCR 与 VLM OCR 的本质区别

### 1. 传统 OCR：先检测，再识别

你以前熟悉的架构：

```
Document Image
      |
      v
   DBNet
      |
      v
Text Bounding Boxes
      |
      v
Crop / Rectification
      |
      v
CRNN / SVTR / Other Recognizer
      |
      v
Recognized Text
      |
      v
Rules / Layout Analysis / KIE
      |
      v
Structured Results
```

典型的传统 OCR 系统可以分成三个部分。

| 模块                    | 作用           | 典型算法              |
| --------------------- | ------------ | ----------------- |
| Text Detection        | 找到文字在哪里      | DBNet、EAST、CRAFT  |
| Text Recognition      | 将文字图像转换为字符序列 | CRNN、SVTR、PARSeq  |
| Post-processing / KIE | 恢复阅读顺序、抽取字段  | 规则、分类器、LayoutLM 等 |

特点是分而治之。

DBNet 只负责找到文字区域，不需要理解文字含义。Recognizer 只需要识别文字，不需要理解证件或者发票的语义。

优势是模型小、速度快、容易部署、模块独立、错误容易排查。

缺点是复杂版面需要额外的布局分析和字段抽取模块，每个模块的错误还可能向后传播。

### 2. VLM OCR：从图像直接生成文字或结构化结果

典型的生成式 VLM OCR：

```
Document Image
      |
      v
Vision Encoder
      |
      v
Visual Features / Tokens
      |
      v
Projector / Connector
      |
      v
LLM Decoder  <----- Prompt / Instructions
      |
      v
Text / Markdown / HTML / JSON
```

例如输入一张发票，用户可以要求：

任务 A：识别所有文字

```
Read all text in this image.
```

任务 B：解析文档结构

```
Convert this document into Markdown.
Preserve tables and reading order.
```

任务 C：抽取字段

```
Extract the invoice number, date,
supplier and total amount as JSON.
```

这三个任务有可能使用同一个 VLM 完成。

区别在于：

传统 OCR：

```
Image → Text
```

VLM OCR：

```
Image + Instruction → Text / Structure / Meaning
```

但需要注意：并不是所有现代 OCR-VLM 都完全跳过检测和版面分析。实际产品仍经常采用版面检测、区域裁剪、VLM 识别的混合架构。

## 二、VLM 是怎样识别文字的？

这是我认为最值得你深入理解的地方。

### 第一步：Vision Encoder 将图片变成 Visual Tokens

传统 CRNN：

```
Text Line Image
      |
      v
CNN Feature Extraction
      |
      v
Sequence Features
      |
      v
CTC / Attention Decoder
      |
      v
Characters
```

例如：

```
Image: [ PASSPORT ]
              |
              v
Feature Sequence
              |
              v
"P A S S P O R T"
```

VLM 则不同。

假设图片尺寸是 1024 × 1024，Vision Encoder 使用 ViT。

首先把图片切成 patch：

```
Image 1024 × 1024
       |
       v
Patch Embedding
       |
       v
Visual Tokens
       |
       v
Vision Transformer
       |
       v
Visual Representations
```

如果 Patch Size = 16，在不考虑额外 token 或压缩的简化情况下：

- 每行 64 个 patch
- 每列 64 个 patch
- 总共 4096 个 patch

每个 patch 转换为一个特征向量。

假设维度是 1024：

```
Image
  |
  v
[4096, 1024]
```

这里最重要的区别是：

Visual Token 不等于 Character Token。

一个 Visual Token 不一定对应一个字符，可能包含笔画、字符局部、背景或文字周围的结构信息。

而经过 Vision Transformer 后，token 还可以融合其他区域的上下文信息。

实际模型通常使用动态分辨率、patch 合并、区域裁剪或视觉 token 压缩，避免处理高分辨率文档时成本过高。

### 第二步：Connector 将视觉特征转换成 LLM 能处理的表示

视觉模型的输出可能是：

```
Visual Features
[4096, 1024]
```

而 LLM 的隐藏维度假设是 2048。

那么需要一个映射：

```
Visual Features
      |
      v
MLP Projector
      |
      v
[4096, 2048]
```

这样视觉特征就可以作为视觉 token 的 embedding 表示进入语言模型。

不同模型可能采用：

- Linear Projector
- MLP Projector
- Q-Former
- Token Compression / Resampler

它们的共同目标，是将视觉信息转换为适合语言模型使用的特征表示。

### 第三步：LLM 根据图像和指令生成文字

假设原图内容是：

```
Name: JOHN SMITH
Passport No: AB1234567
```

输入：

```
<visual tokens>

Read all text from the image.
```

LLM 逐个生成输出 token：

```
Name
:
JOHN
SMITH
Passport
No
:
AB1234567
```

这里字符输出并不是必须由独立的 CRNN 或 CTC 头产生。

它通过语言模型的自回归生成完成。

简化公式：

\\[ P(Y \mid I,Q)=\prod\_{t=1}^{T}P(y_t\mid y\_{\<t},I,Q) \\]

其中：

- I：输入图像
- Q：任务指令
- Y：输出文本序列
- y_t：第 t 个输出 token

这也是 VLM OCR 与传统 OCR 最重要的区别之一。

## 三、为什么 VLM 能够识别文字？

你可能会问：

Vision Encoder 不就是提取图像语义特征吗？为什么它能识别极其细小的字符？

这里有三个关键原因。

### 1. 高分辨率视觉特征保留了字符细节

通用图像分类模型只需要知道一张图片是不是猫。

但是 OCR 需要区分：

```
O / 0
I / l / 1
B / 8
S / 5
```

这些差别非常细微。

因此文档 VLM 往往需要使用高分辨率输入、局部裁剪或专门训练的视觉编码器。

如果视觉编码阶段已经丢失了一个字符的关键笔画，后面的 LLM 不可能可靠地恢复原始信息。

### 2. 语言模型能够利用上下文

例如原图模糊：

```
Invoice Date: 2026-10-1?
```

LLM 不仅能看到字符形状，还能利用日期格式、上下文和任务指令。

这有时候可以提高识别效果。

但也会带来严重问题：

VLM 可能生成一个看起来合理、实际上错误的字符。

例如护照号：

```
AB1234567
```

被模型识别为：

```
AB1234587
```

模型生成的结果非常自然，但这个错误在实际证件业务中可能完全不能接受。

所以在高精度 OCR 中：

> 语言先验既是 VLM 的优势，也是产生 hallucination 的风险来源。

### 3. 大规模文档数据训练

VLM 可以通过多种任务联合训练：

```
Image → Text
Image → Markdown
Image → JSON
Image + Question → Answer
Document → Table Structure
Document → Key-Value Pairs
```

这样模型不只学会识别字符，还能学习文档中的版面规律和字段之间的关系。

训练通常仍然采用 token-level cross-entropy：

\\[ \mathcal{L}=-\sum_t\log P(y_t\mid y\_{\<t},I,Q) \\]

具体模型可能还包括视觉预训练、图文对齐、合成文档训练及其他训练阶段。

## 四、VLM 在哪些任务上超过传统 OCR？

不能笼统比较，需要按任务划分。

| 任务        | 传统 OCR         | VLM OCR           | 更合理的选择       |
| --------- | -------------- | ----------------- | ------------ |
| 清晰印刷文字识别  | 很强             | 很强                | 根据 CER、成本比较  |
| 大批量短文本行识别 | 高效             | 可完成，但生成有开销        | 通常传统 OCR     |
| 固定模板身份证   | 成熟             | 可以完成              | 传统或 Hybrid   |
| 护照 MRZ    | 容易增加格式校验       | 存在生成错误风险          | 专用 OCR + 校验  |
| 发票字段抽取    | OCR + 规则/KIE   | 可直接语义抽取           | VLM 值得优先评估   |
| 表格结构恢复    | 需要 Table Model | 可生成 HTML/Markdown | 专用文档 VLM 有优势 |
| 数学公式识别    | 需要专用模型         | 可以生成 LaTeX        | 需实测比较        |
| 任意复杂版式文档  | Pipeline 较复杂   | 泛化能力可能更好          | VLM 或 Hybrid |
| 多语言混合文档   | 取决于识别模型        | 通用能力较灵活           | 依语言及数据比较     |
| 高吞吐、低延迟部署 | 模型可较轻量         | 生成式计算有开销          | 通常传统 OCR     |

尤其要区别以下三个任务。

任务 1：Text Recognition

将文字图片转换为字符序列。

衡量 CER、WER、Exact Match。

任务 2：Document Parsing

不仅输出文字，还需要表格、阅读顺序、标题层级、公式等。

衡量结构准确率、表格相似度、编辑距离等。

任务 3：Key Information Extraction

不只是识别文字，还需要理解哪些文字属于哪个字段。

衡量字段级 Precision、Recall、F1、Exact Match。

因此：

文档解析 Benchmark 上 VLM 获胜，不等于逐字符 OCR 识别准确率也必然更高。

## 五、2026 年值得重点研究的 OCR-VLM 模型

我建议重点关注三个方向，不需要把所有新模型都研究一遍。

[PaddlePaddle/PaddleOCR-VL · Hugging Face](https://images.openai.com/static-rsc-4/NkkQg-_4m7ns5Pg3JdXbz_w_yhCd46-bw94NTLYZXW3tomn5zpyH0BESbSLpH-lNr5WiY7BKU15zXYogJP8lTgCGDLVXAN1J2lpjrZrGFOA5aQizF0ibItQNThfTtodeQZMgvQji4wkYqe3VBIOp7jbGDAZpodtjjbSEyLdnMCc?purpose=inline)

1\. PaddleOCR-VL-1.6

最推荐：了解生产级文档解析架构

采用约 0.9B 参数的 VLM 组件，并继续结合 PP-DocLayoutV3 进行版面分析。支持文字、表格、公式等文档元素解析。2026 年 5 月发布的 1.6 版在 OmniDocBench v1.6 上报告了 96.3% 综合指标，但这不是字符识别准确率。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

+1



官方 GitHub

[DeepSeek-OCR: Solving LLM Context Limits with Optical Compression | by Ejiro Onose | Medium](https://images.openai.com/static-rsc-4/GYTWouDJJeZMIbTI-YDmESMXcUOd6dolGERMXNTjzfXfirarAzieipuyFcNNBiZjWiGTOeeHHNKMTJXn9aW10weLmRS0MZDrnC-s9VhlzuEvPUG0s343qpM1cewbw8zUYWTgks5QwgExdRqwK39rxwCPgNsbnuoDtiWF861HQHc?purpose=inline)

2\. DeepSeek-OCR / OCR2

推荐：理解视觉 token 压缩

重点研究如何用相对少量的视觉 token 表达大量文字信息，以及压缩与识别精度之间的权衡。这是传统文本行识别工程师值得关注的新技术问题。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

+1



官方 GitHub

[Qwen2.5-VL实现细节：原生动态分辨率(Naive Dynamic Resolution)- 大数跨境](https://images.openai.com/static-rsc-4/FSjajO2lPgf1iI7eAYeMCF2H8CXOgI97bQdPgTm8FxhhAYbUze2w_-fvzuYsiIRhaGzj8VOh6TbOeqq_ws0mRNw1eV2VpS5_SXJ1JQohbOfMKw8up_K_K7P3PqB1nqcc3Q6wUv3edzxttF7DbLpiHsS2MM6k10VyK1C1Z7hvOYQ?purpose=inline)

3\. Qwen3-VL

推荐：学习通用 VLM 做 OCR 和字段抽取

与文档专用 OCR 模型不同，Qwen-VL 适合学习自然语言提示、结构化 JSON 输出、复杂字段理解以及多模态微调。

官方 GitHub

其中 PaddleOCR 的发展非常有代表性。

官方现在同时维护两条路线：

- PP-OCRv6：轻量级传统文字检测和识别，重视字符准确率、运行效率与部署。
- PaddleOCR-VL-1.6：视觉语言模型驱动的文档解析，重视复杂版面、表格、公式及文字元素的整体理解。

这本身就说明：传统 OCR 和 VLM OCR 并非简单的替代关系。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub

+1



## 六、如果重新设计一个多国证件 OCR 系统，我会怎么做？

以你熟悉的护照、身份证、驾驶证等证件为例，我不会马上删除原来的 DBNet + Recognizer。

而是建立三个方案，使用相同的测试集比较。

方案 A：Traditional OCR

DBNet → SVTR → Rules → JSON

作为成熟 Baseline，重点测试字符准确率、字段准确率、速度

方案 B：End-to-End VLM

Document Image → VLM → JSON

测试跨国家、跨模板泛化能力，以及不依赖传统检测流程的效果

方案 C：Hybrid OCR + VLM

Traditional OCR + VLM

Field Matching / Validation

Structured JSON

利用传统 OCR 的字符识别能力和 VLM 的语义理解能力

对于证件 OCR，我目前更倾向于先验证方案 C。

例如：

```
Document Image
       |
       v
Document Classification
       |
       v
Traditional OCR
       |
       v
OCR Text + Bounding Boxes
       |
       v
Field Extraction / Validation
       |
       v
Reliable?
   /         \
 Yes         No
  |           |
  v           v
Output    VLM Fallback
              |
              v
        Cross Validation
              |
              v
       Output / Review
```

但这里有一个工程细节：传统 OCR 的置信度不能直接当成字符正确概率，需要结合实际错误分布做校准。对于护照 MRZ，还可以使用校验位帮助验证。

而且当传统 OCR 和 VLM 输出不一致时，也不能简单认为 VLM 一定正确。特别是身份证号、护照号这些字段，需要保留校验或人工复核路径。

### 评测指标

| 指标                            | 测试目的          |
| ----------------------------- | ------------- |
| CER / WER                     | 字符及单词识别错误     |
| Exact Match                   | 整个字段是否完全正确    |
| Field Precision / Recall / F1 | 字段抽取质量        |
| Hallucination Rate            | 是否生成图像中不存在的信息 |
| P50 / P95 Latency             | 生产环境响应时间      |
| Throughput                    | 单位时间处理文档数量    |
| GPU Memory                    | 部署成本          |

尤其建议单独统计三种错误：字符识别错误、字段对应错误、编造字段。它们对应的改进方案完全不同。

## 七、对你学习 VLM 的建议

既然你已经非常熟悉 DBNet、CRNN、SVTR，以及 OCR 系统的工程实现，我建议不要再从基础 OCR 算法重新开始。

直接围绕三个技术问题来学习。

问题一：VLM 为什么能读懂字符？

研究 ViT、高分辨率视觉编码、visual token、projector、LLM decoder。重点理解视觉特征如何保留足够的字符细节。

问题二：为什么 VLM 能处理复杂文档？

研究 PaddleOCR-VL 的版面分析、区域识别、阅读顺序恢复，以及表格、公式、字段结构化的处理流程。

问题三：为什么不是所有 OCR 都用 VLM？

研究 DeepSeek-OCR 的视觉 token 压缩、生成式推理成本、识别幻觉，以及传统 OCR + VLM 的混合方案。

对于你这样的工程背景，我认为最有价值的小项目不是简单跑通 Qwen3-VL，而是：

用同一批证件数据，对比 DBNet + SVTR、Qwen3-VL 和 Hybrid 三套方案，在字符准确率、字段准确率、延迟、显存及成本上的真实表现。

最终你要掌握的核心认识是：

> 传统 OCR 主要解决“图像里写了什么”；现代 VLM OCR 不仅解决“写了什么”，还尝试解决“这些文字组成了什么结构、表达了什么含义”。但在精确转写任务中，语义理解能力不必然带来更低的字符错误率。

这也是我认为从传统 OCR 算法工程师升级到多模态视觉算法工程师，最值得掌握的技术区别。



