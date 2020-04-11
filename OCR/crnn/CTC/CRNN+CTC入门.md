
# 1 CRNN
CRNN可分成三个部分。假设输入图像是(32,100,3)，顺序为(height,width,channel)。

## 1.1 Convlutional Layers
类似于LeNet5的的卷积网络。输出为(1,25,512)。

## 1.2 Recurrent Layers
深层双向LSTM网络。

## 1.3 Transcription Layers
将RNN输出做softmax后，为字符输出。

# 2 Connectionist Temporal Classification(CTC)详解

## 2.1 CNN Feature map
feature map 为 $ (T,m) = (25,512) $。
一个样本定义为：
$$
x = (x^1,x^2,x^3,,,x^T)
$$

其中$x^t$为：
$$
x^t = (x^t_1, x^t_2, x^t_3,,,,x^t_m)
$$



## 2.2 ctc
输出为`l`的概率：$p(l|x)=\Sigma_{\pi \in B^{-1}(l)} p(\pi|x)$

$\pi \in B^{-1}(l)$ 代表所有 B 变换后是l的路径 $\pi$

任意一条路径：$p(\pi|x)=\prod^T_{t=1}y^t_{\pi_t}$

$\pi_t$ 表示$\pi$路径的t时刻。








# 参考
* [一文读懂CRNN+CTC文字识别](https://zhuanlan.zhihu.com/p/43534801)


