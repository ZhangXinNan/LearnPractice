

import os
import argparse
import numpy as np
import cv2
import json
import random
import math


def get_img_path_list(img_dir):
    img_list = []
    for filename in os.listdir(img_dir):
        basename, suffix = os.path.splitext(filename)
        if suffix.lower() not in ['.jpg', '.png', '.jpeg']:
            continue
        img_list.append(os.path.join(img_dir, filename))
    return img_list



def get_img_path_map(img_dir, img_map={}):
    if img_map is None:
        img_map = {}
    for filename in os.listdir(img_dir):
        basename, suffix = os.path.splitext(filename)
        if suffix.lower() not in ['.jpg', '.png', '.jpeg']:
            continue
        if basename in img_map:
            print(basename, " exists !!!!!!")
            continue
        img_map[basename] = os.path.join(img_dir, filename)
    return img_map


def dist_point(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def crop_img_by_quad(image, box):
    w = int(max(dist_point(box[0], box[1], box[2], box[3]),
                dist_point(box[4], box[5], box[6], box[7])) + 0.5)
    h = int(max(dist_point(box[0], box[1], box[6], box[7]),
                dist_point(box[4], box[5], box[2], box[3])) + 0.5)
    pts1 = np.array(box, dtype=np.float32).reshape(4, 2)
    pts2 = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
    M = cv2.getPerspectiveTransform(pts1, pts2)
    im = cv2.warpPerspective(image, M, (w, h), flags=cv2.INTER_CUBIC)
    return im


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir1', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/train_full_images_0')
    parser.add_argument('--img_dir2', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/train_full_images_1')
    parser.add_argument('--label_json', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/train_full_labels.json')
    parser.add_argument('--out_train_dir', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/train')
    parser.add_argument('--out_val_dir', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/val')
    parser.add_argument('--out_train_dir_ver', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/train_ver')
    parser.add_argument('--out_val_dir_ver', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/val_ver')
    parser.add_argument('--out_dir', default='/Users/zhangxin/data_public/1-ICDAR2019-LSVT/')
    return parser.parse_args()


def main(args):
    if not os.path.isdir(args.out_train_dir):
        os.makedirs(args.out_train_dir)
    if not os.path.isdir(args.out_val_dir):
        os.makedirs(args.out_val_dir)
    if not os.path.isdir(args.out_train_dir_ver):
        os.makedirs(args.out_train_dir_ver)
    if not os.path.isdir(args.out_val_dir_ver):
        os.makedirs(args.out_val_dir_ver)
    
    # img_path_list = get_img_path_list(args.img_dir1)
    # print("img_path_list size :", len(img_path_list))
    # img_path_list += get_img_path_list(args.img_dir2)
    # print("img_path_list size :", len(img_path_list))
    img_path_dict = {}
    get_img_path_map(args.img_dir1, img_path_dict)
    print("img_path_dict size :", len(img_path_dict))
    get_img_path_map(args.img_dir2, img_path_dict)
    print("img_path_dict size :", len(img_path_dict))

    fo_train = open(os.path.join(args.out_dir, 'train.txt'), 'w')
    fo_val = open(os.path.join(args.out_dir, 'val.txt'), 'w')
    fo_train_ver = open(os.path.join(args.out_dir, 'train_ver.txt'), 'w')
    fo_val_ver = open(os.path.join(args.out_dir, 'val_ver.txt'), 'w')

    with open(args.label_json, encoding='utf-8') as fi:
        annot = json.load(fi)
        print(type(annot), len(annot))

        for basename, boxes in annot.items():
            if basename not in img_path_dict:
                print(basename, ' is not in lable_json')
                continue
            img = cv2.imread(img_path_dict[basename], 1)
            print(img.shape)
            for i, box in enumerate(boxes):
                trans = box['transcription']
                pts = [int(x) for pt in box['points'] for x in pt]
                print(trans, pts)
                if trans == '###' or len(pts) != 8:
                    continue
                top_line = math.sqrt((pts[0] - pts[2]) ** 2 + (pts[1] - pts[3]) ** 2)
                left_line = math.sqrt((pts[0] - pts[6]) ** 2 + (pts[1] - pts[7]) ** 2)
                img_text = crop_img_by_quad(img, pts)
                print(img_text.shape, top_line, left_line)
                if random.randint(0, 999) % 10 == 5:
                    if top_line >= left_line:
                        img_save_path = os.path.join(args.out_val_dir, "{}.{}.jpg".format(basename, i))
                        fo_val.write(os.path.sep.join(img_save_path.split(os.path.sep)[-2:]) + '\t' + trans + '\n')
                    else:
                        img_save_path = os.path.join(args.out_val_dir_ver, "{}.{}.jpg".format(basename, i))
                        fo_val_ver.write(os.path.sep.join(img_save_path.split(os.path.sep)[-2:]) + '\t' + trans + '\n')
                else:
                    if top_line >= left_line:
                        img_save_path = os.path.join(args.out_train_dir, "{}.{}.jpg".format(basename, i))
                        fo_train.write(os.path.sep.join(img_save_path.split(os.path.sep)[-2:]) + '\t' + trans + '\n')
                    else:
                        img_save_path = os.path.join(args.out_train_dir_ver, "{}.{}.jpg".format(basename, i))
                        fo_train_ver.write(os.path.sep.join(img_save_path.split(os.path.sep)[-2:]) + '\t' + trans + '\n')
                cv2.imwrite(img_save_path, img_text)
            # break

    fo_train.close()
    fo_val.close()
    fo_train_ver.close()
    fo_val_ver.close()


if __name__ == '__main__':
    main(get_args())

    