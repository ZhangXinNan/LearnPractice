
import os
import argparse
from paddleocr import TextRecognition


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir', default='/home/zhangxin/data_public/OCR/paddle_competition/51vG7A8E/test_images')
    parser.add_argument('--output', default='result.paddleocr.txt')
    return parser.parse_args()


def main(args):
    model = TextRecognition()
    print(model)
    exit()
    fo = open(args.output, 'w', encoding='utf-8')
    for filename in os.listdir(args.in_dir):
        img_path = os.path.join(args.in_dir, filename)
        output = model.predict(input=img_path)
        for res in output:
            res.print()
            # print(type(res), res)
            fo.write(f"{filename}\t{res['rec_text']}\n")
        # break
    fo.close()


if __name__ == '__main__':
    main(get_args())




