

# 1、ICDAR2019-LSVT
数据来源：https://ai.baidu.com/broad/introduction?dataset=lsvt
数据简介： 共45w中文街景图像，包含5w（2w测试+3w训练）全标注数据（文本坐标+文本内容），40w弱标注数据（仅文本内容），如下图所示：
- (a) 全标注数据
- (b) 弱标注数据
下载地址：https://ai.baidu.com/broad/download?dataset=lsvt
说明：其中，test数据集的label目前没有开源，如要评估结果，可以去官网提交：https://rrc.cvc.uab.es/?ch=16


两个压缩文件夹，train_full_images_0.tar.gz train_full_images_1.tar.gz，一共3万张图片。
- 标注文件中 train_full_labels.json 
    - 一共有382606个文本行
    - 其中"###" 139042个，"illegibility": true 有138969个。
    - train     170721  train_ver   45444
    - val       18913   val_ver     5040
    - [预估]还有3456个图片，是弯曲文本，非四边形。


# 2 使用开源模型进行测试

```bash
python3 tools/eval.py \
    -c configs/rec/rec_chinese_lite_train_cpu.yml \
    -o Global.checkpoints=/Users/zhangxin/data_public/paddle-ocr/db_crnn_mobile/ch_rec_mv3_crnn_enhance/best_accuracy
```



```bash
python3 tools/eval.py \
    -c configs/rec/rec_chinese_lite_train.yml \
    -o Global.checkpoints=/Users/zhangxin/data_public/paddle-ocr/db_crnn_mobile/rec_mv3_crnn/best_accuracy
```


