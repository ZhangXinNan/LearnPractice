
'''
cfg = {
    "input_size": (3, 48, 256),
    "epoch": 1,
    "batch_size": 64,
    "learning_rate": 0.0001,
    
    "label_max_len": -1,
    "classify_num": -1,
    "train_list": "/home/aistudio/data/train_label.txt",
    "label_list": "/home/aistudio/data/label_list.txt",
    "data_path": "/home/aistudio/data/train_images",
    "infer_data_path": "/home/aistudio/data/test_images",
    "checkpoint_path": "/home/aistudio/work/output/final",
    "save_dir": "/home/aistudio/work/output",
}
'''

import os
# in_dir = '/media/zhangxin/DATA/data_public/OCR/paddle_competition'
in_dir = "/home/zhangxin/data_public/OCR/paddle_competition"
cfg = {
    "input_size": (3, 48, 256),
    "epoch": 100,
    "batch_size": 64,
    "learning_rate": 0.0001,

    "label_max_len": 100,
    "classify_num": 3096,
    "train_list": os.path.join(in_dir, "SkLXRq6Q/train_label.txt"),
    "label_list": os.path.join(in_dir, "SkLXRq6Q/label_list.txt"),
    "data_path": os.path.join(in_dir, "SkLXRq6Q/train_images"),
    "infer_data_path": os.path.join(in_dir, '51vG7A8E/test_images'),
    "checkpoint_path": os.path.join(in_dir, "work/output/final"),
    "save_dir": os.path.join(in_dir, "work/output"),
}