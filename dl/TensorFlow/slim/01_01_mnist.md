
# mnist
## 下载数据
```
DATA_DIR=$HOME/data/slim/mnist
DATA_DIR=/Users/zhangxin/data_public/slim/mnist

python download_and_convert_data.py \
    --dataset_name=mnist \
    --dataset_dir="${DATA_DIR}"
```
## 训练
```
DATASET_DIR=/data/zhangxin/data/slim/mnist
TRAIN_DIR=/data/zhangxin/data/slim/mnist_train_logs_zx

python train_image_classifier.py \
  --train_dir=${TRAIN_DIR} \
  --dataset_name=mnist \
  --dataset_split_name=train \
  --dataset_dir=${DATASET_DIR} \
  --model_name=lenet \
  --preprocessing_name=lenet \
  --max_number_of_steps=20000 \
  --batch_size=50 \
  --learning_rate=0.01 \
  --save_interval_secs=60 \
  --save_summaries_secs=60 \
  --log_every_n_steps=100 \
  --optimizer=sgd \
  --learning_rate_decay_type=fixed \
  --weight_decay=0
```

## 评价
```
DATASET_DIR=/data/zhangxin/data/slim/mnist
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

python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR} \
  --eval_dir=${TRAIN_DIR} \
  --dataset_name=mnist \
  --dataset_split_name=test \
  --dataset_dir=${DATASET_DIR} \
  --model_name=lenet

```