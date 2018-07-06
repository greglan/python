# -*- coding: utf-8 -*-
# !/usr/bin/env python

import matplotlib.pyplot as plt

from algorithms.sorting.utils import randomize
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.selection_sort import selection_sort
from algorithms.sorting.insertion_sort import insertion_sort


def plot_assignments(assignments):
    plt.figure()
    x = range(1, N + 1)
    for algorithm in assignments:
        plt.plot(x, assignments[algorithm], label=algorithm)
    plt.title("Number of assignments")
    plt.xlabel("Length of list")
    plt.ylabel("Number of assignments")
    plt.legend()
    plt.show()


def plot_comparisons(comparisons):
    plt.figure()
    x = range(1, N + 1)
    for algorithm in comparisons:
        plt.plot(x, comparisons[algorithm], label=algorithm)
    plt.title("Number of comparisons")
    plt.xlabel("Length of list")
    plt.ylabel("Number of comparisons")
    plt.legend()
    plt.show()


def plot_operations(operations):
    plt.figure()
    x = range(1, N + 1)
    for algorithm in operations:
        plt.plot(x, operations[algorithm], label=algorithm)
    plt.title("Number of operations")
    plt.xlabel("Length of list")
    plt.ylabel("Number of operations")
    plt.legend()
    plt.show()


N = 100  # Max length of the lists
STEP = 5  # Step between each list length
SAMPLES = 10  # Number of list to sort for a given length

algorithms = {
    "bubble_sort": bubble_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort
}

assignments = {}
comparisons = {}
operations = {}

for alg in algorithms.keys():
    assignments[alg] = []
    comparisons[alg] = []
    operations[alg] = []


for list_length in range(1, N + 1):
    src = [i for i in range(list_length)]

    # Sort the lists for each algorithm
    for alg in algorithms.keys():
        mean_assignments = 0
        mean_comparisons = 0
        mean_operations = 0

        for i in range(SAMPLES):
            sample = randomize(src)
            _, complexities = algorithms[alg](sample)
            mean_assignments += complexities.assignments
            mean_comparisons += complexities.comparisons
            mean_operations += complexities.operations

        assignments[alg].append(mean_assignments / SAMPLES)
        comparisons[alg].append(mean_comparisons / SAMPLES)
        operations[alg].append(mean_operations / SAMPLES)


plot_assignments(assignments)
plot_comparisons(comparisons)
plot_operations(operations)
