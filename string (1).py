# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:47:33 2024

@author: 1mscds24
"""

def is_pal(x):
    return x==x[::-1]
samp="malayalam"
print(f"is'{samp}'a palindrome?",is_pal(samp))