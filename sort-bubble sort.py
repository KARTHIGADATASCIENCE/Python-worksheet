# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:06:30 2024

@author: 1mscds24
"""

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range (0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[64,4,25,12,22,11,90]
sort_arr=bubble_sort(arr)
print(sort_arr) 