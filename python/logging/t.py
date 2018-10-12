import logging
import time

logging.basicConfig(
    filename='t.log',
    level=logging.INFO,
    format='[%(levelname)s] (%(threadName)-10s)  %(message)s',
)


logging.info(('Starting ', time.time()))
time.sleep(2)
logging.info(('End ', time.time()))
