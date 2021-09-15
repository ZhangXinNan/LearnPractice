
# 下载flowers102数据


进入PaddleClas目录。
```bash
cd path_to_PaddleClas
```

进入dataset/flowers102目录，下载并解压flowers102数据集.
```bash
cd dataset/flowers102
wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz
wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat
wget https://www.robots.ox.ac.uk/~vgg/data/flowers/102/setid.mat
tar -xf 102flowers.tgz
```

制作train/val/test标签文件
```bash
python generate_flowers102_list.py jpg train > train_list.txt
python generate_flowers102_list.py jpg valid > val_list.txt
python generate_flowers102_list.py jpg test > extra_list.txt
cat train_list.txt extra_list.txt > train_extra_list.txt
```

注意：这里将train_list.txt和extra_list.txt合并成train_extra_list.txt，是为了之后在进行知识蒸馏时，使用更多的数据提升无标签知识蒸馏任务的效果。

返回PaddleClas根目录
```bash
cd ../../
```


# 训练

## MobileNetV3_large_x1_0
```bash
export CUDA_VISIBLE_DEVICES=1
python tools/train.py \
    -c ppcls/configs/quick_start/MobileNetV3_large_x1_0.zx.yaml \
    -o pretrained_model="" \
    -o use_gpu=True
```

迭代20轮
```bash
[2021/09/09 16:54:46] root INFO: [Eval][Epoch 20][best metric: 0.26862745098039215]
```

## ResNet50_vd
```bash
export CUDA_VISIBLE_DEVICES=1
python tools/train.py \
    -c ppcls/configs/quick_start/ResNet50_vd.zx.yaml \
    -o pretrained_model="" \
    -o use_gpu=True
```

迭代20轮
```bash
[2021/09/09 18:48:27] root INFO: [Eval][Epoch 20][best metric: 0.30980392156862746]
```

# 微调
pretrained/MobileNetV3_large_x1_0_pretrained.pdparams


```bash
export CUDA_VISIBLE_DEVICES=1
python tools/train.py \
    -c ppcls/configs/quick_start/ResNet50_vd_finetune.zx.yaml \
    -o pretrained_model="pretrained/ResNet50_vd_pretrained.pdparams" \
    -o use_gpu=True
```
visualdl --logdir ./output/ResNet50_vd_ft --port 8893 --host 10.168.47.5

