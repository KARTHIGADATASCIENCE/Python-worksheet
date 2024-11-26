# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 11:42:18 2024

@author: 1mscds24
"""

import math
from io import StringIO
def show_tree(tree,total_width=60,fill=' '):
    output=StringIO()
    last=-1
    for i,n in enumerate(tree):
        if i:
            row=int(math.floor(math.log(i+1,2)))
        else:
            row=0
        if row!=last:
            output.write("\n")
        columns=2**row
        colw=int(math.floor((total_width*1.0/columns)))
        output.write(str(n).center(colw,fill))
        last=row
        print(output.getvalue())
        print('_'*total_width)
        return
    import heapq
    heap=[]
    heapq.heappush(heap,1)
    heapq.heappush(heap,2)
    heapq.heappush(heap,3)
    heapq.heappush(heap,4)
    heapq.heappush(heap,7)
    heapq.heappush(heap,9)
    heapq.heappush(heap,10)
    heapq.heappush(heap,8)
    heapq.heappush(heap,16)
    heapq.heappush(heap,14)
    show_tree(heap) 