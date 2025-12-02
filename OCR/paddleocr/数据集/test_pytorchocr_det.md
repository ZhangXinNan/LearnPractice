


# 1. ICDAR2019-LSVT

## 1.1 PP-OCRv4_mobile_det
```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_cml.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_100.txt]'

# weights/ch_PP-OCRv4_det_train/best_accuracy.pth 模型不对
# weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth 模型不对
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_cml_zx.yml \
    -o Global.pretrained_model= \
    Global.use_gpu=False

python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student_zx.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth \
    Global.use_gpu=False
```
[2025/12/02 08:39:45] torchocr INFO: precision:0.7479452054794521
[2025/12/02 08:39:45] torchocr INFO: recall:0.7165354330708661
[2025/12/02 08:39:45] torchocr INFO: hmean:0.7319034852546917
[2025/12/02 08:39:45] torchocr INFO: fps:1.2231537317767183


## 1.2 PP-OCRv4_server_det
```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher_zx.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth \
    Global.use_gpu=False
```

[2025/12/02 08:37:07] torchocr INFO: precision:0.8550932568149211
[2025/12/02 08:37:07] torchocr INFO: recall:0.7821522309711286
[2025/12/02 08:37:07] torchocr INFO: hmean:0.8169979437971213
[2025/12/02 08:37:07] torchocr INFO: fps:0.619422585012035



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


