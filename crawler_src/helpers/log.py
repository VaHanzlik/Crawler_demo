# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:46:40 2022

@author: vhanzlik
"""


from datetime import datetime
import time
import os

## Init logging start 
import logging
import logging.handlers

def setup_logging(path:str="", filename:str="", debug = False):
    """Adds a configured stream handler to the root logger"""

    print("print in my_logger.logger_init()")
    print("print my_logger.py __name__: " +__name__)
    if path == "":
        path = "log/"
    if filename == "":
        filename = "my_log_test.log"
    
    ## get logger
    logger = logging.getLogger() ## root logger
    if debug == True:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # File handler
    logfilename = datetime.now().strftime("%Y%m%d_%H%M%S") + f"_{filename}"
    file = logging.handlers.TimedRotatingFileHandler(f"{path}{logfilename}", when="midnight", interval=1)
    fileformat = logging.Formatter("%(asctime)s [%(levelname)s]: %(name)s: %(message)s")
    if debug == True:
        file.setLevel(logging.DEBUG)
    else:
        file.setLevel(logging.INFO)
    file.setFormatter(fileformat)

    # Stream handler
    stream = logging.StreamHandler()
    
    streamformat = logging.Formatter("%(asctime)s [%(levelname)s]: %(name)s: %(message)s")
    if debug == True:
        stream.setLevel(logging.DEBUG)
    else:
        stream.setLevel(logging.INFO)
    
    stream.setFormatter(streamformat)

    # Adding all handlers to the logs
    logger.addHandler(file)
    logger.addHandler(stream)

