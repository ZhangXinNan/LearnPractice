import os
import numpy as np
from paddle.io import Dataset
import numpy as np
from paddle.vision.transforms import Compose, ColorJitter, Resize, RandomRotation, Normalize
import cv2
from cfg import cfg


def preprocess(img):
    transform = Compose([
        ColorJitter(0.2, 0.2, 0.2, 0.2),
        Resize(size=(48, 256)),
        RandomRotation(5)
        ])
    img = transform(img).reshape(cfg["input_size"]).astype("float32")
    return img / 255.


class Reader(Dataset):
    def __init__(self, data, is_val=False):
        super().__init__()
        # 划分训练集和测试集
        self.samples = data[-int(len(data)*0.2):] if is_val else data[:-int(len(data)*0.2)]

    def __getitem__(self, idx):
        # 处理图像
        img = self.samples[idx][0]
        img_path = os.path.join(cfg["data_path"], img)
        img = cv2.imread(img_path)
        img = preprocess(img)
        # 处理标签
        label = self.samples[idx][1]
        temp_label = list()
        for c in label:
            with open(cfg["label_list"]) as f:
                for line in f:
                    k, v = line.strip("\n").split("\t")
                    if c == k:
                        temp_label.append(v)
        # 用blank填充label
        label = np.ones(cfg["label_max_len"]+1, dtype="int32") * (cfg["classify_num"]-1)
        label[: len(temp_label)] = np.array(temp_label, dtype="int32")
        return img, label

    def __len__(self):
        # 返回每个Epoch中图片数量
        return len(self.samples)



