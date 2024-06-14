
# 1 快速体验
```bash
# 设置显卡
export CUDA_VISIBLE_DEVICES=0

# 用PP-YOLO算法在COCO数据集上预训练模型预测一张图片
python tools/infer.py -c configs/ppyolo/ppyolo_r50vd_dcn_1x_coco.yml -o use_gpu=true weights=https://paddledet.bj.bcebos.com/models/ppyolo_r50vd_dcn_1x_coco.pdparams --infer_img=demo/000000014439.jpg
```


# 2 数据准备
数据集参考Kaggle数据集 ，包含877张图像，数据类别4类：crosswalk，speedlimit，stop，trafficlight。 将数据划分为训练集701张图和测试集176张图，下载链接.
```bash
# 注意：可跳过这步下载，后面训练会自动下载
python dataset/roadsign_voc/download_roadsign_voc.py

# speedlimit      限速
# crosswalk       人行横道
# trafficlight    红绿灯（等于 traffic signals）
# stop            停止，车站
```

# 3 训练、评估、预测
# 3.1 训练
```bash
# 边训练边测试 CPU需要约1小时(use_gpu=false)，1080Ti GPU需要约10分钟
# -c 参数表示指定使用哪个配置文件
# -o 参数表示指定配置文件中的全局变量（覆盖配置文件中的设置），这里设置使用gpu
# --eval 参数表示边训练边评估，最后会自动保存一个名为model_final.pdparams的模型

python tools/train.py -c configs/yolov3/yolov3_mobilenet_v1_roadsign.yml --eval -o use_gpu=true
```

如果想通过VisualDL实时观察loss变化曲线，在训练命令中添加--use_vdl=true，以及通过--vdl_log_dir设置日志保存路径。
```bash
python -m pip install visualdl -i https://mirror.baidu.com/pypi/simple
```

```bash
python -u tools/train.py \
    -c configs/yolov3/yolov3_mobilenet_v1_roadsign.yml \
    -o use_gpu=true \
    --use_vdl=true \
    --vdl_log_dir=vdl_dir/scalar \
    --eval

visualdl --logdir vdl_dir/scalar/ --host 10.168.47.17 --port 8888

```

## 3.2 评估
```bash
# 评估 默认使用训练过程中保存的model_final.pdparams
# -c 参数表示指定使用哪个配置文件
# -o 参数表示指定配置文件中的全局变量（覆盖配置文件中的设置）
# 目前只支持单卡评估

python tools/eval.py -c configs/yolov3/yolov3_mobilenet_v1_roadsign.yml -o use_gpu=true
```
最终模型精度在mAP=0.85左右，由于数据集较小因此每次训练结束后精度会有一定波动

## 3.3 预测
```bash
# -c 参数表示指定使用哪个配置文件
# -o 参数表示指定配置文件中的全局变量（覆盖配置文件中的设置）
# --infer_img 参数指定预测图像路径
# 预测结束后会在output文件夹中生成一张画有预测结果的同名图像

python tools/infer.py -c configs/yolov3/yolov3_mobilenet_v1_roadsign.yml -o use_gpu=true --infer_img=demo/road554.png
```

