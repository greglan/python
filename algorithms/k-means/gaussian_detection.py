# -*- coding: utf-8 -*-
# !/usr/bin/env python

"""
This file test a set of points for a gaussian distribution.
"""

import utilities
import matplotlib.pyplot as plt
import scipy.stats as stats

""" Parameters """
POINTS = 5000
DIMENSION = 2
TESTS = 5
CLUSTERS = 2

""" Gaussian test """
for test in range(TESTS):
    data = utilities.generate_random_gaussian_data(POINTS, DIMENSION, CLUSTERS)
    utilities.write_data(data, "in.csv")
    data = utilities.read_data("in.csv", ignore_first_column=True)

    print(stats.anderson_ksamp(data))

    points = list(zip(*data))
    plt.scatter(points[0], points[1])
    plt.show()
