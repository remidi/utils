import time
import os
import datetime
import logging
import sys


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)

    formatter = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
    streamhandler = logging.StreamHandler(sys.stdout)
    streamhandler.setFormatter(formatter)
    filehandler = logging.FileHandler('{}.log'.format(logger_name))
    filehandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(streamhandler)
    logger.addHandler(filehandler)

    return logger


def timer(input_func):

    def wrapper(*args, **kwargs):
        ti = time.time()
        input_func(*args, **kwargs)
        print('\n time taken by the function to run ==> {:.2f} mins \n'.format((time.time() - ti)/60))

    return wrapper


def create_timedir(path):
    timedir = str(datetime.datetime.today().strftime('%Y%m%d%H%M'))
    if not os.path.exists(os.path.join(path, timedir)):
        os.makedirs(os.path.join(path, timedir))

    return os.path.join(path, timedir)