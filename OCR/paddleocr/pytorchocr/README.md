
# 1 创建虚拟环境

```bash
conda create -n py310_torchocr python=3.10
conda activate py310_torchocr

conda create -n py310_pytorchocr python=3.10
conda activate py310_pytorchocr

# pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
# CUDA 11.8
pip install torch==2.7.1 torchvision==0.22.1 torchaudio==2.7.1 --index-url https://download.pytorch.org/whl/cu118
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu130

pip install -r requirements.txt
pip install numpy==1.26.4
pip install opencv-python-headless
```


# 2 检测
```bash
ls -alh weights/ch_PP-OCRv3_det_distill
# -rw-------@  1 zhangxin  staff   131M Nov 28 17:03 best_accuracy.pth
# -rw-------@  1 zhangxin  staff   2.5M Nov 28 17:03 student.pth
# mobile
python tools/infer_det.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/student.pth Global.infer_img=doc/imgs/11.jpg

# best_accuracy.pth 【【【没有server模型】】】
python tools/infer_det.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_teacher.yml -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/best_accuracy.pth Global.infer_img=doc/imgs/11.jpg

# v4
ls -alh weights/ch_PP-OCRv4_det_train/best_accuracy.pth
# 14M
python tools/infer_det.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth Global.infer_img=doc/imgs/11.jpg

ls -alh weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth
# 109M
python tools/infer_det.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth Global.infer_img=doc/imgs/11.jpg


# v5
ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth
# 14M
python tools/infer_det.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth Global.infer_img=doc/imgs/11.jpg

ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth
# 101M
python tools/infer_det.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth Global.infer_img=doc/imgs/11.jpg
# AssertionError: when model typs is det, backbone only support ['MobileNetV3', 'ResNet_vd', 'PPLCNetV3', 'PPHGNet_small']
```


# 3 识别
```bash
ls -alh weights/ch_PP-OCRv3_rec/best_accuracy.pth
# 210M
python tools/infer_rec.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.pretrained_model=weights/ch_PP-OCRv3_rec/best_accuracy.pth Global.infer_img=doc/imgs_words/ch/word_2.jpg

ls -alh weights/ch_PP-OCRv3_rec/student.pth
# 105M
python tools/infer_rec.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec.yml -o Global.pretrained_model=weights/ch_PP-OCRv3_rec/student.pth Global.infer_img=doc/imgs_words/ch/word_2.jpg

# v4
ls -alh weights/ch_PP-OCRv4_rec_train/student.pth
# 88M
python tools/infer_rec.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_rec_train/student.pth Global.infer_img=doc/imgs_words/ch

ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ch_ptocr_v4_rec_infer.pth
# 26M
python tools/infer_rec.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec2.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ch_ptocr_v4_rec_infer.pth Global.infer_img=doc/imgs_words/ch

ls -alh weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth
# 151M
python tools/infer_rec.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_hgnet.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth Global.infer_img=doc/imgs_words/ch/word_2.jpg

# v5
ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth
# 31M
python tools/infer_rec.py -c configs/rec/PP-OCRv5/PP-OCRv5_mobile_rec.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth Global.infer_img=doc/imgs_words/ch


ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_rec.pth
# 128M
python tools/infer_rec.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_rec.pth Global.infer_img=doc/imgs_words/ch/word_2.jpg
# AssertionError: when model typs is rec, backbone only support ['MobileNetV1Enhance', 'ResNet31', 'MobileNetV3', 'PPLCNetV3', 'PPHGNet_small', 'ResNet', 'MTB']
```



# 4 分类
```bash
python tools/infer_cls.py -c configs/cls/cls_mv3.yml -o Global.pretrained_model=weights/ch_ppocr_mobile_v2.0_cls_train/best_accuracy.pth Global.infer_img=doc/imgs_words/ch
```

# 5 export
```bash
python tools/export.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml -o Global.pretrained_model=weights/ch_PP-OCRv3_rec/best_accuracy.pth
# 生成了Teacher和Student模型，Stduent模型与下边的一致

python tools/export.py -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec.yml -o Global.pretrained_model=weights/ch_PP-OCRv3_rec/student.pth

python tools/export.py -c configs/det/ch_PP-OCRv3/ch_PP-OCRv3_det_student.yml -o Global.pretrained_model=weights/ch_PP-OCRv3_det_distill/student.pth

# v4
python tools/export.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth
python tools/export.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth
python tools/export.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_rec_train/student.pth
python tools/export.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_hgnet.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth

# v5
python tools/export.py -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth
python tools/export.py -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_det.pth
python tools/export.py -c configs/rec/PP-OCRv5/PP-OCRv5_mobile_rec.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth
python tools/export.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_rec.pth
# 有错
```


```bash
# det + rec
python tools/infer/predict_system.py \
    --det_model_dir=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_det.pth  \
    --rec_model_dir=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth \
    --image_dir=doc/imgs/1.jpg \
    --use_angle_cls=false

```



