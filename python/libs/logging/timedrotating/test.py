#encoding=utf8
import time
import logging
import logging.handlers
 
# logging初始化工作
logging.basicConfig()
 
# nor的初始化工作
nor = logging.getLogger("nor")
nor.setLevel(logging.INFO)
 
# 添加TimedRotatingFileHandler到nor
# 定义一个1分钟换一次log文件的handler
filehandler = logging.handlers.TimedRotatingFileHandler(
        "logging_test2", 'M', 1, 0)
# 设置后缀名称，跟strftime的格式一样
filehandler.suffix = "%Y%m%d-%H%M.log"
nor.addHandler(filehandler)


for i in range(300):
    time.sleep(1)
    st = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    nor.info(st)
    # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
