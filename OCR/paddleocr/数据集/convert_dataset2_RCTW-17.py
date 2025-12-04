
import os
import argparse
import json
import numpy as np
import cv2


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir',
                        default='/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW')
    parser.add_argument('--num', default=1000, type=int)
    parser.add_argument('--max_size', type=int, default=2048)
    return parser.parse_args()


def main(args):
    fo = open(os.path.join(args.in_dir, f"train_{args.max_size}_{args.num}.txt"), 'w', encoding='utf-8')
    img_dir = os.path.join(args.in_dir, "train_images")
    gts_dir = os.path.join(args.in_dir, "train_gts")
    out_img_dir = os.path.join(args.in_dir, f'train_images_{args.max_size}_{args.num}')
    if not os.path.isdir(out_img_dir):
        os.makedirs(out_img_dir)

    n = 0
    for filename in os.listdir(gts_dir):
        name, suffix = os.path.splitext(filename)
        if suffix != ".txt":
            continue
        img_path = os.path.join(img_dir, name + ".jpg")
        if not os.path.isfile(img_path):
            continue
        img = cv2.imread(img_path, cv2.IMREAD_COLOR)
        h, w = img.shape[:2]
        scale = 1.0
        if w >= h and w > args.max_size:
            new_w = args.max_size
            new_h = int(args.max_size * h / w)
            img = cv2.resize(img, (new_w, new_h))
            scale = args.max_size / w
        elif h > w and h > args.max_size:
            new_h = args.max_size
            new_w = int(args.max_size * w / h)
            img = cv2.resize(img, (new_w, new_h))
            scale = args.max_size / h
        cv2.imwrite(os.path.join(out_img_dir, name + ".jpg"), img)
    
        gt_file = os.path.join(gts_dir, filename)
        text_line_list = []
        with open(gt_file, "r", encoding='utf-8') as fi:
            for line in fi:
                arr = line.strip().split(',')
                if len(arr) < 10:
                    continue
                arr[:8] = [round(float(x) * scale) for x in arr[:8]]
                box = [[arr[i * 2], arr[i * 2 + 1]] for i in range(4)]
                text_line_list.append({"transcription": arr[9], "points": box})
        if len(text_line_list) > 0:
            n += 1
        else:
            continue
        fo.write(f"train_images_{args.max_size}_{args.num}/{name}.jpg\t{json.dumps(text_line_list)}\n")

        if n >= args.num:
            break
    fo.close()


if __name__ == '__main__':
    main(get_args())



