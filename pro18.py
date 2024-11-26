# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:56:04 2024

@author: 1mscds24
"""
def tempconverter(scale,temp):
    if scale=='c_to_f' :
        return(temp*9/5)+32
    elif scale=='f_to_c':
        return(temp-32)*5/9
    else:
        return "invalid scale"