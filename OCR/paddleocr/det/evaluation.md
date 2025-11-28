

```bash
cd /Users/zhangxin/data_public/OCR/paddleocr

# Download example dataset
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/ocr_det_dataset_examples.tar
tar -xf ocr_det_dataset_examples.tar
```

数据示例：
```json
images/val_img_61.jpg	[{"transcription": "MASA", "points": [[310, 104], [416, 141], [418, 216], [312, 179]]}, {"transcription": "###", "points": [[1197, 126], [1252, 118], [1257, 136], [1203, 144]]}, {"transcription": "###", "points": [[1137, 140], [1177, 132], [1180, 148], [1140, 156]]}, {"transcription": "###", "points": [[1096, 152], [1130, 145], [1133, 158], [1100, 165]]}, {"transcription": "###", "points": [[1061, 161], [1092, 154], [1093, 168], [1062, 175]]}, {"transcription": "###", "points": [[1030, 168], [1055, 162], [1056, 177], [1030, 183]]}, {"transcription": "###", "points": [[1000, 173], [1023, 168], [1025, 184], [1002, 189]]}, {"transcription": "###", "points": [[223, 293], [313, 288], [313, 311], [222, 316]]}]
```



```bash
# Download PP-OCRv5_server_det pretrained model
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv5_server_det_pretrained.pdparams
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv5_mobile_det_pretrained.pdparams


# Note: Set pretrained_model to local path. For custom-trained models, modify the path and filename as {path/to/weights}/{model_name}.
# Demo dataset evaluation
python3 tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=output/PP-OCRv5_server_det/best_accuracy.pdparams \
    Eval.dataset.data_dir=./ocr_det_dataset_examples \
    Eval.dataset.label_file_list='[./ocr_det_dataset_examples/val.txt]'


# 要使用python，python3找不到paddle，应该是使用了其他环境的python。
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=output/PP-OCRv5_server_det/PP-OCRv5_server_det_pretrained.pdparams \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/paddleocr/ocr_det_dataset_examples \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/paddleocr/ocr_det_dataset_examples/val.txt]'
```

```
[2025/11/28 09:24:36] ppocr INFO: metric eval ***************
[2025/11/28 09:24:36] ppocr INFO: precision:0.6301369863013698
[2025/11/28 09:24:36] ppocr INFO: recall:0.4577114427860697
[2025/11/28 09:24:36] ppocr INFO: hmean:0.5302593659942364
[2025/11/28 09:24:36] ppocr INFO: fps:0.28604721126051846
```



```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.pretrained_model=output/PP-OCRv5_mobile_det/PP-OCRv5_mobile_det_pretrained.pdparams \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/paddleocr/ocr_det_dataset_examples \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/paddleocr/ocr_det_dataset_examples/val.txt]'
```

```
[2025/11/28 09:27:10] ppocr INFO: metric eval ***************
[2025/11/28 09:27:10] ppocr INFO: precision:0.4491017964071856
[2025/11/28 09:27:10] ppocr INFO: recall:0.373134328358209
[2025/11/28 09:27:10] ppocr INFO: hmean:0.4076086956521739
[2025/11/28 09:27:10] ppocr INFO: fps:1.3691117787841809
```


