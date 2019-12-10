

# 1 问题
```bash
D:\ProgramData\Anaconda3\envs\py36_pytorch101\python.exe D:/github/EAST-SakuraRiven/train_zx.py
Traceback (most recent call last):
  File "D:/github/EAST-SakuraRiven/train_zx.py", line 72, in <module>
    train(train_img_path, train_gt_path, pths_path, batch_size, lr, num_workers, epoch_iter, save_interval)	
  File "D:/github/EAST-SakuraRiven/train_zx.py", line 36, in train
    for i, (img, gt_score, gt_geo, ignored_map) in enumerate(train_loader):
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\utils\data\dataloader.py", line 615, in __next__
    batch = self.collate_fn([self.dataset[i] for i in indices])
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\utils\data\dataloader.py", line 615, in <listcomp>
    batch = self.collate_fn([self.dataset[i] for i in indices])
  File "D:\github\EAST-SakuraRiven\dataset.py", line 386, in __getitem__
    lines = f.readlines()
342 D:\github\EAST-SakuraRiven\ICDAR_2015\train_gt\gt_img_406.txt D:\github\EAST-SakuraRiven\ICDAR_2015\train_img\img_406.jpg
UnicodeDecodeError: 'gbk' codec can't decode byte 0xbf in position 2: illegal multibyte sequence
```

# 2 解决

## 2.1 在dataset.py首行添加utf-8
```python
#encoding=utf-8
```
并不能解决此问题

## 2.2 
FILE_OBJECT= open('order.log','r', encoding='UTF-8')


# 3 参考
* [python 读取文件时报错UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 205: illegal multibyte sequence](https://www.cnblogs.com/mengyu/p/6638975.html)