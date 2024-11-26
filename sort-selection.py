# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 12:07:01 2024

@author: 1mscds24
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr    
arr=[64,25,11,3,89]
sort_arr=selection_sort(arr)
print(sort_arr)
                