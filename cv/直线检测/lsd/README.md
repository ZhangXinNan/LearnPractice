

LSD是一种局部提取直线的算法，速度比Hough要快。
但是有局部算法的缺点：
1.对于直线相交情况，因为设置了每个点是否USED，因此每个点只能属于一条直线，若有相交必有至少一条直线被割裂为两条。又因为其基于梯度，直线交点梯度值往往又较小（不被检测为边缘点），因此很有可能相交的两条直线在交点处被割裂为四条线段。
2.由于局部检测算法自增长的特点，对于长线段被遮挡、局部模糊等原因经常割裂为多条直线。这些缺点在Hough变换中不存在。



# 参考
* [基于LSD的直线提取算法](https://blog.csdn.net/tianwaifeimao/article/details/17678669)
* [论文回顾之一 一种新的直线段检测算法---LSD：a Line Segment Detector](https://blog.csdn.net/polly_yang/article/details/10085401)


