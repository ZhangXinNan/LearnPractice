结合你已有十多年的 CV/OCR 经验，以及现在想找国内计算机视觉算法岗位的目标，我建议你只精读 6 篇论文，再选读 1 篇综述。

不建议从几十篇论文开始学习，也不建议一上来就读最新 Qwen-VL 的全部技术细节。

你的目标应该是：

- VLM： 搞懂视觉与语言如何对齐、视觉特征如何接入 LLM、现代 VLM 如何训练。
- VLM + OCR： 搞懂为什么 VLM 可以识别整张文档、如何处理复杂版面、怎样优化精度和推理成本。

## 一、VLM：必读 3 篇

## 01

CLIP — Learning Transferable Visual Models From Natural Language Supervision

2021 · 必读 · 精读

核心问题：图像与文本为什么能够进入同一个特征空间？

重点学习 Image Encoder、Text Encoder、Contrastive Learning、Zero-shot Classification。

学会后应该能解释：为什么 CLIP 不需要重新训练分类头，就能利用自然语言完成图像分类和检索。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 02

BLIP-2 — Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

2023 · 必读 · 重点看架构

核心问题：已有 Vision Encoder 和 LLM，怎样把两者连接起来？

重点学习 Frozen Vision Encoder、Q-Former、Frozen LLM，以及两阶段预训练。

搞懂视觉特征如何转换为语言模型能利用的信息。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 03

LLaVA — Visual Instruction Tuning

2023 · 必读 · 重点看训练

核心问题：如何训练一个能够回答图像问题的多模态助手？

重点学习 Vision Encoder + Projector + LLM、Visual Instruction Tuning、SFT 数据格式。

这是最值得结合代码学习的一篇，能够帮助你建立完整的 VLM 工程认识。

[image](https://www.google.com/s2/favicons?domain=https://searcharxiv.org\&sz=32)

Search arXiv



学完这三篇，你应该能够画出下面的知识主线：

```
CLIP
  │
  └── 图像与语言如何对齐？
              ↓
BLIP-2
  │
  └── 视觉编码器如何连接 LLM？
              ↓
LLaVA
  │
  └── 如何通过指令微调获得视觉问答能力？
              ↓
Modern VLM
```

现代 VLM 的技术报告，建议选读 Qwen2.5-VL Technical Report。 特别关注动态分辨率、视觉定位、文档解析和结构化抽取。它不是我的第四篇精读论文，因为理解技术路线比记住某个版本的架构细节更重要。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 二、VLM + OCR：必读 3 篇

## 04

PaddleOCR-VL — Boosting Multilingual Document Parsing via a 0.9B Ultra-Compact Vision-Language Model

2025 · 必读 · OCR 首选

核心问题：如何设计一个真正实用、轻量化的 VLM 文档解析系统？

重点看动态分辨率视觉编码、语言解码器、文档元素识别、多语言支持和工程效率。

这篇与你过去做的 OCR 项目最接近。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 05

DeepSeek-OCR — Contexts Optical Compression

2025 · 必读 · 重点看视觉压缩

核心问题：为什么一整页密集文字能够用相对少量的视觉 token 表示？

重点学习 DeepEncoder、Visual Token Compression，以及压缩率和 OCR 准确率之间的关系。

这是我认为对你最有启发的一篇，因为它直接涉及传统 OCR 工程师熟悉的精度与计算开销权衡。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



## 06

OCRBench — On the Hidden Mystery of OCR in Large Multimodal Models

2024 期刊版 · 必读 · 重点看评测

核心问题：怎样科学地评价 VLM 的 OCR 能力？

重点关注 Text Recognition、Document VQA、Key Information Extraction 和公式识别等任务。

阅读它可以避免把文档理解准确率误当成纯字符识别准确率。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



这里还建议你了解 OCRBench v2，但不必完整阅读。2026 年的 MDPBench 则对真实拍摄文档、多语种文档评价很有参考价值。

[image](https://www.google.com/s2/favicons?domain=https://github.com\&sz=32)

GitHub



## 三、综述只推荐 1 篇

Multimodal Large Language Models: A Survey（2025）

它覆盖多模态模型的整体架构、训练方法、模态融合和评测挑战。

[image](https://www.google.com/s2/favicons?domain=https://arxiv.org\&sz=32)

arXiv



不过这篇综述的范围比 VLM 更大，还包含音频、视频、其他生成模态等内容。

我的建议是把它当成知识地图，而不是一本教材。 重点看架构分类、训练方式和相关模型对比，不必逐篇追踪它引用的论文。

如果你只关心 VLM+OCR，实际更值得先读 PaddleOCR-VL，而不是先读综述。

## 四、按你的时间，具体怎么安排？

建议阅读计划

阅读 6 篇，总共约 17 小时

0/6 完成

CLIP

3 小时

对比学习、跨模态对齐

BLIP-2

2 小时

Q-Former、视觉到语言的桥接

LLaVA

3 小时

Projector、SFT、指令数据

PaddleOCR-VL

4 小时

现代 OCR-VLM 架构

DeepSeek-OCR

3 小时

视觉 token 压缩

OCRBench

2 小时

OCR 评测方法

&#x20;复制阅读清单

这里的时间是建议的第一遍阅读预算，不包括动手复现。为了避免陷入细节，每篇论文先掌握四个问题：

- What： 这篇论文提出了什么核心思想？
- When： 它解决什么问题，适合什么场景？
- How： 主要模型架构和训练流程是什么？
- Why： 为什么这种方法能够有效？局限在哪里？

不必从头到尾推导全部数学公式，也不必逐项研究所有消融实验。

## 五、如果时间更有限，我会进一步删到 4 篇

按你的 OCR 背景和求职目标，甚至可以只保留：

1. CLIP — 图像语言如何对齐
2. LLaVA — VLM 怎样构造和训练
3. PaddleOCR-VL — VLM 如何应用到 OCR
4. DeepSeek-OCR — 高分辨率文档如何高效编码

BLIP-2 可以只看模型架构图，OCRBench 可以只看任务分类和评测方法。

我更建议你先读透 4 篇，再亲自跑一次 PaddleOCR-VL，与熟悉的 DBNet + SVTR 做同数据集对比，而不是花一个月连续阅读 20 篇 VLM 论文。

这样既补上 VLM 理论，又能把新知识和过去的 OCR 经验连接起来，最后形成面试时能够真正讲清楚的工程能力。




