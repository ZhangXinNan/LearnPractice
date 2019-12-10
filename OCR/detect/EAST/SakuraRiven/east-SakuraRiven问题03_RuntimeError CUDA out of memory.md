
# 1 问题
```bash
Traceback (most recent call last):
  File "D:/github/EAST-SakuraRiven/train_zx.py", line 73, in <module>
    train(train_img_path, train_gt_path, pths_path, batch_size, lr, num_workers, epoch_iter, save_interval)	
  File "D:/github/EAST-SakuraRiven/train_zx.py", line 40, in train
    pred_score, pred_geo = model(img)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\nn\modules\module.py", line 489, in __call__
    result = self.forward(*input, **kwargs)
  File "D:\github\EAST-SakuraRiven\model.py", line 168, in forward
    return self.output(self.merge(self.extractor(x)))
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\nn\modules\module.py", line 489, in __call__
    result = self.forward(*input, **kwargs)
  File "D:\github\EAST-SakuraRiven\model.py", line 73, in forward
    x = m(x)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\nn\modules\module.py", line 489, in __call__
    result = self.forward(*input, **kwargs)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\nn\modules\pooling.py", line 148, in forward
    self.return_indices)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\_jit_internal.py", line 132, in fn
    return if_false(*args, **kwargs)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\nn\functional.py", line 425, in _max_pool2d
    input, kernel_size, stride, padding, dilation, ceil_mode)[0]
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\site-packages\torch\nn\functional.py", line 417, in max_pool2d_with_indices
    return torch._C._nn.max_pool2d_with_indices(input, kernel_size, _stride, padding, dilation, ceil_mode)
RuntimeError: CUDA out of memory. Tried to allocate 384.00 MiB (GPU 0; 8.00 GiB total capacity; 6.14 GiB already allocated; 163.41 MiB free; 515.50 KiB cached)
```

# 2 解决
将batch_size改小，我显卡是一个gtx1070，batch_size改为8是没问题的。

# 3 参考
