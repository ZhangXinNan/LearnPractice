
import os
import argparse
import csv



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir', default='/media/zhangxin/DATA/data_public/OCR/paddle_competition/train')
    parser.add_argument('--out_dir', default='./')
    return parser.parse_args()


def main(args):
    csv_file = os.path.join(args.in_dir, 'train_label.csv')
    '''
    with open(csv_file, 'r', encoding='utf-8') as fi:
        for line in fi:
            print(line)
            break
    '''
    with open(csv_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main(get_args())





