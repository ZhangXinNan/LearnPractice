
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
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_distill_zx.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv4_rec_train/best_accuracy.pth \
       Global.use_gpu=False
```
准确率为0，不知道问题出在哪？

## 3.4 
```bash
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_zx.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv4_rec_server_train/student.pth \
    Global.use_gpu=False
```
准确率为0，不知道问题出在哪？
[2025/12/01 19:21:10] torchocr INFO: acc:0.0
[2025/12/01 19:21:10] torchocr INFO: norm_edit_dis:0.00021005635180404436
[2025/12/01 19:21:10] torchocr INFO: fps:4.420209408560761