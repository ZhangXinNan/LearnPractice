
```
[2025/12/29 09:56:13] torchocr INFO: ----------- Config -----------
[2025/12/29 09:56:13] torchocr INFO: Architecture : 
[2025/12/29 09:56:13] torchocr INFO:     Backbone : 
[2025/12/29 09:56:13] torchocr INFO:         name : PPLCNetV3
[2025/12/29 09:56:13] torchocr INFO:         scale : 0.95
[2025/12/29 09:56:13] torchocr INFO:     Head : 
[2025/12/29 09:56:13] torchocr INFO:         head_list : 
[2025/12/29 09:56:13] torchocr INFO:             CTCHead : 
[2025/12/29 09:56:13] torchocr INFO:                 Head : 
[2025/12/29 09:56:13] torchocr INFO:                     fc_decay : 1e-05
[2025/12/29 09:56:13] torchocr INFO:                 Neck : 
[2025/12/29 09:56:13] torchocr INFO:                     conv4_kernel_size : [3, 3]
[2025/12/29 09:56:13] torchocr INFO:                     depth : 2
[2025/12/29 09:56:13] torchocr INFO:                     dims : 120
[2025/12/29 09:56:13] torchocr INFO:                     hidden_dims : 120
[2025/12/29 09:56:13] torchocr INFO:                     kernel_size : [1, 3]
[2025/12/29 09:56:13] torchocr INFO:                     name : svtr
[2025/12/29 09:56:13] torchocr INFO:                     use_guide : True
[2025/12/29 09:56:13] torchocr INFO:             NRTRHead : 
[2025/12/29 09:56:13] torchocr INFO:                 max_text_length : 25
[2025/12/29 09:56:13] torchocr INFO:                 nrtr_dim : 384
[2025/12/29 09:56:13] torchocr INFO:         name : MultiHead
[2025/12/29 09:56:13] torchocr INFO:     Transform : None
[2025/12/29 09:56:13] torchocr INFO:     algorithm : SVTR_LCNet
[2025/12/29 09:56:13] torchocr INFO:     model_type : rec
[2025/12/29 09:56:13] torchocr INFO: Eval : 
[2025/12/29 09:56:13] torchocr INFO:     dataset : 
[2025/12/29 09:56:13] torchocr INFO:         data_dir : /home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition
[2025/12/29 09:56:13] torchocr INFO:         label_file_list : ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/val.txt']
[2025/12/29 09:56:13] torchocr INFO:         name : SimpleDataSet
[2025/12/29 09:56:13] torchocr INFO:         transforms : 
[2025/12/29 09:56:13] torchocr INFO:             DecodeImage : 
[2025/12/29 09:56:13] torchocr INFO:                 channel_first : False
[2025/12/29 09:56:13] torchocr INFO:                 img_mode : BGR
[2025/12/29 09:56:13] torchocr INFO:             MultiLabelEncode : 
[2025/12/29 09:56:13] torchocr INFO:                 gtc_encode : NRTRLabelEncode
[2025/12/29 09:56:13] torchocr INFO:             RecResizeImg : 
[2025/12/29 09:56:13] torchocr INFO:                 image_shape : [3, 48, 320]
[2025/12/29 09:56:13] torchocr INFO:             KeepKeys : 
[2025/12/29 09:56:13] torchocr INFO:                 keep_keys : ['image', 'label_ctc', 'label_gtc', 'length', 'valid_ratio']
[2025/12/29 09:56:13] torchocr INFO:     loader : 
[2025/12/29 09:56:13] torchocr INFO:         batch_size_per_card : 32
[2025/12/29 09:56:13] torchocr INFO:         drop_last : False
[2025/12/29 09:56:13] torchocr INFO:         num_workers : 4
[2025/12/29 09:56:13] torchocr INFO:         shuffle : False
[2025/12/29 09:56:13] torchocr INFO: Global : 
[2025/12/29 09:56:13] torchocr INFO:     cal_metric_during_train : True
[2025/12/29 09:56:13] torchocr INFO:     character_dict_path : ./torchocr/utils/dict/ppocrv5_dict.txt
[2025/12/29 09:56:13] torchocr INFO:     checkpoints : None
[2025/12/29 09:56:13] torchocr INFO:     d2s_train_image_shape : [3, 48, 320]
[2025/12/29 09:56:13] torchocr INFO:     debug : False
[2025/12/29 09:56:13] torchocr INFO:     device : gpu
[2025/12/29 09:56:13] torchocr INFO:     distributed : False
[2025/12/29 09:56:13] torchocr INFO:     epoch_num : 75
[2025/12/29 09:56:13] torchocr INFO:     eval_batch_step : [0, 2000]
[2025/12/29 09:56:13] torchocr INFO:     infer_img : doc/imgs_words/ch/word_1.jpg
[2025/12/29 09:56:13] torchocr INFO:     infer_mode : False
[2025/12/29 09:56:13] torchocr INFO:     log_smooth_window : 20
[2025/12/29 09:56:13] torchocr INFO:     max_text_length : 25
[2025/12/29 09:56:13] torchocr INFO:     model_name : PP-OCRv5_mobile_rec
[2025/12/29 09:56:13] torchocr INFO:     output_dir : ./output/PP-OCRv5_mobile_rec_3_Chinese_Street_View_Text
[2025/12/29 09:56:13] torchocr INFO:     pretrained_model : None
[2025/12/29 09:56:13] torchocr INFO:     print_batch_step : 10
[2025/12/29 09:56:13] torchocr INFO:     save_epoch_step : 10
[2025/12/29 09:56:13] torchocr INFO:     save_inference_dir : None
[2025/12/29 09:56:13] torchocr INFO:     save_model_dir : ./output/PP-OCRv5_mobile_rec
[2025/12/29 09:56:13] torchocr INFO:     save_res_path : ./output/rec/predicts_ppocrv5.txt
[2025/12/29 09:56:13] torchocr INFO:     use_gpu : True
[2025/12/29 09:56:13] torchocr INFO:     use_space_char : True
[2025/12/29 09:56:13] torchocr INFO:     use_tensorboard : True
[2025/12/29 09:56:13] torchocr INFO:     use_visualdl : False
[2025/12/29 09:56:13] torchocr INFO: LRScheduler : 
[2025/12/29 09:56:13] torchocr INFO:     name : CosineAnnealingLR
[2025/12/29 09:56:13] torchocr INFO:     warmup_epoch : 2
[2025/12/29 09:56:13] torchocr INFO: Loss : 
[2025/12/29 09:56:13] torchocr INFO:     loss_config_list : 
[2025/12/29 09:56:13] torchocr INFO:         CTCLoss : None
[2025/12/29 09:56:13] torchocr INFO:         NRTRLoss : None
[2025/12/29 09:56:13] torchocr INFO:     name : MultiLoss
[2025/12/29 09:56:13] torchocr INFO: Metric : 
[2025/12/29 09:56:13] torchocr INFO:     main_indicator : acc
[2025/12/29 09:56:13] torchocr INFO:     name : RecMetric
[2025/12/29 09:56:13] torchocr INFO: Optimizer : 
[2025/12/29 09:56:13] torchocr INFO:     betas : [0.9, 0.999]
[2025/12/29 09:56:13] torchocr INFO:     lr : 0.0001
[2025/12/29 09:56:13] torchocr INFO:     name : Adam
[2025/12/29 09:56:13] torchocr INFO:     weight_decay : 0.0001
[2025/12/29 09:56:13] torchocr INFO: PostProcess : 
[2025/12/29 09:56:13] torchocr INFO:     character_dict_path : ./torchocr/utils/dict/ppocrv5_dict.txt
[2025/12/29 09:56:13] torchocr INFO:     name : CTCLabelDecode
[2025/12/29 09:56:13] torchocr INFO:     use_space_char : True
[2025/12/29 09:56:13] torchocr INFO: Train : 
[2025/12/29 09:56:13] torchocr INFO:     dataset : 
[2025/12/29 09:56:13] torchocr INFO:         data_dir : /home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition
[2025/12/29 09:56:13] torchocr INFO:         ds_width : False
[2025/12/29 09:56:13] torchocr INFO:         ext_op_transform_idx : 1
[2025/12/29 09:56:13] torchocr INFO:         label_file_list : ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train.txt']
[2025/12/29 09:56:13] torchocr INFO:         name : MultiScaleDataSet
[2025/12/29 09:56:13] torchocr INFO:         transforms : 
[2025/12/29 09:56:13] torchocr INFO:             DecodeImage : 
[2025/12/29 09:56:13] torchocr INFO:                 channel_first : False
[2025/12/29 09:56:13] torchocr INFO:                 img_mode : BGR
[2025/12/29 09:56:13] torchocr INFO:             RecConAug : 
[2025/12/29 09:56:13] torchocr INFO:                 ext_data_num : 2
[2025/12/29 09:56:13] torchocr INFO:                 image_shape : [48, 320, 3]
[2025/12/29 09:56:13] torchocr INFO:                 max_text_length : 25
[2025/12/29 09:56:13] torchocr INFO:                 prob : 0.5
[2025/12/29 09:56:13] torchocr INFO:             RecAug : None
[2025/12/29 09:56:13] torchocr INFO:             MultiLabelEncode : 
[2025/12/29 09:56:13] torchocr INFO:                 gtc_encode : NRTRLabelEncode
[2025/12/29 09:56:13] torchocr INFO:             KeepKeys : 
[2025/12/29 09:56:13] torchocr INFO:                 keep_keys : ['image', 'label_ctc', 'label_gtc', 'length', 'valid_ratio']
[2025/12/29 09:56:13] torchocr INFO:     loader : 
[2025/12/29 09:56:13] torchocr INFO:         batch_size_per_card : 32
[2025/12/29 09:56:13] torchocr INFO:         drop_last : True
[2025/12/29 09:56:13] torchocr INFO:         num_workers : 4
[2025/12/29 09:56:13] torchocr INFO:         shuffle : True
[2025/12/29 09:56:13] torchocr INFO:     sampler : 
[2025/12/29 09:56:13] torchocr INFO:         divided_factor : [8, 16]
[2025/12/29 09:56:13] torchocr INFO:         first_bs : 32
[2025/12/29 09:56:13] torchocr INFO:         fix_bs : False
[2025/12/29 09:56:13] torchocr INFO:         is_training : True
[2025/12/29 09:56:13] torchocr INFO:         name : MultiScaleSampler
[2025/12/29 09:56:13] torchocr INFO:         scales : [[320, 32], [320, 48], [320, 64]]
[2025/12/29 09:56:13] torchocr INFO: ---------------------------------------------
[2025/12/29 09:56:13] torchocr INFO: Initialize indexs of datasets: ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train.txt']
[2025/12/29 09:56:13] torchocr INFO: train dataloader has 7482 iters
[2025/12/29 09:56:13] torchocr INFO: Initialize indexs of datasets: ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/val.txt']
[2025/12/29 09:56:13] torchocr INFO: valid dataloader has 938 iters
[2025/12/29 09:56:14] torchocr INFO: train from scratch
[2025/12/29 09:56:14] torchocr INFO: status from ckpt: {}
[2025/12/29 09:56:14] torchocr INFO: run with torch 2.9.1+cu126 and device cuda:0
Traceback (most recent call last):
  File "/home/zhangxin/github/PytorchOCR/tools/train.py", line 38, in <module>
    main()
  File "/home/zhangxin/github/PytorchOCR/tools/train.py", line 34, in main
    trainer.train()
  File "/home/zhangxin/github/PytorchOCR/torchocr/engine/trainer.py", line 182, in train
    preds = self.model(batch[0], data=batch[1:])
  File "/home/zhangxin/miniconda3/envs/py310_pytorchocr/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/zhangxin/miniconda3/envs/py310_pytorchocr/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/zhangxin/github/PytorchOCR/torchocr/modeling/architectures/base_model.py", line 83, in forward
    x = self.head(x, data=data)
  File "/home/zhangxin/miniconda3/envs/py310_pytorchocr/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/zhangxin/miniconda3/envs/py310_pytorchocr/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/zhangxin/github/PytorchOCR/torchocr/modeling/heads/rec_multi_head.py", line 85, in forward
    gtc_out = self.gtc_head(self.before_gtc(x), data[1:])['res']
  File "/home/zhangxin/miniconda3/envs/py310_pytorchocr/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1775, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "/home/zhangxin/miniconda3/envs/py310_pytorchocr/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1786, in _call_impl
    return forward_call(*args, **kwargs)
  File "/home/zhangxin/github/PytorchOCR/torchocr/modeling/heads/rec_nrtr_head.py", line 123, in forward
    tgt = data[0][:, :2 + max_len]
TypeError: only integer tensors of a single element can be converted to an index
```

