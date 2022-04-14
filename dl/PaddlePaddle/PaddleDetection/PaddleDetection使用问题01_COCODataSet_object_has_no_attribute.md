

# 1 问题


```bash
Traceback (most recent call last):
  File "tools/infer.py", line 177, in <module>
    main()
  File "tools/infer.py", line 173, in main
    run(FLAGS, cfg)
  File "tools/infer.py", line 134, in run
    save_txt=FLAGS.save_txt)
  File "/home/zhangxin/github/PaddleDetection/ppdet/engine/trainer.py", line 541, in predict
    self.dataset.set_images(images)
AttributeError: 'COCODataSet' object has no attribute 'set_images'
```


# 2 解决办法：
错误原因是TestDataset配置错了，在改配置文件时把ImageFolder错改成了COCODataSet。

```xml
metric: COCO
num_classes: 80

TrainDataset:
  !COCODataSet
    image_dir: train2017
    anno_path: annotations/instances_train2017.json
    dataset_dir: dataset/coco
    data_fields: ['image', 'gt_bbox', 'gt_class', 'is_crowd']

EvalDataset:
  !COCODataSet
    image_dir: val2017
    anno_path: annotations/instances_val2017.json
    dataset_dir: dataset/coco

TestDataset:
  !ImageFolder
    anno_path: annotations/instances_val2017.json
    dataset_dir: dataset/coco
```