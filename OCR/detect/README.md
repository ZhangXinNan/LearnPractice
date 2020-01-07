[微软字符识别新研究：OCR提升自然场景下文字识别度](http://www.cnetnews.com.cn/2015/0401/3049311.shtml)
阶段①：采用对比极值区域CER检测方法
阶段②：基于浅层神经网络的文字/非文字分类算法


[chenxinpeng/SSD_scene_text_detection](https://github.com/chenxinpeng/SSD_scene_text_detection)
Detect text in natural images with SSD, Single Shot Detection

[SSD: Signle Shot Detector 用于自然场景文字检测](http://blog.csdn.net/u010167269/article/details/52851667)



[subokita/Robust-Text-Detection](https://github.com/subokita/Robust-Text-Detection)
Robust Text Detection implementation based on [ICIP2011_RobustTextDetection.pdf](http://www.stanford.edu/~hchen2/papers/ICIP2011_RobustTextDetection.pdf)


[chongyangtao/Awesome-Scene-Text-Recognition](https://github.com/chongyangtao/Awesome-Scene-Text-Recognition)


[文字检测与识别资源](http://blog.csdn.net/peaceinmind/article/details/51387367)

[文字检测与识别](http://lufo.me/2016/08/text_detection/)
[文字检测方法综述](http://lufo.me/2017/02/text_detect/)

[[论文笔记]Arbitrary-Oriented Scene Text Detection via Rotation Proposals](https://blog.csdn.net/u013250416/article/details/78597557)
```
Arbitrary-Oriented Scene Text Detection via Rotation Proposals
论文地址：https://arxiv.org/abs/1703.01086
github地址：https://github.com/mjq11302010044/RRPN
```


[Incentering/pixel-anchor-link-and-text-detector-experience](https://github.com/Incentering/pixel-anchor-link-and-text-detector-experience)
1. 最好的还是**pixel-anchor**这篇论文
2. pixel-link和PSENet这些基于像素link的算法，不可避免会碰到粘连的问题，实际应用达不到工业级的鲁棒程度，从原理上没法解决。 比如我们在开发银行存单文本检测器的时候，字段内容和字段名称会印重，我们需要把它们分开，像素link绝对解决不了这个问题，只有直接回归的方式可以。
3. 白翔试验室的论文Textboxes, Textboxes++, seglink，还有旷世那篇著名的East，我天，什么鬼，在长中文场景实际根本没法用，我们都复现了一遍
4. 对于印刷体那种长得变态的文本行，CTPN还可以勉强用用，但是速度太慢。
5. 