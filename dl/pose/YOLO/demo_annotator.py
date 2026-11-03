
import os
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import cv2

# 1. 加载模型并预测
model = YOLO("yolo26n-pose.pt")
# results = model("https://ultralytics.com/images/bus.jpg")
img_path = "https://ultralytics.com/images/bus.jpg"
results = model(img_path)
print(type(results), len(results))
 
# 2. 遍历结果
for result in results:
    # 获取原始图像 (numpy array)
    im = result.orig_img.copy()
    # 初始化 Annotator
    # line_width: 线条宽度, font_size: 字体大小
    annotator = Annotator(im, line_width=2, font_size=0.5)
    # 获取关键点数据
    # kpts shape: (num_persons, num_kpts, 3) -> (x, y, confidence)
    kpts = result.keypoints
    print(type(kpts), len(kpts))

    # 遍历每个人    
    for id, kpt in enumerate(kpts):
        print(id, type(kpt))
        # 绘制骨架 (连接线)
        # kpts.connect 会自动根据 COCO 格式连接关键点        
        annotator.kpts(kpt, kpt_line=True)
        # 绘制检测框 (可选)
        box = result.boxes[id]
        label = f"Person {id+1}: {box.conf[0]:.2f}"
        annotator.box_label(box.xyxy[0], label, color=colors(id, True))
    # 3. 获取绘制后的图像并显示
    annotated_im = annotator.result()
    # cv2.imshow("Custom Pose", annotated_im)
    # cv2.waitKey(0)
    cv2.imwrite(os.path.basename(img_path) + ".result.opencv.jpg", im)



