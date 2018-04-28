
[yeephycho/nasnet-tensorflow](https://github.com/yeephycho/nasnet-tensorflow)


download and convert
```
DATASET_DIR=/Users/zhangxin/data/slim/flowers
python download_and_convert_data.py \
    --dataset_name=flowers \
    --dataset_dir="${DATA_DIR}"

DATASET_DIR=/Users/zhangxin/data/slim/flowers_photo
# Convert the customized data into tfrecords. Be noted that the dataset_name must be "customized"!
python convert_customized_data.py \
    --dataset_name=customized \
    --dataset_dir="${DATASET_DIR}"
```

finetune
```
DATASET_DIR=/Users/zhangxin/data/slim/flowers
TRAIN_DIR=./train
CHECKPOINT_PATH=./pre-trained/nasnet-a_mobile_04_10_2017/model.ckpt

python train_image_classifier.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_dir=${DATASET_DIR} \
    --dataset_name=flowers \
    --dataset_split_name=train \
    --model_name=nasnet_mobile \
    --checkpoint_path=${CHECKPOINT_PATH} \
    --checkpoint_exclude_scopes=final_layer,aux_7 \
    --trainable_scopes=final_layer,aux_7 \
    --clone_on_cpu=True


# customized
DATASET_DIR=/Users/zhangxin/data/slim/flowers_photo
TRAIN_DIR=./train_flowers_photo
CHECKPOINT_PATH=./pre-trained/nasnet-a_mobile_04_10_2017/model.ckpt

python train_image_classifier.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_dir=${DATASET_DIR} \
    --dataset_name=customized \
    --dataset_split_name=train \
    --model_name=nasnet_mobile \
    --checkpoint_path=${CHECKPOINT_PATH} \
    --checkpoint_exclude_scopes=final_layer,aux_7 \
    --trainable_scopes=final_layer,aux_7 \
    --clone_on_cpu=True
```

Evaluation
A nasnet finetuned model for flowers dataset can be downloaded here from google drive.
```
# Please specify the model.ckpt-xxxx file by yourself, for example
CHECKPOINT_FILE=./train/model.ckpt-2039

# For Nasnet-a-mobile
# --dataset_name=customized
python eval_image_classifier.py \
    --alsologtostderr \
    --checkpoint_path=${CHECKPOINT_FILE} \
    --dataset_dir=/Users/zhangxin/data/slim/flowers \
    --dataset_name=flowers \
    --dataset_split_name=validation \
    --model_name=nasnet_mobile
```