# -*- coding: utf-8 -*-


from .utils import *


def selection_sort(t):
    C = Complexity()
    N = len(t)
    
    for i in range(N):
        C.increase_assignments()
        min_index = i
        for j in range(i+1, N):
            C.increase_comparisons()
            if t[j] < t[min_index]:
                C.increase_assignments()
                min_index = j
        C.increase_assignments(2)
        swap(t, i, min_index)
    
    return t, C