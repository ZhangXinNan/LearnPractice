

# 1 准备数据
## 1.1 下载ICDAR2015数据集。下载处理好的标注：
```bash
# Training set label
wget -P ./train_data/ic15_data  https://paddleocr.bj.bcebos.com/dataset/rec_gt_train.txt
# Test Set Label
wget -P ./train_data/ic15_data  https://paddleocr.bj.bcebos.com/dataset/rec_gt_test.txt
```

通过软链放到PaddleOCR目录下。在PaddleOCR目录下：
```bash
ln -sf /Users/zhangxin/data_public/icdar2015/4.3/ch4_training_word_images_gt train_data/ic15_data/train
ln -sf /Users/zhangxin/data_public/icdar2015/4.3/ch4_test_word_images_gt train_data/ic15_data/test
```

目录结构：
```bash
train_data/ic15_data
├── rec_gt_test.txt
├── rec_gt_train.txt
├── test -> /Users/zhangxin/data_public/icdar2015/4.3/ch4_test_word_images_gt
└── train -> /Users/zhangxin/data_public/icdar2015/4.3/ch4_training_word_images_gt

```

## 1.2 配置相关
1. 词表：
```bash
ppocr/utils/ppocr_keys_v1.txt   # is a Chinese dictionary with 6623 characters.
ppocr/utils/ic15_dict.txt       # is an English dictionary with 36 characters.
```

2. 训练的配置文件为：
```bash
configs/rec/rec_icdar15_train.yml
```
- 通过character_type设置中英文。
- use_space_char 支持空格识别。



# 2 训练

下载预训练模型
```bash
cd PaddleOCR/
# Download the pre-trained model of MobileNetV3
wget -P ./pretrain_models/ https://paddleocr.bj.bcebos.com/rec_mv3_none_bilstm_ctc.tar
# Decompress model parameters
cd pretrain_models
tar -xf rec_mv3_none_bilstm_ctc.tar && rm -rf rec_mv3_none_bilstm_ctc.tar
```

开始训练
```bash
# Set PYTHONPATH path
export PYTHONPATH=$PYTHONPATH:.
# GPU training Support single card and multi-card training, specify the card number through CUDA_VISIBLE_DEVICES
export CUDA_VISIBLE_DEVICES=0,1,2,3
# Training icdar15 English data
python3 tools/train.py -c configs/rec/rec_icdar15_train.yml
```

打印日志：
```bash


```
分析：这里粗略看一下，训练集上准确率(acc)在94%左右，已经不再上升；loss在81左右，还在缓慢下降。



# 3 验证
```bash
export CUDA_VISIBLE_DEVICES=0
# GPU evaluation, Global.checkpoints is the weight to be tested
python3 tools/eval.py -c configs/rec/rec_icdar15_train.yml -o Global.checkpoints=output/rec_CRNN/best_accuracy
```

打印日志
```bash
(py36_paddle) ubuntu@10-9-55-176:/mnt_ufs_ssd/zhangxin/github/PaddleOCR$ python3 tools/eval.py -c configs/rec/rec_icdar15_train.yml -o Global.checkpoints=output/rec_CRNN/best_accuracy
2020-08-13 13:36:33,222-INFO: {'Global': {'debug': False, 'algorithm': 'CRNN', 'use_gpu': True, 'epoch_num': 1000, 'log_smooth_window': 20, 'print_batch_step': 10, 'save_model_dir': './output/rec_CRNN', 'save_epoch_step': 300, 'eval_batch_step': 500, 'train_batch_size_per_card': 256, 'test_batch_size_per_card': 256, 'image_shape': [3, 32, 100], 'max_text_length': 25, 'character_type': 'en', 'loss_type': 'ctc', 'distort': True, 'reader_yml': './configs/rec/rec_icdar15_reader.yml', 'pretrain_weights': './pretrain_models/rec_mv3_none_bilstm_ctc/best_accuracy', 'checkpoints': 'output/rec_CRNN/best_accuracy', 'save_inference_dir': None, 'infer_img': None}, 'Architecture': {'function': 'ppocr.modeling.architectures.rec_model,RecModel'}, 'Backbone': {'function': 'ppocr.modeling.backbones.rec_mobilenet_v3,MobileNetV3', 'scale': 0.5, 'model_name': 'large'}, 'Head': {'function': 'ppocr.modeling.heads.rec_ctc_head,CTCPredict', 'encoder_type': 'rnn', 'SeqRNN': {'hidden_size': 96}}, 'Loss': {'function': 'ppocr.modeling.losses.rec_ctc_loss,CTCLoss'}, 'Optimizer': {'function': 'ppocr.optimizer,AdamDecay', 'base_lr': 0.0005, 'beta1': 0.9, 'beta2': 0.999, 'decay': {'function': 'cosine_decay', 'step_each_epoch': 20, 'total_epoch': 1000}}, 'TrainReader': {'reader_function': 'ppocr.data.rec.dataset_traversal,SimpleReader', 'num_workers': 8, 'img_set_dir': './train_data/ic15_data', 'label_file_path': './train_data/ic15_data/rec_gt_train.txt'}, 'EvalReader': {'reader_function': 'ppocr.data.rec.dataset_traversal,SimpleReader', 'img_set_dir': './train_data/ic15_data', 'label_file_path': './train_data/ic15_data/rec_gt_test.txt'}, 'TestReader': {'reader_function': 'ppocr.data.rec.dataset_traversal,SimpleReader'}}
W0813 13:36:34.730130 22292 device_context.cc:237] Please NOTE: device: 0, CUDA Capability: 75, Driver API Version: 10.2, Runtime API Version: 10.0
W0813 13:36:34.732719 22292 device_context.cc:245] device: 0, cuDNN Version: 7.6.
2020-08-13 13:36:36,099-INFO: Finish initing model from output/rec_CRNN/best_accuracy
2020-08-13 13:36:56,621-INFO: eval batch id: 0, acc: 0.68359375
2020-08-13 13:37:16,224-INFO: eval batch id: 1, acc: 0.640625
2020-08-13 13:37:36,609-INFO: eval batch id: 2, acc: 0.73046875
2020-08-13 13:37:56,643-INFO: eval batch id: 3, acc: 0.703125
2020-08-13 13:38:16,108-INFO: eval batch id: 4, acc: 0.67578125
2020-08-13 13:38:36,280-INFO: eval batch id: 5, acc: 0.68359375
2020-08-13 13:38:56,397-INFO: eval batch id: 6, acc: 0.71484375
2020-08-13 13:39:15,606-INFO: eval batch id: 7, acc: 0.703125
2020-08-13 13:39:17,838-INFO: eval batch id: 8, acc: 0.6551724137931034
2020-08-13 13:39:17,839-INFO: Eval result: {'avg_acc': 0.6913818006740491, 'total_acc_num': 1436, 'total_sample_num': 2077}
```

```
# win10
pip install shapely
```