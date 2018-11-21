import torch
import torchvision

from torch.utils.data import Dataset
from PIL import Image


class ImageNetData(Dataset):
    def __init__(self, gt_file, transforms=None):
        with open(gt_file, 'r') as f:
            self.lines = f.readlines()
        if transforms:
            self.transforms = transforms
        print('data length: ', len(self.lines))

    def __getitem__(self, index):
        line_split = self.lines[index].strip().split()
        if len(line_split) != 2:
            print(len(line_split))
        img_path = line_split[0]
        label = int(line_split[-1])
        # print(index, label)
        img = Image.open(img_path)
        img = img.convert('RGB')
        if self.transforms:
            img = self.transforms(img)
        # label = torch.LongTensor([label])
        # print(img.shape, label)
        # sample = {'img': img, 'label': label}
        img *= 255
        return img, label

    def __len__(self):
        return len(self.lines)
