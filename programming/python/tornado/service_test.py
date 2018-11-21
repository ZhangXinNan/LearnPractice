#encoding=utf8
import sys
# import os
# import time
import base64
import argparse
import json
import requests
# import cv2
from PIL import Image

reload(sys)
sys.setdefaultencoding('utf8')


def get_args():
    '''get args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', default="../data/demo/001.jpg")
    # parser.add_argument('--port', default=8094, type=int)
    return parser.parse_args()

def main():
    '''main function
    '''
    args = get_args()
    in_file = args.image

    # post imagefile
    host = "http://127.0.0.1:23331/ocr_segment_line"
    img_file = open(in_file, "rb").read()

    data = {}
    data["image_base64"] = base64.b64encode(img_file)
    data = json.dumps(data)
    result = requests.post(host, data)
    print result
    result = json.loads(result.text)
    print result
    if 'result' not in result:
        return 'there is no result'
    if 'lines' not in result['result']:
        return 'there is no lines in result'
    lines = result['result']['lines']

    import cv2
    img = cv2.imread(args.image, 1)
    # img = Image.open(args.image)
    img_show = cv2.imread(args.image, 1)
    for i, line in enumerate(lines):
        print line
        box = line['box']
        cv2.line(img_show, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 3)
        cv2.line(img_show, (box[0], box[1]), (box[4], box[5]), (255, 0, 0), 3)
        cv2.line(img_show, (box[6], box[7]), (box[2], box[3]), (0, 0, 255), 3)
        cv2.line(img_show, (box[6], box[7]), (box[4], box[5]), (255, 255, 255), 3)
    cv2.imwrite('result.jpg', img_show)
if __name__ == "__main__":
    main()
