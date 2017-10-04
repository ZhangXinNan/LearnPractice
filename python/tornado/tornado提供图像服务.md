服务器端代码：
```
#encoding=utf8
"""
程序功能: 接收 post 请求, 检测图片中的汽车
post请求体: form-data body
输入:
    图片文件base64编码
输出:
    result
 
"""
import os
import time
# import sys
import base64
import json
import argparse
import logging
import random
# import numpy as np
# # import cv2
# from PIL import Image
import tornado.ioloop
import tornado.web
import tornado.httpserver
# from tornado.options import define, options
# 8092 提供post服务请求
# define("port", default=8094, help="--port", type=int)
 
imgtempdir = './tmp/'
log_dir = './log'
 
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
            return {'message':'no image_base64'}
        # 从base64 编码得到图像文件
        try:
            imgfile = base64.b64decode(image_base64)
        except:
            return {'message':'base64.b64decode error'}
 
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
            return {'message':'write temp img file error'}
 
        result = {}
        result['message'] = 'OK'
        result['result'] = {}
        logging.info(str(result))
        return result
 
    def get(self):
        self.write(json.dumps(self.recog()))
    def post(self):
        self.write(json.dumps(self.recog()))
    def data_received(self, chunk):
        """data received
        """
        pass
 
def main(args):
    """main function
    """
    strtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    if not os.path.isdir(imgtempdir):
        os.mkdir(imgtempdir)
    filename = strtime + '.service_demo.' + str(args.port) + ".log"
    logging.basicConfig(
        filename=os.path.join(log_dir, filename),
        level=logging.INFO,
        format='[%(levelname)s] (%(process)d) (%(threadName)-10s) %(message)s',
    )
 
    logging.info("Listen...")
    # tornado.options.parse_command_line()
    application = tornado.web.Application([(r"/service_demo", MainGetHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(args.port)
    tornado.ioloop.IOLoop.instance().start()
 
 
def get_args():
    '''get args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=9123, type=int)
    return parser.parse_args()
 
if __name__ == "__main__":
    main(get_args())
```


客户端代码：
```
#encoding=utf8
import sys
# import os
# import time
import base64
import argparse
import json
import requests
import cv2
 
reload(sys)
sys.setdefaultencoding('utf8')
 
 
def get_args():
    '''get args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', default="../image/1.jpg")
    return parser.parse_args()
 
def main():
    '''main function
    '''
    args = get_args()
    in_file = args.image
 
    # post imagefile
    host = "http://127.0.0.1:9123/service_demo"
    img_file = open(in_file, "rb").read()
 
    data = {}
    data["image_base64"] = base64.b64encode(img_file)
 
    result = requests.post(host, json=data)
    print result
    result = json.loads(result.text)
    print result
 
 
if __name__ == "__main__":
    main()
```