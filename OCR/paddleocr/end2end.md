


```bash
python3 tools/infer/predict_system.py \
    --image_dir="./doc/imgs/" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --rec_model_dir="./inference/ch_ppocr_mobile_v1.1_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_mobile_v1.1_cls_infer/" \
    --use_angle_cls=True \
    --use_space_char=True
```