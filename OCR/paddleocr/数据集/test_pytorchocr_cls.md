
# 3 PaddleOCR
## 3.1 
```bash
python tools/eval.py \
    -c configs/cls/cls_mv3.yml \
    -o Global.checkpoints=weights/ch_ppocr_mobile_v2.0_cls_train/best_accuracy.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_10000.txt']"
```

```bash
python tools/eval.py \
    -c configs/cls/cls_mv3.yml \
    -o Global.checkpoints=weights/ch_ppocr_mobile_v2.0_cls_train/best_accuracy.pth \
    Global.device=mps \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/test_cls.txt']"
```
[2026/01/04 09:42:06] torchocr INFO: acc:0.8565999991434
[2026/01/04 09:42:06] torchocr INFO: fps:20855.915659499395




