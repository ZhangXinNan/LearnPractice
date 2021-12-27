## 作业一（100分）
题目：本节DB算法的训练使用MobileV3Large作为Backbone，请更换Backbone为ResNet50网络在[icdar2015数据集](https://aistudio.baidu.com/aistudio/datasetdetail/96799)上训练并调优，配置文件参考[det_r50_vd_db.yml](https://github.com/PaddlePaddle/PaddleOCR/blob/release%2F2.3/configs/det/det_r50_vd_db.yml)。

icdar2015数据集下载路径：https://aistudio.baidu.com/aistudio/datasetdetail/96799

评判标准：能够跑通给60分，训练精度hmean达到0.72-0.74之间给80分，训练精度hmean达到0.74-0.75之间给90分，训练精度hmean达到0.75以上给100分。

```bash
python3 tools/train.py -c configs/det/det_r50_vd_db.lesson.yml  \
         -o Global.pretrained_model=./pretrain_models/ResNet50_vd_ssld_pretrained


visualdl --logdir output/det_r50_vd.lesson/vdl --port 8040 --host 10.168.47.18
```

## 作业二（100分）
题目：使用DB算法配置文件configs/det/det_mv3_db.yml在数据集[det_data_lesson_demo.tar](https://paddleocr.bj.bcebos.com/dataset/det_data_lesson_demo.tar)上训练文本检测模型，并调优实验精度。

数据集下载路径：https://paddleocr.bj.bcebos.com/dataset/det_data_lesson_demo.tar

评判标准：能够跑通给60分，训练精度hmean在达到0.68-0.70之间给80分，训练精度hmean达到0.70-0.71之间给90分，训练精度hmean达到0.71以上给100分。

## 提交说明
提交格式为notebook项目，具体提交步骤参考[预习作业](https://aistudio.baidu.com/aistudio/projectdetail/3259472)部分

项目中需提供**训练好的模型**和**训练log**，同时给出**评估脚本**

```bash
下载模型
cd PaddleOCR/
# Download the pre-trained model of MobileNetV3
wget -P ./pretrain_models/ https://paddle-imagenet-models-name.bj.bcebos.com/dygraph/MobileNetV3_large_x0_5_pretrained.pdparams
```


```bash
# 训练
python3 tools/train.py -c /home/aistudio/work/det_mv3_db.lesson2.yml  \
         -o Global.pretrain_weights=./pretrain_models/MobileNetV3_large_x0_5_pretrained
# 观察训练过程
visualdl --logdir output/db_mv3.lesson2/vdl --host 10.168.47.4 --port 8040
```

# 评估脚本
```bash
# 验证
python3 tools/eval.py -c /home/aistudio/work/det_mv3_db.lesson2.yml  -o Global.checkpoints="output/db_mv3.lesson2/best_accuracy" PostProcess.box_thresh=0.6 PostProcess.unclip_ratio=1.5
```
输出结果：
```
eval model:: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 250/250 [01:37<00:00,  2.57it/s]
[2021/12/27 01:15:49] root INFO: metric eval ***************
[2021/12/27 01:15:49] root INFO: precision:0.7428623057462956
[2021/12/27 01:15:49] root INFO: recall:0.6883791024782318
[2021/12/27 01:15:49] root INFO: hmean:0.7145836954632364
[2021/12/27 01:15:49] root INFO: fps:8.208583904669904
```

EVAL/best hmean

![](https://ai-studio-static-online.cdn.bcebos.com/47f87b2854654e95bb33b3a28b66b52dde48e120729044f6a2544dccd389b3ce)

训练好的模型：/home/aistudio/db_mv3.lesson2/best_accuracy.pdparams

训练log：/home/aistudio/db_mv3.lesson2/train.log
