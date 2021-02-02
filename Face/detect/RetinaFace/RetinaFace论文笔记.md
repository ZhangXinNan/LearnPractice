
RetinaFace: Single-stage Dense Face Localisation in the Wild

RetinaFace：野外单阶段密集脸部定位
__________

# 0 概述
```
tremendous      adj. 极大的，巨大的；惊人的；极好的
stride          n. 大步；步幅；进展
                vt. 跨过；大踏步走过；跨坐在…
                vi. 跨；跨过；大步行走
uncontrolled    adj. 不受控制的
```

尽管在不受控制的面部检测方面已取得了长足的进步，但在野外进行准确有效的面部定位仍然是一个开放的挑战。本文介绍了一种强大的单级面部检测器，名为RetinaFace，它可以利用**联合监督**和**自我监督**的多任务学习优势，对各种比例的面部进行像素级面部定位。具体来说，我们在以下五个方面做出了贡献：
（1）我们在WIDER FACE数据集上手动注释了五个面部标志，并借助此额外的监督信号在硬脸检测中观察到了重大改进。 
（2）我们进一步添加了一个自监督网格解码器分支，用于与现有的监督分支并行地预测像素级3D形状人脸信息。 
（3）在WIDER FACE硬质测试仪上，RetinaFace的表现优于最新的平均精度（AP）1.1％（达到AP等于91.4％）。 
（4）在IJB-C测试仪上，RetinaFace使最先进的方法（ArcFace）可以改进其面部验证结果（对于FAR = 1e-6，TAR = 89.59％）。 
（5）通过采用轻型骨干网络，RetinaFace可以在单个CPU内核上实时运行，以提供VGA分辨率的图像。
额外的注释和代码已在以下位置提供：https://github.com/deepinsight/insightface/tree/master/RetinaFace。


