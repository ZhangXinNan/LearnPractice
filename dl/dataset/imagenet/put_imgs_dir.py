

import os
import argparse
import shutil

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--val_dir', default='D:/data_public/imagenet/ILSVRC2012_img_val')
    parser.add_argument('--val_file', default='val.txt')
    parser.add_argument('--synsets_file', default='synsets.txt')
    parser.add_argument('--out_dir', default='D:/data_public/imagenet/ILSVRC2012_img_val_dir')
    parser.add_argument('--val_file_dir', default='val_dir.txt')
    return parser.parse_args()

def main(args):
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)
    # 读取文件夹名称列表
    label_dirname_list = []
    with open(args.synsets_file, 'r') as fi:
        label_dirname_list = [s.strip() for s in fi.readlines()]

    # 打开输出文件列表
    val_file_new = open(args.val_file_dir, 'w')
    # 读取文件与label列表
    with open(args.val_file, 'r') as fi:
        for s in fi.readlines():
            s = s.strip()
            arr = s.split(' ')
            if len(arr) < 2:
                print(s, 'len(arr) < 2', arr)
                continue
            label = int(arr[1])                 # label
            filename = arr[0]                   # 文件名
            dirname = label_dirname_list[label] # 文件夹名
            out_dir_new = os.path.join(args.out_dir, dirname) # 存放文件夹
            if not os.path.isdir(out_dir_new):
                os.makedirs(out_dir_new)
            src_file = os.path.join(args.val_dir, filename)
            dst_file = os.path.join(args.out_dir, dirname, filename)
            shutil.copyfile(src_file, dst_file)
            print(src_file, dst_file)
            val_file_new.write(dst_file + ' ' + str(label) + '\n')
    val_file_new.close()


if __name__ == '__main__':
    main(get_args())


