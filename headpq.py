# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 12:00:59 2024

@author: 1mscds24
"""

import heapq
class solution(object):
    def nth_ugly_number(self,n):
        ugly_num=0
        heap=[]
        heapq.heappush(heap,1)
        for _ in range(n):
            ugly_num=heapq.heappop(heap)
            if ugly_num%2==0:
                heapq.heappush(heap,ugly_num*2)
            elif ugly_num%3==0:
                heapq.heappush(heap,ugly_num*3)
            else:
                 heapq.heappush(heap,ugly_num*2)
                 heapq.heappush(heap,ugly_num*3)
                 heapq.heappush(heap,ugly_num*5)
        return ugly_num
n=11
s=solution()
result=s.nth_ugly_number(n)
print("7th ugly no is:")
print(result)
n=1
result=s.nth_ugly_number(n)
print("10th ugly no is:")
print(result)