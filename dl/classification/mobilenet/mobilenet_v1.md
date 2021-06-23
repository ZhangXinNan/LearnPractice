# 0 摘要

- depthwise separable convolutions
  - 大大减少运算量和参数数量
- two simple global hyperparameters
  - width
  - depth

# 1 介绍

## 1.1 背景
1. CNN越来越流行
2. 倾向于越来越深和越来越复杂的结构来提升准确率，没有考虑模型大小和速度
3. 现实世界中有些应用需要小且快的模型

## 1.2 怎么做的
1. 高效的网络结构
2. 两个超参数使模型更小、更低延迟


# 2 早先工作

MobileNets是第一个关注低延迟且小尺寸的模型。
