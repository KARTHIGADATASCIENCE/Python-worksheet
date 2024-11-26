# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 11:47:16 2024

@author: 1mscds24
"""

import sys
def cli_parser(com):
    switcher={
            'start':'starting',
            'stop':'finish',
            'restart':'restart the pp'
            }
    return switcher.get(com,"unknown")