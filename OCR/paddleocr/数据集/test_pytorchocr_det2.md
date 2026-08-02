
# 2. ICDAR2017-RCTW-17

Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW \
Eval.dataset.label_file_list='[/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_1000.txt]'


## 2.1 PP-OCRv3_mobile_det
```bash
python tools/eval.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/student.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_2048_1000.txt']"
```
[2025/12/22 16:34:13] torchocr INFO: precision:0.6510546420860323
[2025/12/22 16:34:13] torchocr INFO: recall:0.46650005950255863
[2025/12/22 16:34:13] torchocr INFO: hmean:0.5435385468663338
[2025/12/22 16:34:13] torchocr INFO: fps:26.19551303510169


```bash
python tools/eval.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/student.pth \
    Global.device=mps \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_1024_1000.txt']"
```
- 1024
[2026/08/02 12:40:33] torchocr INFO: precision:0.7679275934091436
[2026/08/02 12:40:33] torchocr INFO: recall:0.3937879328811139
[2026/08/02 12:40:33] torchocr INFO: hmean:0.5206104468219005
[2026/08/02 12:40:33] torchocr INFO: fps:50.52267605698781
- 2048
[2026/08/02 12:06:39] torchocr INFO: precision:0.6514798802793482
[2026/08/02 12:06:39] torchocr INFO: recall:0.46626204926811854
[2026/08/02 12:06:39] torchocr INFO: hmean:0.5435250052021919
[2026/08/02 12:06:39] torchocr INFO: fps:31.319063414020174



## 2.2 PP-OCRv3_server_det
```bash
# configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_dml.yml       指标为0
# configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml   指标为0
python tools/eval.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_cml.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/best_accuracy.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_2048_1000.txt']"
```
[2025/12/22 16:39:10] torchocr INFO: precision:0.6509465293922285
[2025/12/22 16:39:10] torchocr INFO: recall:0.46650005950255863
[2025/12/22 16:39:10] torchocr INFO: hmean:0.5435008665511265
[2025/12/22 16:39:10] torchocr INFO: fps:6.585626622568462

## 2.3 PP-OCRv4_mobile_det
```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_2048_1000.txt']"
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


```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth \
    Global.device=mps \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_1024_1000.txt']"
```
- 1024
[2026/08/02 12:38:42] torchocr INFO: precision:0.7480832420591457
[2026/08/02 12:38:42] torchocr INFO: recall:0.4064024753064382
[2026/08/02 12:38:42] torchocr INFO: hmean:0.5266810610734115
[2026/08/02 12:38:42] torchocr INFO: fps:36.53963512548125
- 2048
[2026/08/02 12:09:42] torchocr INFO: precision:0.6343170063888044
[2026/08/02 12:09:42] torchocr INFO: recall:0.4962513388075687
[2026/08/02 12:09:42] torchocr INFO: hmean:0.5568538425585899
[2026/08/02 12:09:42] torchocr INFO: fps:14.716511515796995

## 2.4 PP-OCRv4_server_det
```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_2048_1000.txt']"
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


```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth \
    Global.device=mps \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_1024_1000.txt']"
```
- 1024
[2026/08/02 12:36:10] torchocr INFO: precision:0.8283011272141707
[2026/08/02 12:36:10] torchocr INFO: recall:0.4897060573604665
[2026/08/02 12:36:10] torchocr INFO: hmean:0.6155111809139182
[2026/08/02 12:36:10] torchocr INFO: fps:12.105851515902529
- 2048
[2026/08/02 12:17:53] torchocr INFO: precision:0.7677662891843099
[2026/08/02 12:17:53] torchocr INFO: recall:0.5567059383553493
[2026/08/02 12:17:53] torchocr INFO: hmean:0.6454194260485652
[2026/08/02 12:17:53] torchocr INFO: fps:3.778316414385232


## 2.5 PP-OCRv5_mobile_det
```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_2048_1000.txt']"
```
[2025/12/24 12:00:18] torchocr INFO: precision:0.5991611743559018
[2025/12/24 12:00:18] torchocr INFO: recall:0.47602046888016186
[2025/12/24 12:00:18] torchocr INFO: hmean:0.5305391604217786
[2025/12/24 12:00:18] torchocr INFO: fps:30.047678498643094

```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth \
    Global.use_gpu=false \
    Global.device=mps \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_1024_1000.txt']"
```
- 1024
[2026/08/02 12:32:57] torchocr INFO: precision:0.7443527367506516
[2026/08/02 12:32:57] torchocr INFO: recall:0.4078305367130787
[2026/08/02 12:32:57] torchocr INFO: hmean:0.526947028523103
[2026/08/02 12:32:57] torchocr INFO: fps:36.92994281274863
- 2048
[2025/12/28 02:15:11] torchocr INFO: precision:0.6000600060006
[2025/12/28 02:15:11] torchocr INFO: recall:0.47602046888016186
[2025/12/28 02:15:11] torchocr INFO: hmean:0.5308912336585042
[2025/12/28 02:15:11] torchocr INFO: fps:11.791757717937454

## 2.6 PP-OCRv5_server_det
```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_2048_1000.txt']"
```
[2025/12/26 16:39:36] torchocr INFO: precision:0.7376420018421861
[2025/12/26 16:39:36] torchocr INFO: recall:0.5718195882422944
[2025/12/26 16:39:36] torchocr INFO: hmean:0.6442314138231547
[2025/12/26 16:39:36] torchocr INFO: fps:6.018932818326822

```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth \
    Global.use_gpu=false \
    Global.device=mps \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW/train_1024_1000.txt']"
```
- 1024
[2026/08/02 12:28:45] torchocr INFO: precision:0.8217117300264282
[2026/08/02 12:28:45] torchocr INFO: recall:0.48101868380340357
[2026/08/02 12:28:45] torchocr INFO: hmean:0.6068157934244107
[2026/08/02 12:28:45] torchocr INFO: fps:14.263587748774954
- 2048
[2025/12/28 02:21:44] torchocr INFO: precision:0.7350780532598714
[2025/12/28 02:21:44] torchocr INFO: recall:0.5715815780078544
[2025/12/28 02:21:44] torchocr INFO: hmean:0.6431010243020686
[2025/12/28 02:21:44] torchocr INFO: fps:4.78065556955719


