
# 1 准备数据
```bash
wget -P ./train_data/icdar2015/text_localization  https://paddleocr.bj.bcebos.com/dataset/train_icdar2015_label.txt
wget -P ./train_data/icdar2015/text_localization  https://paddleocr.bj.bcebos.com/dataset/test_icdar2015_label.txt
```


```bash
# 2024-05-20 
text_localization git:(main) ✗ tree -L 1                  
.
├── Challenge4_Test_Task1_GT.zip
├── ch4_test_images
├── ch4_test_images.zip
├── ch4_training_images.zip
├── ch4_training_localization_transcription_gt.zip
├── icdar_c4_train_imgs
├── test_icdar2015_label.txt
└── train_icdar2015_label.txt
```

# 2 下载预训练模型
```bash
# 2024-05-20
cd PaddleOCR/
# 根据backbone的不同选择下载对应的预训练模型
# 下载MobileNetV3的预训练模型
wget -P ./pretrain_models/ https://paddleocr.bj.bcebos.com/pretrained/MobileNetV3_large_x0_5_pretrained.pdparams
# 或，下载ResNet18_vd的预训练模型
wget -P ./pretrain_models/ https://paddleocr.bj.bcebos.com/pretrained/ResNet18_vd_pretrained.pdparams
# 或，下载ResNet50_vd的预训练模型
wget -P ./pretrain_models/ https://paddleocr.bj.bcebos.com/pretrained/ResNet50_vd_ssld_pretrained.pdparams
```

# 3 训练
```bash
python3 tools/train.py -c configs/det/det_mv3_db_zx_m3.yml \
     -o Global.pretrained_model=./pretrain_models/MobileNetV3_large_x0_5_pretrained
```

```bash
visualdl --logdir output/east_mv3/vdl
```