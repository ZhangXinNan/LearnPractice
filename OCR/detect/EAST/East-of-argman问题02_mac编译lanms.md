

# 1 问题
```bash
(py36_tf) ➜  EAST git:(zxdev_mac) ✗ python eval.py \                                   
        --test_data_path=/Users/zhangxin/data_md/crop \
        --gpu_list=0 \
        --checkpoint_path=models/east_icdar2015_resnet_v1_50_rbox/ \
        --output_dir=tmp/
find: -xtype: unknown primary or operator
make: `adaptor.so' is up to date.
WARNING:tensorflow:From /Users/zhangxin/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/framework/op_def_library.py:263: colocate_with (from tensorflow.python.framework.ops) is deprecated and will be removed in a future version.
Instructions for updating:
Colocations handled automatically by placer.
resnet_v1_50/block1 (?, ?, ?, 256)
resnet_v1_50/block2 (?, ?, ?, 512)
resnet_v1_50/block3 (?, ?, ?, 1024)
resnet_v1_50/block4 (?, ?, ?, 2048)
Shape of f_0 (?, ?, ?, 2048)
Shape of f_1 (?, ?, ?, 512)
Shape of f_2 (?, ?, ?, 256)
Shape of f_3 (?, ?, ?, 64)
Shape of h_0 (?, ?, ?, 2048), g_0 (?, ?, ?, 2048)
Shape of h_1 (?, ?, ?, 128), g_1 (?, ?, ?, 128)
Shape of h_2 (?, ?, ?, 64), g_2 (?, ?, ?, 64)
Shape of h_3 (?, ?, ?, 32), g_3 (?, ?, ?, 32)
2019-11-17 21:19:37.498600: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2019-11-17 21:19:37.498845: I tensorflow/core/common_runtime/process_util.cc:71] Creating new thread pool with default inter op setting: 4. Tune using inter_op_parallelism_threads for best performance.
Restore from models/east_icdar2015_resnet_v1_50_rbox/model.ckpt-49491
WARNING:tensorflow:From /Users/zhangxin/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/training/saver.py:1266: checkpoint_exists (from tensorflow.python.training.checkpoint_management) is deprecated and will be removed in a future version.
Instructions for updating:
Use standard file APIs to check for files with this prefix.
Find 30 images
2257 text boxes before nms
Traceback (most recent call last):
  File "eval.py", line 191, in <module>
    tf.app.run()
  File "/Users/zhangxin/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/platform/app.py", line 125, in run
    _sys.exit(main(argv))
  File "eval.py", line 158, in main
    boxes, timer = detect(score_map=score, geo_map=geometry, timer=timer)
  File "eval.py", line 93, in detect
    boxes = lanms.merge_quadrangle_n9(boxes.astype('float32'), nms_thres)
  File "/Users/zhangxin/github/EAST/lanms/__init__.py", line 12, in merge_quadrangle_n9
    from .adaptor import merge_quadrangle_n9 as nms_impl
ImportError: dynamic module does not define module export function (PyInit_adaptor)
```


# 2 解决
