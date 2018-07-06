# -*- coding: utf-8 -*-


from algorithms.sorting.utils import *


def insertion_sort(t):
    C = Complexity()
    n = len(t)
    
    for i in range(n):
        C.increase_assignments()
        j = i
        
        while j > 0 and t[j] < t[j-1]:
            C.increase_comparisons(2)
            C.increase_assignments(2)
            swap(t, j, j-1)
            C.increase_assignments()
            j -= 1

        C.increase_comparisons(2)
        
    return t, C
    

def insertion_sort(t):
    C = Complexity()
    n = len(t)
    
    for i in range(n):
        C.increase_assignments(2)
        k = t[i]
        j = i
        
        while j > 0 and k < t[j-1]:
            C.increase_comparisons(2)
            C.increase_assignments(2)
            t[j] = t[j-1]
            j -= 1
        C.increase_comparisons(2)
        
        C.increase_assignments()
        t[j] = k
    return t, C