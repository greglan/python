# -*- coding: utf-8 -*-


from utils import *

def selection_sort(t):
    C = Complexity()
    N = len(t)
    
    for i in range(N):
        C.increase_assignements()
        minIndex = i
        for j in range(i+1, N):
            C.increase_comparisons()
            if t[j] < t[minIndex]:
                C.increase_assignements()
                minIndex = j
        C.increase_assignements(2)
        swap(t, i, minIndex)
    
    return t, C