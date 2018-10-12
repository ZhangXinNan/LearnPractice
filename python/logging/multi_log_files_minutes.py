import logging
import time

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
formatter2 = logging.Formatter("%(message)s")

def setup_logger(name, log_file, level=logging.INFO, format=formatter):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(format)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# first file logger
logger = setup_logger('first_logger', 'first_logfile.log')
logger.info('This is just info message')

# second file logger
super_logger = setup_logger('second_logger', 'second_logfile.log')
super_logger.error('This is an error message')
super_logger.info('aaabbbccc')

logger3 = setup_logger('third_logger', '3rd.log', format=formatter2)
logger3.info('abc123')
logger3.info('567890')

str_time_now = time.strftime("%Y%m%d_%H%M%S", time.localtime())
logfilename = str_time_now + '.log'
logging.basicConfig(
                    filename=logfilename,
                    level=logging.DEBUG,
                    format="%(message)s",)
logging.info('logging 0000001')
logging.info('logging 0000002')