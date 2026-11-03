
import os
from ultralytics import YOLO
import cv2
import numpy as np


# COCO 骨架连接索引对 (例如：鼻子连左眼，鼻子连右眼...)
SKELETON = [    [16, 14], [14, 12], [17, 15], [15, 13], [12, 13], [6, 12], [7, 13],     [6, 7], [6, 8], [7, 9], [8, 10], [9, 11], [2, 3], [1, 2], [1, 3],     [2, 4], [3, 5], [4, 6], [5, 7]]

# "yolo11n-pose.pt"
model_name = "yolo26n-pose.pt"
model = YOLO(model_name)
img_path = "https://ultralytics.com/images/bus.jpg"
results = model(img_path)

print(len(results))

for result in results:
    im = result.orig_img.copy()
    kpts = result.keypoints.xy.cpu().numpy() # 获取 x, y 坐标
    conf = result.keypoints.conf.cpu().numpy() # 获取置信度
    for person_kpts, person_conf in zip(kpts, conf):
        # 1. 绘制关键点 (点)
        for i, (x, y) in enumerate(person_kpts):
            if person_conf[i] > 0.5: # 过滤低置信度点
                cv2.circle(im, (int(x), int(y)), 3, (0, 255, 0), -1)
        # 2. 绘制骨架 (线)
        for sk in SKELETON:
            kpt1, kpt2 = sk[0] - 1, sk[1] - 1 # COCO索引从1开始，数组从0开始
            if person_conf[kpt1] > 0.5 and person_conf[kpt2] > 0.5:
                pt1 = (int(person_kpts[kpt1][0]), int(person_kpts[kpt1][1]))
                pt2 = (int(person_kpts[kpt2][0]), int(person_kpts[kpt2][1])) 
                cv2.line(im, pt1, pt2, (255, 0, 0), 2)
    # cv2.imshow("Manual Draw", im)
    # cv2.waitKey(0)
    cv2.imwrite(os.path.basename(img_path) + ".result.opencv.jpg", im)