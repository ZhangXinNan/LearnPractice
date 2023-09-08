

# v1.1
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

# v2.0
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

# v3
```bash
python3 tools/infer/predict_system.py \
    --image_dir="./doc/imgs/" \
    --draw_img_save_dir="./inference_results" \
    --det_model_dir="./inference/ch_PP-OCRv3_det_infer" \
    --rec_model_dir="./inference/ch_PP-OCRv3_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer" \
    --use_angle_cls=true

python3 tools/infer/predict_system.py --image_dir="./doc/imgs/00018069.jpg" --draw_img_save_dir="./inference_results/v3" --det_model_dir="./inference/ch_PP-OCRv3_det_infer/" --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer" --rec_model_dir="./inference/ch_PP-OCRv3_rec_infer/" --use_angle_cls=true
```


python3 tools/infer/predict_system.py \
    --image_dir="/Users/zhangxin/pic/ruguo.png" \
    --draw_img_save_dir="/Users/zhangxin/pic/pic_result" \
    --det_model_dir="./inference/ch_PP-OCRv3_det_infer" \
    --rec_model_dir="./inference/ch_PP-OCRv3_rec_infer/" \
    --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer" \
    --use_angle_cls=true

# v4
```bash
# 使用方向分类器
python3 tools/infer/predict_system.py --image_dir="./doc/imgs/00018069.jpg" --draw_img_save_dir="./inference_results/v4" --det_model_dir="./inference/ch_PP-OCRv4_det_infer/" --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer" --rec_model_dir="./inference/ch_PP-OCRv4_rec_infer/" --use_angle_cls=true

# 不使用方向分类器
python3 tools/infer/predict_system.py --image_dir="./doc/imgs/00018069.jpg" --det_model_dir="./ch_PP-OCRv3_det_infer/" --rec_model_dir="./ch_PP-OCRv3_rec_infer/" --use_angle_cls=false
```





