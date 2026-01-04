
import os
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default='/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/test.txt')
    parser.add_argument('--output',
                        default='/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/test_cls.txt')
    return parser.parse_args()


def main(args):
    fo = open(args.output, 'w', encoding='utf-8')
    with open(args.input, 'r', encoding='utf-8') as fi:
        for line in fi:
            arr = line.strip().split('\t')
            if len(arr) != 2:
                continue
            fo.write(f"{arr[0]}\t0\n")
    fo.close()


if __name__ == '__main__':
    main(get_args())
