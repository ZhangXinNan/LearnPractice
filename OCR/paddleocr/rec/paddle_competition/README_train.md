
/home/zhangxin/data_public/OCR/paddle_competition/SkLXRq6Q/train_label.csv

/media/zhangxin/DATA/data_public/OCR/paddle_competition/train

python process.py
得到 train_label.txt

python create.py
得到 label_list.txt

nohup python train.py >nohup.out &





```bash
#单卡训练 (默认训练方式)
python3 tools/train.py \
    -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml \
    -o Global.pretrained_model=./PP-OCRv5_server_rec_pretrained.pdparams

#多卡训练，通过--gpus参数指定卡号
python3 -m paddle.distributed.launch --gpus '0,1,2,3'  tools/train.py -c configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml \
        -o Global.pretrained_model=./PP-OCRv5_server_rec_pretrained.pdparams
```

/home/zhangxin/github/PaddleOCR/configs/rec/PP-OCRv5/PP-OCRv5_server_rec.yml
/home/zhangxin/github/PaddleOCR/configs/rec/PP-OCRv5/PP-OCRv5_mobile_rec.yml

```bash
# 下载 PP-OCRv5_server_rec 预训练模型
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv5_server_rec_pretrained.pdparams
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/PP-OCRv5_mobile_rec_pretrained.pdparams


nohup python3 /home/zhangxin/github/PaddleOCR/tools/train.py \
    -c PP-OCRv5_mobile_rec.yml \
    -o Global.pretrained_model=./PP-OCRv5_mobile_rec_pretrained.pdparams \
    Global.save_model_dir=./output/PP-OCRv5_mobile_rec \
    Global.character_dict_path=/home/zhangxin/github/PaddleOCR/ppocr/utils/dict/ppocrv5_dict.txt \
    Train.dataset.data_dir=/home/zhangxin/data_public/OCR/paddle_competition/SkLXRq6Q/train_images \
    Train.dataset.label_file_list=/home/zhangxin/data_public/OCR/paddle_competition/SkLXRq6Q/train.txt \
    Eval.dataset.data_dir=/home/zhangxin/data_public/OCR/paddle_competition/SkLXRq6Q/train_images \
    Eval.dataset.label_file_list=/home/zhangxin/data_public/OCR/paddle_competition/SkLXRq6Q/val.txt \
    >nohup.train.ppocrv5_mobile_rec.out &
    
```