
# 2. ICDAR2017-RCTW-17

Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW \
Eval.dataset.label_file_list='[/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_1000.txt]'

## 2.1 PP-OCRv4_mobile_det
```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student_zx2.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth \
    Global.use_gpu=True
```
[2025/12/17 12:28:12] torchocr INFO: precision:0.4240389294403893
[2025/12/17 12:28:12] torchocr INFO: recall:0.5185052957277163
[2025/12/17 12:28:12] torchocr INFO: hmean:0.46653817325195424
[2025/12/17 12:28:12] torchocr INFO: fps:18.72839829249217
- 192.168.18.178 gpu train_1024_1000.txt
[2025/12/17 13:00:22] torchocr INFO: precision:0.7490135905304691
[2025/12/17 13:00:22] torchocr INFO: recall:0.4066404855408783
[2025/12/17 13:00:22] torchocr INFO: hmean:0.527111453914385
[2025/12/17 13:00:22] torchocr INFO: fps:38.362938811422474
- 192.168.18.178 gpu train_2048_1000.txt
[2025/12/17 13:02:08] torchocr INFO: precision:0.6347852573865367
[2025/12/17 13:02:08] torchocr INFO: recall:0.49601332857312863
[2025/12/17 13:02:08] torchocr INFO: hmean:0.5568842274033001
[2025/12/17 13:02:08] torchocr INFO: fps:29.631491988741725

## 2.2 PP-OCRv4_server_det
```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher_zx2.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth \
    Global.use_gpu=True
```

- 192.168.18.178 gpu train_1024_1000.txt
[2025/12/17 12:52:43] torchocr INFO: precision:0.8288996372430472
[2025/12/17 12:52:43] torchocr INFO: recall:0.48946804712602643
[2025/12/17 12:52:43] torchocr INFO: hmean:0.6154882154882154
[2025/12/17 12:52:43] torchocr INFO: fps:8.786709798086722
- 192.168.18.178 gpu train_2048_1000.txt
[2025/12/17 12:58:20] torchocr INFO: precision:0.7683587974371612
[2025/12/17 12:58:20] torchocr INFO: recall:0.5565869332381292
[2025/12/17 12:58:20] torchocr INFO: hmean:0.6455486542443064
[2025/12/17 12:58:20] torchocr INFO: fps:5.693781364434131



