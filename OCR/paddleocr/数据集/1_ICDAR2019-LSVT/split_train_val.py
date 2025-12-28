
import os
import argparse
import json
import random


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir',
                        default="/Users/zhangxin/data_public/OCR/1_ICDAR2019-LSVT"
                        )
    # parser.add_argument('--ratio', type=float, default=0.2)
    parser.add_argument('--val_num', default=5000, type=int)
    parser.add_argument('--test_num', default=1000, type=int)
    return parser.parse_args()


def main(args):
    t1 = "train_full_images_0"
    t2 = "train_full_images_1"
    fo_train = open(os.path.join(args.in_dir, f'train.txt'), 'w', encoding='utf-8')
    fo_val = open(os.path.join(args.in_dir, f'val.txt'), 'w', encoding='utf-8')
    fo_test = open(os.path.join(args.in_dir, f'test.txt'), 'w', encoding='utf-8')
    json_path = os.path.join(args.in_dir, "train_full_labels.json")

    train_num = 0
    val_num = 0
    test_num = 0
    with open(json_path, 'r', encoding='utf-8') as fi:
        data = json.loads(fi.read())
        print(len(data), type(data))
        ks = list(data.keys())
        random.shuffle(ks)

        i = 0
        for k in ks:
            if os.path.isfile(os.path.join(args.in_dir, t1, k + ".jpg")):
                dir_name = t1
            elif os.path.isfile(os.path.join(args.in_dir, t2, k + ".jpg")):
                dir_name = t2
            else:
                print(f'{k}.jpg is not a file !!!')
                continue
            v = data[k]
            if i < args.test_num:
                fo_test.write(os.path.join(dir_name, k + ".jpg") + "\t" + json.dumps(v) + "\n")
                test_num += 1
            elif i < args.test_num + args.val_num:
                fo_val.write(os.path.join(dir_name, k + ".jpg") + "\t" + json.dumps(v) + "\n")
                val_num += 1
            else:
                fo_train.write(os.path.join(dir_name, k + ".jpg") + "\t" + json.dumps(v) + "\n")
                train_num += 1
            i += 1

    fo_train.close()
    fo_val.close()
    fo_test.close()
    print(train_num, val_num, test_num)


if __name__ == '__main__':
    main(get_args())





