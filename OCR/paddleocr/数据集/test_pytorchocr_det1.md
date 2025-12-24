
```bash
conda create -n py310_torchocr python=3.10
conda activate py310_torchocr
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130
pip install -r requirements.txt
pip install numpy==1.26.4
```

ls -alh weights/ch_PP-OCRv4_det_train/best_accuracy.pth
14M
ls -alh weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth
109M

# 1. ICDAR2019-LSVT

## 1.1 PP-OCRv4_mobile_det
```bash
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


## 1.2 PP-OCRv4_server_det
```bash
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

## 1.3 PP-OCRv3_mobile_det
```bash
ls weights/ch_PP-OCRv3_det_distill/student.pth
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



## 1.4 PP-OCRv3_server_det
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

## 1.5 PP-OCRv5_mobile_det
```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```
[2025/12/24 11:49:30] torchocr INFO: precision:0.7350534054653904
[2025/12/24 11:49:30] torchocr INFO: recall:0.6679692424051431
[2025/12/24 11:49:30] torchocr INFO: hmean:0.699907541936336
[2025/12/24 11:49:30] torchocr INFO: fps:76.99832001989842


## 1.6 PP-OCRv5_server_det
```bash
python tools/eval.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.pretrained_model=/home/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth \
    Global.use_gpu=True \
    Global.device=gpu \
    Global.use_tensorboard=false \
    Eval.dataset.data_dir="/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT" \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train_1000.txt']"
```



