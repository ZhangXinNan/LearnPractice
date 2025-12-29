


import os
import argparse
import random


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir',
                        default="/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition")
    parser.add_argument('--val_num', default=30000, type=int)
    parser.add_argument('--test_num', default=10000, type=int)
    return parser.parse_args()


def main(args):
    fo_train = open(os.path.join(args.in_dir, f"train.txt"), 'w', encoding='utf-8')
    fo_test = open(os.path.join(args.in_dir, f"test.txt"), 'w', encoding='utf-8')
    fo_val = open(os.path.join(args.in_dir, f"val.txt"), 'w', encoding='utf-8')
    train_num, test_num, val_num = 0, 0, 0
    with open(os.path.join(args.in_dir, "train.list"), 'r', encoding='utf-8') as fi:
        data = []
        for line in fi:
            arr = line.strip().split('\t')
            if len(arr) < 4:
                continue
            img_path = os.path.join(args.in_dir, 'train_images', arr[2])
            if not os.path.isfile(img_path):
                continue
            data.append([os.path.join('train_images', arr[2]), arr[3]])
        random.shuffle(data)

        for i, x in enumerate(data):
            if i < args.test_num:
                fo_test.write(f"{x[0]}\t{x[1]}\n")
            elif i < args.test_num + args.val_num:
                fo_val.write(f"{x[0]}\t{x[1]}\n")
            else:
                fo_train.write(f"{x[0]}\t{x[1]}\n")

    fo_train.close()
    fo_test.close()
    fo_val.close()


if __name__ == '__main__':
    main(get_args())




