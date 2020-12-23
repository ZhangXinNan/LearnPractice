

```bash

# 不使用扩充数据
nohup python train.py \
       --config configs/ocrnet/ocrnet_hrnetw18_voc12_512x512_40k.yml \
       --do_eval \
       --use_vdl \
       --save_interval 100 \
       --save_dir output_ocrnet_voc > nohup_ocrnet_voc.out &
```