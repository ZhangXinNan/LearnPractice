

## mnist
```
DATA_DIR=$HOME/data/slim/mnist

python download_and_convert_data.py \
    --dataset_name=mnist \
    --dataset_dir="${DATA_DIR}"
```

```
DATASET_DIR=$HOME/data/slim/mnist
TRAIN_DIR=$HOME/data/slim/mnist_train_logs

python train_image_classifier.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_name=mnist \
    --dataset_split_name=train \
    --dataset_dir=${DATASET_DIR} \
    --model_name=lenet \
    --clone_on_cpu=True
```


## flowers
```
DATA_DIR=$HOME/data/slim/flowers

python download_and_convert_data.py \
    --dataset_name=flowers \
    --dataset_dir="${DATA_DIR}"
```

```
DATASET_DIR=$HOME/data/slim/flowers
TRAIN_DIR=$HOME/data/slim/flowers_train_logs

python train_image_classifier.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_name=flowers \
    --dataset_split_name=train \
    --dataset_dir=${DATASET_DIR} \
    --model_name=flowers
```

## cifar10
```
DATA_DIR=$HOME/data/slim/cifar10

python download_and_convert_data.py \
    --dataset_name=cifar10 \
    --dataset_dir="${DATA_DIR}"
```

```
DATASET_DIR=$HOME/data/slim/cifar10
TRAIN_DIR=$HOME/data/slim/cifar10_train_logs

python train_image_classifier.py \
    --train_dir=${TRAIN_DIR} \
    --dataset_name=cifar10 \
    --dataset_split_name=train \
    --dataset_dir=${DATASET_DIR} \
    --model_name=lenet
```