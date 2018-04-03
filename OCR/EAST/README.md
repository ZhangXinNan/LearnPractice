# 1 github EAST
[argman/EAST](https://github.com/argman/EAST)

## 1.1 installation
tensorflow version > 1.0

## 1.2 Download
Models trained on ICDAR 2013 (training set) + ICDAR 2015 (training set): [BaiduYun link](http://pan.baidu.com/s/1jHWDrYQ) [GoogleDrive](https://drive.google.com/open?id=0B3APw5BZJ67ETHNPaU9xUkVoV0U)
Resnet V1 50 provided by tensorflow slim: [slim resnet v1 50](http://download.tensorflow.org/models/resnet_v1_50_2016_08_28.tar.gz)

## 1.3 test
```
python eval.py \
	--test_data_path=/tmp/images/ \
	--gpu_list=0 \
	--checkpoint_path=/tmp/east_icdar2015_resnet_v1_50_rbox/ \
	--output_dir=/tmp/

python eval.py \
	--test_data_path=training_samples/ \
	--gpu_list=0 \
	--checkpoint_path=models/east_icdar2015_resnet_v1_50_rbox/ \
	--output_dir=training_samples_rst
```

## 1.4 train
```
# docker
python multigpu_train.py \
	--gpu_list=0,1,2,3 \
	--input_size=512 \
	--batch_size_per_gpu=14 \
	--checkpoint_path=models/icdar2015_20171019/ \
	--text_scale=512 \
	--training_data_path=/root/zhangxin/data/idcar2015/train \
	--geometry=RBOX \
	--learning_rate=0.0001 \
	--num_readers=24 \
	--pretrained_model_path=models/resnet_v1_50.ckpt


```