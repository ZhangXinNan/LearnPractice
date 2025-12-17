
# 2. ICDAR2017-RCTW-17
## 2.1 PP-OCRv4_mobile_det
```bash
python tools/eval.py -c configs/det/PP-OCRv4/PP-OCRv4_mobile_det.yml \
    -o Global.pretrained_model=output/PP-OCRv4_mobile_det_pretrained.pdparams \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_100.txt]'
```


## 2.2 PP-OCRv4_server_det
```bash
python tools/eval.py -c configs/det/PP-OCRv4/PP-OCRv4_server_det.yml \
    -o Global.pretrained_model=output/PP-OCRv4_server_det_pretrained.pdparams \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_10.txt]'
```


