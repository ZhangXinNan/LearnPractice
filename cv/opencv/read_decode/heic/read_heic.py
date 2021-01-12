



import os
import argparse
import whatimage
import pyheif
from io import BytesIO
from PIL import Image


def read_image_heif(img_file, to_fmt='JPEG'):
    heif_file = pyheif.read(img_file)
    image = Image.frombytes(heif_file.mode,
                            heif_file.size,
                            heif_file.data,
                            "raw",
                            heif_file.mode,
                            heif_file.stride,
                            )
    with BytesIO() as out:
        image.save(out, format=to_fmt)
        img_file = out.getvalue()
    return img_file



def change_fmt(img_path, out_dir, to_fmt='JPEG', suffix='.jpg'):
    basename, _ = os.path.splitext(os.path.basename(img_path))
    out_path = os.path.join(out_dir, basename + suffix)

    img_file = open(img_path, 'rb').read()
    fmt = whatimage.identify_image(img_file)
    if fmt in ['heic']:
        img_file = read_image_heif(img_file)
        with open(out_path, 'wb') as fo:
            fo.write(img_file)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='/Users/zhangxin/data_public/yaohe/heic')
    parser.add_argument('--out_dir', default='/Users/zhangxin/data_public/yaohe/jpg')
    return parser.parse_args()


def main(args):
    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    if os.path.isfile(args.input):
        change_fmt(args.input, args.out_dir)
    elif os.path.isdir(args.input):
        for filename in os.listdir(args.input):
            if filename[0] == '.':
                continue
            img_path = os.path.join(args.input, filename)
            change_fmt(img_path, args.out_dir)


if __name__ == '__main__':
    main(get_args())
