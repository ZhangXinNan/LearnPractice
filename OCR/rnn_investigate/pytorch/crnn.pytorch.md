

# mac
## lmdb
```
➜  crnn.pytorch git:(master) ✗ pip install lmdb
Collecting lmdb
Installing collected packages: lmdb
Successfully installed lmdb-0.92
➜  crnn.pytorch git:(master) ✗ python demo.py  
loading pretrained model from ./data/crnn.pth
a-----v--a-i-l-a-bb-l-e--- => available  
```

## 训练 ImportError: No module named warpctc_pytorch
```
crnn.pytorch git:(zxdev) ✗ python crnn_main.py --trainroot=data/lmdb/plate --valroot=data/lmdb/plate_test
Traceback (most recent call last):
  File "crnn_main.py", line 10, in <module>
    from warpctc_pytorch import CTCLoss
ImportError: No module named warpctc_pytorch
```
解决方法：
安装pytorch_binding[SeanNaren/warp-ctc](https://github.com/SeanNaren/warp-ctc/tree/pytorch_bindings/pytorch_binding)

## _warp_ctc.so Library not loaded
```
➜  crnn.pytorch git:(zxdev) ✗ python crnn_main.py --trainroot=data/lmdb/plate --valroot=data/lmdb/plate_test
Traceback (most recent call last):
  File "crnn_main.py", line 10, in <module>
    from warpctc_pytorch import CTCLoss
  File "/usr/local/lib/python2.7/site-packages/warpctc_pytorch/__init__.py", line 7, in <module>
    from ._warp_ctc import lib as _lib, ffi as _ffi
ImportError: dlopen(/usr/local/lib/python2.7/site-packages/warpctc_pytorch/_warp_ctc.so, 2): Library not loaded: @rpath/libwarpctc.dylib
  Referenced from: /usr/local/lib/python2.7/site-packages/warpctc_pytorch/_warp_ctc.so
  Reason: image not found
```

# seele

```
zhangxin@seele:~/github/torch/crnn.pytorch$ python demo.py 
loading pretrained model from ./data/crnn.pth
a-----v--a-i-l-a-bb-l-e--- => available  
```


```
zhangxin@seele:~/github/torch/crnn.pytorch$ python crnn_main.py 
Traceback (most recent call last):
  File "crnn_main.py", line 10, in <module>
    from warpctc_pytorch import CTCLoss
ImportError: No module named warpctc_pytorch
```

# 142 conda
```
Start val
Traceback (most recent call last):
  File "crnn_main.py", line 207, in <module>
    val(crnn, test_dataset, criterion)
  File "crnn_main.py", line 158, in val
    sim_preds = converter.decode(preds.data, preds_size.data, raw=False)
  File "/data/zhangxin/github/crnn.pytorch/utils.py", line 80, in decode
    assert t.numel() == length.sum(), "texts with length: {} does not match declared length: {}".format(t.numel(), length.sum())
AssertionError: texts with length: 1664 does not match declared length: 6656
You have mail in /var/spool/mail/root
```