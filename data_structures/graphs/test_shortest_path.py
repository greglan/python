from unittest import TestCase

from data_structures.graphs.shortest_path import *


class TestShortestPath(TestCase):
    def setUp(self):
        self.test_graphs = []

        self.g1 = [[1, 2], [3, 4], [], [], []]
        self.test_graphs.append(self.g1)

    def test_distances_from(self):
        d = distances_from(self.g1, 0)
        self.assertListEqual(d, [0, 1, 1, 2, 2])

    def test_path_from(self):
        pass

    def test_bellman_ford(self):
        pass

    def test_dijkstra(self):
        pass

    def test_floyd_warshall(self):
        g = {0: {1: 1, 2: 2}, 1: {3: 3, 2: 2}}
        d, p = floyd_warshall(g)
        self.assertListEqual(d, [])
        self.assertListEqual()

