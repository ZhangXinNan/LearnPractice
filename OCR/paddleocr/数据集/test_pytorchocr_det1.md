

# 1. ICDAR2019-LSVT


## 1.1 PP-OCRv3_mobile_det
```bash
ls -alh weights/ch_PP-OCRv3_det_distill/student.pth
# 2.5M
python tools/eval.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/student.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
[2025/12/22 16:05:26] torchocr INFO: precision:0.7802960222016652
[2025/12/22 16:05:26] torchocr INFO: recall:0.6379679818479768
[2025/12/22 16:05:26] torchocr INFO: hmean:0.7019904292946806
[2025/12/22 16:05:26] torchocr INFO: fps:80.90832826824881


```bash
python tools/eval.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/student.pth \
    Global.device=mps \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
[2025/12/30 17:33:10] torchocr INFO: precision:0.7801418439716312
[2025/12/30 17:33:10] torchocr INFO: recall:0.63784192613135
[2025/12/30 17:33:10] torchocr INFO: hmean:0.7018517234204867
[2025/12/30 17:33:10] torchocr INFO: fps:70.77158451121066

## 1.2 PP-OCRv3_server_det
```bash
ls -alh weights/ch_PP-OCRv3_det_distill/best_accuracy.pth
# 131M
# configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_dml.yml       指标为0
# configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml   指标为0
python tools/eval.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_cml.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/best_accuracy.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```

[2025/12/22 16:25:45] torchocr INFO: precision:0.7802960222016652
[2025/12/22 16:25:45] torchocr INFO: recall:0.6379679818479768
[2025/12/22 16:25:45] torchocr INFO: hmean:0.7019904292946806
[2025/12/22 16:25:45] torchocr INFO: fps:23.343504367634903
> 【这个结果有问题】

## 1.3 PP-OCRv4_mobile_det
```bash
ls -alh weights/ch_PP-OCRv4_det_train/best_accuracy.pth
# 14M
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
[2025/12/02 08:39:45] torchocr INFO: precision:0.7479452054794521
[2025/12/02 08:39:45] torchocr INFO: recall:0.7165354330708661
[2025/12/02 08:39:45] torchocr INFO: hmean:0.7319034852546917
[2025/12/02 08:39:45] torchocr INFO: fps:1.2231537317767183
- 192.168.18.178 gpu 100个样本  与PaddleOCR低0.2%
[2025/12/17 11:11:54] torchocr INFO: precision:0.746922024623803
[2025/12/17 11:11:54] torchocr INFO: recall:0.7165354330708661
[2025/12/17 11:11:54] torchocr INFO: hmean:0.7314132618888145
[2025/12/17 11:11:54] torchocr INFO: fps:18.03294455788872
- 192.168.18.178 gpu 1000个样本 与PaddleOCR低0.2%
[2025/12/17 11:21:28] torchocr INFO: precision:0.7350975310326013
[2025/12/17 11:21:28] torchocr INFO: recall:0.6793142569015505
[2025/12/17 11:21:28] torchocr INFO: hmean:0.7061058700209644
[2025/12/17 11:21:28] torchocr INFO: fps:75.46508510221719

[2025/12/17 11:44:44] torchocr INFO: precision:0.7352981307136035
[2025/12/17 11:44:44] torchocr INFO: recall:0.6793142569015505
[2025/12/17 11:44:44] torchocr INFO: hmean:0.7061984012580265
[2025/12/17 11:44:44] torchocr INFO: fps:75.9563110103279

[2025/12/17 11:45:59] torchocr INFO: precision:0.7354345749761223
[2025/12/17 11:45:59] torchocr INFO: recall:0.6794403126181773
[2025/12/17 11:45:59] torchocr INFO: hmean:0.7063294456820863
[2025/12/17 11:45:59] torchocr INFO: fps:76.33578116711098

```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth \
    Global.device=mps \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
[2025/12/30 17:34:46] torchocr INFO: precision:0.7351056578050443
[2025/12/30 17:34:46] torchocr INFO: recall:0.6796924240514307
[2025/12/30 17:34:46] torchocr INFO: hmean:0.7063138590516111
[2025/12/30 17:34:46] torchocr INFO: fps:36.20869534979981


## 1.4 PP-OCRv4_server_det
```bash
ls -alh weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth
# 109M
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth \
    Global.use_gpu=True \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```

