


```bash
python3 tools/infer/predict_system.py \
    --image_dir="./doc/imgs/" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --rec_model_dir="./inference/ch_ppocr_mobile_v1.1_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_mobile_v1.1_cls_infer/" \
    --use_angle_cls=True \
    --use_space_char=True


python3 tools/infer/predict_system.py \
    --image_dir="/Users/zhangxin/data_md/王玉琨主任影像资料类型" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --rec_model_dir="./inference/ch_ppocr_mobile_v1.1_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_mobile_v1.1_cls_infer/" \
    --use_angle_cls=True \
    --use_space_char=True
```


```bash
python3 tools/infer/predict_system.py \
    --image_dir="/Users/zhangxin/gitlab_md/md-data-evaluation/HuaYanDan/20201117/imgs" \
    --det_model_dir="./inference/ch_ppocr_mobile_v2.0_det_infer/" \
    --rec_model_dir="./inference/ch_ppocr_mobile_v2.0_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer/" \
    --use_angle_cls=False \
    --use_space_char=True


python3 tools/infer/predict_system.py \
    --image_dir="/Users/zhangxin/gitlab_md/md-data-evaluation/HuaYanDan/20201117/imgs" \
    --det_model_dir="./inference/ch_ppocr_server_v2.0_det_infer/" \
    --rec_model_dir="./inference/ch_ppocr_server_v2.0_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_server_v2.0_cls_infer/" \
    --use_angle_cls=False \
    --use_space_char=True
```