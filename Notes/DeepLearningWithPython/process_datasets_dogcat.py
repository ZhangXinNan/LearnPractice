

import os, shutil
import argparse
import random

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir', default='D:/data_public/dog-cats/train')
    parser.add_argument('--out_dir', default='D:/data_public/dog-cats/big_datasets')
    parser.add_argument('--train_num', default=10000, type=int)
    parser.add_argument('--val_num', default=2000, type=int)
    parser.add_argument('--test_num', default=500, type=int)
    return parser.parse_args()


def copy_files(files, dst_dir):
    print(len(files), ' copy to ', dst_dir)
    if not os.path.isdir(dst_dir):
        os.makedirs(dst_dir)
    for img in files:
        shutil.copy(img, dst_dir)


def main(args):
    # cat : 0,  dog : 1
    cats = []
    dogs = []
    for i in range(12500):
        cats.append(os.path.join(args.in_dir, 'cat.%d.jpg' % i))
        dogs.append(os.path.join(args.in_dir, 'dog.%d.jpg' % i))
    random.shuffle(cats)
    random.shuffle(dogs)

    b, e = 0, args.train_num
    copy_files(cats[b:e], os.path.join(args.out_dir, 'train', 'cats'))
    copy_files(dogs[b:e], os.path.join(args.out_dir, 'train', 'dogs'))
    b, e = e, e + args.val_num
    copy_files(cats[b:e], os.path.join(args.out_dir, 'val', 'cats'))
    copy_files(dogs[b:e], os.path.join(args.out_dir, 'val', 'dogs'))
    b, e = e, e + args.test_num
    copy_files(cats[b:e], os.path.join(args.out_dir, 'test', 'cats'))
    copy_files(dogs[b:e], os.path.join(args.out_dir, 'test', 'dogs'))


if __name__ == '__main__':
    main(get_args())

