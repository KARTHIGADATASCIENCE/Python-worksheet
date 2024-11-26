# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:39:40 2024

@author: 1mscds24
"""

def signal(colour):
    switcher={
            "red":"stop",
            "yellow":"slow down",
            "green":"go"
            }
    return switcher.get(colour,"invalid index")