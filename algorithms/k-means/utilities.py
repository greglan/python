# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import sqrt
import distance
import numpy as np
import random


def read_data(filename, skip_first_line=False, ignore_first_column=False, data_type='points'):
    """
    Loads data from a csv file and returns the corresponding list. See provided input files for format convention.

    :param filename: csv file name.

    :param skip_first_line: if True, the first line is not read. Default value: False.

    :param ignore_first_column: if True, the first column is ignored. Default value: False.

    :param data_type: either 'points' or 'words'.

    :return: a list of data.
    """

    f = open(filename, 'r')
    if skip_first_line:
        f.readline()

    data = []

    if data_type == 'points':
        for line in f:
            line = line.split(",")
            line[1:] = [float(x) for x in line[1:]]
            if ignore_first_column:
                line = line[1:]
            data.append(tuple(line))
    else:
        for line in f:
            line = line.split(' ')
            data.append(line[0].strip())
    f.close()
    return data


def write_data(data, filename):
    """
    Writes data in a csv file.

    :param data: a list of lists
    :param filename: the path of the file in which data is written.
    The file is created if necessary; if it exists, it is overwritten.
    """
    # If you're curious, look at python's module csv instead, which offers
    # more powerful means to write (and read!) csv files.
    f = open(filename, 'w')
    for item in data:
        f.write(','.join([repr(x) for x in item]))
        f.write('\n')
    f.close()


def generate_random_data(nb_objs, nb_attrs):
    """
    Generates a matrix of random data.
    :param nb_attrs: the dimension of the data
    :type nb_attrs: int
    :return: a matrix with nb_objs rows and nb_attrs+1 columns.
    The 1st column is filled with line numbers (integers, from 1 to nb_objs).
    """
    data = []
    for i in range(nb_objs):
        line = [i + 1] + list(map(lambda x: random.random(), range(nb_attrs)))
        data.append(tuple(line))
    return data


def generate_random_gaussian_data(nb_objs, nb_attrs, k):
    """
    Generate k cluster of points following a gaussian repartition.
    :param nb_objs: total number of points to generate
    :param nb_attrs:
    :param k: The number of groups to create.
    :return:
    """
    data = []

    centers = generate_random_data(k, nb_attrs)

    centers = np.array(centers)
    centers = centers[:, 1:]

    for i in range(nb_objs):
        center = centers[random.randint(0, len(centers) - 1)]
        line = [i + 1] + list(map(lambda x: random.gauss(x, 0.05), center))
        # line = [i+1, random.gauss(center[j],1) for j in range(len(center))]
        data.append(line)
    return data


def write_solution(filename, solution):
    f = open(filename, 'w')
    k = 1  # Cluster index
    i = 1  # Points index

    for cluster in solution:
        for point in cluster:
            s = str(i) + ',' + str(point)[1:-1] + ',' + str(k)
            s = s.replace(' ', '')  # Remove whitespaces
            f.write(s + '\n')
            i += 1
        k += 1
    # f.close()


def write_centers(filename, centers):
    f = open(filename, 'w')
    k = 1  # Center index

    for center in centers:
        s = str(k) + ',' + str(center)[1:-1]
        s = s.replace(' ', '')  # Remove whitespaces
        f.write(s + '\n')
        k += 1
    # f.close()


def display_points_cluster(clusters, centers, dimension):
    """
    Display the cluster using a different color for each cluster. Only 2D and 3D representation are supported.
    :param clusters: List of clusters.
    :param centers: List of centers.
    :param dimension: dimension of the points (2 or 3)
    :return: None
    """
    if dimension == 2:
        for cluster in clusters:
            if cluster != []:
                points = list(zip(*cluster))
                plt.scatter(points[0], points[1], s=10)

        for center in centers:
            plt.scatter(*center, marker='*', s=200, color='black')
        plt.show()

    elif dimension == 3:
        fig = plt.figure()
        ax = Axes3D(fig)

        for cluster in clusters:
            if cluster != []:
                points = list(zip(*cluster))
                ax.scatter(points[0], points[1], points[2], s=10)
        plt.show()

    else:
        raise Exception("Wrong dimension")


def display_words_cluster(C):
    """
    Display the cluster of words.
    :param C: List of clusters.
    :return: None
    """
    for cluster in C:
        print(cluster)


class Distance:
    """
    Implements the different distances available.
    """
    def __init__(self):
        def euclidean(X, Y):
            """
            Returns the euclidean distance between X and Y. No sqrt applied.
            X and Y are tuples of the same dimension.
            """
            if len(X) != len(Y):
                raise Exception("Arguments do not have the same dimension")
            else:
                d = len(X)
                s = 0
                for i in range(d):
                    s += (X[i] - Y[i]) ** 2
                return sqrt(s)

        def levenshtein(X, Y):
            """
            Returns the Levenshtein distance between X and Y.
            X and Y are strings.
            """
            return distance.levenshtein(X, Y, normalized=True)

        self.euclidean = euclidean
        self.levenshtein = levenshtein


class Data:
    """
    Implements the different data available.
    """
    def __init__(self, data, data_type='points'):
        self.data = data
        self.data_type = data_type
