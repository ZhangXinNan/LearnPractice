
# 关于Pascal VOC 2012数据集
Pascal VOC 2012数据集以对象分割为主，包含20个类别和背景类，其中训练集1464张，验证集1449张。 通常情况下会利用SBD(Semantic Boundaries Dataset)进行扩充，扩充后训练集10582张。 运行下列命令进行SBD数据集下载并进行扩充：
```bash
python tools/voc_augment.py --voc_path data/VOCdevkit --num_workers 8
```


```bash
export CUDA_VISIBLE_DEVICES=0 # 设置1张可用的卡
# windows下请执行以下命令
# set CUDA_VISIBLE_DEVICES=0
python train.py \
       --config configs/pspnet/pspnet_resnet50_os8_voc12aug_512x512_40k.yml \
       --do_eval \
       --use_vdl \
       --save_interval 500 \
       --save_dir output

# 可视化
visualdl --logdir output/ --port 3389 --host 0.0.0.0

# 不使用扩充数据
nohup python train.py \
       --config configs/pspnet/pspnet_resnet50_os8_voc12_512x512_40k.yml \
       --do_eval \
       --use_vdl \
       --save_interval 100 \
       --save_dir output > nohup_psenet_voc.out &
```


