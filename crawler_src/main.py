# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 2022

@author: vhanzlik
"""


import requests
from helpers import log
from helpers import arg_parser
import time



if __name__ == '__main__':

    logger = log.setup_logging("pokus.log")
    logger.debug('Start ===========================')

    try:
        parser = arg_parser.create_parser()
        args = parser.parse_args()

        print(args)
    except KeyboardInterrupt:
        logger.debug('požadavek na ukončení')
        