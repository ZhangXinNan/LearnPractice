# 识别模型

```bash
nohup python tools/train.py \
    -c configs/rec/PP-OCRv5/PP-OCRv5_mobile_rec.yml \
    -o Global.output_dir=./output/PP-OCRv5_mobile_rec_3_Chinese_Street_View_Text \
    Global.use_gpu=true \
    Global.device=gpu \
    Global.use_tensorboard=true \
    Train.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Train.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train.txt']" \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/val.txt']" \
    >nohup.train.PP-OCRv5_mobile_rec.3_Chinese-Street-View-Text-Recognition.out &
```

```bash
nohup python tools/train.py \
    -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml \
    -o Global.output_dir=./output/PP-OCRv5_server_rec_3_Chinese_Street_View_Text \
    Global.use_gpu=true \
    Global.device=gpu \
    Global.use_tensorboard=true \
    Train.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Train.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train.txt']" \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/val.txt']" \
    >nohup.train.PP-OCRv5_server_rec.3_Chinese-Street-View-Text-Recognition.out &
```
