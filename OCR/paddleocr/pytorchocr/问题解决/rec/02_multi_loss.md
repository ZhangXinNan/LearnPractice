
```
[2025/12/29 10:15:18] torchocr INFO: ----------- Config -----------
[2025/12/29 10:15:18] torchocr INFO: Architecture : 
[2025/12/29 10:15:18] torchocr INFO:     Backbone : 
[2025/12/29 10:15:18] torchocr INFO:         name : PPLCNetV3
[2025/12/29 10:15:18] torchocr INFO:         scale : 0.95
[2025/12/29 10:15:18] torchocr INFO:     Head : 
[2025/12/29 10:15:18] torchocr INFO:         head_list : 
[2025/12/29 10:15:18] torchocr INFO:             CTCHead : 
[2025/12/29 10:15:18] torchocr INFO:                 Head : 
[2025/12/29 10:15:18] torchocr INFO:                     fc_decay : 1e-05
[2025/12/29 10:15:18] torchocr INFO:                 Neck : 
[2025/12/29 10:15:18] torchocr INFO:                     conv4_kernel_size : [3, 3]
[2025/12/29 10:15:18] torchocr INFO:                     depth : 2
[2025/12/29 10:15:18] torchocr INFO:                     dims : 120
[2025/12/29 10:15:18] torchocr INFO:                     hidden_dims : 120
[2025/12/29 10:15:18] torchocr INFO:                     kernel_size : [1, 3]
[2025/12/29 10:15:18] torchocr INFO:                     name : svtr
[2025/12/29 10:15:18] torchocr INFO:                     use_guide : True
[2025/12/29 10:15:18] torchocr INFO:         name : MultiHead
[2025/12/29 10:15:18] torchocr INFO:     Transform : None
[2025/12/29 10:15:18] torchocr INFO:     algorithm : SVTR_LCNet
[2025/12/29 10:15:18] torchocr INFO:     model_type : rec
[2025/12/29 10:15:18] torchocr INFO: Eval : 
[2025/12/29 10:15:18] torchocr INFO:     dataset : 
[2025/12/29 10:15:18] torchocr INFO:         data_dir : /home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition
[2025/12/29 10:15:18] torchocr INFO:         label_file_list : ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/val.txt']
[2025/12/29 10:15:18] torchocr INFO:         name : SimpleDataSet
[2025/12/29 10:15:18] torchocr INFO:         transforms : 
[2025/12/29 10:15:18] torchocr INFO:             DecodeImage : 
[2025/12/29 10:15:18] torchocr INFO:                 channel_first : False
[2025/12/29 10:15:18] torchocr INFO:                 img_mode : BGR
[2025/12/29 10:15:18] torchocr INFO:             RecResizeImg : 
[2025/12/29 10:15:18] torchocr INFO:                 image_shape : [3, 48, 320]
[2025/12/29 10:15:18] torchocr INFO:             KeepKeys : 
[2025/12/29 10:15:18] torchocr INFO:                 keep_keys : ['image', 'label_ctc', 'length', 'valid_ratio']
[2025/12/29 10:15:18] torchocr INFO:     loader : 
[2025/12/29 10:15:18] torchocr INFO:         batch_size_per_card : 32
[2025/12/29 10:15:18] torchocr INFO:         drop_last : False
[2025/12/29 10:15:18] torchocr INFO:         num_workers : 4
[2025/12/29 10:15:18] torchocr INFO:         shuffle : False
[2025/12/29 10:15:18] torchocr INFO: Global : 
[2025/12/29 10:15:18] torchocr INFO:     cal_metric_during_train : True
[2025/12/29 10:15:18] torchocr INFO:     character_dict_path : ./torchocr/utils/dict/ppocrv5_dict.txt
[2025/12/29 10:15:18] torchocr INFO:     checkpoints : None
[2025/12/29 10:15:18] torchocr INFO:     d2s_train_image_shape : [3, 48, 320]
[2025/12/29 10:15:18] torchocr INFO:     debug : False
[2025/12/29 10:15:18] torchocr INFO:     device : gpu
[2025/12/29 10:15:18] torchocr INFO:     distributed : False
[2025/12/29 10:15:18] torchocr INFO:     epoch_num : 75
[2025/12/29 10:15:18] torchocr INFO:     eval_batch_step : [0, 2000]
[2025/12/29 10:15:18] torchocr INFO:     infer_img : doc/imgs_words/ch/word_1.jpg
[2025/12/29 10:15:18] torchocr INFO:     infer_mode : False
[2025/12/29 10:15:18] torchocr INFO:     log_smooth_window : 20
[2025/12/29 10:15:18] torchocr INFO:     max_text_length : 25
[2025/12/29 10:15:18] torchocr INFO:     model_name : PP-OCRv5_mobile_rec
[2025/12/29 10:15:18] torchocr INFO:     output_dir : ./output/PP-OCRv5_mobile_rec_3_Chinese_Street_View_Text
[2025/12/29 10:15:18] torchocr INFO:     pretrained_model : None
[2025/12/29 10:15:18] torchocr INFO:     print_batch_step : 10
[2025/12/29 10:15:18] torchocr INFO:     save_epoch_step : 10
[2025/12/29 10:15:18] torchocr INFO:     save_inference_dir : None
[2025/12/29 10:15:18] torchocr INFO:     save_model_dir : ./output/PP-OCRv5_mobile_rec
[2025/12/29 10:15:18] torchocr INFO:     save_res_path : ./output/rec/predicts_ppocrv5.txt
[2025/12/29 10:15:18] torchocr INFO:     use_gpu : True
[2025/12/29 10:15:18] torchocr INFO:     use_space_char : True
[2025/12/29 10:15:18] torchocr INFO:     use_tensorboard : True
[2025/12/29 10:15:18] torchocr INFO:     use_visualdl : False
[2025/12/29 10:15:18] torchocr INFO: LRScheduler : 
[2025/12/29 10:15:18] torchocr INFO:     name : CosineAnnealingLR
[2025/12/29 10:15:18] torchocr INFO:     warmup_epoch : 2
[2025/12/29 10:15:18] torchocr INFO: Loss : 
[2025/12/29 10:15:18] torchocr INFO:     loss_config_list : 
[2025/12/29 10:15:18] torchocr INFO:         CTCLoss : None
[2025/12/29 10:15:18] torchocr INFO:     name : MultiLoss
[2025/12/29 10:15:18] torchocr INFO: Metric : 
[2025/12/29 10:15:18] torchocr INFO:     main_indicator : acc
[2025/12/29 10:15:18] torchocr INFO:     name : RecMetric
[2025/12/29 10:15:18] torchocr INFO: Optimizer : 
[2025/12/29 10:15:18] torchocr INFO:     betas : [0.9, 0.999]
[2025/12/29 10:15:18] torchocr INFO:     lr : 0.0001
[2025/12/29 10:15:18] torchocr INFO:     name : Adam
[2025/12/29 10:15:18] torchocr INFO:     weight_decay : 0.0001
[2025/12/29 10:15:18] torchocr INFO: PostProcess : 
[2025/12/29 10:15:18] torchocr INFO:     character_dict_path : ./torchocr/utils/dict/ppocrv5_dict.txt
[2025/12/29 10:15:18] torchocr INFO:     name : CTCLabelDecode
[2025/12/29 10:15:18] torchocr INFO:     use_space_char : True
[2025/12/29 10:15:18] torchocr INFO: Train : 
[2025/12/29 10:15:18] torchocr INFO:     dataset : 
[2025/12/29 10:15:18] torchocr INFO:         data_dir : /home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition
[2025/12/29 10:15:18] torchocr INFO:         ds_width : False
[2025/12/29 10:15:18] torchocr INFO:         ext_op_transform_idx : 1
[2025/12/29 10:15:18] torchocr INFO:         label_file_list : ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train.txt']
[2025/12/29 10:15:18] torchocr INFO:         name : MultiScaleDataSet
[2025/12/29 10:15:18] torchocr INFO:         transforms : 
[2025/12/29 10:15:18] torchocr INFO:             DecodeImage : 
[2025/12/29 10:15:18] torchocr INFO:                 channel_first : False
[2025/12/29 10:15:18] torchocr INFO:                 img_mode : BGR
[2025/12/29 10:15:18] torchocr INFO:             RecConAug : 
[2025/12/29 10:15:18] torchocr INFO:                 ext_data_num : 2
[2025/12/29 10:15:18] torchocr INFO:                 image_shape : [48, 320, 3]
[2025/12/29 10:15:18] torchocr INFO:                 max_text_length : 25
[2025/12/29 10:15:18] torchocr INFO:                 prob : 0.5
[2025/12/29 10:15:18] torchocr INFO:             RecAug : None
[2025/12/29 10:15:18] torchocr INFO:             KeepKeys : 
[2025/12/29 10:15:18] torchocr INFO:                 keep_keys : ['image', 'label_ctc', 'length', 'valid_ratio']
[2025/12/29 10:15:18] torchocr INFO:     loader : 
[2025/12/29 10:15:18] torchocr INFO:         batch_size_per_card : 32
[2025/12/29 10:15:18] torchocr INFO:         drop_last : True
[2025/12/29 10:15:18] torchocr INFO:         num_workers : 4
[2025/12/29 10:15:18] torchocr INFO:         shuffle : True
[2025/12/29 10:15:18] torchocr INFO:     sampler : 
[2025/12/29 10:15:18] torchocr INFO:         divided_factor : [8, 16]
[2025/12/29 10:15:18] torchocr INFO:         first_bs : 32
[2025/12/29 10:15:18] torchocr INFO:         fix_bs : False
[2025/12/29 10:15:18] torchocr INFO:         is_training : True
[2025/12/29 10:15:18] torchocr INFO:         name : MultiScaleSampler
[2025/12/29 10:15:18] torchocr INFO:         scales : [[320, 32], [320, 48], [320, 64]]
[2025/12/29 10:15:18] torchocr INFO: ---------------------------------------------
[2025/12/29 10:15:18] torchocr INFO: Initialize indexs of datasets: ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train.txt']
[2025/12/29 10:15:18] torchocr INFO: train dataloader has 7482 iters
[2025/12/29 10:15:18] torchocr INFO: Initialize indexs of datasets: ['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/val.txt']
[2025/12/29 10:15:18] torchocr INFO: valid dataloader has 938 iters
Traceback (most recent call last):
  File "/home/zhangxin/github/PytorchOCR/tools/train.py", line 38, in <module>
    main()
  File "/home/zhangxin/github/PytorchOCR/tools/train.py", line 33, in main
    trainer = Trainer(cfg, mode='train_eval' if FLAGS['eval'] else 'train')
  File "/home/zhangxin/github/PytorchOCR/torchocr/engine/trainer.py", line 78, in __init__
    update_rec_head_out_channels(self.cfg, self.post_process_class)
  File "/home/zhangxin/github/PytorchOCR/tools/utility.py", line 81, in update_rec_head_out_channels
    if list(cfg['Loss']['loss_config_list'][1].keys())[0] == 'SARLoss':
IndexError: list index out of range
```




