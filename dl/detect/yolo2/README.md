# 代码
[marvis/pytorch-yolo2](https://github.com/marvis/pytorch-yolo2)

# 文章
[YOLO2](https://zhuanlan.zhihu.com/p/25167153)
[YOLOv2 论文笔记](https://blog.csdn.net/jesse_mx/article/details/53925356)




```
# 检测不到
python detect_cpu.py ~/data_public/yolo/darknet/yolo2coco/yolov2-tiny.cfg ~/data_public/yolo/darknet/yolo2coco/yolov2-tiny.weights data/dog.jpg
# 正常，检测狗、自行车、车
python detect_cpu.py ~/data_public/yolo/darknet/yolo2coco/yolov2.cfg ~/data_public/yolo/darknet/yolo2coco/yolov2.weights data/dog.jpg
# 没检测到
python detect_cpu.py ~/data_public/yolo/darknet/yolo2voc/yolov2-voc.cfg ~/data_public/yolo/darknet/yolo2voc/yolov2-voc.weights data/dog.jpg
# 检测到狗和车
python detect_cpu.py ~/data_public/yolo/darknet/yolo2voc/yolov2-tiny-voc.cfg ~/data_public/yolo/darknet/yolo2voc/yolov2-tiny-voc.weights data/dog.jpg
```