


# 1 问题
```bash
Traceback (most recent call last):
  File "D:/github/EAST-SakuraRiven/train_zx.py", line 70, in <module>
    train(train_img_path, train_gt_path, pths_path, batch_size, lr, num_workers, epoch_iter, save_interval)	
  File "D:/github/EAST-SakuraRiven/train_zx.py", line 36, in train
    for i, (img, gt_score, gt_geo, ignored_map) in enumerate(train_loader):
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\utils\data\dataloader.py", line 637, in __next__
    return self._process_next_batch(batch)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\utils\data\dataloader.py", line 658, in _process_next_batch
    raise batch.exc_type(batch.exc_msg)
TypeError: function takes exactly 5 arguments (1 given)
```

# 2 解决
将num_works 改为0，可以跳过此错误。

# 3 参考
* [trian #3](https://github.com/SakuraRiven/EAST/issues/3)
