# -*- coding: utf-8 -*-


from utils import *

def insertion_sort(t):
    """
        2 assignements instead of 1 in the loop
    """
    C = Complexity()
    N = len(t)
    
    for i in range(N):
        C.increase_assignements()
        j = i
        
        C.increase_comparisons(2)
        while j > 0 and t[j]<t[j-1]:
            C.increase_assignements(2)
            swap(t, j, j-1)
            C.increase_assignements()
            j -= 1
        
    return t, C
    

def insertion_sort(t):
    C = Complexity()
    N = len(t)
    
    for i in range(N):
        C.increase_assignements(2)
        k = t[i]
        j = i
        
        C.increase_comparisons(2)
        while j > 0 and k<t[j-1]:
            C.increase_assignements(2)
            t[j] = t[j-1]
            j -= 1
        
        C.increase_assignements()
        t[j] = k
    return t, C