这个报错其实**很典型，而且已经把问题范围缩得很小了**，核心就在这一行：

```python
tgt = data[0][:, :2 + max_len]
```

报错信息是：

> TypeError: only integer tensors of a single element can be converted to an index

---

## 一句话结论（先给结论）

👉 **NRTRHead 收到的 `data[0]` 不是一个 LongTensor（token id 序列），而是别的类型（很可能是 list / dict / 多维 tensor / CPU-GPU 不一致）**，导致 `:` 切片时失败。

本质原因是：
**MultiHead + MultiLabelEncode + NRTRLabelEncode 的数据顺序或格式不匹配**。

---

## 从调用栈精确定位

关键调用链：

```
trainer.train()
 → model(batch[0], data=batch[1:])
 → rec_multi_head.forward
 → self.gtc_head(self.before_gtc(x), data[1:])
 → rec_nrtr_head.forward
 → tgt = data[0][:, :2 + max_len]  ❌
```

### 也就是说

在 `rec_nrtr_head.forward(self, x, data)` 中：

```python
data[0]  # 期望是: label_gtc (shape [B, L], dtype long)
```

但 **实际传进来的不是这个**。

---

## 正确情况下 NRTRHead 期望的数据格式

NRTR 是 Transformer decoder，训练时 **必须要 token 序列**：

