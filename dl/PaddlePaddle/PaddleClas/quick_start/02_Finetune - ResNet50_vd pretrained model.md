
```bash
# Finetune ResNet50_vd model pretrained on the 1000-class Imagenet dataset
python3 tools/train.py -c ./configs/quick_start/ResNet50_vd_finetune.yaml

python3 tools/train.py -c ./configs/quick_start/ResNet50_vd_finetune.yaml  -o use_gpu=False
```


日志
```bash
(py37_paddle2) ➜  PaddleClas git:(zxdev_release_2.0) ✗ python3 tools/train.py -c ./configs/quick_start/ResNet50_vd_finetune.yaml                    
2021-03-19 21:45:58,976 - INFO - 
===========================================================
==        PaddleClas is powered by PaddlePaddle !        ==
===========================================================
==                                                       ==
==   For more info please go to the following website.   ==
==                                                       ==
==       https://github.com/PaddlePaddle/PaddleClas      ==
===========================================================

2021-03-19 21:45:58,976 - INFO - ARCHITECTURE : 
2021-03-19 21:45:58,976 - INFO -     name : ResNet50_vd
2021-03-19 21:45:58,976 - INFO - ------------------------------------------------------------
2021-03-19 21:45:58,976 - INFO - LEARNING_RATE : 
2021-03-19 21:45:58,976 - INFO -     function : Cosine
2021-03-19 21:45:58,976 - INFO -     params : 
2021-03-19 21:45:58,976 - INFO -         lr : 0.00375
2021-03-19 21:45:58,976 - INFO - ------------------------------------------------------------
2021-03-19 21:45:58,976 - INFO - OPTIMIZER : 
2021-03-19 21:45:58,976 - INFO -     function : Momentum
2021-03-19 21:45:58,976 - INFO -     params : 
2021-03-19 21:45:58,976 - INFO -         momentum : 0.9
2021-03-19 21:45:58,976 - INFO -     regularizer : 
2021-03-19 21:45:58,976 - INFO -         factor : 1e-06
2021-03-19 21:45:58,976 - INFO -         function : L2
2021-03-19 21:45:58,976 - INFO - ------------------------------------------------------------
2021-03-19 21:45:58,976 - INFO - TRAIN : 
2021-03-19 21:45:58,976 - INFO -     batch_size : 32
2021-03-19 21:45:58,976 - INFO -     data_dir : ./dataset/flowers102/
2021-03-19 21:45:58,976 - INFO -     file_list : ./dataset/flowers102/train_list.txt
2021-03-19 21:45:58,976 - INFO -     num_workers : 0
2021-03-19 21:45:58,976 - INFO -     shuffle_seed : 0
2021-03-19 21:45:58,976 - INFO -     transforms : 
2021-03-19 21:45:58,976 - INFO -         DecodeImage : 
2021-03-19 21:45:58,977 - INFO -             channel_first : False
2021-03-19 21:45:58,977 - INFO -             to_np : False
2021-03-19 21:45:58,977 - INFO -             to_rgb : True
2021-03-19 21:45:58,977 - INFO -         RandCropImage : 
2021-03-19 21:45:58,977 - INFO -             size : 224
2021-03-19 21:45:58,977 - INFO -         RandFlipImage : 
2021-03-19 21:45:58,977 - INFO -             flip_code : 1
2021-03-19 21:45:58,977 - INFO -         NormalizeImage : 
2021-03-19 21:45:58,977 - INFO -             mean : [0.485, 0.456, 0.406]
2021-03-19 21:45:58,977 - INFO -             order : 
2021-03-19 21:45:58,977 - INFO -             scale : 1./255.
2021-03-19 21:45:58,977 - INFO -             std : [0.229, 0.224, 0.225]
2021-03-19 21:45:58,977 - INFO -         ToCHWImage : None
2021-03-19 21:45:58,977 - INFO - ------------------------------------------------------------
2021-03-19 21:45:58,977 - INFO - VALID : 
2021-03-19 21:45:58,977 - INFO -     batch_size : 20
2021-03-19 21:45:58,977 - INFO -     data_dir : ./dataset/flowers102/
2021-03-19 21:45:58,977 - INFO -     file_list : ./dataset/flowers102/val_list.txt
2021-03-19 21:45:58,977 - INFO -     num_workers : 0
2021-03-19 21:45:58,977 - INFO -     shuffle_seed : 0
2021-03-19 21:45:58,977 - INFO -     transforms : 
2021-03-19 21:45:58,977 - INFO -         DecodeImage : 
2021-03-19 21:45:58,977 - INFO -             channel_first : False
2021-03-19 21:45:58,977 - INFO -             to_np : False
2021-03-19 21:45:58,977 - INFO -             to_rgb : True
2021-03-19 21:45:58,977 - INFO -         ResizeImage : 
2021-03-19 21:45:58,977 - INFO -             resize_short : 256
2021-03-19 21:45:58,977 - INFO -         CropImage : 
2021-03-19 21:45:58,977 - INFO -             size : 224
2021-03-19 21:45:58,977 - INFO -         NormalizeImage : 
2021-03-19 21:45:58,977 - INFO -             mean : [0.485, 0.456, 0.406]
2021-03-19 21:45:58,977 - INFO -             order : 
2021-03-19 21:45:58,978 - INFO -             scale : 1.0/255.0
2021-03-19 21:45:58,978 - INFO -             std : [0.229, 0.224, 0.225]
2021-03-19 21:45:58,978 - INFO -         ToCHWImage : None
2021-03-19 21:45:58,978 - INFO - ------------------------------------------------------------
2021-03-19 21:45:58,978 - INFO - classes_num : 102
2021-03-19 21:45:58,978 - INFO - epochs : 20
2021-03-19 21:45:58,978 - INFO - image_shape : [3, 224, 224]
2021-03-19 21:45:58,978 - INFO - mode : train
2021-03-19 21:45:58,978 - INFO - model_save_dir : ./output/
2021-03-19 21:45:58,978 - INFO - pretrained_model : ./pretrained/ResNet50_vd_pretrained
2021-03-19 21:45:58,978 - INFO - save_interval : 1
2021-03-19 21:45:58,978 - INFO - topk : 5
2021-03-19 21:45:58,978 - INFO - total_images : 1020
2021-03-19 21:45:58,978 - INFO - use_gpu : True
2021-03-19 21:45:58,978 - INFO - valid_interval : 1
2021-03-19 21:45:58,978 - INFO - validate : True
W0319 21:45:58.980592 272035 device_context.cc:362] Please NOTE: device: 0, GPU Compute Capability: 6.0, Driver API Version: 10.1, Runtime API Version: 10.1
W0319 21:45:58.984421 272035 device_context.cc:372] device: 0, cuDNN Version: 7.6.
/data_sata/home/zhangxin/miniconda3/envs/py37_paddle2/lib/python3.7/site-packages/paddle/fluid/dygraph/layers.py:1303: UserWarning: Skip loading for out.weight. out.weight receives a shape [2048, 1000], but the expected shape is [2048, 102].
  warnings.warn(("Skip loading for {}. ".format(key) + str(err)))
/data_sata/home/zhangxin/miniconda3/envs/py37_paddle2/lib/python3.7/site-packages/paddle/fluid/dygraph/layers.py:1303: UserWarning: Skip loading for out.bias. out.bias receives a shape [1000], but the expected shape is [102].
  warnings.warn(("Skip loading for {}. ".format(key) + str(err)))
2021-03-19 21:46:02,592 - INFO - Finish initing model from ./pretrained/ResNet50_vd_pretrained
2021-03-19 21:46:03,213 - INFO - epoch:0  , train step:0   , top1: 0.00000, top5: 0.06250, loss: 4.63757, lr: 0.003750, batch_cost: 0.61383 s, reader_cost: 0.41014 s, ips: 52.13169 images/sec.
2021-03-19 21:46:06,157 - INFO - epoch:0  , train step:10  , top1: 0.00000, top5: 0.09375, loss: 4.58557, lr: 0.003748, batch_cost: 0.30388 s, reader_cost: 0.13033 s, ips: 105.30300 images/sec.
2021-03-19 21:46:09,200 - INFO - epoch:0  , train step:20  , top1: 0.03125, top5: 0.12500, loss: 4.50153, lr: 0.003740, batch_cost: 0.30426 s, reader_cost: 0.13033 s, ips: 105.17253 images/sec.
2021-03-19 21:46:12,312 - INFO - epoch:0  , train step:30  , top1: 0.06250, top5: 0.28125, loss: 4.47054, lr: 0.003728, batch_cost: 0.30759 s, reader_cost: 0.13360 s, ips: 104.03593 images/sec.
2021-03-19 21:46:12,313 - INFO - END epoch:0   train top1: 0.03024, top5: 0.10282, loss: 4.59630,  batch_cost: 0.30759 s, reader_cost: 0.13360 s, batch_cost_sum: 6.45931 s, ips: 104.03593 images/sec.
2021-03-19 21:46:12,509 - INFO - epoch:0  , valid step:0   , top1: 0.15000, top5: 0.45000, loss: 4.29943, lr: 0.000000, batch_cost: 0.19178 s, reader_cost: 0.15288 s, ips: 104.28495 images/sec.
2021-03-19 21:46:13,957 - INFO - epoch:0  , valid step:10  , top1: 0.25000, top5: 0.40000, loss: 4.29855, lr: 0.000000, batch_cost: 0.14744 s, reader_cost: 0.10749 s, ips: 135.64822 images/sec.
2021-03-19 21:46:15,452 - INFO - epoch:0  , valid step:20  , top1: 0.15000, top5: 0.50000, loss: 4.29625, lr: 0.000000, batch_cost: 0.14928 s, reader_cost: 0.11029 s, ips: 133.97285 images/sec.
2021-03-19 21:46:16,943 - INFO - epoch:0  , valid step:30  , top1: 0.20000, top5: 0.50000, loss: 4.31952, lr: 0.000000, batch_cost: 0.14923 s, reader_cost: 0.11023 s, ips: 134.01957 images/sec.
2021-03-19 21:46:18,361 - INFO - epoch:0  , valid step:40  , top1: 0.10000, top5: 0.30000, loss: 4.38249, lr: 0.000000, batch_cost: 0.14682 s, reader_cost: 0.10784 s, ips: 136.22083 images/sec.
2021-03-19 21:46:19,730 - INFO - epoch:0  , valid step:50  , top1: 0.45000, top5: 0.70000, loss: 4.22633, lr: 0.000000, batch_cost: 0.14440 s, reader_cost: 0.10557 s, ips: 138.50063 images/sec.
2021-03-19 21:46:19,730 - INFO - END epoch:0   valid top1: 0.23922, top5: 0.49216, loss: 4.29754,  batch_cost: 0.14440 s, reader_cost: 0.10557 s, batch_cost_sum: 5.92055 s, ips: 138.50063 images/sec.
2021-03-19 21:46:21,741 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:46:21,741 - INFO - The best top1 acc 0.23922, in epoch: 0
2021-03-19 21:46:23,655 - INFO - Already save model in ./output/ResNet50_vd/0
2021-03-19 21:46:24,025 - INFO - epoch:1  , train step:0   , top1: 0.28125, top5: 0.56250, loss: 4.23577, lr: 0.003727, batch_cost: 0.36145 s, reader_cost: 0.17639 s, ips: 88.53295 images/sec.
2021-03-19 21:46:27,070 - INFO - epoch:1  , train step:10  , top1: 0.28125, top5: 0.62500, loss: 4.06497, lr: 0.003710, batch_cost: 0.29515 s, reader_cost: 0.12167 s, ips: 108.41987 images/sec.
2021-03-19 21:46:30,163 - INFO - epoch:1  , train step:20  , top1: 0.43750, top5: 0.71875, loss: 3.76849, lr: 0.003688, batch_cost: 0.30802 s, reader_cost: 0.13409 s, ips: 103.89036 images/sec.
2021-03-19 21:46:33,255 - INFO - epoch:1  , train step:30  , top1: 0.40625, top5: 0.62500, loss: 3.70325, lr: 0.003661, batch_cost: 0.30858 s, reader_cost: 0.13458 s, ips: 103.70170 images/sec.
2021-03-19 21:46:33,255 - INFO - END epoch:1   train top1: 0.29637, top5: 0.57762, loss: 4.01297,  batch_cost: 0.30858 s, reader_cost: 0.13458 s, batch_cost_sum: 6.48013 s, ips: 103.70170 images/sec.
2021-03-19 21:46:33,439 - INFO - epoch:1  , valid step:0   , top1: 0.85000, top5: 0.90000, loss: 3.31560, lr: 0.000000, batch_cost: 0.17879 s, reader_cost: 0.13916 s, ips: 111.86392 images/sec.
2021-03-19 21:46:34,763 - INFO - epoch:1  , valid step:10  , top1: 0.65000, top5: 1.00000, loss: 3.16052, lr: 0.000000, batch_cost: 0.11846 s, reader_cost: 0.07957 s, ips: 168.83820 images/sec.
2021-03-19 21:46:36,136 - INFO - epoch:1  , valid step:20  , top1: 0.60000, top5: 0.95000, loss: 2.93439, lr: 0.000000, batch_cost: 0.13559 s, reader_cost: 0.09584 s, ips: 147.49847 images/sec.
2021-03-19 21:46:37,670 - INFO - epoch:1  , valid step:30  , top1: 0.70000, top5: 0.95000, loss: 3.41167, lr: 0.000000, batch_cost: 0.14406 s, reader_cost: 0.10424 s, ips: 138.82665 images/sec.
2021-03-19 21:46:39,164 - INFO - epoch:1  , valid step:40  , top1: 0.75000, top5: 1.00000, loss: 3.39145, lr: 0.000000, batch_cost: 0.14580 s, reader_cost: 0.10592 s, ips: 137.17772 images/sec.
2021-03-19 21:46:40,527 - INFO - epoch:1  , valid step:50  , top1: 0.55000, top5: 1.00000, loss: 3.19248, lr: 0.000000, batch_cost: 0.14347 s, reader_cost: 0.10386 s, ips: 139.39734 images/sec.
2021-03-19 21:46:40,528 - INFO - END epoch:1   valid top1: 0.51176, top5: 0.80784, loss: 3.33061,  batch_cost: 0.14347 s, reader_cost: 0.10386 s, batch_cost_sum: 5.88247 s, ips: 139.39734 images/sec.
2021-03-19 21:46:42,396 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:46:42,396 - INFO - The best top1 acc 0.51176, in epoch: 1
2021-03-19 21:46:44,363 - INFO - Already save model in ./output/ResNet50_vd/1
2021-03-19 21:46:44,729 - INFO - epoch:2  , train step:0   , top1: 0.46875, top5: 0.93750, loss: 3.34420, lr: 0.003658, batch_cost: 0.36191 s, reader_cost: 0.18834 s, ips: 88.41893 images/sec.
2021-03-19 21:46:47,797 - INFO - epoch:2  , train step:10  , top1: 0.56250, top5: 0.84375, loss: 3.07946, lr: 0.003627, batch_cost: 0.30239 s, reader_cost: 0.12880 s, ips: 105.82365 images/sec.
2021-03-19 21:46:50,928 - INFO - epoch:2  , train step:20  , top1: 0.43750, top5: 0.81250, loss: 2.91093, lr: 0.003590, batch_cost: 0.31215 s, reader_cost: 0.13828 s, ips: 102.51390 images/sec.
2021-03-19 21:46:53,951 - INFO - epoch:2  , train step:30  , top1: 0.62500, top5: 0.87500, loss: 2.51850, lr: 0.003550, batch_cost: 0.30744 s, reader_cost: 0.13371 s, ips: 104.08669 images/sec.
2021-03-19 21:46:53,951 - INFO - END epoch:2   train top1: 0.48690, top5: 0.77823, loss: 3.07358,  batch_cost: 0.30744 s, reader_cost: 0.13371 s, batch_cost_sum: 6.45616 s, ips: 104.08669 images/sec.
2021-03-19 21:46:54,146 - INFO - epoch:2  , valid step:0   , top1: 0.80000, top5: 0.95000, loss: 1.89931, lr: 0.000000, batch_cost: 0.19066 s, reader_cost: 0.15196 s, ips: 104.89838 images/sec.
2021-03-19 21:46:55,554 - INFO - epoch:2  , valid step:10  , top1: 0.75000, top5: 0.95000, loss: 1.77128, lr: 0.000000, batch_cost: 0.14165 s, reader_cost: 0.10230 s, ips: 141.18932 images/sec.
2021-03-19 21:46:57,020 - INFO - epoch:2  , valid step:20  , top1: 0.30000, top5: 0.95000, loss: 2.23763, lr: 0.000000, batch_cost: 0.14619 s, reader_cost: 0.10689 s, ips: 136.81210 images/sec.
2021-03-19 21:46:58,581 - INFO - epoch:2  , valid step:30  , top1: 0.70000, top5: 1.00000, loss: 2.34715, lr: 0.000000, batch_cost: 0.15088 s, reader_cost: 0.11213 s, ips: 132.55593 images/sec.
2021-03-19 21:47:00,027 - INFO - epoch:2  , valid step:40  , top1: 0.90000, top5: 1.00000, loss: 2.31092, lr: 0.000000, batch_cost: 0.14886 s, reader_cost: 0.11026 s, ips: 134.35204 images/sec.
2021-03-19 21:47:01,351 - INFO - epoch:2  , valid step:50  , top1: 0.85000, top5: 1.00000, loss: 1.52641, lr: 0.000000, batch_cost: 0.14485 s, reader_cost: 0.10621 s, ips: 138.07428 images/sec.
2021-03-19 21:47:01,351 - INFO - END epoch:2   valid top1: 0.67255, top5: 0.90784, loss: 2.19537,  batch_cost: 0.14485 s, reader_cost: 0.10621 s, batch_cost_sum: 5.93883 s, ips: 138.07428 images/sec.
2021-03-19 21:47:03,174 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:47:03,175 - INFO - The best top1 acc 0.67255, in epoch: 2
2021-03-19 21:47:05,027 - INFO - Already save model in ./output/ResNet50_vd/2
2021-03-19 21:47:05,361 - INFO - epoch:3  , train step:0   , top1: 0.71875, top5: 0.93750, loss: 2.47943, lr: 0.003546, batch_cost: 0.32926 s, reader_cost: 0.15559 s, ips: 97.18725 images/sec.
2021-03-19 21:47:08,469 - INFO - epoch:3  , train step:10  , top1: 0.50000, top5: 0.78125, loss: 2.61358, lr: 0.003500, batch_cost: 0.29602 s, reader_cost: 0.12219 s, ips: 108.10201 images/sec.
2021-03-19 21:47:11,505 - INFO - epoch:3  , train step:20  , top1: 0.68750, top5: 0.81250, loss: 2.34183, lr: 0.003451, batch_cost: 0.30292 s, reader_cost: 0.12907 s, ips: 105.63995 images/sec.
2021-03-19 21:47:14,535 - INFO - epoch:3  , train step:30  , top1: 0.84375, top5: 0.96875, loss: 1.50382, lr: 0.003397, batch_cost: 0.30293 s, reader_cost: 0.12916 s, ips: 105.63408 images/sec.
2021-03-19 21:47:14,535 - INFO - END epoch:3   train top1: 0.68548, top5: 0.90827, loss: 2.11648,  batch_cost: 0.30293 s, reader_cost: 0.12916 s, batch_cost_sum: 6.36158 s, ips: 105.63408 images/sec.
2021-03-19 21:47:14,728 - INFO - epoch:3  , valid step:0   , top1: 0.85000, top5: 0.95000, loss: 0.93842, lr: 0.000000, batch_cost: 0.18848 s, reader_cost: 0.14926 s, ips: 106.11171 images/sec.
2021-03-19 21:47:16,153 - INFO - epoch:3  , valid step:10  , top1: 0.95000, top5: 1.00000, loss: 1.50248, lr: 0.000000, batch_cost: 0.13312 s, reader_cost: 0.09439 s, ips: 150.23736 images/sec.
2021-03-19 21:47:17,570 - INFO - epoch:3  , valid step:20  , top1: 0.55000, top5: 1.00000, loss: 1.53924, lr: 0.000000, batch_cost: 0.14092 s, reader_cost: 0.10211 s, ips: 141.92870 images/sec.
2021-03-19 21:47:19,093 - INFO - epoch:3  , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.88403, lr: 0.000000, batch_cost: 0.14634 s, reader_cost: 0.10723 s, ips: 136.67125 images/sec.
2021-03-19 21:47:20,567 - INFO - epoch:3  , valid step:40  , top1: 0.95000, top5: 1.00000, loss: 1.03803, lr: 0.000000, batch_cost: 0.14670 s, reader_cost: 0.10742 s, ips: 136.33636 images/sec.
2021-03-19 21:47:21,990 - INFO - epoch:3  , valid step:50  , top1: 0.80000, top5: 1.00000, loss: 1.38336, lr: 0.000000, batch_cost: 0.14560 s, reader_cost: 0.10641 s, ips: 137.36660 images/sec.
2021-03-19 21:47:21,990 - INFO - END epoch:3   valid top1: 0.76275, top5: 0.93039, loss: 1.49231,  batch_cost: 0.14560 s, reader_cost: 0.10641 s, batch_cost_sum: 5.96943 s, ips: 137.36660 images/sec.
2021-03-19 21:47:23,955 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:47:23,955 - INFO - The best top1 acc 0.76275, in epoch: 3
2021-03-19 21:47:25,984 - INFO - Already save model in ./output/ResNet50_vd/3
2021-03-19 21:47:26,371 - INFO - epoch:4  , train step:0   , top1: 0.93750, top5: 0.96875, loss: 1.46174, lr: 0.003392, batch_cost: 0.37785 s, reader_cost: 0.19292 s, ips: 84.68920 images/sec.
2021-03-19 21:47:29,487 - INFO - epoch:4  , train step:10  , top1: 0.90625, top5: 0.96875, loss: 1.38458, lr: 0.003334, batch_cost: 0.33197 s, reader_cost: 0.15814 s, ips: 96.39412 images/sec.
2021-03-19 21:47:32,558 - INFO - epoch:4  , train step:20  , top1: 0.81250, top5: 0.96875, loss: 1.32102, lr: 0.003273, batch_cost: 0.30934 s, reader_cost: 0.13560 s, ips: 103.44690 images/sec.
2021-03-19 21:47:35,639 - INFO - epoch:4  , train step:30  , top1: 0.87500, top5: 1.00000, loss: 1.13964, lr: 0.003208, batch_cost: 0.30872 s, reader_cost: 0.13495 s, ips: 103.65266 images/sec.
2021-03-19 21:47:35,639 - INFO - END epoch:4   train top1: 0.81149, top5: 0.94960, loss: 1.47248,  batch_cost: 0.30872 s, reader_cost: 0.13495 s, batch_cost_sum: 6.48319 s, ips: 103.65266 images/sec.
2021-03-19 21:47:35,828 - INFO - epoch:4  , valid step:0   , top1: 0.90000, top5: 0.95000, loss: 0.82829, lr: 0.000000, batch_cost: 0.18378 s, reader_cost: 0.14445 s, ips: 108.82862 images/sec.
2021-03-19 21:47:37,171 - INFO - epoch:4  , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.79086, lr: 0.000000, batch_cost: 0.13158 s, reader_cost: 0.09291 s, ips: 151.99838 images/sec.
2021-03-19 21:47:38,622 - INFO - epoch:4  , valid step:20  , top1: 0.65000, top5: 1.00000, loss: 1.34405, lr: 0.000000, batch_cost: 0.14387 s, reader_cost: 0.10444 s, ips: 139.01666 images/sec.
2021-03-19 21:47:40,207 - INFO - epoch:4  , valid step:30  , top1: 0.95000, top5: 1.00000, loss: 0.67374, lr: 0.000000, batch_cost: 0.15083 s, reader_cost: 0.11134 s, ips: 132.59739 images/sec.
2021-03-19 21:47:41,666 - INFO - epoch:4  , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.44438, lr: 0.000000, batch_cost: 0.14924 s, reader_cost: 0.11014 s, ips: 134.00967 images/sec.
2021-03-19 21:47:42,977 - INFO - epoch:4  , valid step:50  , top1: 0.90000, top5: 1.00000, loss: 0.82368, lr: 0.000000, batch_cost: 0.14481 s, reader_cost: 0.10575 s, ips: 138.11178 images/sec.
2021-03-19 21:47:42,978 - INFO - END epoch:4   valid top1: 0.82451, top5: 0.95294, loss: 1.04970,  batch_cost: 0.14481 s, reader_cost: 0.10575 s, batch_cost_sum: 5.93722 s, ips: 138.11178 images/sec.
2021-03-19 21:47:44,865 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:47:44,865 - INFO - The best top1 acc 0.82451, in epoch: 4
2021-03-19 21:47:46,869 - INFO - Already save model in ./output/ResNet50_vd/4
2021-03-19 21:47:47,244 - INFO - epoch:5  , train step:0   , top1: 0.96875, top5: 1.00000, loss: 0.84477, lr: 0.003201, batch_cost: 0.36916 s, reader_cost: 0.19488 s, ips: 86.68391 images/sec.
2021-03-19 21:47:50,268 - INFO - epoch:5  , train step:10  , top1: 0.84375, top5: 0.90625, loss: 1.26304, lr: 0.003132, batch_cost: 0.29721 s, reader_cost: 0.12326 s, ips: 107.66626 images/sec.
2021-03-19 21:47:53,353 - INFO - epoch:5  , train step:20  , top1: 0.84375, top5: 1.00000, loss: 0.95927, lr: 0.003060, batch_cost: 0.30747 s, reader_cost: 0.13344 s, ips: 104.07432 images/sec.
2021-03-19 21:47:56,409 - INFO - epoch:5  , train step:30  , top1: 0.93750, top5: 0.96875, loss: 0.74264, lr: 0.002985, batch_cost: 0.30658 s, reader_cost: 0.13281 s, ips: 104.37899 images/sec.
2021-03-19 21:47:56,409 - INFO - END epoch:5   train top1: 0.86996, top5: 0.95766, loss: 1.02753,  batch_cost: 0.30658 s, reader_cost: 0.13281 s, batch_cost_sum: 6.43808 s, ips: 104.37899 images/sec.
2021-03-19 21:47:56,600 - INFO - epoch:5  , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.45158, lr: 0.000000, batch_cost: 0.18305 s, reader_cost: 0.14308 s, ips: 109.25882 images/sec.
2021-03-19 21:47:58,034 - INFO - epoch:5  , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.59840, lr: 0.000000, batch_cost: 0.14734 s, reader_cost: 0.10716 s, ips: 135.73953 images/sec.
2021-03-19 21:47:59,525 - INFO - epoch:5  , valid step:20  , top1: 0.95000, top5: 1.00000, loss: 0.65759, lr: 0.000000, batch_cost: 0.14892 s, reader_cost: 0.10967 s, ips: 134.29842 images/sec.
2021-03-19 21:48:01,061 - INFO - epoch:5  , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.57949, lr: 0.000000, batch_cost: 0.15117 s, reader_cost: 0.11184 s, ips: 132.29804 images/sec.
2021-03-19 21:48:02,468 - INFO - epoch:5  , valid step:40  , top1: 0.95000, top5: 1.00000, loss: 0.63542, lr: 0.000000, batch_cost: 0.14778 s, reader_cost: 0.10850 s, ips: 135.33775 images/sec.
2021-03-19 21:48:03,840 - INFO - epoch:5  , valid step:50  , top1: 0.90000, top5: 1.00000, loss: 0.68157, lr: 0.000000, batch_cost: 0.14522 s, reader_cost: 0.10617 s, ips: 137.72555 images/sec.
2021-03-19 21:48:03,841 - INFO - END epoch:5   valid top1: 0.87353, top5: 0.97353, loss: 0.78142,  batch_cost: 0.14522 s, reader_cost: 0.10617 s, batch_cost_sum: 5.95387 s, ips: 137.72555 images/sec.
2021-03-19 21:48:05,870 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:48:05,870 - INFO - The best top1 acc 0.87353, in epoch: 5
2021-03-19 21:48:07,733 - INFO - Already save model in ./output/ResNet50_vd/5
2021-03-19 21:48:08,113 - INFO - epoch:6  , train step:0   , top1: 0.93750, top5: 0.96875, loss: 0.91812, lr: 0.002977, batch_cost: 0.37212 s, reader_cost: 0.19711 s, ips: 85.99307 images/sec.
2021-03-19 21:48:11,201 - INFO - epoch:6  , train step:10  , top1: 0.87500, top5: 1.00000, loss: 0.85722, lr: 0.002899, batch_cost: 0.29892 s, reader_cost: 0.12486 s, ips: 107.05166 images/sec.
2021-03-19 21:48:14,276 - INFO - epoch:6  , train step:20  , top1: 0.87500, top5: 0.93750, loss: 0.81820, lr: 0.002818, batch_cost: 0.30672 s, reader_cost: 0.13238 s, ips: 104.32836 images/sec.
2021-03-19 21:48:17,373 - INFO - epoch:6  , train step:30  , top1: 0.93750, top5: 0.96875, loss: 0.68859, lr: 0.002735, batch_cost: 0.30817 s, reader_cost: 0.13408 s, ips: 103.83744 images/sec.
2021-03-19 21:48:17,374 - INFO - END epoch:6   train top1: 0.90726, top5: 0.97984, loss: 0.73892,  batch_cost: 0.30817 s, reader_cost: 0.13408 s, batch_cost_sum: 6.47165 s, ips: 103.83744 images/sec.
2021-03-19 21:48:17,557 - INFO - epoch:6  , valid step:0   , top1: 0.85000, top5: 1.00000, loss: 0.44709, lr: 0.000000, batch_cost: 0.17846 s, reader_cost: 0.13977 s, ips: 112.07150 images/sec.
2021-03-19 21:48:18,956 - INFO - epoch:6  , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.48797, lr: 0.000000, batch_cost: 0.13087 s, reader_cost: 0.09208 s, ips: 152.82301 images/sec.
2021-03-19 21:48:20,319 - INFO - epoch:6  , valid step:20  , top1: 0.95000, top5: 1.00000, loss: 0.60090, lr: 0.000000, batch_cost: 0.13582 s, reader_cost: 0.09679 s, ips: 147.25652 images/sec.
2021-03-19 21:48:21,784 - INFO - epoch:6  , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.26776, lr: 0.000000, batch_cost: 0.14092 s, reader_cost: 0.10170 s, ips: 141.92385 images/sec.
2021-03-19 21:48:23,212 - INFO - epoch:6  , valid step:40  , top1: 0.95000, top5: 1.00000, loss: 0.30889, lr: 0.000000, batch_cost: 0.14152 s, reader_cost: 0.10230 s, ips: 141.31857 images/sec.
2021-03-19 21:48:24,568 - INFO - epoch:6  , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.37543, lr: 0.000000, batch_cost: 0.14007 s, reader_cost: 0.10095 s, ips: 142.78177 images/sec.
2021-03-19 21:48:24,569 - INFO - END epoch:6   valid top1: 0.89902, top5: 0.97843, loss: 0.62853,  batch_cost: 0.14007 s, reader_cost: 0.10095 s, batch_cost_sum: 5.74303 s, ips: 142.78177 images/sec.
2021-03-19 21:48:26,341 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:48:26,342 - INFO - The best top1 acc 0.89902, in epoch: 6
2021-03-19 21:48:28,165 - INFO - Already save model in ./output/ResNet50_vd/6
2021-03-19 21:48:28,556 - INFO - epoch:7  , train step:0   , top1: 0.96875, top5: 1.00000, loss: 0.37358, lr: 0.002726, batch_cost: 0.38404 s, reader_cost: 0.20170 s, ips: 83.32411 images/sec.
2021-03-19 21:48:31,660 - INFO - epoch:7  , train step:10  , top1: 0.90625, top5: 0.93750, loss: 0.65042, lr: 0.002641, batch_cost: 0.30155 s, reader_cost: 0.12718 s, ips: 106.11808 images/sec.
2021-03-19 21:48:34,780 - INFO - epoch:7  , train step:20  , top1: 0.93750, top5: 1.00000, loss: 0.53672, lr: 0.002553, batch_cost: 0.31105 s, reader_cost: 0.13654 s, ips: 102.87711 images/sec.
2021-03-19 21:48:38,007 - INFO - epoch:7  , train step:30  , top1: 0.93750, top5: 1.00000, loss: 0.46545, lr: 0.002463, batch_cost: 0.31656 s, reader_cost: 0.14224 s, ips: 101.08578 images/sec.
2021-03-19 21:48:38,007 - INFO - END epoch:7   train top1: 0.92540, top5: 0.97681, loss: 0.59688,  batch_cost: 0.31656 s, reader_cost: 0.14224 s, batch_cost_sum: 6.64782 s, ips: 101.08578 images/sec.
2021-03-19 21:48:38,210 - INFO - epoch:7  , valid step:0   , top1: 0.95000, top5: 1.00000, loss: 0.39521, lr: 0.000000, batch_cost: 0.19856 s, reader_cost: 0.15958 s, ips: 100.72292 images/sec.
2021-03-19 21:48:39,652 - INFO - epoch:7  , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.27560, lr: 0.000000, batch_cost: 0.14739 s, reader_cost: 0.10853 s, ips: 135.69715 images/sec.
2021-03-19 21:48:41,067 - INFO - epoch:7  , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.50669, lr: 0.000000, batch_cost: 0.14196 s, reader_cost: 0.10311 s, ips: 140.88954 images/sec.
2021-03-19 21:48:42,585 - INFO - epoch:7  , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.14713, lr: 0.000000, batch_cost: 0.14667 s, reader_cost: 0.10757 s, ips: 136.35660 images/sec.
2021-03-19 21:48:44,006 - INFO - epoch:7  , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.27111, lr: 0.000000, batch_cost: 0.14520 s, reader_cost: 0.10590 s, ips: 137.74543 images/sec.
2021-03-19 21:48:45,422 - INFO - epoch:7  , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.27559, lr: 0.000000, batch_cost: 0.14431 s, reader_cost: 0.10508 s, ips: 138.59060 images/sec.
2021-03-19 21:48:45,422 - INFO - END epoch:7   valid top1: 0.90784, top5: 0.98039, loss: 0.52839,  batch_cost: 0.14431 s, reader_cost: 0.10508 s, batch_cost_sum: 5.91671 s, ips: 138.59060 images/sec.
2021-03-19 21:48:47,254 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:48:47,255 - INFO - The best top1 acc 0.90784, in epoch: 7
2021-03-19 21:48:49,222 - INFO - Already save model in ./output/ResNet50_vd/7
2021-03-19 21:48:49,590 - INFO - epoch:8  , train step:0   , top1: 0.96875, top5: 1.00000, loss: 0.35822, lr: 0.002454, batch_cost: 0.35820 s, reader_cost: 0.18238 s, ips: 89.33626 images/sec.
2021-03-19 21:48:52,713 - INFO - epoch:8  , train step:10  , top1: 0.90625, top5: 1.00000, loss: 0.56702, lr: 0.002363, batch_cost: 0.29921 s, reader_cost: 0.12514 s, ips: 106.94955 images/sec.
2021-03-19 21:48:55,776 - INFO - epoch:8  , train step:20  , top1: 0.96875, top5: 1.00000, loss: 0.41615, lr: 0.002271, batch_cost: 0.30566 s, reader_cost: 0.13159 s, ips: 104.69034 images/sec.
2021-03-19 21:48:58,784 - INFO - epoch:8  , train step:30  , top1: 0.93750, top5: 0.96875, loss: 0.55075, lr: 0.002178, batch_cost: 0.30332 s, reader_cost: 0.12919 s, ips: 105.49942 images/sec.
2021-03-19 21:48:58,784 - INFO - END epoch:8   train top1: 0.93851, top5: 0.98891, loss: 0.47959,  batch_cost: 0.30332 s, reader_cost: 0.12919 s, batch_cost_sum: 6.36970 s, ips: 105.49942 images/sec.
2021-03-19 21:48:58,969 - INFO - epoch:8  , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.36128, lr: 0.000000, batch_cost: 0.18031 s, reader_cost: 0.14049 s, ips: 110.91905 images/sec.
2021-03-19 21:49:00,323 - INFO - epoch:8  , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.20838, lr: 0.000000, batch_cost: 0.12230 s, reader_cost: 0.08350 s, ips: 163.52796 images/sec.
2021-03-19 21:49:01,717 - INFO - epoch:8  , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.46617, lr: 0.000000, batch_cost: 0.13785 s, reader_cost: 0.09894 s, ips: 145.08222 images/sec.
2021-03-19 21:49:03,177 - INFO - epoch:8  , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.15463, lr: 0.000000, batch_cost: 0.14172 s, reader_cost: 0.10266 s, ips: 141.12661 images/sec.
2021-03-19 21:49:04,546 - INFO - epoch:8  , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.24205, lr: 0.000000, batch_cost: 0.14017 s, reader_cost: 0.10110 s, ips: 142.68147 images/sec.
2021-03-19 21:49:05,934 - INFO - epoch:8  , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.20755, lr: 0.000000, batch_cost: 0.13983 s, reader_cost: 0.10101 s, ips: 143.03059 images/sec.
2021-03-19 21:49:05,934 - INFO - END epoch:8   valid top1: 0.92255, top5: 0.98235, loss: 0.47242,  batch_cost: 0.13983 s, reader_cost: 0.10101 s, batch_cost_sum: 5.73304 s, ips: 143.03059 images/sec.
2021-03-19 21:49:08,020 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:49:08,020 - INFO - The best top1 acc 0.92255, in epoch: 8
2021-03-19 21:49:10,102 - INFO - Already save model in ./output/ResNet50_vd/8
2021-03-19 21:49:10,469 - INFO - epoch:9  , train step:0   , top1: 0.93750, top5: 1.00000, loss: 0.34969, lr: 0.002168, batch_cost: 0.35914 s, reader_cost: 0.18516 s, ips: 89.10259 images/sec.
2021-03-19 21:49:13,552 - INFO - epoch:9  , train step:10  , top1: 0.96875, top5: 0.96875, loss: 0.28479, lr: 0.002074, batch_cost: 0.31684 s, reader_cost: 0.14167 s, ips: 100.99661 images/sec.
2021-03-19 21:49:16,726 - INFO - epoch:9  , train step:20  , top1: 0.93750, top5: 1.00000, loss: 0.51710, lr: 0.001979, batch_cost: 0.31739 s, reader_cost: 0.14279 s, ips: 100.82123 images/sec.
2021-03-19 21:49:19,883 - INFO - epoch:9  , train step:30  , top1: 0.87500, top5: 0.96875, loss: 0.57297, lr: 0.001885, batch_cost: 0.31655 s, reader_cost: 0.14216 s, ips: 101.09061 images/sec.
2021-03-19 21:49:19,884 - INFO - END epoch:9   train top1: 0.94960, top5: 0.98891, loss: 0.40195,  batch_cost: 0.31655 s, reader_cost: 0.14216 s, batch_cost_sum: 6.64750 s, ips: 101.09061 images/sec.
2021-03-19 21:49:20,072 - INFO - epoch:9  , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.43471, lr: 0.000000, batch_cost: 0.18437 s, reader_cost: 0.14558 s, ips: 108.47553 images/sec.
2021-03-19 21:49:21,448 - INFO - epoch:9  , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.12762, lr: 0.000000, batch_cost: 0.12593 s, reader_cost: 0.08750 s, ips: 158.82011 images/sec.
2021-03-19 21:49:22,791 - INFO - epoch:9  , valid step:20  , top1: 0.95000, top5: 1.00000, loss: 0.37537, lr: 0.000000, batch_cost: 0.13349 s, reader_cost: 0.09468 s, ips: 149.82831 images/sec.
2021-03-19 21:49:24,271 - INFO - epoch:9  , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.19616, lr: 0.000000, batch_cost: 0.14043 s, reader_cost: 0.10143 s, ips: 142.41982 images/sec.
2021-03-19 21:49:25,702 - INFO - epoch:9  , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.20242, lr: 0.000000, batch_cost: 0.14128 s, reader_cost: 0.10245 s, ips: 141.55875 images/sec.
2021-03-19 21:49:27,157 - INFO - epoch:9  , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.17568, lr: 0.000000, batch_cost: 0.14230 s, reader_cost: 0.10351 s, ips: 140.54596 images/sec.
2021-03-19 21:49:27,157 - INFO - END epoch:9   valid top1: 0.92451, top5: 0.98235, loss: 0.43157,  batch_cost: 0.14230 s, reader_cost: 0.10351 s, batch_cost_sum: 5.83439 s, ips: 140.54596 images/sec.
2021-03-19 21:49:29,260 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:49:29,260 - INFO - The best top1 acc 0.92451, in epoch: 9
2021-03-19 21:49:31,370 - INFO - Already save model in ./output/ResNet50_vd/9
2021-03-19 21:49:31,756 - INFO - epoch:10 , train step:0   , top1: 0.96875, top5: 1.00000, loss: 0.21060, lr: 0.001875, batch_cost: 0.38142 s, reader_cost: 0.20029 s, ips: 83.89693 images/sec.
2021-03-19 21:49:34,826 - INFO - epoch:10 , train step:10  , top1: 0.96875, top5: 1.00000, loss: 0.31087, lr: 0.001780, batch_cost: 0.30873 s, reader_cost: 0.13442 s, ips: 103.64904 images/sec.
2021-03-19 21:49:37,951 - INFO - epoch:10 , train step:20  , top1: 0.96875, top5: 1.00000, loss: 0.32934, lr: 0.001685, batch_cost: 0.31210 s, reader_cost: 0.13826 s, ips: 102.53093 images/sec.
2021-03-19 21:49:41,031 - INFO - epoch:10 , train step:30  , top1: 0.96875, top5: 1.00000, loss: 0.31913, lr: 0.001591, batch_cost: 0.31016 s, reader_cost: 0.13628 s, ips: 103.17205 images/sec.
2021-03-19 21:49:41,031 - INFO - END epoch:10  train top1: 0.95565, top5: 0.99194, loss: 0.34804,  batch_cost: 0.31016 s, reader_cost: 0.13628 s, batch_cost_sum: 6.51339 s, ips: 103.17205 images/sec.
2021-03-19 21:49:41,228 - INFO - epoch:10 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.37112, lr: 0.000000, batch_cost: 0.19192 s, reader_cost: 0.15291 s, ips: 104.20981 images/sec.
2021-03-19 21:49:42,641 - INFO - epoch:10 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.14179, lr: 0.000000, batch_cost: 0.13054 s, reader_cost: 0.09150 s, ips: 153.21127 images/sec.
2021-03-19 21:49:44,077 - INFO - epoch:10 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.30681, lr: 0.000000, batch_cost: 0.14246 s, reader_cost: 0.10307 s, ips: 140.39520 images/sec.
2021-03-19 21:49:45,645 - INFO - epoch:10 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.11970, lr: 0.000000, batch_cost: 0.14927 s, reader_cost: 0.11003 s, ips: 133.98100 images/sec.
2021-03-19 21:49:47,100 - INFO - epoch:10 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.19141, lr: 0.000000, batch_cost: 0.14804 s, reader_cost: 0.10862 s, ips: 135.10094 images/sec.
2021-03-19 21:49:48,440 - INFO - epoch:10 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.23935, lr: 0.000000, batch_cost: 0.14460 s, reader_cost: 0.10522 s, ips: 138.30923 images/sec.
2021-03-19 21:49:48,441 - INFO - END epoch:10  valid top1: 0.92451, top5: 0.98431, loss: 0.42443,  batch_cost: 0.14460 s, reader_cost: 0.10522 s, batch_cost_sum: 5.92874 s, ips: 138.30923 images/sec.
2021-03-19 21:49:48,441 - INFO - The best top1 acc 0.92451, in epoch: 9
2021-03-19 21:49:50,421 - INFO - Already save model in ./output/ResNet50_vd/10
2021-03-19 21:49:50,793 - INFO - epoch:11 , train step:0   , top1: 1.00000, top5: 1.00000, loss: 0.25724, lr: 0.001582, batch_cost: 0.36469 s, reader_cost: 0.19095 s, ips: 87.74482 images/sec.
2021-03-19 21:49:53,932 - INFO - epoch:11 , train step:10  , top1: 0.93750, top5: 0.96875, loss: 0.44793, lr: 0.001488, batch_cost: 0.29645 s, reader_cost: 0.12254 s, ips: 107.94508 images/sec.
2021-03-19 21:49:57,053 - INFO - epoch:11 , train step:20  , top1: 0.90625, top5: 1.00000, loss: 0.36811, lr: 0.001396, batch_cost: 0.31068 s, reader_cost: 0.13663 s, ips: 103.00040 images/sec.
2021-03-19 21:50:00,100 - INFO - epoch:11 , train step:30  , top1: 1.00000, top5: 1.00000, loss: 0.29016, lr: 0.001305, batch_cost: 0.30782 s, reader_cost: 0.13392 s, ips: 103.95556 images/sec.
2021-03-19 21:50:00,100 - INFO - END epoch:11  train top1: 0.95766, top5: 0.98992, loss: 0.33080,  batch_cost: 0.30782 s, reader_cost: 0.13392 s, batch_cost_sum: 6.46430 s, ips: 103.95556 images/sec.
2021-03-19 21:50:00,293 - INFO - epoch:11 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.43915, lr: 0.000000, batch_cost: 0.18874 s, reader_cost: 0.14988 s, ips: 105.96694 images/sec.
2021-03-19 21:50:01,729 - INFO - epoch:11 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.12890, lr: 0.000000, batch_cost: 0.14123 s, reader_cost: 0.10252 s, ips: 141.60832 images/sec.
2021-03-19 21:50:03,194 - INFO - epoch:11 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.31965, lr: 0.000000, batch_cost: 0.14602 s, reader_cost: 0.10690 s, ips: 136.96522 images/sec.
2021-03-19 21:50:04,739 - INFO - epoch:11 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.12152, lr: 0.000000, batch_cost: 0.15005 s, reader_cost: 0.11073 s, ips: 133.29166 images/sec.
2021-03-19 21:50:06,185 - INFO - epoch:11 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.20811, lr: 0.000000, batch_cost: 0.14830 s, reader_cost: 0.10889 s, ips: 134.86484 images/sec.
2021-03-19 21:50:07,609 - INFO - epoch:11 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.12672, lr: 0.000000, batch_cost: 0.14686 s, reader_cost: 0.10764 s, ips: 136.18691 images/sec.
2021-03-19 21:50:07,610 - INFO - END epoch:11  valid top1: 0.91667, top5: 0.98431, loss: 0.40027,  batch_cost: 0.14686 s, reader_cost: 0.10764 s, batch_cost_sum: 6.02114 s, ips: 136.18691 images/sec.
2021-03-19 21:50:07,610 - INFO - The best top1 acc 0.92451, in epoch: 9
2021-03-19 21:50:09,617 - INFO - Already save model in ./output/ResNet50_vd/11
2021-03-19 21:50:09,968 - INFO - epoch:12 , train step:0   , top1: 0.93750, top5: 1.00000, loss: 0.35859, lr: 0.001296, batch_cost: 0.34181 s, reader_cost: 0.16755 s, ips: 93.61894 images/sec.
2021-03-19 21:50:13,132 - INFO - epoch:12 , train step:10  , top1: 0.96875, top5: 1.00000, loss: 0.28512, lr: 0.001206, batch_cost: 0.30643 s, reader_cost: 0.13263 s, ips: 104.42928 images/sec.
2021-03-19 21:50:16,164 - INFO - epoch:12 , train step:20  , top1: 1.00000, top5: 1.00000, loss: 0.21688, lr: 0.001118, batch_cost: 0.30357 s, reader_cost: 0.12970 s, ips: 105.41336 images/sec.
2021-03-19 21:50:19,290 - INFO - epoch:12 , train step:30  , top1: 0.93750, top5: 1.00000, loss: 0.31865, lr: 0.001032, batch_cost: 0.30787 s, reader_cost: 0.13385 s, ips: 103.94088 images/sec.
2021-03-19 21:50:19,291 - INFO - END epoch:12  train top1: 0.96169, top5: 0.99093, loss: 0.31550,  batch_cost: 0.30787 s, reader_cost: 0.13385 s, batch_cost_sum: 6.46521 s, ips: 103.94088 images/sec.
2021-03-19 21:50:19,489 - INFO - epoch:12 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.43053, lr: 0.000000, batch_cost: 0.19355 s, reader_cost: 0.15431 s, ips: 103.33127 images/sec.
2021-03-19 21:50:20,844 - INFO - epoch:12 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.10996, lr: 0.000000, batch_cost: 0.13643 s, reader_cost: 0.09761 s, ips: 146.59299 images/sec.
2021-03-19 21:50:22,242 - INFO - epoch:12 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.25068, lr: 0.000000, batch_cost: 0.13944 s, reader_cost: 0.10020 s, ips: 143.42913 images/sec.
2021-03-19 21:50:23,787 - INFO - epoch:12 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.13892, lr: 0.000000, batch_cost: 0.14662 s, reader_cost: 0.10723 s, ips: 136.40438 images/sec.
2021-03-19 21:50:25,299 - INFO - epoch:12 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.24195, lr: 0.000000, batch_cost: 0.14811 s, reader_cost: 0.10865 s, ips: 135.03226 images/sec.
2021-03-19 21:50:26,598 - INFO - epoch:12 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.14134, lr: 0.000000, batch_cost: 0.14367 s, reader_cost: 0.10436 s, ips: 139.20446 images/sec.
2021-03-19 21:50:26,599 - INFO - END epoch:12  valid top1: 0.92549, top5: 0.98627, loss: 0.37469,  batch_cost: 0.14367 s, reader_cost: 0.10436 s, batch_cost_sum: 5.89062 s, ips: 139.20446 images/sec.
2021-03-19 21:50:28,543 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:50:28,543 - INFO - The best top1 acc 0.92549, in epoch: 12
2021-03-19 21:50:30,503 - INFO - Already save model in ./output/ResNet50_vd/12
2021-03-19 21:50:30,856 - INFO - epoch:13 , train step:0   , top1: 1.00000, top5: 1.00000, loss: 0.13774, lr: 0.001024, batch_cost: 0.34785 s, reader_cost: 0.16385 s, ips: 91.99359 images/sec.
2021-03-19 21:50:34,071 - INFO - epoch:13 , train step:10  , top1: 1.00000, top5: 1.00000, loss: 0.15618, lr: 0.000940, batch_cost: 0.31819 s, reader_cost: 0.14460 s, ips: 100.56972 images/sec.
2021-03-19 21:50:37,221 - INFO - epoch:13 , train step:20  , top1: 1.00000, top5: 1.00000, loss: 0.17202, lr: 0.000859, batch_cost: 0.31527 s, reader_cost: 0.14124 s, ips: 101.50070 images/sec.
2021-03-19 21:50:40,350 - INFO - epoch:13 , train step:30  , top1: 1.00000, top5: 1.00000, loss: 0.17678, lr: 0.000781, batch_cost: 0.31416 s, reader_cost: 0.14018 s, ips: 101.85793 images/sec.
2021-03-19 21:50:40,350 - INFO - END epoch:13  train top1: 0.96169, top5: 0.98185, loss: 0.28802,  batch_cost: 0.31416 s, reader_cost: 0.14018 s, batch_cost_sum: 6.59742 s, ips: 101.85793 images/sec.
2021-03-19 21:50:40,539 - INFO - epoch:13 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.40501, lr: 0.000000, batch_cost: 0.18358 s, reader_cost: 0.14497 s, ips: 108.94650 images/sec.
2021-03-19 21:50:41,905 - INFO - epoch:13 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.10247, lr: 0.000000, batch_cost: 0.12596 s, reader_cost: 0.08683 s, ips: 158.78193 images/sec.
2021-03-19 21:50:43,269 - INFO - epoch:13 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.26263, lr: 0.000000, batch_cost: 0.13541 s, reader_cost: 0.09595 s, ips: 147.69416 images/sec.
2021-03-19 21:50:44,743 - INFO - epoch:13 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.11593, lr: 0.000000, batch_cost: 0.14112 s, reader_cost: 0.10143 s, ips: 141.72583 images/sec.
2021-03-19 21:50:46,129 - INFO - epoch:13 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.20738, lr: 0.000000, batch_cost: 0.14030 s, reader_cost: 0.10076 s, ips: 142.54758 images/sec.
2021-03-19 21:50:47,524 - INFO - epoch:13 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.15726, lr: 0.000000, batch_cost: 0.14012 s, reader_cost: 0.10094 s, ips: 142.73362 images/sec.
2021-03-19 21:50:47,525 - INFO - END epoch:13  valid top1: 0.92941, top5: 0.98333, loss: 0.36815,  batch_cost: 0.14012 s, reader_cost: 0.10094 s, batch_cost_sum: 5.74497 s, ips: 142.73362 images/sec.
2021-03-19 21:50:49,600 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:50:49,601 - INFO - The best top1 acc 0.92941, in epoch: 13
2021-03-19 21:50:51,717 - INFO - Already save model in ./output/ResNet50_vd/13
2021-03-19 21:50:52,082 - INFO - epoch:14 , train step:0   , top1: 0.93750, top5: 1.00000, loss: 0.26167, lr: 0.000773, batch_cost: 0.35672 s, reader_cost: 0.18247 s, ips: 89.70640 images/sec.
2021-03-19 21:50:55,070 - INFO - epoch:14 , train step:10  , top1: 0.96875, top5: 0.96875, loss: 0.30288, lr: 0.000697, batch_cost: 0.29916 s, reader_cost: 0.12521 s, ips: 106.96574 images/sec.
2021-03-19 21:50:58,125 - INFO - epoch:14 , train step:20  , top1: 0.93750, top5: 0.96875, loss: 0.46578, lr: 0.000625, batch_cost: 0.30484 s, reader_cost: 0.13093 s, ips: 104.97293 images/sec.
2021-03-19 21:51:01,162 - INFO - epoch:14 , train step:30  , top1: 1.00000, top5: 1.00000, loss: 0.17455, lr: 0.000556, batch_cost: 0.30430 s, reader_cost: 0.13044 s, ips: 105.15814 images/sec.
2021-03-19 21:51:01,162 - INFO - END epoch:14  train top1: 0.97177, top5: 0.98992, loss: 0.27791,  batch_cost: 0.30430 s, reader_cost: 0.13044 s, batch_cost_sum: 6.39038 s, ips: 105.15814 images/sec.
2021-03-19 21:51:01,344 - INFO - epoch:14 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.39800, lr: 0.000000, batch_cost: 0.17749 s, reader_cost: 0.13750 s, ips: 112.67938 images/sec.
2021-03-19 21:51:02,783 - INFO - epoch:14 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.11290, lr: 0.000000, batch_cost: 0.14075 s, reader_cost: 0.10164 s, ips: 142.09141 images/sec.
2021-03-19 21:51:04,246 - INFO - epoch:14 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.24830, lr: 0.000000, batch_cost: 0.14580 s, reader_cost: 0.10599 s, ips: 137.17286 images/sec.
2021-03-19 21:51:05,766 - INFO - epoch:14 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.12545, lr: 0.000000, batch_cost: 0.14877 s, reader_cost: 0.10897 s, ips: 134.43639 images/sec.
2021-03-19 21:51:07,144 - INFO - epoch:14 , valid step:40  , top1: 0.95000, top5: 1.00000, loss: 0.23504, lr: 0.000000, batch_cost: 0.14523 s, reader_cost: 0.10539 s, ips: 137.71655 images/sec.
2021-03-19 21:51:08,546 - INFO - epoch:14 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.15859, lr: 0.000000, batch_cost: 0.14400 s, reader_cost: 0.10442 s, ips: 138.89147 images/sec.
2021-03-19 21:51:08,547 - INFO - END epoch:14  valid top1: 0.93137, top5: 0.98235, loss: 0.36797,  batch_cost: 0.14400 s, reader_cost: 0.10442 s, batch_cost_sum: 5.90389 s, ips: 138.89147 images/sec.
2021-03-19 21:51:10,573 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:51:10,573 - INFO - The best top1 acc 0.93137, in epoch: 14
2021-03-19 21:51:12,736 - INFO - Already save model in ./output/ResNet50_vd/14
2021-03-19 21:51:13,096 - INFO - epoch:15 , train step:0   , top1: 1.00000, top5: 1.00000, loss: 0.17039, lr: 0.000549, batch_cost: 0.35320 s, reader_cost: 0.17921 s, ips: 90.60036 images/sec.
2021-03-19 21:51:16,140 - INFO - epoch:15 , train step:10  , top1: 0.93750, top5: 0.96875, loss: 0.30987, lr: 0.000484, batch_cost: 0.29408 s, reader_cost: 0.12036 s, ips: 108.81401 images/sec.
2021-03-19 21:51:19,205 - INFO - epoch:15 , train step:20  , top1: 0.93750, top5: 1.00000, loss: 0.29858, lr: 0.000422, batch_cost: 0.30536 s, reader_cost: 0.13148 s, ips: 104.79484 images/sec.
2021-03-19 21:51:22,220 - INFO - epoch:15 , train step:30  , top1: 0.96875, top5: 0.96875, loss: 0.32843, lr: 0.000364, batch_cost: 0.30350 s, reader_cost: 0.12981 s, ips: 105.43597 images/sec.
2021-03-19 21:51:22,220 - INFO - END epoch:15  train top1: 0.97077, top5: 0.99194, loss: 0.21899,  batch_cost: 0.30350 s, reader_cost: 0.12981 s, batch_cost_sum: 6.37354 s, ips: 105.43597 images/sec.
2021-03-19 21:51:22,407 - INFO - epoch:15 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.41520, lr: 0.000000, batch_cost: 0.18218 s, reader_cost: 0.14334 s, ips: 109.78100 images/sec.
2021-03-19 21:51:23,825 - INFO - epoch:15 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.10603, lr: 0.000000, batch_cost: 0.14408 s, reader_cost: 0.10617 s, ips: 138.81253 images/sec.
2021-03-19 21:51:25,313 - INFO - epoch:15 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.25371, lr: 0.000000, batch_cost: 0.14834 s, reader_cost: 0.10990 s, ips: 134.82484 images/sec.
2021-03-19 21:51:26,894 - INFO - epoch:15 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.12004, lr: 0.000000, batch_cost: 0.15303 s, reader_cost: 0.11412 s, ips: 130.69252 images/sec.
2021-03-19 21:51:28,345 - INFO - epoch:15 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.16556, lr: 0.000000, batch_cost: 0.15045 s, reader_cost: 0.11148 s, ips: 132.93678 images/sec.
2021-03-19 21:51:29,739 - INFO - epoch:15 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.11484, lr: 0.000000, batch_cost: 0.14776 s, reader_cost: 0.10880 s, ips: 135.35529 images/sec.
2021-03-19 21:51:29,739 - INFO - END epoch:15  valid top1: 0.93235, top5: 0.98627, loss: 0.35716,  batch_cost: 0.14776 s, reader_cost: 0.10880 s, batch_cost_sum: 6.05813 s, ips: 135.35529 images/sec.
2021-03-19 21:51:31,823 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:51:31,824 - INFO - The best top1 acc 0.93235, in epoch: 15
2021-03-19 21:51:33,893 - INFO - Already save model in ./output/ResNet50_vd/15
2021-03-19 21:51:34,268 - INFO - epoch:16 , train step:0   , top1: 1.00000, top5: 1.00000, loss: 0.11155, lr: 0.000358, batch_cost: 0.36709 s, reader_cost: 0.18812 s, ips: 87.17254 images/sec.
2021-03-19 21:51:37,337 - INFO - epoch:16 , train step:10  , top1: 0.96875, top5: 1.00000, loss: 0.32349, lr: 0.000304, batch_cost: 0.29964 s, reader_cost: 0.12569 s, ips: 106.79399 images/sec.
2021-03-19 21:51:40,387 - INFO - epoch:16 , train step:20  , top1: 0.87500, top5: 1.00000, loss: 0.42390, lr: 0.000254, batch_cost: 0.30459 s, reader_cost: 0.13091 s, ips: 105.06022 images/sec.
2021-03-19 21:51:43,468 - INFO - epoch:16 , train step:30  , top1: 0.96875, top5: 0.96875, loss: 0.33745, lr: 0.000209, batch_cost: 0.30625 s, reader_cost: 0.13260 s, ips: 104.48846 images/sec.
2021-03-19 21:51:43,469 - INFO - END epoch:16  train top1: 0.96472, top5: 0.98891, loss: 0.25529,  batch_cost: 0.30625 s, reader_cost: 0.13260 s, batch_cost_sum: 6.43133 s, ips: 104.48846 images/sec.
2021-03-19 21:51:43,651 - INFO - epoch:16 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.39771, lr: 0.000000, batch_cost: 0.17783 s, reader_cost: 0.13876 s, ips: 112.46441 images/sec.
2021-03-19 21:51:44,987 - INFO - epoch:16 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.10175, lr: 0.000000, batch_cost: 0.12440 s, reader_cost: 0.08564 s, ips: 160.77245 images/sec.
2021-03-19 21:51:46,448 - INFO - epoch:16 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.20605, lr: 0.000000, batch_cost: 0.14410 s, reader_cost: 0.10520 s, ips: 138.78990 images/sec.
2021-03-19 21:51:48,033 - INFO - epoch:16 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.11345, lr: 0.000000, batch_cost: 0.15093 s, reader_cost: 0.11201 s, ips: 132.50822 images/sec.
2021-03-19 21:51:49,532 - INFO - epoch:16 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.17127, lr: 0.000000, batch_cost: 0.15060 s, reader_cost: 0.11149 s, ips: 132.80006 images/sec.
2021-03-19 21:51:50,945 - INFO - epoch:16 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.14028, lr: 0.000000, batch_cost: 0.14834 s, reader_cost: 0.10927 s, ips: 134.82339 images/sec.
2021-03-19 21:51:50,946 - INFO - END epoch:16  valid top1: 0.93333, top5: 0.98431, loss: 0.35523,  batch_cost: 0.14834 s, reader_cost: 0.10927 s, batch_cost_sum: 6.08203 s, ips: 134.82339 images/sec.
2021-03-19 21:51:52,911 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:51:52,911 - INFO - The best top1 acc 0.93333, in epoch: 16
2021-03-19 21:51:54,868 - INFO - Already save model in ./output/ResNet50_vd/16
2021-03-19 21:51:55,227 - INFO - epoch:17 , train step:0   , top1: 0.96875, top5: 1.00000, loss: 0.28023, lr: 0.000204, batch_cost: 0.35225 s, reader_cost: 0.17879 s, ips: 90.84338 images/sec.
2021-03-19 21:51:58,296 - INFO - epoch:17 , train step:10  , top1: 0.93750, top5: 1.00000, loss: 0.30267, lr: 0.000163, batch_cost: 0.30880 s, reader_cost: 0.13486 s, ips: 103.62815 images/sec.
2021-03-19 21:52:01,415 - INFO - epoch:17 , train step:20  , top1: 0.90625, top5: 0.93750, loss: 0.45526, lr: 0.000127, batch_cost: 0.31161 s, reader_cost: 0.13693 s, ips: 102.69132 images/sec.
2021-03-19 21:52:04,436 - INFO - epoch:17 , train step:30  , top1: 0.96875, top5: 0.96875, loss: 0.24771, lr: 0.000095, batch_cost: 0.30708 s, reader_cost: 0.13270 s, ips: 104.20653 images/sec.
2021-03-19 21:52:04,437 - INFO - END epoch:17  train top1: 0.97177, top5: 0.99194, loss: 0.23533,  batch_cost: 0.30708 s, reader_cost: 0.13270 s, batch_cost_sum: 6.44873 s, ips: 104.20653 images/sec.
2021-03-19 21:52:04,632 - INFO - epoch:17 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.37886, lr: 0.000000, batch_cost: 0.19078 s, reader_cost: 0.15144 s, ips: 104.83139 images/sec.
2021-03-19 21:52:06,004 - INFO - epoch:17 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.10877, lr: 0.000000, batch_cost: 0.13910 s, reader_cost: 0.10107 s, ips: 143.78162 images/sec.
2021-03-19 21:52:07,434 - INFO - epoch:17 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.23731, lr: 0.000000, batch_cost: 0.14261 s, reader_cost: 0.10365 s, ips: 140.24067 images/sec.
2021-03-19 21:52:08,983 - INFO - epoch:17 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.10705, lr: 0.000000, batch_cost: 0.14848 s, reader_cost: 0.10931 s, ips: 134.69705 images/sec.
2021-03-19 21:52:10,481 - INFO - epoch:17 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.17107, lr: 0.000000, batch_cost: 0.14890 s, reader_cost: 0.10954 s, ips: 134.31480 images/sec.
2021-03-19 21:52:11,864 - INFO - epoch:17 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.12958, lr: 0.000000, batch_cost: 0.14632 s, reader_cost: 0.10708 s, ips: 136.68616 images/sec.
2021-03-19 21:52:11,865 - INFO - END epoch:17  valid top1: 0.93333, top5: 0.98431, loss: 0.35539,  batch_cost: 0.14632 s, reader_cost: 0.10708 s, batch_cost_sum: 5.99914 s, ips: 136.68616 images/sec.
2021-03-19 21:52:13,977 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 21:52:13,978 - INFO - The best top1 acc 0.93333, in epoch: 17
2021-03-19 21:52:16,123 - INFO - Already save model in ./output/ResNet50_vd/17
2021-03-19 21:52:16,505 - INFO - epoch:18 , train step:0   , top1: 0.96875, top5: 1.00000, loss: 0.28804, lr: 0.000092, batch_cost: 0.37564 s, reader_cost: 0.19757 s, ips: 85.18905 images/sec.
2021-03-19 21:52:19,586 - INFO - epoch:18 , train step:10  , top1: 0.96875, top5: 0.96875, loss: 0.27210, lr: 0.000065, batch_cost: 0.32218 s, reader_cost: 0.14830 s, ips: 99.32306 images/sec.
2021-03-19 21:52:22,660 - INFO - epoch:18 , train step:20  , top1: 1.00000, top5: 1.00000, loss: 0.14587, lr: 0.000042, batch_cost: 0.30874 s, reader_cost: 0.13475 s, ips: 103.64586 images/sec.
2021-03-19 21:52:25,704 - INFO - epoch:18 , train step:30  , top1: 1.00000, top5: 1.00000, loss: 0.12849, lr: 0.000025, batch_cost: 0.30663 s, reader_cost: 0.13256 s, ips: 104.35895 images/sec.
2021-03-19 21:52:25,705 - INFO - END epoch:18  train top1: 0.97177, top5: 0.99194, loss: 0.24449,  batch_cost: 0.30663 s, reader_cost: 0.13256 s, batch_cost_sum: 6.43931 s, ips: 104.35895 images/sec.
2021-03-19 21:52:25,902 - INFO - epoch:18 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.40827, lr: 0.000000, batch_cost: 0.19193 s, reader_cost: 0.14949 s, ips: 104.20320 images/sec.
2021-03-19 21:52:27,287 - INFO - epoch:18 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.11159, lr: 0.000000, batch_cost: 0.14173 s, reader_cost: 0.10304 s, ips: 141.11830 images/sec.
2021-03-19 21:52:28,733 - INFO - epoch:18 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.23260, lr: 0.000000, batch_cost: 0.14430 s, reader_cost: 0.10518 s, ips: 138.59961 images/sec.
2021-03-19 21:52:30,286 - INFO - epoch:18 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.11446, lr: 0.000000, batch_cost: 0.14951 s, reader_cost: 0.11029 s, ips: 133.77160 images/sec.
2021-03-19 21:52:31,656 - INFO - epoch:18 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.16034, lr: 0.000000, batch_cost: 0.14549 s, reader_cost: 0.10632 s, ips: 137.46875 images/sec.
2021-03-19 21:52:33,035 - INFO - epoch:18 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.12766, lr: 0.000000, batch_cost: 0.14365 s, reader_cost: 0.10474 s, ips: 139.22845 images/sec.
2021-03-19 21:52:33,036 - INFO - END epoch:18  valid top1: 0.93235, top5: 0.98431, loss: 0.35442,  batch_cost: 0.14365 s, reader_cost: 0.10474 s, batch_cost_sum: 5.88960 s, ips: 139.22845 images/sec.
2021-03-19 21:52:33,036 - INFO - The best top1 acc 0.93333, in epoch: 17
2021-03-19 21:52:35,035 - INFO - Already save model in ./output/ResNet50_vd/18
2021-03-19 21:52:35,388 - INFO - epoch:19 , train step:0   , top1: 0.96875, top5: 1.00000, loss: 0.22398, lr: 0.000023, batch_cost: 0.34638 s, reader_cost: 0.16384 s, ips: 92.38453 images/sec.
2021-03-19 21:52:38,466 - INFO - epoch:19 , train step:10  , top1: 0.96875, top5: 0.96875, loss: 0.32986, lr: 0.000011, batch_cost: 0.29632 s, reader_cost: 0.12224 s, ips: 107.99016 images/sec.
2021-03-19 21:52:41,560 - INFO - epoch:19 , train step:20  , top1: 0.93750, top5: 0.96875, loss: 0.34714, lr: 0.000003, batch_cost: 0.30814 s, reader_cost: 0.13376 s, ips: 103.84876 images/sec.
2021-03-19 21:52:44,647 - INFO - epoch:19 , train step:30  , top1: 0.96875, top5: 0.96875, loss: 0.39851, lr: 0.000000, batch_cost: 0.30841 s, reader_cost: 0.13397 s, ips: 103.75772 images/sec.
2021-03-19 21:52:44,647 - INFO - END epoch:19  train top1: 0.97782, top5: 0.98891, loss: 0.22878,  batch_cost: 0.30841 s, reader_cost: 0.13397 s, batch_cost_sum: 6.47663 s, ips: 103.75772 images/sec.
2021-03-19 21:52:44,848 - INFO - epoch:19 , valid step:0   , top1: 0.90000, top5: 1.00000, loss: 0.36925, lr: 0.000000, batch_cost: 0.19662 s, reader_cost: 0.15751 s, ips: 101.72140 images/sec.
2021-03-19 21:52:46,267 - INFO - epoch:19 , valid step:10  , top1: 1.00000, top5: 1.00000, loss: 0.10133, lr: 0.000000, batch_cost: 0.13787 s, reader_cost: 0.09878 s, ips: 145.06838 images/sec.
2021-03-19 21:52:47,660 - INFO - epoch:19 , valid step:20  , top1: 1.00000, top5: 1.00000, loss: 0.21907, lr: 0.000000, batch_cost: 0.13919 s, reader_cost: 0.10004 s, ips: 143.68920 images/sec.
2021-03-19 21:52:49,160 - INFO - epoch:19 , valid step:30  , top1: 1.00000, top5: 1.00000, loss: 0.09779, lr: 0.000000, batch_cost: 0.14436 s, reader_cost: 0.10519 s, ips: 138.54705 images/sec.
2021-03-19 21:52:50,598 - INFO - epoch:19 , valid step:40  , top1: 1.00000, top5: 1.00000, loss: 0.17780, lr: 0.000000, batch_cost: 0.14416 s, reader_cost: 0.10523 s, ips: 138.73476 images/sec.
2021-03-19 21:52:51,961 - INFO - epoch:19 , valid step:50  , top1: 1.00000, top5: 1.00000, loss: 0.13044, lr: 0.000000, batch_cost: 0.14224 s, reader_cost: 0.10338 s, ips: 140.60280 images/sec.
2021-03-19 21:52:51,962 - INFO - END epoch:19  valid top1: 0.93235, top5: 0.98431, loss: 0.35172,  batch_cost: 0.14224 s, reader_cost: 0.10338 s, batch_cost_sum: 5.83203 s, ips: 140.60280 images/sec.
2021-03-19 21:52:51,962 - INFO - The best top1 acc 0.93333, in epoch: 17
2021-03-19 21:52:53,779 - INFO - Already save model in ./output/ResNet50_vd/19
```





