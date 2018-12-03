# -*- coding: utf-8 -*-


from algorithms.sorting.utils import *


def bubble_sort(t):
    C = Complexity()
    n = len(t)
    
    for i in range(n-1, 0, -1):
        for j in range(0, i):
            C.increase_comparisons()

            if t[j] > t[j+1]:
                C.increase_assignments(2)
                swap(t, j, j+1)
    return t, C
