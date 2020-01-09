

# 问题
```bash
D:\ProgramData\Anaconda3\envs\py36_pytorch13\python.exe D:/github/EfficientDet.Pytorch/demo_zx.py
Traceback (most recent call last):
  File "D:/github/EfficientDet.Pytorch/demo_zx.py", line 9, in <module>
    from datasets import get_augumentation, VOC_CLASSES
  File "D:\github\EfficientDet.Pytorch\datasets\__init__.py", line 2, in <module>
    from .augmentation import get_augumentation, detection_collate, Resizer, Normalizer, Augmenter, collater
  File "D:\github\EfficientDet.Pytorch\datasets\augmentation.py", line 1, in <module>
    import albumentations as albu
ModuleNotFoundError: No module named 'albumentations'
```


# 解决方法

```bash
pip install albumentations
```


