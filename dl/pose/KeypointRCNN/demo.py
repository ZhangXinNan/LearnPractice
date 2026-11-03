
from pathlib import Path
import numpy as np
import cv2
import torch
from torchvision.models.detection import keypointrcnn_resnet50_fpn, KeypointRCNN_ResNet50_FPN_Weights
from torchvision.io import decode_image


coco_keypoints = [
    "nose", "left_eye", "right_eye", "left_ear", "right_ear",
    "left_shoulder", "right_shoulder", "left_elbow", "right_elbow",
    "left_wrist", "right_wrist", "left_hip", "right_hip",
    "left_knee", "right_knee", "left_ankle", "right_ankle",
]
'''
nose -> left_eye -> left_ear. (0, 1), (1, 3)
nose -> right_eye -> right_ear. (0, 2), (2, 4)
nose -> left_shoulder -> left_elbow -> left_wrist. (0, 5), (5, 7), (7, 9)
nose -> right_shoulder -> right_elbow -> right_wrist. (0, 6), (6, 8), (8, 10)
left_shoulder -> left_hip -> left_knee -> left_ankle. (5, 11), (11, 13), (13, 15)
right_shoulder -> right_hip -> right_knee -> right_ankle. (6, 12), (12, 14), (14, 16)
'''
connect_skeleton = [
    (0, 1), (0, 2), (1, 3), (2, 4), (0, 5), (0, 6), (5, 7), (6, 8),
    (7, 9), (8, 10), (5, 11), (6, 12), (11, 13), (12, 14), (13, 15), (14, 16)
]


# person_int = decode_image(str(Path("../assets") / "person1.jpg"))

person_int = decode_image(str(Path("../YOLO") / "bus.jpg"))

# weights = KeypointRCNN_ResNet50_FPN_Weights.DEFAULT
weights = KeypointRCNN_ResNet50_FPN_Weights.COCO_LEGACY
transforms = weights.transforms()

person_float = transforms(person_int)

model = keypointrcnn_resnet50_fpn(weights=weights, progress=False)
model = model.eval()

outputs = model([person_float])
print(len(outputs))
# keys boxes, labels, scores, keypoints and keypoint_scores
for k, v in outputs[0].items():
    print(k, type(v), v.shape)

kpts = outputs[0]['keypoints']
scores = outputs[0]['scores']

# print(kpts)
print(scores)

detect_threshold = 0.75
idx = torch.where(scores > detect_threshold)
keypoints = kpts[idx]

print(idx)
print(keypoints.shape)



from torchvision.utils import draw_keypoints

res = draw_keypoints(person_int, keypoints, colors="blue", radius=3)
# show(res)
print(type(res), res.shape)

img = res.permute(1, 2, 0).numpy()
print(type(img), img.shape, img.dtype)
print(cv2.imwrite("result_keypoints.jpg", img))

res = draw_keypoints(person_int, keypoints, connectivity=connect_skeleton, colors="blue", radius=4, width=3)
# show(res)
img = res.permute(1, 2, 0).numpy()
print(type(img), img.shape, img.dtype)
print(cv2.imwrite("result_skeleton.jpg", img))

'''
prediction = kpts
coordinates, visibility = prediction.split([2, 1], dim=-1)
visibility = visibility.bool()

res = draw_keypoints(
    person_int, coordinates, visibility=visibility, connectivity=connect_skeleton, colors="blue", radius=4, width=3
)
# show(res)
img = res.permute(1, 2, 0).numpy()
print(type(img), img.shape, img.dtype)
print(cv2.imwrite("result_skeleton_vis.jpg", img))
'''

