
## 3.1 ch_PP-OCRv3_rec_distillation
```bash
python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/best_accuracy.pth \
       Global.use_gpu=False \
       Eval.dataset.data_dir='/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition' \
       Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_1000.txt']"

python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation_zx.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/best_accuracy.pth \
       Global.use_gpu=False
```
[2025/12/01 18:54:38] torchocr INFO: acc:0.4665334618727926
[2025/12/01 18:54:38] torchocr INFO: norm_edit_dis:0.603722111875189
[2025/12/01 18:54:38] torchocr INFO: Teacher_acc:0.4635364589057297
[2025/12/01 18:54:38] torchocr INFO: Teacher_norm_edit_dis:0.6013467004729998
[2025/12/01 18:54:38] torchocr INFO: fps:8.753937061066555



## 3.2 ch_PP-OCRv3_rec
```bash
python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/student.pth \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_1000.txt']"

python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_zx.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/student.pth \
    Global.use_gpu=False
```
[2025/12/01 18:49:44] torchocr INFO: metric eval ***************
[2025/12/01 18:49:44] torchocr INFO: acc:0.4665334618727926
[2025/12/01 18:49:44] torchocr INFO: norm_edit_dis:0.603722111875189
[2025/12/01 18:49:44] torchocr INFO: fps:17.535619453890845

## 3.3 ch_PP-OCRv4_rec_distill_zx
```bash
# weights/ch_PP-OCRv4_rec_train/student.pth                 模型不对
# weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth    模型不对
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_distill_zx.yml \
    -o Global.checkpoints= \
       Global.use_gpu=False
```
没找到转换好的模型。



## 3.4 
```bash
# weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth 模型不对
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_zx.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv4_rec_train/student.pth \
    Global.use_gpu=False
```
[2025/12/02 07:55:16] torchocr INFO: acc:0.4925074875873378
[2025/12/02 07:55:16] torchocr INFO: norm_edit_dis:0.6237686581971686
[2025/12/02 07:55:16] torchocr INFO: fps:4.7129600298317635


## 3.5
```bash
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_hgnet_zx.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth \
    Global.use_gpu=False
```

[2025/12/02 08:02:37] torchocr INFO: acc:0.5254745202250298
[2025/12/02 08:02:37] torchocr INFO: norm_edit_dis:0.649389017361619
[2025/12/02 08:02:37] torchocr INFO: fps:10.873490362810074





