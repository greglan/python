# -*- coding: utf-8 -*-


from algorithms.sorting.utils import *


def insertion_sort(t):
    operations = Complexity()
    n = len(t)
    
    for i in range(n):
        operations.assignments += 1
        j = i
        
        while j > 0 and t[j] < t[j-1]:
            operations.comparisons += 2
            operations.assignments += 2
            swap(t, j, j-1)
            operations.assignments += 1
            j -= 1

        operations.comparisons += 2
        
    return t, operations
    

def insertion_sort(t):
    operations = Complexity()
    n = len(t)
    
    for i in range(n):
        operations.assignments += 2

        k = t[i]
        j = i
        
        while j > 0 and k < t[j-1]:
            operations.comparisons += 2
            operations.assignments += 2
            t[j] = t[j-1]
            j -= 1

        operations.comparisons += 2
        operations.assignments += 1

        t[j] = k

    return t, operations
