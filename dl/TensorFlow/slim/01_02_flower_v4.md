

flowers
-----------------------
# 下载数据
```
# DATA_DIR=$HOME/data/slim/flowers
DATA_DIR=/Users/zhangxin/data_public/slim/flowers
python download_and_convert_data.py \
    --dataset_name=flowers \
    --dataset_dir="${DATA_DIR}"
```

# 训练(需要提前下载好inception_v4.ckpt) Fine-tune only the new layers for 1000 steps.

```
# PRETRAINED_CHECKPOINT_DIR=$HOME/data_public/goolenet
# TRAIN_DIR=$HOME/data/slim/flowers_train_logs
# DATASET_DIR=$HOME/data/slim/flowers

PRETRAINED_CHECKPOINT_DIR=/Users/zhangxin/data_public/googlenet
TRAIN_DIR=/Users/zhangxin/data_public/slim/flowers_train_logs_v4
DATASET_DIR=/Users/zhangxin/data_public/slim/flowers
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR} \
  --dataset_dir=${DATASET_DIR} \
  --dataset_name=flowers \
  --dataset_split_name=train \
  --model_name=inception_v4 \
  --checkpoint_path=${PRETRAINED_CHECKPOINT_DIR}/inception_v4.ckpt \
  --checkpoint_exclude_scopes=InceptionV4/Logits,InceptionV4/AuxLogits \
  --trainable_scopes=InceptionV4/Logits,InceptionV4/AuxLogits \
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
  --model_name=inception_v4
```
结果：
```
INFO:tensorflow:Restoring parameters from /data/zhangxin/data/slim/flowers_train_logs_v4/model.ckpt-1000
2018-01-18 15:11:02.599341: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:247] PoolAllocator: After 1223 get requests, put_count=1200 evicted_count=1000 eviction_rate=0.833333 and unsatisfied allocation rate=0.918234
2018-01-18 15:11:02.599419: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:259] Raising pool_size_limit_ from 100 to 110
INFO:tensorflow:Evaluation [1/7]
INFO:tensorflow:Evaluation [2/7]
INFO:tensorflow:Evaluation [3/7]
INFO:tensorflow:Evaluation [4/7]
INFO:tensorflow:Evaluation [5/7]
INFO:tensorflow:Evaluation [6/7]
INFO:tensorflow:Evaluation [7/7]
2018-01-18 15:11:14.448064: I tensorflow/core/kernels/logging_ops.cc:79] eval/Accuracy[0.85714287]
2018-01-18 15:11:14.448174: I tensorflow/core/kernels/logging_ops.cc:79] eval/Recall_5[1]
INFO:tensorflow:Finished evaluation at 2018-01-18-07:11:14
```

# Fine-tune all the new layers for 500 steps.
```
python train_image_classifier.py \
  --train_dir=${TRAIN_DIR}/all \
  --dataset_name=flowers \
  --dataset_split_name=train \
  --dataset_dir=${DATASET_DIR} \
  --model_name=inception_v4 \
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
  --model_name=inception_v4
```

结果：
```
INFO:tensorflow:Restoring parameters from /data/zhangxin/data/slim/flowers_train_logs_v4/all/model.ckpt-500
2018-01-18 15:39:18.366181: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:247] PoolAllocator: After 1223 get requests, put_count=1200 evicted_count=1000 eviction_rate=0.833333 and unsatisfied allocation rate=0.918234
2018-01-18 15:39:18.366229: I tensorflow/core/common_runtime/gpu/pool_allocator.cc:259] Raising pool_size_limit_ from 100 to 110
INFO:tensorflow:Evaluation [1/7]
INFO:tensorflow:Evaluation [2/7]
INFO:tensorflow:Evaluation [3/7]
INFO:tensorflow:Evaluation [4/7]
INFO:tensorflow:Evaluation [5/7]
INFO:tensorflow:Evaluation [6/7]
INFO:tensorflow:Evaluation [7/7]
2018-01-18 15:39:30.158116: I tensorflow/core/kernels/logging_ops.cc:79] eval/Accuracy[0.86285716]
2018-01-18 15:39:30.158182: I tensorflow/core/kernels/logging_ops.cc:79] eval/Recall_5[1]
INFO:tensorflow:Finished evaluation at 2018-01-18-07:39:30
```