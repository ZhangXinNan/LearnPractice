
# icdar2015
python3 tools/train.py -c configs/rec/rec_icdar15_train_zx.yml -o Global.pretrained_model=./pretrain_models/en_PP-OCRv3_rec_train/best_accuracy

visualdl --logdir output/rec/ic15

```bash
# GPU训练 支持单卡，多卡训练
# 训练icdar15英文数据 训练日志会自动保存为 "{save_model_dir}" 下的train.log

#单卡训练（训练周期长，不建议）
python3 tools/train.py -c configs/rec/PP-OCRv4/en_PP-OCRv4_rec_zx.yml -o Global.pretrained_model=./pretrain_models/en_PP-OCRv4_rec_train/best_accuracy

#多卡训练，通过--gpus参数指定卡号
python3 -m paddle.distributed.launch --gpus '0,1'  tools/train.py -c configs/rec/PP-OCRv4/en_PP-OCRv4_rec_zx.yml -o Global.pretrained_model=./pretrain_models/en_PP-OCRv4_rec_train/best_accuracy
```


```bash
# GPU 评估， Global.checkpoints 为待测权重
python3 -m paddle.distributed.launch --gpus '1' tools/eval.py -c configs/rec/PP-OCRv4/en_PP-OCRv4_rec_zx.yml -o Global.checkpoints=pretrain_models/en_PP-OCRv4_rec_train/best_accuracy
```

```
[2024/07/02 17:09:52] ppocr INFO: metric eval ***************
[2024/07/02 17:09:52] ppocr INFO: acc:0.6971593611114137
[2024/07/02 17:09:52] ppocr INFO: norm_edit_dis:0.8656436278697051
[2024/07/02 17:09:52] ppocr INFO: fps:274.7312496982364
```

```bash
# GPU 评估， Global.checkpoints 为待测权重
python3 -m paddle.distributed.launch --gpus '1' tools/eval.py -c configs/rec/PP-OCRv4/en_PP-OCRv4_rec_zx.yml -o Global.checkpoints=output/rec_ppocr_v4/best_accuracy
```

[2024/07/02 18:04:12] ppocr INFO: acc:0.6586422693373024
[2024/07/02 18:04:12] ppocr INFO: norm_edit_dis:0.8527611645437293
[2024/07/02 18:04:12] ppocr INFO: fps:287.34378728859133
