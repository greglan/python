# -*- coding: utf-8 -*-

from random import randint


def swap(l, i, j):
    """
    Swap elements at indexes i and j in list
    :type l: list
    :type i: int
    :type j: int
    :return: None
    """
    l[i], l[j] = l[j], l[i]


def randomize(l):
    n = len(l) - 1
    for i in range(n ** 2):
        swap(l, randint(0, n), randint(0, n))
    return l


class Complexity(object):
    def __init__(self):
        self.assignments = 0
        self.comparisons = 0
        self.operations = 0

    def increase_assignments(self, i=1):
        self.assignments += i
        self.operations += i

    def increase_comparisons(self, i=1):
        self.comparisons += i
        self.operations += i

    def increase_operations(self, i=1):
        self.operations += i