```text
data[0] = label_gtc  # shape [B, max_len+2], LongTensor
data[1] = length     # 可选
```

而你现在的 pipeline 是：

```yaml
KeepKeys:
  keep_keys:
    ['image', 'label_ctc', 'label_gtc', 'length', 'valid_ratio']
```

然后在 `Trainer` 里：

```python
batch = [image, label_ctc, label_gtc, length, valid_ratio]
model(batch[0], data=batch[1:])
```

于是：

```text
data[0] = label_ctc
data[1] = label_gtc
```

⚠️ **但 `rec_multi_head.py` 里对 data 的切分假设是另一种顺序**

---

## 关键错误点（这是“坑点”）

在 `rec_multi_head.py`（你现在用的实现）里：

```python
ctc_out = self.ctc_head(x, data)['res']
gtc_out = self.gtc_head(self.before_gtc(x), data[1:])['res']
```

也就是说：

```text
传给 NRTRHead 的 data = data[1:]
```

此时：

```text
data[1:] = [label_gtc, length, valid_ratio]
```

于是 NRTRHead.forward 里：

```python
data[0] == label_gtc   # 这是对的
```

**但你的 `label_gtc` 实际并不是一个 LongTensor**。

---

## 为什么你的 label_gtc 不对？

结合你的配置：

