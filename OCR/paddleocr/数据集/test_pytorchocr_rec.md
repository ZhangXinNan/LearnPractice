
# 3 PaddleOCR
## 3.1 ch_PP-OCRv3_rec
```bash
ls -alh weights/ch_PP-OCRv3_rec/student.pth
# 106M
python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/student.pth \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
```
[2025/12/01 18:49:44] torchocr INFO: metric eval ***************
[2025/12/01 18:49:44] torchocr INFO: acc:0.4665334618727926
[2025/12/01 18:49:44] torchocr INFO: norm_edit_dis:0.603722111875189
[2025/12/01 18:49:44] torchocr INFO: fps:17.535619453890845
- 192.168.18.178 gpu 10000
[2025/12/17 14:12:52] torchocr INFO: acc:0.474999999525
[2025/12/17 14:12:52] torchocr INFO: norm_edit_dis:0.61852884967915
[2025/12/17 14:12:52] torchocr INFO: fps:8468.686202998311


## 3.2 ch_PP-OCRv3_rec_distillation

```bash
ls -alh weights/ch_PP-OCRv3_rec/best_accuracy.pth
# 211M
python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/best_accuracy.pth \
    Global.use_gpu=False \
    Eval.dataset.data_dir='/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition' \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
```
[2025/12/01 18:54:38] torchocr INFO: acc:0.4665334618727926
[2025/12/01 18:54:38] torchocr INFO: norm_edit_dis:0.603722111875189
[2025/12/01 18:54:38] torchocr INFO: Teacher_acc:0.4635364589057297
[2025/12/01 18:54:38] torchocr INFO: Teacher_norm_edit_dis:0.6013467004729998
[2025/12/01 18:54:38] torchocr INFO: fps:8.753937061066555

- 192.168.18.178 gpu 10000
[2025/12/17 14:10:58] torchocr INFO: acc:0.4750999995249
[2025/12/17 14:10:58] torchocr INFO: norm_edit_dis:0.6185398753201646
[2025/12/17 14:10:58] torchocr INFO: Teacher_acc:0.4768999995231
[2025/12/17 14:10:58] torchocr INFO: Teacher_norm_edit_dis:0.6196739362911121
[2025/12/17 14:10:58] torchocr INFO: fps:7319.471786737848


## 3.3 ch_PP-OCRv4_rec
```bash
ls -alh weights/ch_PP-OCRv4_rec_train/student.pth
# 89M
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv4_rec_train/student.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir='/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition' \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
```
[2025/12/02 07:55:16] torchocr INFO: acc:0.4925074875873378
[2025/12/02 07:55:16] torchocr INFO: norm_edit_dis:0.6237686581971686
[2025/12/02 07:55:16] torchocr INFO: fps:4.7129600298317635
- 192.168.18.178 gpu 1000
- 192.168.18.178 gpu 10000
[2025/12/17 14:20:26] torchocr INFO: acc:0.5061999994938
[2025/12/17 14:20:26] torchocr INFO: norm_edit_dis:0.6449092859863765
[2025/12/17 14:20:26] torchocr INFO: fps:6026.165513004454

## 3.4 ch_PP-OCRv4_rec_hgnet
```bash
# weights/ch_PP-OCRv4_rec_train/student.pth                 模型不对
# weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth    模型不对
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_distill.yml \
    -o Global.checkpoints= \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
# 没找到转换好的模型。

ls -alh weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth
# 151M
python tools/eval.py \
    -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_hgnet.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
```

[2025/12/02 08:02:37] torchocr INFO: acc:0.5254745202250298
[2025/12/02 08:02:37] torchocr INFO: norm_edit_dis:0.649389017361619
[2025/12/02 08:02:37] torchocr INFO: fps:10.873490362810074
- 192.168.18.178 gpu 1000
[2025/12/17 14:17:27] torchocr INFO: acc:0.5254745202250298
[2025/12/17 14:17:27] torchocr INFO: norm_edit_dis:0.649389017361619
[2025/12/17 14:17:27] torchocr INFO: fps:245.14804349477492
- 192.168.18.178 gpu 10000
[2025/12/17 14:21:39] torchocr INFO: acc:0.5467999994532
[2025/12/17 14:21:39] torchocr INFO: norm_edit_dis:0.670459106335054
[2025/12/17 14:21:39] torchocr INFO: fps:3301.2878182178524
- 192.168.0.115 gtx1070 10000
[2025/12/26 14:52:34] torchocr INFO: acc:0.5467999994532
[2025/12/26 14:52:34] torchocr INFO: norm_edit_dis:0.670459106335054
[2025/12/26 14:52:34] torchocr INFO: fps:994.4350997344453




## 3.5 PP-OCRv5_mobile_rec
```bash
ls -alh /home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth
# 32M
python tools/eval.py -c configs/rec/PP-OCRv5/PP-OCRv5_mobile_rec.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Global.character_dict_path=torchocr/utils/dict/ppocrv5_dict.txt \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
```
[2025/12/25 18:10:48] torchocr INFO: acc:0.4507999995492
[2025/12/25 18:10:48] torchocr INFO: norm_edit_dis:0.6048595113310833
[2025/12/25 18:10:48] torchocr INFO: fps:6177.860588430239


## 3.6 PP-OCRv5_server_rec
```bash
ls -alh /home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_rec.pth
# 129M
python tools/eval.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_rec.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
```
[2025/12/26 18:25:58] torchocr INFO: acc:0.5384999994615001
[2025/12/26 18:25:58] torchocr INFO: norm_edit_dis:0.6633685283809352
[2025/12/26 18:25:58] torchocr INFO: fps:3942.8562296655396

