开源项目：
[ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)
[cmusatyalab/openface](https://github.com/cmusatyalab/openface)
[davidsandberg/facenet](https://github.com/davidsandberg/facenet)

年龄和性别：
[dpressel/rude-carnie](https://github.com/dpressel/rude-carnie)
[yu4u/age-gender-estimation](https://github.com/yu4u/age-gender-estimation)
[BoyuanJiang/Age-Gender-Estimate-TF](https://github.com//BoyuanJiang/Age-Gender-Estimate-TF)

文章介绍：
[技术综述】人脸年龄估计研究现状](https://zhuanlan.zhihu.com/p/39029303)

# 2.1 公开数据集
## 2.1.1 The IMDB-WIKI dataset数据集 【1】
网址：https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/
介绍：从IMDb和维基百科上爬取的名人图片，根据照片拍摄时间戳和出生日期计算得到的年龄信息。应该是目前最大的人脸年龄数据集
大小： 共523051张face images
标签：年龄和性别

## 2.1.2 Adience Benchmark Of Unfiltered Faces For Gender AndAge Classification 数据集【2】
网址：https://www.openu.ac.il/home/hassner/Adience/data.html#frontalized
介绍：iPhone5或更新的智能手机拍摄
标签：年龄段（0-2, 4-6, 8-13, 15-20, 25-32, 38-43, 48-53, 60+）
大小：26580张， 2284人

## 2.1.3 Cross-Age Celebrity Dataset (CACD)【3】
网址：http://bcsiriuschen.github.io/CARC/
描述：与数据集2.1.1类似
标签：年龄
大小：163446张名人图片，约4.4G


# 2.2 算法评价指标
## 2.2.1 MAE
平均绝对误差是指估计年龄和真实年龄之间绝对误差的平均值，其表达式为

## 2.2.2 CS
年龄估计性能评价中，人们关注更多的是所估计出的年龄值的绝对误差范围是否在人们能接受的范围内，因此累积指数被用于年龄估计的性能评价中，累积指数的定义如下：

# 3.1 特征提取模型

# 3.2 年龄估计
分类问题：每个年龄看作一个类
回归问题：年龄值的增长是一个有序数列的不断变化过程

# 深度学习研究思路