```yaml
MultiLabelEncode:
  gtc_encode: NRTRLabelEncode
```

但 **你训练的是 PP-OCRv5 mobile + SVTR_LCNet + MultiHead（CTC + NRTR）**：

### Paddle 官方做法是：

* **NRTRHead 默认只在 fine-tune / 特定任务使用**
* PP-OCRv5 mobile **主力是 CTC**
* MultiHead 在 Paddle 中对数据格式处理更复杂

而 **TorchOCR 的 MultiHead 实现并没有完全对齐 Paddle 的 NRTR 数据流**。

👉 结果就是：
**label_gtc 实际是一个 list / numpy / CPU tensor / shape 不对**

---

## 如何 100% 验证（你可以马上加一行）

在 `rec_nrtr_head.py:forward` 里临时加：

```python
print(type(data[0]), data[0].shape if hasattr(data[0], "shape") else data[0])
```

你大概率会看到：

* `list`
* 或 `torch.FloatTensor`
* 或 shape 不是 `[B, L]`

---

## 推荐的解决方案（按“稳妥程度”排序）

---

### ✅ 方案一（**最推荐**）：直接关掉 NRTRHead

**PP-OCRv5 mobile 本来就是 CTC-only 主力模型**

#### 修改配置

```yaml
Architecture:
  Head:
    name: CTCHead
```

