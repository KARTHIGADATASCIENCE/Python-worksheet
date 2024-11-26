# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:49:23 2024

@author: 1mscds24
"""

def day_week(day_number):
    switcher ={
            1:"sunday",
            2:"monday",
            3:"tuesday",
            4:"wedensday",
            5:"thursday",
            6:"friday",
            7:"saturday"
            }
    return switcher.get(day_number,"invalid day number")