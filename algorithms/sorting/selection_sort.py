# -*- coding: utf-8 -*-


from algorithms.sorting.utils import *


def selection_sort(t):
    C = Complexity()
    n = len(t)
    
    for i in range(n):
        C.increase_assignments()
        min_index = i
        for j in range(i+1, n):
            C.increase_comparisons()
            if t[j] < t[min_index]:
                C.increase_assignments()
                min_index = j
        C.increase_assignments(2)
        swap(t, i, min_index)
    
    return t, C