'''
File: logger.py
Project: logger
File Created: Thursday, 30th July 2020 11:08:17 pm
Author: Sparsh Dutta (sparsh.dtt@gmail.com)
-----
Last Modified: Friday, 31st July 2020 1:49:30 am
Modified By: Sparsh Dutta (sparsh.dtt@gmail.com>)
-----
Copyright 2020 Sparsh Dutta
'''

from ..config import LOGGER_OUTPUT_PATH

import sys
import logging

def logger(name=None):
    """[Logger for logging all the details of the program]

    Args:
        name ([type], optional): [description]. Defaults to None.

    Returns:
        [logger]: [description]
    """
    logging.basicConfig(filename=LOGGER_OUTPUT_PATH + 'logs.txt',
                        level=logging.INFO,
                        format="[%(asctime)s] %(levelname)s %(message)s",
                        datefmt="%H:%M:%S")

    logger_function = logging.getLogger(name=name)
    return logger_function