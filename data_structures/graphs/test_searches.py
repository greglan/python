from unittest import TestCase

from data_structures.graphs.searches import *


class TestSearches(TestCase):
    def setUp(self):
        self.graphs = []

        g = [[1, 2], [3, 4], [], [], []]
        self.graphs.append(g)

        g = [[1, 2], [3, 4], [0], [], []]
        self.graphs.append(g)

        g = [[1, 2], [2, 3, 4], [1], [], []]
        self.graphs.append(g)

    def test_bfs_list(self):
        v, d, p = bfs_list(self.graphs[0], 0)
        self.assertListEqual(v, [0, 1, 2, 3, 4])
        self.assertListEqual(d, [0, 1, 1, 2, 2])
        self.assertListEqual(p, [-1, 0, 0, 1, 1])

        v, d, p = bfs_list(self.graphs[0], 1)
        self.assertListEqual(v, [1, 3, 4])
        self.assertListEqual(d, [float('inf'), 0, float('inf'), 1, 1])
        self.assertListEqual(p, [-1, -1, -1, 1, 1])

    def test_dfs_rec_list(self):
        v = dfs_rec_list(self.graphs[0], 0)
        self.assertListEqual(v, [0, 1, 3, 4, 2])

        v = dfs_rec_list(self.graphs[1], 0)
        self.assertListEqual(v, [0, 1, 3, 4, 2])

        v = dfs_rec_list(self.graphs[2], 0)
        self.assertListEqual(v, [0, 1, 3, 4, 2])

    def test_dfs_imp_list(self):
        v = dfs_imp_list(self.graphs[0], 0)
        self.assertListEqual(v, [0, 2, 1, 4, 3])

        v = dfs_imp_list(self.graphs[1], 0)
        self.assertListEqual(v, [0, 2, 1, 4, 3])

        v = dfs_imp_list(self.graphs[2], 0)
        self.assertListEqual(v, [0, 2, 1, 4, 3])
