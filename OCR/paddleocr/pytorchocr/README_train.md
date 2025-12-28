
python tools/train.py \
    -c /Users/zhangxin/github/LearnPractice/OCR/paddleocr/数据集/1_ICDAR2019-LSVT/PP-OCRv5_mobile_det.yml

python tools/train.py \
    -c /Users/zhangxin/github/LearnPractice/OCR/paddleocr/数据集/1_ICDAR2019-LSVT/PP-OCRv5_mobile_det_train_mps.yml


nohup python tools/train.py \
    -c configs/det/PP-OCRv5/PP-OCRv5_mobile_det.yml \
    -o Global.output_dir=./output/PP-OCRv5_mobile_det_1_ICDAR2019-LSVT \
    Global.use_gpu=true \
    Global.device=gpu \
    Global.use_tensorboard=true \
    Train.dataset.data_dir=/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT \
    Train.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train.txt']" \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/val.txt']" \
    >nohup.train.PP-OCRv5_mobile_det.1_ICDAR2019-LSVT.out &


nohup python tools/train.py \
    -c configs/det/PP-OCRv5/PP-OCRv5_server_det.yml \
    -o Global.output_dir=./output/PP-OCRv5_server_det_1_ICDAR2019-LSVT \
    Global.use_gpu=true \
    Global.device=gpu \
    Global.use_tensorboard=true \
    Train.dataset.data_dir=/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT \
    Train.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/train.txt']" \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT \
    Eval.dataset.label_file_list="['/home/zhangxin/data_public/OCR/1_ICDAR2019-LSVT/val.txt']" \
    >nohup.train.PP-OCRv5_server_det.1_ICDAR2019-LSVT.out &