[2025/12/02 08:37:07] torchocr INFO: precision:0.8550932568149211
[2025/12/02 08:37:07] torchocr INFO: recall:0.7821522309711286
[2025/12/02 08:37:07] torchocr INFO: hmean:0.8169979437971213
[2025/12/02 08:37:07] torchocr INFO: fps:0.619422585012035
- 192.168.18.178 gpu 100个样本 与PaddleOCR在CPU下结果一致
[2025/12/17 11:14:07] torchocr INFO: precision:0.8550932568149211
[2025/12/17 11:14:07] torchocr INFO: recall:0.7821522309711286
[2025/12/17 11:14:07] torchocr INFO: hmean:0.8169979437971213
[2025/12/17 11:14:07] torchocr INFO: fps:3.7846982156590583
- 192.168.18.178 gpu 1000个样本 与PaddleOCR低0.3% 结果不稳定
[2025/12/17 11:26:51] torchocr INFO: precision:0.8305249965185907
[2025/12/17 11:26:51] torchocr INFO: recall:0.7517962939619312
[2025/12/17 11:26:51] torchocr INFO: hmean:0.7892020643112347
[2025/12/17 11:26:51] torchocr INFO: fps:21.66514208978694

[2025/12/17 11:55:47] torchocr INFO: precision:0.8304093567251462
[2025/12/17 11:55:47] torchocr INFO: recall:0.7517962939619312
[2025/12/17 11:55:47] torchocr INFO: hmean:0.7891498511412505
[2025/12/17 11:55:47] torchocr INFO: fps:21.623592960468528

```bash
python tools/eval.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml \
    -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth \
    Global.device=mps \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
[2025/12/30 17:37:44] torchocr INFO: precision:0.829346314325452
[2025/12/30 17:37:44] torchocr INFO: recall:0.7516702382453044
[2025/12/30 17:37:44] torchocr INFO: hmean:0.7886001454737818
[2025/12/30 17:37:44] torchocr INFO: fps:12.02012385131989

## 1.5 PP-OCRv5_mobile_det
```bash
ls -alh /home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth
# 14M
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/test.txt']"
```
- train_1000.txt
[2025/12/24 11:49:30] torchocr INFO: precision:0.7350534054653904
[2025/12/24 11:49:30] torchocr INFO: recall:0.6679692424051431
[2025/12/24 11:49:30] torchocr INFO: hmean:0.699907541936336
[2025/12/24 11:49:30] torchocr INFO: fps:76.99832001989842
- test.txt
[2025/12/28 14:56:37] torchocr INFO: precision:0.719674355495251
[2025/12/28 14:56:37] torchocr INFO: recall:0.6625031226580065
[2025/12/28 14:56:37] torchocr INFO: hmean:0.6899063475546307
[2025/12/28 14:56:37] torchocr INFO: fps:70.65181394901943

```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth \
    Global.use_gpu=false \
    Global.device=cpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
- cpu macbpookpro
[2025/12/28 01:50:44] torchocr INFO: precision:0.7354328523862376
[2025/12/28 01:50:44] torchocr INFO: recall:0.6682213538383965
[2025/12/28 01:50:44] torchocr INFO: hmean:0.7002179512581731
[2025/12/28 01:50:44] torchocr INFO: fps:1.222927491794297
```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth \
    Global.use_gpu=false \
    Global.device=mps \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
[2025/12/28 02:06:56] torchocr INFO: precision:0.7354328523862376
[2025/12/28 02:06:56] torchocr INFO: recall:0.6682213538383965
[2025/12/28 02:06:56] torchocr INFO: hmean:0.7002179512581731
[2025/12/28 02:06:56] torchocr INFO: fps:31.8428260921157

## 1.6 PP-OCRv5_server_det
```bash
ls -alh /home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth
# 101M
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/test.txt']"
```
- train_1000.txt
[2025/12/26 16:33:54] torchocr INFO: precision:0.8182070496808216
[2025/12/26 16:33:54] torchocr INFO: recall:0.7432245052313122
[2025/12/26 16:33:54] torchocr INFO: hmean:0.7789153841072726
[2025/12/26 16:33:54] torchocr INFO: fps:22.428419558429475
- test.txt
[2025/12/28 14:51:21] torchocr INFO: precision:0.8170982326346075
[2025/12/28 14:51:21] torchocr INFO: recall:0.7449412940294778
[2025/12/28 14:51:21] torchocr INFO: hmean:0.7793531525645214
[2025/12/28 14:51:21] torchocr INFO: fps:19.33500649996818

```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth \
    Global.use_gpu=false \
    Global.device=mps \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/test.txt']"
```
- train_1000.txt
[2025/12/28 02:11:55] torchocr INFO: precision:0.817223686035224
[2025/12/28 02:11:55] torchocr INFO: recall:0.742846338081432
[2025/12/28 02:11:55] torchocr INFO: hmean:0.7782620179609088
[2025/12/28 02:11:55] torchocr INFO: fps:14.726046019792618
- test.txt
[2025/12/30 17:41:42] torchocr INFO: precision:0.8176212661003015
[2025/12/30 17:41:42] torchocr INFO: recall:0.7453160129902573
[2025/12/30 17:41:42] torchocr INFO: hmean:0.7797961317302666
[2025/12/30 17:41:42] torchocr INFO: fps:15.204596054672997

