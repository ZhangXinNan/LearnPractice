

![https://github.com/PaddlePaddle/PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection)



# 使用ppyolo训练coco


export CUDA_VISIBLE_DEVICES=1 #windows和Mac下不需要执行该命令
python tools/train.py -c configs/ppyolo/ppyolo_mbv3_small_coco.yml
                        --use_vdl=true \
                        --vdl_log_dir=vdl_dir/scalar \



