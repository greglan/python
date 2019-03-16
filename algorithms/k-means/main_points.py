# -*- coding: utf-8 -*-
# !/usr/bin/env python

from algorithms import *
from utilities import *

""" Parameters """
nPoints = 5000
dimension = 2
nClusters = 5
D = Distance()


""" Points test """
data = generate_random_gaussian_data(nPoints, dimension, 5)
# data = filesManagment.generate_random_data(nPoints, dimension)

write_data(data, "in.csv")
p = read_data("in.csv", ignore_first_column=True)

A = GeneralizedLlyod(p, nClusters, D.euclidean, iter_max=5)
A.run()

B = GeneralizedLlyod_clusterAsCenter(p, nClusters, D.euclidean, iter_max=5)
B.run()

C = GeneralizedLlyod_stopUnchanged(p, nClusters, D.euclidean, iter_max=5)
C.run()

# Display the clusters and the centers. Support dimensions 2 and 3.
display_points_cluster(A.clusters, A.centers, dimension)
display_points_cluster(B.clusters, B.centers, dimension)
display_points_cluster(C.clusters, C.centers, dimension)


# Write the solution
write_solution('out.csv', A.clusters)
write_centers('centers.csv', A.centers)
