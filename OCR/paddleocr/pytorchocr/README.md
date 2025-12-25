
# 1 创建虚拟环境
```bash
conda create -n py310_pytorchocr python=3.10

conda activate py310_pytorchocr


pip3 install torch torchvision
pip install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2
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

ls -alh weights/ch_PP-OCRv4_det_train/best_accuracy.pth
# 14M
python tools/infer_det.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_student.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_det_train/best_accuracy.pth Global.infer_img=doc/imgs/11.jpg

ls -alh weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth
# 109M
python tools/infer_det.py -c configs/det/ch_PP-OCRv4/ch_PP-OCRv4_det_teacher.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_det_server_train/best_accuracy.pth Global.infer_img=doc/imgs/11.jpg



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

ls -alh weights/ch_PP-OCRv4_rec_train/student.pth
# 88M
python tools/infer_rec.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_rec_train/student.pth Global.infer_img=doc/imgs_words/ch

ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ch_ptocr_v4_rec_infer.pth
# 26M
python tools/infer_rec.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec2.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ch_ptocr_v4_rec_infer.pth Global.infer_img=doc/imgs_words/ch

ls -alh weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth
# 151M
python tools/infer_rec.py -c configs/rec/PP-OCRv4/ch_PP-OCRv4_rec_hgnet.yml -o Global.pretrained_model=weights/ch_PP-OCRv4_rec_server_train/best_accuracy.pth Global.infer_img=doc/imgs_words/ch/word_2.jpg


ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth
# 31M
python tools/infer_rec.py -c configs/rec/PP-OCRv5/PP-OCRv5_mobile_rec.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_mobile_rec.pth Global.infer_img=doc/imgs_words/ch


ls -alh /Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_rec.pth
# 128M
python tools/infer_rec.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml -o Global.pretrained_model=/Users/zhangxin/github/PaddleOCR2Pytorch/models/ptocrv5/ptocr_v5_server_rec.pth Global.infer_img=doc/imgs_words/ch/word_2.jpg
# AssertionError: when model typs is rec, backbone only support ['MobileNetV1Enhance', 'ResNet31', 'MobileNetV3', 'PPLCNetV3', 'PPHGNet_small', 'ResNet', 'MTB']
```



