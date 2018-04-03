
单GPU
```
python train_1gpu.py \
	--gpu_id=2 \
	--input_size=512 \
	--batch_size_per_gpu=14 \
	--checkpoint_path=models/icdar_20180403/ \
	--text_scale=512 \
	--training_data_path=data/train/ \
	--geometry=RBOX \
	--learning_rate=0.0001 --num_readers=24 \
	--pretrained_model_path=models/resnet_v1_50.ckpt
```


多GPU
```
python multigpu_train.py \
	--gpu_list=0 \
	--input_size=512 \
	--batch_size_per_gpu=14 \
	--checkpoint_path=/tmp/east_icdar2015_resnet_v1_50_rbox/ \
	--text_scale=512 \
	--training_data_path=/data/ocr/icdar2015/ \
	--geometry=RBOX \
	--learning_rate=0.0001 --num_readers=24 \
	--pretrained_model_path=/tmp/resnet_v1_50.ckpt
```