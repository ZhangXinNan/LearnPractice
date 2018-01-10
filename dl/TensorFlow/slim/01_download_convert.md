使用CPU训练时加上``` --clone_on_cpu=True```

## mnist
### 下载数据
```
DATA_DIR=$HOME/data/slim/mnist

python download_and_convert_data.py \
    --dataset_name=mnist \
    --dataset_dir="${DATA_DIR}"
```
### 训练
```
DATASET_DIR=/data/zhangxin/data/slim/mnist_zx
TRAIN_DIR=/data/zhangxin/data/slim/mnist_train_logs_zx

python train_image_classifier.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_name=mnist \
    --dataset_split_name=train \
    --dataset_dir=${DATASET_DIR} \
    --model_name=lenet \
    --save_interval_secs=60
```

### 评价
```
DATASET_DIR=/data/zhangxin/data/slim/mnist_zx
CHECKPOINT_DIR=/data/zhangxin/data/slim/mnist_train_logs_zx
CHECKPOINT_FILE=${CHECKPOINT_DIR}  # Example
python eval_image_classifier.py \
    --alsologtostderr \
    --checkpoint_path=${CHECKPOINT_FILE} \
    --dataset_dir=${DATASET_DIR} \
    --dataset_name=mnist \
    --dataset_split_name=test \
    --model_name=lenet \
    --batch_size=100
```


## flowers
### 下载数据
```
# DATA_DIR=$HOME/data/slim/flowers
DATA_DIR=/data/zhangxin/data/slim/flowers
python download_and_convert_data.py \
    --dataset_name=flowers \
    --dataset_dir="${DATA_DIR}"
```

### 训练(需要提前下载好inception_v3.ckpt)
```
# PRETRAINED_CHECKPOINT_DIR=$HOME/data_public/goolenet
# TRAIN_DIR=$HOME/data/slim/flowers_train_logs
# DATASET_DIR=$HOME/data/slim/flowers
PRETRAINED_CHECKPOINT_DIR=/data/zhangxin/data
TRAIN_DIR=/data/zhangxin/data/slim/flowers_train_logs
DATASET_DIR=/data/zhangxin/data/slim/flowers
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR} \
  --dataset_dir=${DATASET_DIR} \
  --dataset_name=flowers \
  --dataset_split_name=train \
  --model_name=inception_v3 \
  --checkpoint_path=${PRETRAINED_CHECKPOINT_DIR}/inception_v3.ckpt \
  --checkpoint_exclude_scopes=InceptionV3/Logits,InceptionV3/AuxLogits \
  --trainable_scopes=InceptionV3/Logits,InceptionV3/AuxLogits \
  --max_number_of_steps=1000 \
  --batch_size=32 \
  --learning_rate=0.01 \
  --learning_rate_decay_type=fixed \
  --save_interval_secs=60 \
  --save_summaries_secs=60 \
  --log_every_n_steps=100 \
  --optimizer=rmsprop \
  --weight_decay=0.00004
#  --clone_on_cpu=True
```
### 评价
```
python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR} \
  --eval_dir=${TRAIN_DIR} \
  --dataset_name=flowers \
  --dataset_split_name=validation \
  --dataset_dir=${DATASET_DIR} \
  --model_name=inception_v3
```

## cifar10
### 下载数据
```
DATA_DIR=$HOME/data/slim/cifar10

python download_and_convert_data.py \
    --dataset_name=cifar10 \
    --dataset_dir="${DATA_DIR}"
```

### 训练
```
DATASET_DIR=$HOME/data/slim/cifar10
TRAIN_DIR=$HOME/data/slim/cifar10_train_logs

python train_image_classifier.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_name=cifar10 \
    --dataset_split_name=train \
    --dataset_dir=${DATASET_DIR} \
    --model_name=cifarnet \
    --clone_on_cpu=True
```
### 评估
```
DATASET_DIR=$HOME/data/slim/cifar10
CHECKPOINT_DIR=$HOME/data/slim/cifar10_train_logs
CHECKPOINT_FILE=${CHECKPOINT_DIR}  # Example
python eval_image_classifier.py \
    --alsologtostderr \
    --checkpoint_path=${CHECKPOINT_FILE} \
    --dataset_dir=${DATASET_DIR} \
    --dataset_name=cifar10 \
    --dataset_split_name=test \
    --model_name=cifarnet \
    --batch_size=1000
```