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
    N = len(l) - 1
    for i in range(N ** 2):
        swap(l, randint(0, N), randint(0, N))
    return l


class Complexity(object):
    def __init__(self):
        self.comparisons = 0
        self.assignments = 0

    def increase_comparisons(self, i=1):
        self.comparisons += i

    def increase_assignments(self, i=1):
        self.assignments += i
