
```bash
# Train ResNet50_vd
python3 tools/train.py -c ./configs/quick_start/ResNet50_vd.yaml
# If you want to train on cpu device, the command is as follows.
python3 tools/train.py -c ./configs/quick_start/ResNet50_vd.yaml -o use_gpu=False
```


日志
```bash
(py37_paddle2) ➜  PaddleClas git:(zxdev_release_2.0) ✗ python3 tools/train.py -c ./configs/quick_start/ResNet50_vd.yaml
2021-03-19 20:19:35,686 - INFO - 
===========================================================
==        PaddleClas is powered by PaddlePaddle !        ==
===========================================================
==                                                       ==
==   For more info please go to the following website.   ==
==                                                       ==
==       https://github.com/PaddlePaddle/PaddleClas      ==
===========================================================

2021-03-19 20:19:35,686 - INFO - ARCHITECTURE : 
2021-03-19 20:19:35,687 - INFO -     name : ResNet50_vd
2021-03-19 20:19:35,687 - INFO - ------------------------------------------------------------
2021-03-19 20:19:35,687 - INFO - LEARNING_RATE : 
2021-03-19 20:19:35,687 - INFO -     function : Cosine
2021-03-19 20:19:35,687 - INFO -     params : 
2021-03-19 20:19:35,687 - INFO -         lr : 0.0125
2021-03-19 20:19:35,687 - INFO - ------------------------------------------------------------
2021-03-19 20:19:35,687 - INFO - OPTIMIZER : 
2021-03-19 20:19:35,687 - INFO -     function : Momentum
2021-03-19 20:19:35,687 - INFO -     params : 
2021-03-19 20:19:35,687 - INFO -         momentum : 0.9
2021-03-19 20:19:35,687 - INFO -     regularizer : 
2021-03-19 20:19:35,687 - INFO -         factor : 1e-05
2021-03-19 20:19:35,687 - INFO -         function : L2
2021-03-19 20:19:35,687 - INFO - ------------------------------------------------------------
2021-03-19 20:19:35,687 - INFO - TRAIN : 
2021-03-19 20:19:35,687 - INFO -     batch_size : 32
2021-03-19 20:19:35,687 - INFO -     data_dir : ./dataset/flowers102/
2021-03-19 20:19:35,687 - INFO -     file_list : ./dataset/flowers102/train_list.txt
2021-03-19 20:19:35,687 - INFO -     num_workers : 0
2021-03-19 20:19:35,687 - INFO -     shuffle_seed : 0
2021-03-19 20:19:35,688 - INFO -     transforms : 
2021-03-19 20:19:35,688 - INFO -         DecodeImage : 
2021-03-19 20:19:35,688 - INFO -             channel_first : False
2021-03-19 20:19:35,688 - INFO -             to_np : False
2021-03-19 20:19:35,688 - INFO -             to_rgb : True
2021-03-19 20:19:35,688 - INFO -         RandCropImage : 
2021-03-19 20:19:35,688 - INFO -             size : 224
2021-03-19 20:19:35,688 - INFO -         RandFlipImage : 
2021-03-19 20:19:35,688 - INFO -             flip_code : 1
2021-03-19 20:19:35,688 - INFO -         NormalizeImage : 
2021-03-19 20:19:35,688 - INFO -             mean : [0.485, 0.456, 0.406]
2021-03-19 20:19:35,688 - INFO -             order : 
2021-03-19 20:19:35,688 - INFO -             scale : 1./255.
2021-03-19 20:19:35,688 - INFO -             std : [0.229, 0.224, 0.225]
2021-03-19 20:19:35,688 - INFO -         ToCHWImage : None
2021-03-19 20:19:35,688 - INFO - ------------------------------------------------------------
2021-03-19 20:19:35,688 - INFO - VALID : 
2021-03-19 20:19:35,688 - INFO -     batch_size : 20
2021-03-19 20:19:35,688 - INFO -     data_dir : ./dataset/flowers102/
2021-03-19 20:19:35,688 - INFO -     file_list : ./dataset/flowers102/val_list.txt
2021-03-19 20:19:35,688 - INFO -     num_workers : 0
2021-03-19 20:19:35,688 - INFO -     shuffle_seed : 0
2021-03-19 20:19:35,689 - INFO -     transforms : 
2021-03-19 20:19:35,689 - INFO -         DecodeImage : 
2021-03-19 20:19:35,689 - INFO -             channel_first : False
2021-03-19 20:19:35,689 - INFO -             to_np : False
2021-03-19 20:19:35,689 - INFO -             to_rgb : True
2021-03-19 20:19:35,689 - INFO -         ResizeImage : 
2021-03-19 20:19:35,689 - INFO -             resize_short : 256
2021-03-19 20:19:35,689 - INFO -         CropImage : 
2021-03-19 20:19:35,689 - INFO -             size : 224
2021-03-19 20:19:35,689 - INFO -         NormalizeImage : 
2021-03-19 20:19:35,689 - INFO -             mean : [0.485, 0.456, 0.406]
2021-03-19 20:19:35,689 - INFO -             order : 
2021-03-19 20:19:35,689 - INFO -             scale : 1.0/255.0
2021-03-19 20:19:35,689 - INFO -             std : [0.229, 0.224, 0.225]
2021-03-19 20:19:35,689 - INFO -         ToCHWImage : None
2021-03-19 20:19:35,689 - INFO - ------------------------------------------------------------
2021-03-19 20:19:35,689 - INFO - checkpoints : 
2021-03-19 20:19:35,689 - INFO - classes_num : 102
2021-03-19 20:19:35,689 - INFO - epochs : 20
2021-03-19 20:19:35,689 - INFO - image_shape : [3, 224, 224]
2021-03-19 20:19:35,689 - INFO - mode : train
2021-03-19 20:19:35,689 - INFO - model_save_dir : ./output/
2021-03-19 20:19:35,690 - INFO - pretrained_model : 
2021-03-19 20:19:35,690 - INFO - save_interval : 1
2021-03-19 20:19:35,690 - INFO - topk : 5
2021-03-19 20:19:35,690 - INFO - total_images : 1020
2021-03-19 20:19:35,690 - INFO - use_gpu : True
2021-03-19 20:19:35,690 - INFO - valid_interval : 1
2021-03-19 20:19:35,690 - INFO - validate : True
W0319 20:19:35.693763 145123 device_context.cc:362] Please NOTE: device: 0, GPU Compute Capability: 6.0, Driver API Version: 10.1, Runtime API Version: 10.1
W0319 20:19:35.698918 145123 device_context.cc:372] device: 0, cuDNN Version: 7.6.
2021-03-19 20:19:40,099 - INFO - epoch:0  , train step:0   , top1: 0.00000, top5: 0.06250, loss: 4.86664, lr: 0.012500, batch_cost: 0.96304 s, reader_cost: 0.77114 s, ips: 33.22826 images/sec.
2021-03-19 20:19:45,498 - INFO - epoch:0  , train step:10  , top1: 0.00000, top5: 0.06250, loss: 6.99402, lr: 0.012492, batch_cost: 0.60194 s, reader_cost: 0.42753 s, ips: 53.16187 images/sec.
2021-03-19 20:19:51,673 - INFO - epoch:0  , train step:20  , top1: 0.00000, top5: 0.03125, loss: 7.12747, lr: 0.012468, batch_cost: 0.61606 s, reader_cost: 0.44217 s, ips: 51.94323 images/sec.
2021-03-19 20:19:57,221 - INFO - epoch:0  , train step:30  , top1: 0.00000, top5: 0.00000, loss: 7.44012, lr: 0.012428, batch_cost: 0.58692 s, reader_cost: 0.41308 s, ips: 54.52226 images/sec.
2021-03-19 20:19:57,222 - INFO - END epoch:0   train top1: 0.01210, top5: 0.05343, loss: 6.19272,  batch_cost: 0.58692 s, reader_cost: 0.41308 s, batch_cost_sum: 12.32524 s, ips: 54.52226 images/sec.
2021-03-19 20:19:57,652 - INFO - epoch:0  , valid step:0   , top1: 0.00000, top5: 0.15000, loss: 259.22046, lr: 0.000000, batch_cost: 0.42536 s, reader_cost: 0.32728 s, ips: 47.01874 images/sec.
2021-03-19 20:20:00,296 - INFO - epoch:0  , valid step:10  , top1: 0.00000, top5: 0.00000, loss: 586.73242, lr: 0.000000, batch_cost: 0.22649 s, reader_cost: 0.18511 s, ips: 88.30560 images/sec.
2021-03-19 20:20:02,672 - INFO - epoch:0  , valid step:20  , top1: 0.00000, top5: 0.00000, loss: 276.41537, lr: 0.000000, batch_cost: 0.23659 s, reader_cost: 0.19549 s, ips: 84.53575 images/sec.
2021-03-19 20:20:05,218 - INFO - epoch:0  , valid step:30  , top1: 0.00000, top5: 0.00000, loss: 75.37308, lr: 0.000000, batch_cost: 0.24516 s, reader_cost: 0.20369 s, ips: 81.58041 images/sec.
2021-03-19 20:20:07,495 - INFO - epoch:0  , valid step:40  , top1: 0.00000, top5: 0.00000, loss: 143.24066, lr: 0.000000, batch_cost: 0.23953 s, reader_cost: 0.19813 s, ips: 83.49586 images/sec.
2021-03-19 20:20:10,373 - INFO - epoch:0  , valid step:50  , top1: 0.00000, top5: 0.00000, loss: 676.67651, lr: 0.000000, batch_cost: 0.25130 s, reader_cost: 0.20991 s, ips: 79.58546 images/sec.
2021-03-19 20:20:10,374 - INFO - END epoch:0   valid top1: 0.00882, top5: 0.04804, loss: 295.28711,  batch_cost: 0.25130 s, reader_cost: 0.20991 s, batch_cost_sum: 10.30339 s, ips: 79.58546 images/sec.
2021-03-19 20:20:12,240 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:20:12,240 - INFO - The best top1 acc 0.00882, in epoch: 0
2021-03-19 20:20:14,183 - INFO - Already save model in ./output/ResNet50_vd/0
2021-03-19 20:20:14,603 - INFO - epoch:1  , train step:0   , top1: 0.03125, top5: 0.12500, loss: 4.83545, lr: 0.012423, batch_cost: 0.41142 s, reader_cost: 0.22877 s, ips: 77.77911 images/sec.
2021-03-19 20:20:18,319 - INFO - epoch:1  , train step:10  , top1: 0.00000, top5: 0.00000, loss: 7.07517, lr: 0.012366, batch_cost: 0.57491 s, reader_cost: 0.40059 s, ips: 55.66085 images/sec.
2021-03-19 20:20:21,873 - INFO - epoch:1  , train step:20  , top1: 0.00000, top5: 0.12500, loss: 5.98773, lr: 0.012292, batch_cost: 0.37538 s, reader_cost: 0.20154 s, ips: 85.24611 images/sec.
2021-03-19 20:20:25,135 - INFO - epoch:1  , train step:30  , top1: 0.00000, top5: 0.09375, loss: 6.52457, lr: 0.012204, batch_cost: 0.35195 s, reader_cost: 0.17815 s, ips: 90.92073 images/sec.
2021-03-19 20:20:25,136 - INFO - END epoch:1   train top1: 0.00907, top5: 0.04637, loss: 6.03543,  batch_cost: 0.35195 s, reader_cost: 0.17815 s, batch_cost_sum: 7.39105 s, ips: 90.92073 images/sec.
2021-03-19 20:20:25,332 - INFO - epoch:1  , valid step:0   , top1: 0.05000, top5: 0.25000, loss: 11.28157, lr: 0.000000, batch_cost: 0.19206 s, reader_cost: 0.15292 s, ips: 104.13542 images/sec.
2021-03-19 20:20:26,713 - INFO - epoch:1  , valid step:10  , top1: 0.00000, top5: 0.00000, loss: 92.52206, lr: 0.000000, batch_cost: 0.13176 s, reader_cost: 0.09365 s, ips: 151.79045 images/sec.
2021-03-19 20:20:28,125 - INFO - epoch:1  , valid step:20  , top1: 0.50000, top5: 0.50000, loss: 19.24900, lr: 0.000000, batch_cost: 0.14034 s, reader_cost: 0.10232 s, ips: 142.50932 images/sec.
2021-03-19 20:20:29,640 - INFO - epoch:1  , valid step:30  , top1: 0.00000, top5: 0.00000, loss: 16.14626, lr: 0.000000, batch_cost: 0.14566 s, reader_cost: 0.10739 s, ips: 137.30695 images/sec.
2021-03-19 20:20:31,145 - INFO - epoch:1  , valid step:40  , top1: 0.00000, top5: 0.00000, loss: 10.21349, lr: 0.000000, batch_cost: 0.14721 s, reader_cost: 0.10852 s, ips: 135.86291 images/sec.
2021-03-19 20:20:32,507 - INFO - epoch:1  , valid step:50  , top1: 0.00000, top5: 0.00000, loss: 8.78653, lr: 0.000000, batch_cost: 0.14452 s, reader_cost: 0.10584 s, ips: 138.38744 images/sec.
2021-03-19 20:20:32,508 - INFO - END epoch:1   valid top1: 0.01078, top5: 0.06176, loss: 22.63437,  batch_cost: 0.14452 s, reader_cost: 0.10584 s, batch_cost_sum: 5.92539 s, ips: 138.38744 images/sec.
2021-03-19 20:20:34,483 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:20:34,483 - INFO - The best top1 acc 0.01078, in epoch: 1
2021-03-19 20:20:36,359 - INFO - Already save model in ./output/ResNet50_vd/1
2021-03-19 20:20:36,747 - INFO - epoch:2  , train step:0   , top1: 0.00000, top5: 0.03125, loss: 5.79515, lr: 0.012194, batch_cost: 0.37814 s, reader_cost: 0.20437 s, ips: 84.62512 images/sec.
2021-03-19 20:20:39,854 - INFO - epoch:2  , train step:10  , top1: 0.03125, top5: 0.09375, loss: 6.04636, lr: 0.012089, batch_cost: 0.30347 s, reader_cost: 0.13009 s, ips: 105.44819 images/sec.
2021-03-19 20:20:42,945 - INFO - epoch:2  , train step:20  , top1: 0.00000, top5: 0.03125, loss: 5.17775, lr: 0.011968, batch_cost: 0.30854 s, reader_cost: 0.13490 s, ips: 103.71567 images/sec.
2021-03-19 20:20:45,999 - INFO - epoch:2  , train step:30  , top1: 0.00000, top5: 0.09375, loss: 4.55504, lr: 0.011833, batch_cost: 0.30706 s, reader_cost: 0.13345 s, ips: 104.21377 images/sec.
2021-03-19 20:20:45,999 - INFO - END epoch:2   train top1: 0.00806, top5: 0.04335, loss: 5.33692,  batch_cost: 0.30706 s, reader_cost: 0.13345 s, batch_cost_sum: 6.44828 s, ips: 104.21377 images/sec.
2021-03-19 20:20:46,191 - INFO - epoch:2  , valid step:0   , top1: 0.00000, top5: 0.00000, loss: 4.67726, lr: 0.000000, batch_cost: 0.18726 s, reader_cost: 0.14844 s, ips: 106.80465 images/sec.
2021-03-19 20:20:47,583 - INFO - epoch:2  , valid step:10  , top1: 0.00000, top5: 0.00000, loss: 4.44760, lr: 0.000000, batch_cost: 0.13321 s, reader_cost: 0.09518 s, ips: 150.13437 images/sec.
2021-03-19 20:20:48,974 - INFO - epoch:2  , valid step:20  , top1: 0.00000, top5: 0.45000, loss: 14.47852, lr: 0.000000, batch_cost: 0.13858 s, reader_cost: 0.09965 s, ips: 144.32522 images/sec.
2021-03-19 20:20:50,499 - INFO - epoch:2  , valid step:30  , top1: 0.00000, top5: 0.00000, loss: 4.76801, lr: 0.000000, batch_cost: 0.14519 s, reader_cost: 0.10593 s, ips: 137.74853 images/sec.
2021-03-19 20:20:51,886 - INFO - epoch:2  , valid step:40  , top1: 0.00000, top5: 0.00000, loss: 11.13570, lr: 0.000000, batch_cost: 0.14310 s, reader_cost: 0.10359 s, ips: 139.76294 images/sec.
2021-03-19 20:20:53,233 - INFO - epoch:2  , valid step:50  , top1: 0.00000, top5: 0.20000, loss: 6.99386, lr: 0.000000, batch_cost: 0.14104 s, reader_cost: 0.10168 s, ips: 141.80411 images/sec.
2021-03-19 20:20:53,233 - INFO - END epoch:2   valid top1: 0.01961, top5: 0.08137, loss: 22.41946,  batch_cost: 0.14104 s, reader_cost: 0.10168 s, batch_cost_sum: 5.78262 s, ips: 141.80411 images/sec.
2021-03-19 20:20:55,107 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:20:55,107 - INFO - The best top1 acc 0.01961, in epoch: 2
2021-03-19 20:20:56,908 - INFO - Already save model in ./output/ResNet50_vd/2
2021-03-19 20:20:57,285 - INFO - epoch:3  , train step:0   , top1: 0.00000, top5: 0.03125, loss: 5.28182, lr: 0.011819, batch_cost: 0.36620 s, reader_cost: 0.18690 s, ips: 87.38338 images/sec.
2021-03-19 20:21:00,395 - INFO - epoch:3  , train step:10  , top1: 0.03125, top5: 0.06250, loss: 4.72577, lr: 0.011668, batch_cost: 0.30136 s, reader_cost: 0.12804 s, ips: 106.18390 images/sec.
2021-03-19 20:21:03,486 - INFO - epoch:3  , train step:20  , top1: 0.00000, top5: 0.06250, loss: 4.85962, lr: 0.011503, batch_cost: 0.30839 s, reader_cost: 0.13450 s, ips: 103.76607 images/sec.
2021-03-19 20:21:06,613 - INFO - epoch:3  , train step:30  , top1: 0.03125, top5: 0.09375, loss: 4.36318, lr: 0.011325, batch_cost: 0.31044 s, reader_cost: 0.13652 s, ips: 103.07995 images/sec.
2021-03-19 20:21:06,614 - INFO - END epoch:3   train top1: 0.01714, top5: 0.07661, loss: 4.78645,  batch_cost: 0.31044 s, reader_cost: 0.13652 s, batch_cost_sum: 6.51921 s, ips: 103.07995 images/sec.
2021-03-19 20:21:06,806 - INFO - epoch:3  , valid step:0   , top1: 0.00000, top5: 0.00000, loss: 4.44174, lr: 0.000000, batch_cost: 0.18839 s, reader_cost: 0.14933 s, ips: 106.16381 images/sec.
2021-03-19 20:21:08,249 - INFO - epoch:3  , valid step:10  , top1: 0.00000, top5: 0.40000, loss: 4.68642, lr: 0.000000, batch_cost: 0.13499 s, reader_cost: 0.09611 s, ips: 148.15496 images/sec.
2021-03-19 20:21:09,666 - INFO - epoch:3  , valid step:20  , top1: 0.05000, top5: 0.60000, loss: 4.01161, lr: 0.000000, batch_cost: 0.14110 s, reader_cost: 0.10189 s, ips: 141.74314 images/sec.
2021-03-19 20:21:11,177 - INFO - epoch:3  , valid step:30  , top1: 0.00000, top5: 0.30000, loss: 4.34854, lr: 0.000000, batch_cost: 0.14583 s, reader_cost: 0.10658 s, ips: 137.14249 images/sec.
2021-03-19 20:21:12,583 - INFO - epoch:3  , valid step:40  , top1: 0.00000, top5: 0.00000, loss: 4.52146, lr: 0.000000, batch_cost: 0.14415 s, reader_cost: 0.10493 s, ips: 138.74708 images/sec.
2021-03-19 20:21:13,964 - INFO - epoch:3  , valid step:50  , top1: 0.00000, top5: 0.00000, loss: 4.58276, lr: 0.000000, batch_cost: 0.14269 s, reader_cost: 0.10363 s, ips: 140.16815 images/sec.
2021-03-19 20:21:13,965 - INFO - END epoch:3   valid top1: 0.03235, top5: 0.13627, loss: 6.39129,  batch_cost: 0.14269 s, reader_cost: 0.10363 s, batch_cost_sum: 5.85012 s, ips: 140.16815 images/sec.
2021-03-19 20:21:15,902 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:21:15,902 - INFO - The best top1 acc 0.03235, in epoch: 3
2021-03-19 20:21:17,878 - INFO - Already save model in ./output/ResNet50_vd/3
2021-03-19 20:21:18,259 - INFO - epoch:4  , train step:0   , top1: 0.03125, top5: 0.18750, loss: 4.47206, lr: 0.011306, batch_cost: 0.37348 s, reader_cost: 0.20015 s, ips: 85.68055 images/sec.
2021-03-19 20:21:21,251 - INFO - epoch:4  , train step:10  , top1: 0.03125, top5: 0.09375, loss: 4.79451, lr: 0.011114, batch_cost: 0.29818 s, reader_cost: 0.12459 s, ips: 107.31838 images/sec.
2021-03-19 20:21:24,341 - INFO - epoch:4  , train step:20  , top1: 0.00000, top5: 0.15625, loss: 4.35169, lr: 0.010909, batch_cost: 0.30798 s, reader_cost: 0.13424 s, ips: 103.90439 images/sec.
2021-03-19 20:21:27,500 - INFO - epoch:4  , train step:30  , top1: 0.00000, top5: 0.15625, loss: 4.46359, lr: 0.010692, batch_cost: 0.31175 s, reader_cost: 0.13795 s, ips: 102.64661 images/sec.
2021-03-19 20:21:27,500 - INFO - END epoch:4   train top1: 0.02016, top5: 0.13206, loss: 4.45923,  batch_cost: 0.31175 s, reader_cost: 0.13795 s, batch_cost_sum: 6.54673 s, ips: 102.64661 images/sec.
2021-03-19 20:21:27,682 - INFO - epoch:4  , valid step:0   , top1: 0.00000, top5: 0.00000, loss: 4.51527, lr: 0.000000, batch_cost: 0.17673 s, reader_cost: 0.13784 s, ips: 113.16886 images/sec.
2021-03-19 20:21:29,044 - INFO - epoch:4  , valid step:10  , top1: 0.10000, top5: 0.30000, loss: 4.07118, lr: 0.000000, batch_cost: 0.12561 s, reader_cost: 0.08697 s, ips: 159.21741 images/sec.
2021-03-19 20:21:30,404 - INFO - epoch:4  , valid step:20  , top1: 0.00000, top5: 0.35000, loss: 25.35397, lr: 0.000000, batch_cost: 0.13509 s, reader_cost: 0.09626 s, ips: 148.04952 images/sec.
2021-03-19 20:21:31,932 - INFO - epoch:4  , valid step:30  , top1: 0.00000, top5: 0.00000, loss: 4.41398, lr: 0.000000, batch_cost: 0.14352 s, reader_cost: 0.10457 s, ips: 139.35478 images/sec.
2021-03-19 20:21:33,343 - INFO - epoch:4  , valid step:40  , top1: 0.00000, top5: 0.00000, loss: 5.70639, lr: 0.000000, batch_cost: 0.14273 s, reader_cost: 0.10348 s, ips: 140.12480 images/sec.
2021-03-19 20:21:34,726 - INFO - epoch:4  , valid step:50  , top1: 0.00000, top5: 0.45000, loss: 3.94955, lr: 0.000000, batch_cost: 0.14165 s, reader_cost: 0.10247 s, ips: 141.19640 images/sec.
2021-03-19 20:21:34,726 - INFO - END epoch:4   valid top1: 0.04902, top5: 0.18922, loss: 11.56401,  batch_cost: 0.14165 s, reader_cost: 0.10247 s, batch_cost_sum: 5.80751 s, ips: 141.19640 images/sec.
2021-03-19 20:21:36,687 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:21:36,688 - INFO - The best top1 acc 0.04902, in epoch: 4
2021-03-19 20:21:38,662 - INFO - Already save model in ./output/ResNet50_vd/4
2021-03-19 20:21:39,059 - INFO - epoch:5  , train step:0   , top1: 0.03125, top5: 0.25000, loss: 4.27060, lr: 0.010669, batch_cost: 0.38606 s, reader_cost: 0.21239 s, ips: 82.88852 images/sec.
2021-03-19 20:21:42,191 - INFO - epoch:5  , train step:10  , top1: 0.06250, top5: 0.18750, loss: 4.35091, lr: 0.010440, batch_cost: 0.32957 s, reader_cost: 0.15550 s, ips: 97.09711 images/sec.
2021-03-19 20:21:45,347 - INFO - epoch:5  , train step:20  , top1: 0.00000, top5: 0.09375, loss: 4.51615, lr: 0.010200, batch_cost: 0.31682 s, reader_cost: 0.14236 s, ips: 101.00238 images/sec.
2021-03-19 20:21:48,459 - INFO - epoch:5  , train step:30  , top1: 0.06250, top5: 0.18750, loss: 4.30240, lr: 0.009949, batch_cost: 0.31417 s, reader_cost: 0.14011 s, ips: 101.85544 images/sec.
2021-03-19 20:21:48,459 - INFO - END epoch:5   train top1: 0.03226, top5: 0.15423, loss: 4.30388,  batch_cost: 0.31417 s, reader_cost: 0.14011 s, batch_cost_sum: 6.59759 s, ips: 101.85544 images/sec.
2021-03-19 20:21:48,645 - INFO - epoch:5  , valid step:0   , top1: 0.00000, top5: 0.00000, loss: 4.24593, lr: 0.000000, batch_cost: 0.18067 s, reader_cost: 0.14185 s, ips: 110.69642 images/sec.
2021-03-19 20:21:50,027 - INFO - epoch:5  , valid step:10  , top1: 0.00000, top5: 0.30000, loss: 3.91487, lr: 0.000000, batch_cost: 0.12639 s, reader_cost: 0.08701 s, ips: 158.24487 images/sec.
2021-03-19 20:21:51,466 - INFO - epoch:5  , valid step:20  , top1: 0.00000, top5: 0.15000, loss: 4.12740, lr: 0.000000, batch_cost: 0.14235 s, reader_cost: 0.10293 s, ips: 140.49962 images/sec.
2021-03-19 20:21:52,967 - INFO - epoch:5  , valid step:30  , top1: 0.00000, top5: 0.35000, loss: 4.24569, lr: 0.000000, batch_cost: 0.14599 s, reader_cost: 0.10659 s, ips: 136.99612 images/sec.
2021-03-19 20:21:54,364 - INFO - epoch:5  , valid step:40  , top1: 0.00000, top5: 0.00000, loss: 4.33213, lr: 0.000000, batch_cost: 0.14400 s, reader_cost: 0.10485 s, ips: 138.88940 images/sec.
2021-03-19 20:21:55,760 - INFO - epoch:5  , valid step:50  , top1: 0.00000, top5: 0.10000, loss: 3.85181, lr: 0.000000, batch_cost: 0.14292 s, reader_cost: 0.10398 s, ips: 139.93968 images/sec.
2021-03-19 20:21:55,761 - INFO - END epoch:5   valid top1: 0.04902, top5: 0.23627, loss: 4.20145,  batch_cost: 0.14292 s, reader_cost: 0.10398 s, batch_cost_sum: 5.85967 s, ips: 139.93968 images/sec.
2021-03-19 20:21:57,878 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:21:57,878 - INFO - The best top1 acc 0.04902, in epoch: 5
2021-03-19 20:21:59,878 - INFO - Already save model in ./output/ResNet50_vd/5
2021-03-19 20:22:00,247 - INFO - epoch:6  , train step:0   , top1: 0.00000, top5: 0.25000, loss: 4.07936, lr: 0.009924, batch_cost: 0.35729 s, reader_cost: 0.17675 s, ips: 89.56214 images/sec.
2021-03-19 20:22:03,364 - INFO - epoch:6  , train step:10  , top1: 0.03125, top5: 0.21875, loss: 4.06672, lr: 0.009663, batch_cost: 0.31223 s, reader_cost: 0.13924 s, ips: 102.48922 images/sec.
2021-03-19 20:22:06,496 - INFO - epoch:6  , train step:20  , top1: 0.03125, top5: 0.21875, loss: 3.98617, lr: 0.009393, batch_cost: 0.31303 s, reader_cost: 0.13906 s, ips: 102.22572 images/sec.
2021-03-19 20:22:09,572 - INFO - epoch:6  , train step:30  , top1: 0.12500, top5: 0.25000, loss: 3.86710, lr: 0.009116, batch_cost: 0.31049 s, reader_cost: 0.13657 s, ips: 103.06320 images/sec.
2021-03-19 20:22:09,573 - INFO - END epoch:6   train top1: 0.05040, top5: 0.20665, loss: 4.08595,  batch_cost: 0.31049 s, reader_cost: 0.13657 s, batch_cost_sum: 6.52027 s, ips: 103.06320 images/sec.
2021-03-19 20:22:09,760 - INFO - epoch:6  , valid step:0   , top1: 0.35000, top5: 0.75000, loss: 3.58071, lr: 0.000000, batch_cost: 0.18260 s, reader_cost: 0.14350 s, ips: 109.52644 images/sec.
2021-03-19 20:22:11,146 - INFO - epoch:6  , valid step:10  , top1: 0.00000, top5: 0.10000, loss: 4.22208, lr: 0.000000, batch_cost: 0.14159 s, reader_cost: 0.10325 s, ips: 141.25446 images/sec.
2021-03-19 20:22:12,595 - INFO - epoch:6  , valid step:20  , top1: 0.00000, top5: 0.00000, loss: 4.78096, lr: 0.000000, batch_cost: 0.14459 s, reader_cost: 0.10548 s, ips: 138.32080 images/sec.
2021-03-19 20:22:14,138 - INFO - epoch:6  , valid step:30  , top1: 0.40000, top5: 0.45000, loss: 3.70558, lr: 0.000000, batch_cost: 0.14924 s, reader_cost: 0.11006 s, ips: 134.00935 images/sec.
2021-03-19 20:22:15,629 - INFO - epoch:6  , valid step:40  , top1: 0.15000, top5: 0.20000, loss: 3.99691, lr: 0.000000, batch_cost: 0.14917 s, reader_cost: 0.10981 s, ips: 134.07240 images/sec.
2021-03-19 20:22:17,089 - INFO - epoch:6  , valid step:50  , top1: 0.15000, top5: 0.65000, loss: 3.18714, lr: 0.000000, batch_cost: 0.14841 s, reader_cost: 0.10914 s, ips: 134.76181 images/sec.
2021-03-19 20:22:17,091 - INFO - END epoch:6   valid top1: 0.09412, top5: 0.27941, loss: 4.15426,  batch_cost: 0.14841 s, reader_cost: 0.10914 s, batch_cost_sum: 6.08481 s, ips: 134.76181 images/sec.
2021-03-19 20:22:19,117 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:22:19,118 - INFO - The best top1 acc 0.09412, in epoch: 6
2021-03-19 20:22:21,105 - INFO - Already save model in ./output/ResNet50_vd/6
2021-03-19 20:22:21,497 - INFO - epoch:7  , train step:0   , top1: 0.09375, top5: 0.28125, loss: 3.77055, lr: 0.009087, batch_cost: 0.38288 s, reader_cost: 0.20718 s, ips: 83.57700 images/sec.
2021-03-19 20:22:24,620 - INFO - epoch:7  , train step:10  , top1: 0.06250, top5: 0.28125, loss: 3.88618, lr: 0.008802, batch_cost: 0.30989 s, reader_cost: 0.13633 s, ips: 103.26196 images/sec.
2021-03-19 20:22:27,693 - INFO - epoch:7  , train step:20  , top1: 0.00000, top5: 0.06250, loss: 4.31368, lr: 0.008509, batch_cost: 0.30760 s, reader_cost: 0.13369 s, ips: 104.03105 images/sec.
2021-03-19 20:22:30,750 - INFO - epoch:7  , train step:30  , top1: 0.09375, top5: 0.18750, loss: 4.18981, lr: 0.008211, batch_cost: 0.30668 s, reader_cost: 0.13280 s, ips: 104.34252 images/sec.
2021-03-19 20:22:30,750 - INFO - END epoch:7   train top1: 0.05746, top5: 0.21371, loss: 3.98258,  batch_cost: 0.30668 s, reader_cost: 0.13280 s, batch_cost_sum: 6.44033 s, ips: 104.34252 images/sec.
2021-03-19 20:22:30,942 - INFO - epoch:7  , valid step:0   , top1: 0.35000, top5: 0.65000, loss: 3.28838, lr: 0.000000, batch_cost: 0.18771 s, reader_cost: 0.14815 s, ips: 106.54501 images/sec.
2021-03-19 20:22:32,369 - INFO - epoch:7  , valid step:10  , top1: 0.25000, top5: 0.50000, loss: 3.45008, lr: 0.000000, batch_cost: 0.13426 s, reader_cost: 0.09543 s, ips: 148.96503 images/sec.
2021-03-19 20:22:33,803 - INFO - epoch:7  , valid step:20  , top1: 0.05000, top5: 0.20000, loss: 5.15885, lr: 0.000000, batch_cost: 0.14262 s, reader_cost: 0.10354 s, ips: 140.23240 images/sec.
2021-03-19 20:22:35,318 - INFO - epoch:7  , valid step:30  , top1: 0.50000, top5: 0.50000, loss: 3.56399, lr: 0.000000, batch_cost: 0.14684 s, reader_cost: 0.10786 s, ips: 136.20479 images/sec.
2021-03-19 20:22:36,788 - INFO - epoch:7  , valid step:40  , top1: 0.00000, top5: 0.15000, loss: 4.30021, lr: 0.000000, batch_cost: 0.14687 s, reader_cost: 0.10769 s, ips: 136.17837 images/sec.
2021-03-19 20:22:38,165 - INFO - epoch:7  , valid step:50  , top1: 0.15000, top5: 0.50000, loss: 3.51091, lr: 0.000000, batch_cost: 0.14464 s, reader_cost: 0.10556 s, ips: 138.27614 images/sec.
2021-03-19 20:22:38,165 - INFO - END epoch:7   valid top1: 0.09314, top5: 0.29216, loss: 4.99010,  batch_cost: 0.14464 s, reader_cost: 0.10556 s, batch_cost_sum: 5.93016 s, ips: 138.27614 images/sec.
2021-03-19 20:22:38,165 - INFO - The best top1 acc 0.09412, in epoch: 6
2021-03-19 20:22:40,049 - INFO - Already save model in ./output/ResNet50_vd/7
2021-03-19 20:22:40,420 - INFO - epoch:8  , train step:0   , top1: 0.06250, top5: 0.31250, loss: 3.75868, lr: 0.008181, batch_cost: 0.36099 s, reader_cost: 0.18764 s, ips: 88.64616 images/sec.
2021-03-19 20:22:43,478 - INFO - epoch:8  , train step:10  , top1: 0.09375, top5: 0.15625, loss: 3.89148, lr: 0.007878, batch_cost: 0.29821 s, reader_cost: 0.12449 s, ips: 107.30602 images/sec.
2021-03-19 20:22:46,583 - INFO - epoch:8  , train step:20  , top1: 0.06250, top5: 0.31250, loss: 3.96159, lr: 0.007570, batch_cost: 0.30939 s, reader_cost: 0.13580 s, ips: 103.43016 images/sec.
2021-03-19 20:22:49,653 - INFO - epoch:8  , train step:30  , top1: 0.06250, top5: 0.12500, loss: 4.08431, lr: 0.007259, batch_cost: 0.30824 s, reader_cost: 0.13466 s, ips: 103.81357 images/sec.
2021-03-19 20:22:49,654 - INFO - END epoch:8   train top1: 0.07964, top5: 0.25504, loss: 3.90158,  batch_cost: 0.30824 s, reader_cost: 0.13466 s, batch_cost_sum: 6.47314 s, ips: 103.81357 images/sec.
2021-03-19 20:22:49,852 - INFO - epoch:8  , valid step:0   , top1: 0.00000, top5: 0.35000, loss: 3.77564, lr: 0.000000, batch_cost: 0.19350 s, reader_cost: 0.15433 s, ips: 103.35877 images/sec.
2021-03-19 20:22:51,220 - INFO - epoch:8  , valid step:10  , top1: 0.25000, top5: 0.50000, loss: 3.59278, lr: 0.000000, batch_cost: 0.13089 s, reader_cost: 0.09209 s, ips: 152.80380 images/sec.
2021-03-19 20:22:52,573 - INFO - epoch:8  , valid step:20  , top1: 0.00000, top5: 0.00000, loss: 4.78005, lr: 0.000000, batch_cost: 0.13487 s, reader_cost: 0.09577 s, ips: 148.28712 images/sec.
2021-03-19 20:22:54,145 - INFO - epoch:8  , valid step:30  , top1: 0.25000, top5: 0.50000, loss: 3.65141, lr: 0.000000, batch_cost: 0.14552 s, reader_cost: 0.10615 s, ips: 137.43534 images/sec.
2021-03-19 20:22:55,601 - INFO - epoch:8  , valid step:40  , top1: 0.00000, top5: 0.00000, loss: 5.28320, lr: 0.000000, batch_cost: 0.14555 s, reader_cost: 0.10626 s, ips: 137.40598 images/sec.
2021-03-19 20:22:56,989 - INFO - epoch:8  , valid step:50  , top1: 0.20000, top5: 0.30000, loss: 3.25699, lr: 0.000000, batch_cost: 0.14388 s, reader_cost: 0.10482 s, ips: 139.00085 images/sec.
2021-03-19 20:22:56,989 - INFO - END epoch:8   valid top1: 0.08922, top5: 0.34412, loss: 3.92694,  batch_cost: 0.14388 s, reader_cost: 0.10482 s, batch_cost_sum: 5.89924 s, ips: 139.00085 images/sec.
2021-03-19 20:22:56,989 - INFO - The best top1 acc 0.09412, in epoch: 6
2021-03-19 20:22:58,868 - INFO - Already save model in ./output/ResNet50_vd/8
2021-03-19 20:22:59,225 - INFO - epoch:9  , train step:0   , top1: 0.18750, top5: 0.43750, loss: 3.53258, lr: 0.007228, batch_cost: 0.34956 s, reader_cost: 0.17544 s, ips: 91.54246 images/sec.
2021-03-19 20:23:02,289 - INFO - epoch:9  , train step:10  , top1: 0.00000, top5: 0.21875, loss: 3.85580, lr: 0.006914, batch_cost: 0.30743 s, reader_cost: 0.13385 s, ips: 104.08752 images/sec.
2021-03-19 20:23:05,305 - INFO - epoch:9  , train step:20  , top1: 0.12500, top5: 0.28125, loss: 3.99234, lr: 0.006598, batch_cost: 0.30213 s, reader_cost: 0.12840 s, ips: 105.91501 images/sec.
2021-03-19 20:23:08,377 - INFO - epoch:9  , train step:30  , top1: 0.18750, top5: 0.31250, loss: 3.44448, lr: 0.006282, batch_cost: 0.30451 s, reader_cost: 0.13075 s, ips: 105.08568 images/sec.
2021-03-19 20:23:08,377 - INFO - END epoch:9   train top1: 0.07258, top5: 0.30040, loss: 3.81065,  batch_cost: 0.30451 s, reader_cost: 0.13075 s, batch_cost_sum: 6.39478 s, ips: 105.08568 images/sec.
2021-03-19 20:23:08,575 - INFO - epoch:9  , valid step:0   , top1: 0.15000, top5: 0.60000, loss: 3.37804, lr: 0.000000, batch_cost: 0.19301 s, reader_cost: 0.15390 s, ips: 103.62216 images/sec.
2021-03-19 20:23:09,987 - INFO - epoch:9  , valid step:10  , top1: 0.50000, top5: 0.75000, loss: 2.77825, lr: 0.000000, batch_cost: 0.13541 s, reader_cost: 0.09629 s, ips: 147.70106 images/sec.
2021-03-19 20:23:11,394 - INFO - epoch:9  , valid step:20  , top1: 0.00000, top5: 0.15000, loss: 5.49396, lr: 0.000000, batch_cost: 0.14024 s, reader_cost: 0.10114 s, ips: 142.61179 images/sec.
2021-03-19 20:23:12,906 - INFO - epoch:9  , valid step:30  , top1: 0.50000, top5: 0.50000, loss: 3.19289, lr: 0.000000, batch_cost: 0.14547 s, reader_cost: 0.10631 s, ips: 137.48630 images/sec.
2021-03-19 20:23:14,330 - INFO - epoch:9  , valid step:40  , top1: 0.00000, top5: 0.10000, loss: 4.68827, lr: 0.000000, batch_cost: 0.14446 s, reader_cost: 0.10537 s, ips: 138.44539 images/sec.
2021-03-19 20:23:15,767 - INFO - epoch:9  , valid step:50  , top1: 0.00000, top5: 0.55000, loss: 3.43434, lr: 0.000000, batch_cost: 0.14427 s, reader_cost: 0.10533 s, ips: 138.63316 images/sec.
2021-03-19 20:23:15,767 - INFO - END epoch:9   valid top1: 0.10686, top5: 0.34510, loss: 4.59049,  batch_cost: 0.14427 s, reader_cost: 0.10533 s, batch_cost_sum: 5.91489 s, ips: 138.63316 images/sec.
2021-03-19 20:23:17,680 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:23:17,680 - INFO - The best top1 acc 0.10686, in epoch: 9
2021-03-19 20:23:19,602 - INFO - Already save model in ./output/ResNet50_vd/9
2021-03-19 20:23:19,994 - INFO - epoch:10 , train step:0   , top1: 0.15625, top5: 0.46875, loss: 3.23671, lr: 0.006250, batch_cost: 0.38300 s, reader_cost: 0.19852 s, ips: 83.54995 images/sec.
2021-03-19 20:23:23,014 - INFO - epoch:10 , train step:10  , top1: 0.09375, top5: 0.28125, loss: 4.05488, lr: 0.005933, batch_cost: 0.30422 s, reader_cost: 0.13079 s, ips: 105.18837 images/sec.
2021-03-19 20:23:26,063 - INFO - epoch:10 , train step:20  , top1: 0.12500, top5: 0.46875, loss: 3.40690, lr: 0.005618, batch_cost: 0.30485 s, reader_cost: 0.13128 s, ips: 104.96938 images/sec.
2021-03-19 20:23:29,220 - INFO - epoch:10 , train step:30  , top1: 0.03125, top5: 0.25000, loss: 3.77371, lr: 0.005304, batch_cost: 0.31003 s, reader_cost: 0.13628 s, ips: 103.21458 images/sec.
2021-03-19 20:23:29,221 - INFO - END epoch:10  train top1: 0.10786, top5: 0.35484, loss: 3.61430,  batch_cost: 0.31003 s, reader_cost: 0.13628 s, batch_cost_sum: 6.51071 s, ips: 103.21458 images/sec.
2021-03-19 20:23:29,409 - INFO - epoch:10 , valid step:0   , top1: 0.25000, top5: 0.50000, loss: 3.52156, lr: 0.000000, batch_cost: 0.18405 s, reader_cost: 0.14488 s, ips: 108.66509 images/sec.
2021-03-19 20:23:30,776 - INFO - epoch:10 , valid step:10  , top1: 0.30000, top5: 0.50000, loss: 3.30263, lr: 0.000000, batch_cost: 0.12662 s, reader_cost: 0.08744 s, ips: 157.95256 images/sec.
2021-03-19 20:23:32,110 - INFO - epoch:10 , valid step:20  , top1: 0.00000, top5: 0.10000, loss: 5.08234, lr: 0.000000, batch_cost: 0.13286 s, reader_cost: 0.09364 s, ips: 150.52972 images/sec.
2021-03-19 20:23:33,590 - INFO - epoch:10 , valid step:30  , top1: 0.55000, top5: 0.60000, loss: 2.88694, lr: 0.000000, batch_cost: 0.14005 s, reader_cost: 0.10083 s, ips: 142.80600 images/sec.
2021-03-19 20:23:35,027 - INFO - epoch:10 , valid step:40  , top1: 0.10000, top5: 0.15000, loss: 4.59184, lr: 0.000000, batch_cost: 0.14124 s, reader_cost: 0.10210 s, ips: 141.60221 images/sec.
2021-03-19 20:23:36,385 - INFO - epoch:10 , valid step:50  , top1: 0.30000, top5: 0.80000, loss: 2.69427, lr: 0.000000, batch_cost: 0.13991 s, reader_cost: 0.10084 s, ips: 142.94893 images/sec.
2021-03-19 20:23:36,386 - INFO - END epoch:10  valid top1: 0.13431, top5: 0.35392, loss: 4.20621,  batch_cost: 0.13991 s, reader_cost: 0.10084 s, batch_cost_sum: 5.73631 s, ips: 142.94893 images/sec.
2021-03-19 20:23:38,353 - INFO - Already save model in ./output/ResNet50_vd/best_model
2021-03-19 20:23:38,353 - INFO - The best top1 acc 0.13431, in epoch: 10
2021-03-19 20:23:40,262 - INFO - Already save model in ./output/ResNet50_vd/10

```