

```bash
python3 tools/infer/calibrate_image2.py \
    --image_dir="/Users/zhangxin/data_md/zhangxin/20200525idcard-1" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --use_space_char=True


python3 tools/infer/calibrate_image2.py \
    --image_dir="/Users/zhangxin/data_md/zhangxin/20200525idcard-2" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --use_gpu False \
    --use_space_char=True


python3 tools/infer/calibrate_image2.py \
    --image_dir="/Users/zhangxin/gitlab_md/md-data-evaluation/idcard/20200805idcard/imgs" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --use_space_char=True



python3 tools/infer/calibrate_image2.py \
    --image_dir="/Users/zhangxin/data_public/yaohe/jpg" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --use_space_char=True




python3 tools/infer/calibrate_image2.py \
    --image_dir="/Users/zhangxin/data_md/zhangxin/20200525idcard-1" \
    --det_model_dir="./inference/ch_ppocr_server_v1.1_det_infer" \
    --use_space_char=True


python3 tools/infer/calibrate_image2.py \
    --image_dir="/Users/zhangxin/data_md/zhangxin/20200525idcard-2" \
    --det_model_dir="./inference/ch_ppocr_server_v1.1_det_infer" \
    --use_space_char=True
```