这个报错**和模型/数据都无关**，是一个**典型的 TorchOCR 配置兼容性 bug**，而且你这份 log 反而证明了一件好事：
👉 **你已经把 NRTR / SAR 全部删干净了，方向是完全正确的**。

下面我给你**精准定位 + 最小修改方案（不改一行模型代码）**。

---

# 一句话结论（先给你吃个定心丸）

> **你现在是：CTC-only 模型，但 TorchOCR 的 `update_rec_head_out_channels()` 还在“假设你有第二个 Loss（SAR/NRTR）”，于是直接数组越界。**

这不是你配置写错，是 **TorchOCR 工具函数写死假设的问题**。

---

# 报错精确定位

## 报错点

```text
File "tools/utility.py", line 81
if list(cfg['Loss']['loss_config_list'][1].keys())[0] == 'SARLoss':
IndexError: list index out of range
```

### 这行代码在干嘛？

它**强行假设**：

```python
cfg['Loss']['loss_config_list'] = [
    {...CTCLoss...},
    {...SARLoss or NRTRLoss...}
]
```

但你现在的配置是：

```yaml
Loss:
  name: MultiLoss
  loss_config_list:
    - CTCLoss: None
```

👉 **长度只有 1**
👉 访问 `[1]` 直接炸

---

# 为什么你会遇到这个 bug（而别人“好像没遇到”）

