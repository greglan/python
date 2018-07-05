# -*- coding: utf-8 -*-
# !/usr/bin/env python

import matplotlib.pyplot as plt
from .utils import *
from .bubble_sort import bubble_sort
from .selection_sort import selection_sort
from .insertion_sort import insertion_sort


N = 10000  # Max length of the lists
STEP = 10  # Step between each list length
SAMPLES = 10  # Number of list to sort for a given length

algorithms = {
    "bubble_sort": bubble_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort
}

comparisons = {}
assignments = {}

for alg in algorithms.keys():
    comparisons[alg] = []
    assignments[alg] = []


for list_length in range(1, N + 1):
    src = [i for i in range(list_length)]

    # Sort the lists for each algorithm
    for alg in algorithms.keys():
        mean_comparisons = 0
        mean_assignments = 0

        for i in range(SAMPLES):
            sample = randomize(src)
            _, complexities = algorithms[alg](sample)
            mean_assignments += complexities.comparisons
            mean_comparisons += complexities.assignements

        comparisons[alg].append(mean_assignments / SAMPLES)
        assignments[alg].append(mean_comparisons / SAMPLES)

for algorithm in assignments:
    x = range(1, N+1)
    plt.plot(x, assignments[algorithm], label=algorithm)

plt.legend()
plt.show()
