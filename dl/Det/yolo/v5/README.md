

代码：[ultralytics/yolov5](https://github.com/ultralytics/yolov5)


# 测试
```bash

python detect.py --source data/images --weights yolov5s.pt --conf 0.25

python detect.py --source data/images --weights yolov5x.pt --conf 0.25 --save-txt --save-conf --save-crop


```


# 转onnx
```bash
pip install onnx

python export.py --weights yolov5s.pt --include onnx


python detect.py --weights yolov5s.onnx
```