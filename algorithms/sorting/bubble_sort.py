# -*- coding: utf-8 -*-

#TODO: Sort with i in range(N)

from utils import *

def bubble_sort(t):
    C = Complexity()
    N = len(t)
    
    for i in range(N-1, 0, -1):
        #for j in range(1, i+1):
        for j in range(0, i):
            
            C.increase_comparisons()
            #if t[j-1] > t[j]:
            if t[j] > t[j+1]:
                C.increase_assignements(2)
                #swap(t, j-1, j)
                swap(t, j, j+1)
    return t, C