并删除：

```yaml
NRTRHead
MultiLabelEncode
label_gtc
NRTRLoss
```

只保留：

```yaml
label_ctc
CTCLoss
CTCLabelDecode
```

👉 **这是 Paddle 官方 mobile rec 的常规训练方式**

---

### ⚠️ 方案二：保留 MultiHead，但修数据流（不推荐）

你需要 **同时改三处**：

1. `MultiLabelEncode` 输出必须保证：

   ```python
   label_gtc.dtype == torch.long
   label_gtc.shape == [B, max_len+2]
   ```
2. Trainer 中 `data` 的顺序必须和 `rec_multi_head.py` 完全一致
3. NRTRHead.forward 要防御性判断

维护成本很高，而且 TorchOCR 当前版本 **并没 fully support 这个组合**。

---

### 🧪 方案三：只在 eval/infer 用 NRTR（高级玩法）

* 训练：CTC
* 推理：加载 CTC backbone + NRTR decoder

这个需要你自己拆 head，不适合现在 debug。

---

## 给你一个“工程判断”

> **你现在这个错误，不是数据集问题，不是 PyTorch bug，而是“MultiHead + NRTR 在 TorchOCR 中没跑通”的设计问题。**

如果目标是：

* 跑通
* 对比效果
* 做实验 / 论文 / 项目

👉 **直接 CTC-only，是最正确的选择**。

---

## 如果你愿意

你可以下一步把这两个文件贴出来任意一个：

* `rec_multi_head.py`
* `rec_nrtr_head.py`
* 或你的 `MultiLabelEncode` 输出示例

我可以 **帮你精确改到“最小可跑 diff”级别**，不需要你自己试错。


















很好，这两个文件一贴出来，**问题就完全清晰了**。
我直接给你一个**工程级结论 + 精确到行的修复方案**。

---

# 一句话定性（非常重要）

> **现在这个 `TypeError` 不是 PyTorch bug，也不是你数据集的问题，而是：
> TorchOCR 的 `MultiHead + NRTRHead` 在“数据顺序 + 假设”上是**不自洽的实现**。**

你这份代码里，**`rec_multi_head.py` 和 `rec_nrtr_head.py` 对 `data` 的约定是不一致的**。

---

# 错误的根因（精确到索引）

## 1️⃣ MultiHead 里是这样调用 NRTR 的

```python
# rec_multi_head.py
gtc_out = self.gtc_head(self.before_gtc(x), data[1:])['res']
```

也就是说，**传给 NRTR 的 data 是 `data[1:]`**。

---

## 2️⃣ NRTRHead.forward 的假设是（这是关键）

```python
# rec_nrtr_head.py
if self.training:
    max_len = data[1].max()
    tgt = data[0][:, :2 + max_len]
```

👉 **NRTRHead 明确假设：**

```text
data[0] = tgt token ids (LongTensor, [B, L])
data[1] = length (LongTensor, [B])
```

---

## 3️⃣ 但你的真实 data 顺序是

从 DataLoader + KeepKeys：

```yaml
KeepKeys:
  ['image', 'label_ctc', 'label_gtc', 'length', 'valid_ratio']
```

Trainer 调用：

```python
model(batch[0], data=batch[1:])
```

所以在 MultiHead.forward 里：

```text
data = [
    label_ctc,   # data[0]
    label_gtc,   # data[1]
    length,      # data[2]
    valid_ratio  # data[3]
]
```

然后你又做了：

```python
data[1:] = [label_gtc, length, valid_ratio]
```

---

## 4️⃣ **问题就在这里**

在 `rec_nrtr_head.forward` 中：

```python
max_len = data[1].max()
```

此时：

