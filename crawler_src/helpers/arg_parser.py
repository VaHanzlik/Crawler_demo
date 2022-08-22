# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 10:46:40 2022

@author: vhanzlik
"""

import argparse

def create_parser():
    """Returns argument parser """

    parser = argparse.ArgumentParser(
        description =
            'Searches all url links in provided webpage.' \
            'By default the depth of searching is the third link.'
    )

    parser.add_argument(
        '--output-file',
        '-o',
        dest ='output_name',
        default = 'seznam.json',
        help = 'Output file name. By default it is set to seznam.json',
    )

    parser.add_argument(
        '--debug',
        '-b',
        dest ='debug',
        action ='store_true',
        help ='Turns on the debug mode logging'
    )

    parser.add_argument(
        '--log-file',
        dest = 'log_filename',
        default = 'def_log.log',
        help = 'Log file name, by default def_log.log',
    )
    parser.add_argument(
        '--input-address',
        '-i',
        dest = 'input_addr',
        default = 'www.seznam.cz',
        help =
            'Web page from which should the Crawler start',
    )
    parser.add_argument(
        '--depth',
        '-d',
        dest = 'depth',
        default = '3',
        help =
            'The depth of webpages search.' \
            'Default is 3',
    )

    return parser
