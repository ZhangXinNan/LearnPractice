
```bash
# Download the example dataset
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/ocr_rec_dataset_examples.tar
tar -xf ocr_rec_dataset_examples.tar
```


数据示例：
```
images/val_word_1.png   JOINT
images/val_word_2.png   yourself
images/val_word_3.png   154
images/val_word_4.png   197
images/val_word_5.png   727
images/val_word_6.png   198
images/val_word_7.png   20029
```


```
# Download the PP-OCRv5_server_rec pre-trained model
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv5_server_rec_pretrained.pdparams
```

```bash
# Note: Set the path of pretrained_model to a local path. If you use a model you trained and saved yourself, please modify the path and file name to {path/to/weights}/{model_name}.
# Demo test set evaluation
python tools/eval.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml -o \
    Global.pretrained_model=output/PP-OCRv5_server_rec_pretrained.pdparams \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/paddleocr/ocr_rec_dataset_examples \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/paddleocr/ocr_rec_dataset_examples/val.txt]'
```

[2025/11/28 16:22:09] ppocr INFO: metric eval ***************
[2025/11/28 16:22:09] ppocr INFO: acc:0.7226769344117624
[2025/11/28 16:22:09] ppocr INFO: norm_edit_dis:0.8798817060979708
[2025/11/28 16:22:09] ppocr INFO: fps:19.645540551609773