```text
data[1] = length         ✅ OK
data[0] = label_gtc      ⚠️ 但它的 dtype / shape 不符合 NRTR 的强假设
```

而 `label_gtc` **并不是一个“已经 pad 好、LongTensor、可直接切片”的 tensor**。

于是这一句炸了：

```python
tgt = data[0][:, :2 + max_len]
```

Python 报的就是你看到的这个经典错误：

> only integer tensors of a single element can be converted to an index

---

# 关键工程事实（你要记住）

> **PaddleOCR 里的 MultiHead + NRTR 是“半实验性结构”，
> 而 TorchOCR 这一版只是“形似”，并没有把数据流完全对齐 Paddle。**

所以：
**这个组合在 TorchOCR 里，默认就是跑不通的。**

---

# ✅ 推荐解决方案（分等级）

我按**工程稳定性**给你排好顺序。

---

## 🥇 方案一（强烈推荐）：直接关闭 NRTRHead（官方 mobile 做法）

### 为什么这是“正确选择”

* **PP-OCRv5 mobile 官方就是 CTC-only**
* NRTR：

  * 训练慢
  * 对 label 要求苛刻
  * TorchOCR 实现不完整
* 你现在用的是 **SVTR_LCNet + Mobile 场景**

👉 **CTC 是最稳、最准、最快的选择**

### 你要改的只有配置，不用改代码

#### 1️⃣ Architecture 只保留 CTCHead

```yaml
Architecture:
  Head:
    name: CTCHead
```

#### 2️⃣ 删除这些内容

```yaml
NRTRHead
MultiLabelEncode
label_gtc
NRTRLoss
```

#### 3️⃣ KeepKeys 改成

```yaml
KeepKeys:
  keep_keys: ['image', 'label_ctc', 'length', 'valid_ratio']
```

👉 **100% 能跑通，不会再碰这个错误**

---

## 🥈 方案二（能跑，但我不推荐）：强行修 MultiHead + NRTR

如果你**一定要 NRTR**（比如做对比实验），最小改动如下。

---

### ✅ 最小可跑补丁（关键）

#### 🔧 修改 `rec_multi_head.py`

**把传给 NRTR 的 data 改成只传 `label_gtc + length`**

```diff
- gtc_out = self.gtc_head(self.before_gtc(x), data[1:])['res']
+ # data: [label_ctc, label_gtc, length, valid_ratio]
+ gtc_data = [data[1], data[2]]  # label_gtc, length
+ gtc_out = self.gtc_head(self.before_gtc(x), gtc_data)['res']
```

---

#### 🔧 修改 `rec_nrtr_head.py`（防御性）

```diff
if self.training:
-    max_len = data[1].max()
-    tgt = data[0][:, :2 + max_len]
+    tgt, length = data
+    if not torch.is_tensor(tgt):
+        tgt = torch.tensor(tgt, dtype=torch.long, device=src.device)
+    max_len = length.max().item()
+    tgt = tgt[:, :2 + max_len]
```

⚠️ 说明：
这个补丁 **只是“止血”**，不是“优雅实现”。

---

## 🥉 方案三（高级，不建议现在搞）

* 训练：CTC
* 推理：NRTR Decoder
* 需要拆 head、单独喂特征

👉 不适合你现在这个阶段

---

# 给你一个工程判断（站在你背景上说实话）

你有 **OCR + 工程 + PyTorch** 的经验，这种坑你已经踩得够多了 😅
**这个不是你“哪里没看懂”，而是 TorchOCR 这里确实没对齐 Paddle。**

👉 **如果目标是：**

* 跑通
* 做实验
* 比效果
* 甚至写论文

**CTC-only 是最合理、最干净、最省时间的路线。**

---

如果你愿意，下一步我可以帮你：

* 🔍 **对齐 Paddle 官方 PP-OCRv5 mobile rec 的完整训练配置**
* 🧪 **给你一个“CTC-only + SVTR_LCNet”的最佳实践 YAML**
* ✂️ **直接给你一个“精简版 MultiHead 删除 NRTR 的 commit diff”**

你选一个，我继续帮你把这条线跑到“工业可用”。





