




# 1.1

```bash
python3 tools/infer/predict_det.py \
    --image_dir="/Users/zhangxin/gitlab_md/md-data-evaluation/MedicalRecord/bingli0819/imgs" \
    --det_model_dir="./inference/ch_ppocr_mobile_v1.1_det_infer/" \
    --use_space_char=True
```


./inference/ch_ppocr_server_v1.1_det_infer

# 2.0
```bash
python3 tools/infer/predict_det.py \
    --image_dir="/Users/zhangxin/data_md/idcard1" \
    --det_model_dir="./inference/ch_ppocr_mobile_v2.0_det_infer/" \
    --use_space_char=True
```

python3 tools/infer/predict_det.py \
    --image_dir="./doc/imgs/00018069.jpg" \
    --det_model_dir="inference/ch_ppocr_mobile_v2.0_det_infer"

# 3.0
```bash
# download DB text detection inference model
wget  https://paddleocr.bj.bcebos.com/PP-OCRv3/chinese/ch_PP-OCRv3_det_infer.tar
tar xf ch_PP-OCRv3_det_infer.tar
# run inference
python3 tools/infer/predict_det.py --image_dir="./doc/imgs/00018069.jpg" --det_model_dir="./ch_PP-OCRv3_det_infer/"
```