因为：

* PaddleOCR 官方：

  * CTC-only → 用 `CTCLoss`
  * MultiHead → 才用 `MultiLoss`
* **TorchOCR 把两种情况混在了一起**
* 但你现在是：

  * ✅ CTC-only Head
  * ❌ 还在用 `MultiLoss`

---

# ✅ 最优解（推荐，1 行 YAML 解决）

## 👉 把 Loss 从 `MultiLoss` 改成 `CTCLoss`

### 🔧 修改前

```yaml
Loss:
  name: MultiLoss
  loss_config_list:
    - CTCLoss: None
```

### ✅ 修改后（关键）

```yaml
Loss:
  name: CTCLoss
```

✔ 不需要 `loss_config_list`
✔ 不会再走 `update_rec_head_out_channels` 的错误分支
✔ 和 **PP-OCRv5 mobile 官方配置完全一致**

---

# 🔍 为什么这个改动是“语义正确”的？

你现在的模型是：

```text
Backbone: PPLCNetV3
Neck: SVTR
Head: CTCHead
```

👉 **只有一个输出头**
👉 **只有一个 loss**

那用 `MultiLoss` 本来就是“历史遗留 + 多余设计”。

---

# 🧪 如果你非要保留 MultiLoss（不推荐）

那只能**修代码**：

