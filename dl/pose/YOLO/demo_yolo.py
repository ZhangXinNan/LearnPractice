
import os
import numpy as np
import cv2
from ultralytics import YOLO


# COCO 骨架连接索引对 (例如：鼻子连左眼，鼻子连右眼...)
SKELETON = [
    [16, 14], [14, 12], [17, 15], [15, 13], [12, 13], [6, 12], [7, 13], 
    [6, 7], [6, 8], [7, 9], [8, 10], [9, 11], [2, 3], [1, 2], [1, 3], 
    [2, 4], [3, 5], [4, 6], [5, 7]
]



# Load a model
model = YOLO("yolo26n-pose.pt")  # load an official model
# model = YOLO("path/to/best.pt")  # load a custom model

# Predict with the model
img_path = "https://ultralytics.com/images/bus.jpg"
results = model(img_path)  # predict on an image

# Access the results
for result in results:
    xy = result.keypoints.xy  # x and y coordinates
    xyn = result.keypoints.xyn  # normalized
    kpts = result.keypoints.data  # x, y, visibility (if available)
    print(type(xy), xy.shape)
    print(type(xyn), xyn.shape)
    print(type(kpts), kpts.shape)

    # .plot() 会返回一张绘制了关键点和骨架的 BGR 图像 (numpy array)
    # 你可以直接传入参数，例如 boxes=False 隐藏检测框，只显示骨架
    im_array = result.plot(boxes=True, conf=True) 

    # 4. 显示或保存图像
    # cv2.imshow("YOLO Pose Estimation", im_array)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # 如果需要保存
    cv2.imwrite(os.path.basename(img_path) + ".result.yolo.jpg", im_array)

