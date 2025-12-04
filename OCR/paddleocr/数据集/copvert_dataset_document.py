



import os
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir',
                        default="/home/zhangxin/data_public/OCR/4_Chinese-Document-Text-Recognition/DataSet")
    parser.add_argument('--num', default=10000, type=int)
    return parser.parse_args()


def main(args):
    fo = open(os.path.join(args.in_dir, f"train_{args.num}.txt"), 'w', encoding='utf-8')
    with open(os.path.join(args.in_dir, "labels.txt"), 'r', encoding='utf-8') as fi:
        n = 0
        for line in fi:
            arr = line.strip().split('\t')
            if len(arr) != 2:
                continue
            img_path = os.path.join(args.in_dir, 'images', arr[2])
            if not os.path.isfile(img_path):
                continue
            fo.write(f"{os.path.join('images', arr[2])}\t{arr[3]}\n")
            n += 1
            if n > args.num:
                break
    fo.close()  


if __name__ == '__main__':
    main(get_args())