```diff
# tools/utility.py
- if list(cfg['Loss']['loss_config_list'][1].keys())[0] == 'SARLoss':
+ if len(cfg['Loss']['loss_config_list']) > 1 and \
+    list(cfg['Loss']['loss_config_list'][1].keys())[0] == 'SARLoss':
```

但我明确说一句：

> ❌ **不值得**
> ❌ 会影响你后面升级 / 对齐 PaddleOCR

---

# ✅ 你现在的整体状态评估（很重要）

我帮你“复盘”一下你现在的配置质量：

| 模块                   | 状态         |
| -------------------- | ---------- |
| Backbone (PPLCNetV3) | ✅ 正确       |
| SVTR Neck            | ✅ 正确       |
| CTC-only             | ✅ **强烈推荐** |
| 数据管道                 | ✅ 干净       |
| KeepKeys             | ✅ 正确       |
| Eval / Metric        | ✅ 正确       |
| ❌ 唯一问题               | Loss 名字    |

👉 **你已经离“可稳定训练的 PP-OCRv5 mobile rec”只差这一行 YAML。**

---

# 🚀 下一步我可以继续帮你的（你选）

1️⃣ 给你一份 **「完全对齐 PaddleOCR 的 PP-OCRv5 mobile rec YAML」**
2️⃣ 帮你检查 **字典、blank index、CTC decode 是否 100% 对齐**
3️⃣ 训练跑起来后，帮你看 **acc 不涨 / loss 不降的常见坑**
4️⃣ 推理导出（onnx / trt）路线图

你现在这个进度，说实话：
**已经是“工程级 OCR 调参”而不是“新手踩坑”阶段了**。



