
import os
import time
import numpy as np
import cv2
import math
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--angle', type=float)
    parser.add_argument('--out_dir', default='/Users/zhangxin/data_md/zhangxin/20200525idcard-1.result2')
    return parser.parse_args()


def main(args):
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    image = cv2.imread(args.input)
    print("image.shape : ", image.shape)
    if args.angle < -45 or args.angle > 45:
        image = cv2.flip(cv2.transpose(image), 0)
        print("image.shape : ", image.shape)
        
    save_path = os.path.join(args.out_dir, os.path.basename(args.input))
    cv2.imwrite(save_path, image)


if __name__ == "__main__":
    main(get_args())


