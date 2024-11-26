# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:54:34 2024

@author: 1mscds24
"""

def calculator(operation,a,b):
    switcher={
            'add':a+b,
            'sub':a-b,
            'multi':a*b,
            'divide':a/b
            if b!=0 
            else 'error:division by zero'
            }
    return switcher.get(operation,"invalid operation")
