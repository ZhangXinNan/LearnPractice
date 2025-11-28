
import os
import argparse
import json


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num', type=int, default=100)
    return parser.parse_args()


def main(args):
    in_dir = "/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT"
    # t1 = os.path.join(in_dir, "test_part1_images")
    # t2 = os.path.join(in_dir, "test_part2_images")
    t1 = "train_full_images_0"
    t2 = "train_full_images_1"
    fo = open(os.path.join(in_dir, f'train_{args.num}.txt'), 'w', encoding='utf-8')
    json_path = os.path.join(in_dir, "train_full_labels.json")

    n = 0
    with open(json_path, 'r', encoding='utf-8') as fi:
        data = json.loads(fi.read())
        print(len(data), type(data))
        for k, v in data.items():
            # print(k, v)
            img_path = os.path.join(in_dir, t1, k + ".jpg")
            if os.path.isfile(img_path):
                fo.write(os.path.join(t1, k + ".jpg") + "\t" + json.dumps(v) + "\n")
                n += 1
            else:
                img_path = os.path.join(in_dir, t2, k + ".jpg")
                if os.path.isfile(img_path):
                    fo.write(os.path.join(t2, k + ".jpg") + "\t" + json.dumps(v) + "\n")
                    n += 1
            if n > args.num:
                break

    fo.close()


if __name__ == '__main__':
    main(get_args())





