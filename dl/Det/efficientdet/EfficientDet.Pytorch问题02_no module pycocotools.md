
# 问题
```bash
D:\ProgramData\Anaconda3\envs\py36_pytorch13\python.exe D:/github/EfficientDet.Pytorch/demo_zx.py
Traceback (most recent call last):
  File "D:/github/EfficientDet.Pytorch/demo_zx.py", line 9, in <module>
    from datasets import get_augumentation, VOC_CLASSES
  File "D:\github\EfficientDet.Pytorch\datasets\__init__.py", line 3, in <module>
    from .coco import CocoDataset
  File "D:\github\EfficientDet.Pytorch\datasets\coco.py", line 13, in <module>
    from pycocotools.coco import COCO
ModuleNotFoundError: No module named 'pycocotools'
```


# 解决办法

```bash
pip install pycocotools
```

windows 下此命令存在问题，尚未解决。



# 参考
1. [philferriere/cocoapi](https://github.com/philferriere/cocoapi)


