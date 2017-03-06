# -*- coding: utf-8 -*-
# !/usr/bin/env python

# TODO: check if all sorted lists are correct. If not, raise Exception("Sorted lists were not the same")
# TODO: average for each length of list.
# TODO: worst case

import matplotlib.pyplot as plt

from utils import *
import bubble_sort
import selection_sort
import insertion_sort


N=100 # Max length of the lists
algorithms = {
    "bubble_sort": bubble_sort.bubble_sort,
    "selection_sort": selection_sort.selection_sort,
    "insertion_sort": insertion_sort.insertion_sort
}

comparisons = {}
assignements = {}

for alg in algorithms.keys():
    comparisons[alg] = [0]
    assignements[alg] = [0]


for k in range(1, N+1):
    src = [i for i in range(k)]
    sample = randomize(src)
    
    t_sorted = {}
    complexities = {}
    
    for alg in algorithms.keys():
        t_sorted[alg], complexities = algorithms[alg](list(sample))
        comparisons[alg].append(complexities.comparisons)
        assignements[alg].append(complexities.assignements)
    
    


for alg in algorithms.keys():
    x = range(N+1)
    plt.plot(x, assignements[alg], label=alg)
plt.legend()
plt.show()
