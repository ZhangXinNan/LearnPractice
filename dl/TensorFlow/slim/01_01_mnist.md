
# mnist
## 下载数据
```
DATA_DIR=$HOME/data/slim/mnist

python download_and_convert_data.py \
    --dataset_name=mnist \
    --dataset_dir="${DATA_DIR}"
```
## 训练
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

## 评价
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