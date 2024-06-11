# 1 准备数据
```bash
cd PaddleSeg
mkdir data && cd data
wget https://paddleseg.bj.bcebos.com/dataset/optic_disc_seg.zip
unzip optic_disc_seg.zip
cd ..
```

# 2 准备配置文件
本示例使用的配置文件是：PaddleSeg/configs/quick_start/pp_liteseg_optic_disc_512x512_1k.yml


# 3 模型训练

```bash
export CUDA_VISIBLE_DEVICES=0 # 设置1张可用的卡
# windows下请执行以下命令
# set CUDA_VISIBLE_DEVICES=0
python tools/train.py \
       --config configs/quick_start/pp_liteseg_optic_disc_512x512_1k.yml \
       --save_interval 500 \
       --do_eval \
       --use_vdl \
       --save_dir output
```

# 4 模型评估
```bash
python tools/val.py \
       --config configs/quick_start/pp_liteseg_optic_disc_512x512_1k.yml \
       --model_path output/best_model/model.pdparams
```

# 5 模型预测
在PaddleSeg根目录下，执行如下命令，使用predict.py脚本加载模型，对图像进行预测，并且保存预测结果。
```bash
python tools/predict.py \
       --config configs/quick_start/pp_liteseg_optic_disc_512x512_1k.yml \
       --model_path output/best_model/model.pdparams \
       --image_path data/optic_disc_seg/JPEGImages/H0002.jpg \
       --save_dir output/result
```


