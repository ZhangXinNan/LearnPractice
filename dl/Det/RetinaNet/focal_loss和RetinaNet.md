

类别不均衡（class imbalance)是目标检测模型训练一大难点。
- faster r-cnn 
  - 第一阶段RPN过滤掉一大部分负样本，第二阶段的检测模块只需少量的候选框。而且检测模块还采用正负样本固定比例抽样（比如1:3）或者OHEM方法（online hard example mining）来进一步解决正负样本不平衡问题。
- SSD 
  - hard mining，从大量的负样本中选出loss最大的topk的负样本以保证正负样本比例为1:3。


与抽样方法不同，Focal Loss从另外的视角来解决样本不平衡问题，那就是根据置信度动态调整交叉熵loss，当预测正确的置信度增加时，loss的权重系数会逐渐衰减至0，这样模型训练的loss更关注难例，而大量容易的例子其loss贡献很低。这里以二分类来介绍Focal Loss（FL），对二分类最常用的是cross entropy （CE）loss，

