# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 11:44:33 2024

@author: 1mscds24
"""

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key <arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[12,31,45,5]
sort_arr=insertion_sort(arr)
print(sort_arr)    