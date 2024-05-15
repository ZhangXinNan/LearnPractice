博客：
[tensorflow LSTM + CTC实现端到端OCR](http://ilovin.me/2017-04-06/tensorflow-lstm-ctc-ocr/)
代码：
[ilovin/lstm_ctc_ocr](https://github.com/ilovin/lstm_ctc_ocr)

进展：
能够在本机和服务器上跑通，还没有用GPU。

问题：
（1）训练特别慢
（2）用的python3，没法用gpu
（3）需要最新版本
```
AttributeError: 'module' object has no attribute 'MultiRNNCell'
```
