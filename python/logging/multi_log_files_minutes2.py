from __future__ import absolute_import
import time
import logging

def setup_logger(logger_name, log_file, level=logging.INFO):
    l = logging.getLogger(logger_name)
    formatter = logging.Formatter('%(asctime)s : %(message)s')
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)    

def main():
    l1 = '' 
    l2 = ''
    log1 = None
    log2 = None
    for i in range(300):
	logfile1 = time.strftime("log_error_%Y%m%d_%H%M", time.localtime())
	logfile2 = time.strftime("log_info_%Y%m%d_%H%M", time.localtime())
	#if l1 != logfile1:
	setup_logger('log_error', logfile1)
    	log1 = logging.getLogger('log_error')
	#    l1 = logfile1
	#if l2 != logfile2:
	#    setup_logger('log_info', logfile2)
    	#    log2 = logging.getLogger('log_info')
	#    l2 = logfile2
    	log1.info('Info for log 1!')
    	#log2.info('Info for log 2!')
    	# log1.error('Oh, no! Something went wrong!')
	time.sleep(1)

if '__main__' == __name__:
    main()
