
# 1 基本概念

## 1.1 混淆矩阵
混淆矩阵又称错误矩阵，指每个类别下，模型预测结果的类别和数量在一个矩阵中展示出来。

## 1.2 二元混淆矩阵
* TP : True Positive        真阳
* FN : False Negative       假阴
* FP : False Positive       假阳
* TN : True Negative        真阴

真实标签 | 预测为正 | 预测为负 | 
--| --| -- | --
真实为正 | **TP** | FN | 
真实为负 | FP | **TN** | 

### 1.2.1 召回 Recall 
又称为 TPR （True Positive Rate）
或者 敏感度Sensitivity

通俗理解：真实为正的样本中识别为正的占比。

$TPR = \frac {TP} {TP+FN}$

### 1.2.2 精度Precision 
又称为PPV (Positive Predictive Value)

通俗理解：识别为正的样本中真实为正的占比。

$PPV=\frac{TP}{TP+FP}$

### 1.2.3 准确率 Accuracy
通俗理解：所有样本中识别正确的比例。

$accuracy = \frac {TP+TN} {TP + FN + FP + TN}$

## 1.3 P-R曲线 (精度-召回曲线) (Precision-Recall curve)
直观理解：阈值降低，召回率升高时，精度下降情况。
* 横坐标：召回 Recall
* 纵坐标：精度 Precision

## 1.4 AP 平均精度 （Average-Precision）

P-R曲线围起来的面积

### mAP
把每个类别的AP都单独拎出来，然后计算所有类别AP的平均值 。

## 1.5 受试者工作特征曲线 （Receiver Operating Curve）
直观理解：阈值降低，假阳升高时，真阳升高情况。

* 横轴：假阳率 FPR    $FPR = \frac{FP} {FP + TN}$
* 纵轴：真阳率 TPR    $TPR = \frac{TP} {TP + FN}$

P 为真实的正样本的数量；
N 为真实的负样本的数量。

## 1.6 AUC (Area Under Curve)
ROC曲线围住的面积。
AUC就是从所有正样本中随机选取一个，所有负样本中随机选取一个，然后用分类器预测，概率分别为p1、p0，p1>p0的概率就等于AUC。所以AUC反应的是**分类器对样本的排序能力**。根据这个解释，如果我们完全随机的对样本分类，那么 AUC应该接近0.5。另外，**AUC对样本是否均衡并不敏感**，这也是不均衡样本通常用AUC评价分类器性能的一个原因。

## 1.7 F1 score
$F1 = \frac{2*Precision*Recall} {Precision + Recall}$  



# 参考资料
* 《深度学习与计算机视觉——算法原理、框架应用与代码实现》
* 《百面机器学习》
* [如何理解机器学习和统计中的AUC？](https://www.zhihu.com/question/39840928)
* 《机器学习》周志华