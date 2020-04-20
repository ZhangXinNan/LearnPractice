#encoding=utf8
from __future__ import print_function
import numpy as np
import os, sys, cv2
import glob
import shutil

import random
import json
import base64
import time
import logging
import argparse
import tornado.ioloop
import tornado.web
import tornado.httpserver


log_dir = './log/'
imgtempdir = './tmp/'


class MainGetHandler(tornado.web.RequestHandler):
    """Main Get Handler
    """
    def recog(self):
        """recive image , return recog result
        """
        logging.info(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # 获取图像的 base64 编码
        params = json.loads(self.request.body)

        if 'image_base64' in params:
            image_base64 = params["image_base64"]
        else:
            return {'message':'no image_base64', 'returncode':10001}
        # 从base64 编码得到图像文件
        try:
            imgfile = base64.b64decode(image_base64)
        except:
            return {'message':'base64.b64decode error', 'returncode':10002}

        # 将图片解码
        # try:
        #     file_bytes = np.asarray(bytearray(imgfile), dtype=np.uint8)
        #     img = cv2.imdecode(file_bytes, cv2.CV_LOAD_IMAGE_UNCHANGED)
        # except:
        #     return {'message':'cv2.imdecode error', 'returncode':10003}

        # 图片写到本地再读取
        strtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        imgfilename = os.path.join(imgtempdir, strtime + str(random.randint(10000, 99999)) + '.jpg')
        logging.info('imgfilename : ' + imgfilename)
        try:
            with open(imgfilename, 'w') as obj:
                obj.write(imgfile)
        except:
            return {'message':'write temp img file error', 'returncode':10003}


        im = cv2.imread(imgfilename)

        result = {}
        result['message'] = 'OK'
        result['returncode'] = 0
        result['result'] = {}

        logging.info(str(result))
        return result

    def get(self):
        self.write(json.dumps(self.recog()))
    def post(self):
        self.write(json.dumps(self.recog()))
    def data_received(self, chunk):
        """data received"""
        pass


def main(args):
    """main function
    """
    strtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    if not os.path.isdir(imgtempdir):
        os.mkdir(imgtempdir)

    filename = os.path.join(log_dir,
                            strtime + '.dmocr_textlines_detect.' + str(args.port) + ".log")
    logging.basicConfig(
        filename=filename,
        level=logging.INFO,
        format='[%(levelname)s] (%(process)d) (%(threadName)-10s) %(message)s',
    )
    print("Listen...")
    # tornado.options.parse_command_line()
    application = tornado.web.Application([(r"/ocr_segment_line", MainGetHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()


def get_args():
    '''get args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=23331, type=int)
    # parser.add_argument('--gpu', default=0, type=int, help='gpu id, TEST_GPU_ID')
    return parser.parse_args()



if __name__ == "__main__":
    main(get_args())
