
import os
import argparse
import json


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir',
                        default='/Users/zhangxin/data_public/OCR/2_ICDAR2017-RCTW-17/RCTW')
    parser.add_argument('--num', default=100, type=int)
    return parser.parse_args()


def main(args):
    fo = open(os.path.join(args.in_dir, f"train_{args.num}.txt"), 'w', encoding='utf-8')
    img_dir = os.path.join(args.in_dir, "train_images")
    gts_dir = os.path.join(args.in_dir, "train_gts")
    n = 0
    for filename in os.listdir(gts_dir):
        name, suffix = os.path.splitext(filename)
        if suffix != ".txt":
            continue
        img_path = os.path.join(img_dir, name + ".jpg")
        if not os.path.isfile(img_path):
            continue
        gt_file = os.path.join(gts_dir, filename)
        text_line_list = []
        with open(gt_file, "r", encoding='utf-8') as fi:
            for line in fi:
                arr = line.strip().split(',')
                if len(arr) < 10:
                    continue
                box = [[arr[i * 2], arr[i * 2 + 1]] for i in range(4)]
                text_line_list.append({"transcription": arr[9], "points": box})
        if len(text_line_list) > 0:
            n += 1
        if n > args.num:
            break
        fo.write(f"train_images/{name}.jpg\t{json.dumps(text_line_list)}\n")
    fo.close()


if __name__ == '__main__':
    main(get_args())



