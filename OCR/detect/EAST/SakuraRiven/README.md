

[SakuraRiven/EAST](https://github.com/SakuraRiven/EAST)

Only RBOX part is implemented.
Using dice loss instead of class-balanced cross-entropy loss. Some codes refer to argman/EAST and songdejia/EAST
The pre-trained model provided achieves 82.79 F-score on ICDAR 2015 Challenge 4 using only the 1000 images. see here for the detailed results.
```
Model	Loss	Recall	Precision	F-score
Original	CE	72.75	80.46	76.41
Re-Implement	Dice	81.27	84.36	82.79
```


Only tested on
```bash
Anaconda3
Python 3.7.1
PyTorch 1.0.1
Shapely 1.6.4
opencv-python 4.0.0.21
lanms 1.0.2
```



# 2019-12-10 
已经可以训练。

存在问题：
1. 加载已经训练过的模型，继续训练
2. 画loss曲线
3. 