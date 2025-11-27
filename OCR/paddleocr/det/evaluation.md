

```bash
# Note: Set pretrained_model to local path. For custom-trained models, modify the path and filename as {path/to/weights}/{model_name}.
# Demo dataset evaluation
python3 tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=output/PP-OCRv5_server_det/best_accuracy.pdparams \
    Eval.dataset.data_dir=./ocr_det_dataset_examples \
    Eval.dataset.label_file_list='[./ocr_det_dataset_examples/val.txt]'


python3 tools/eval.py -c "D:\github\PaddleOCR\configs\det\PP-OCRv5\PP-OCRv5_mobile_det.yml" -o Global.pretrained_model="D:\github\PaddleOCR\pretrained\PP-OCRv4_mobile_det_pretrained.pdparams" Eval.dataset.data_dir="D:\data_public\ocr\ocr_det_dataset_examples" Eval.dataset.label_file_list="D:\data_public\ocr\ocr_det_dataset_examples\val.txt"
```



