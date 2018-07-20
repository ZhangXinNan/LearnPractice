

flowers

# 下载数据
```
# DATA_DIR=$HOME/data/slim/flowers
DATA_DIR=/Users/zhangxin/data_public/slim/flowers
python download_and_convert_data.py \
    --dataset_name=flowers \
    --dataset_dir="${DATA_DIR}"
```

# 训练(需要提前下载好inception_v3.ckpt) Fine-tune only the new layers for 1000 steps.

```
PRETRAINED_CHECKPOINT_DIR=/Users/zhangxin/data_public/googlenet
TRAIN_DIR=/Users/zhangxin/data_public/slim/flowers_train_logs
DATASET_DIR=/Users/zhangxin/data_public/slim/flowers
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
  --weight_decay=0.00004 \
  --clone_on_cpu=True
```
# 评价
```
python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR} \
  --eval_dir=${TRAIN_DIR} \
  --dataset_name=flowers \
  --dataset_split_name=validation \
  --dataset_dir=${DATASET_DIR} \
  --model_name=inception_v3
```
结果：
```
2018-01-18 14:18:01.465016: I tensorflow/core/kernels/logging_ops.cc:79] eval/Accuracy[0.83714288]
2018-01-18 14:18:01.465236: I tensorflow/core/kernels/logging_ops.cc:79] eval/Recall_5[1]
```

# Fine-tune all the new layers for 500 steps.
```
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR}/all \
  --dataset_name=flowers \
  --dataset_split_name=train \
  --dataset_dir=${DATASET_DIR} \
  --model_name=inception_v3 \
  --checkpoint_path=${TRAIN_DIR} \
  --max_number_of_steps=500 \
  --batch_size=32 \
  --learning_rate=0.0001 \
  --learning_rate_decay_type=fixed \
  --save_interval_secs=60 \
  --save_summaries_secs=60 \
  --log_every_n_steps=10 \
  --optimizer=rmsprop \
  --weight_decay=0.00004
```

# Run evaluation.
```
python eval_image_classifier.py \
  --checkpoint_path=${TRAIN_DIR}/all \
  --eval_dir=${TRAIN_DIR}/all \
  --dataset_name=flowers \
  --dataset_split_name=validation \
  --dataset_dir=${DATASET_DIR} \
  --model_name=inception_v3
```

结果：
```
INFO:tensorflow:Restoring parameters from /data/zhangxin/data/slim/flowers_train_logs/all/model.ckpt-500
INFO:tensorflow:Evaluation [1/7]
INFO:tensorflow:Evaluation [2/7]
INFO:tensorflow:Evaluation [3/7]
INFO:tensorflow:Evaluation [4/7]
INFO:tensorflow:Evaluation [5/7]
INFO:tensorflow:Evaluation [6/7]
INFO:tensorflow:Evaluation [7/7]
2018-01-18 14:36:19.862576: I tensorflow/core/kernels/logging_ops.cc:79] eval/Accuracy[0.89428574]
2018-01-18 14:36:19.862789: I tensorflow/core/kernels/logging_ops.cc:79] eval/Recall_5[1]
```