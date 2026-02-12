
import os
import argparse
import csv
import random


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir', default='/home/zhangxin/data_public/OCR/paddle_competition/SkLXRq6Q')
    # parser.add_argument('--out_dir', default='./')
    return parser.parse_args()


def main(args):
    csv_file = os.path.join(args.in_dir, 'train_label.csv')
    '''
    with open(csv_file, 'r', encoding='utf-8') as fi:
        for line in fi:
            print(line)
            break
    '''
    input_file = os.path.join(args.in_dir, 'train_label.txt')
    with open(input_file, newline='') as fi:
        lines = fi.readlines()
        random.shuffle(lines)
        val_num = int(len(lines) * 0.2)
        print(len(lines), val_num)
    with open(os.path.join(args.in_dir, 'val.txt'), 'w', encoding='utf-8') as fo:
        for line in lines[:val_num]:
            fo.write(line)
    with open(os.path.join(args.in_dir, 'train.txt'), 'w', encoding='utf-8') as fo:
        for line in lines[val_num:]:
            fo.write(line)



if __name__ == '__main__':
    main(get_args())





