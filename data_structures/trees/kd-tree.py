# -*- coding: utf-8 -*-
# !/usr/bin/env python


class KDTree:
    def __init__(self, points):
        self.dimension = len(points[0])
        self.root = KDTreeNode(points[0], self.dimension, 0)

        for point in points[1:]:
            self.root.insert(point)

    def insert(self, element):
        self.root.insert(element)

    def delete(self):
        pass

    def __str__(self):
        return self.root.__str__()


class KDTreeNode:
    def __init__(self, x, dimension, dimension_index):
        self.root = x
        self.dimension = dimension
        self.dimension_index = dimension_index
        self.lChild = None
        self.rChild = None

    def insert(self, u):
        if u[self.dimension_index] < self.root[self.dimension_index]:
            if self.lChild is None:
                self.lChild = KDTreeNode(u, self.dimension, (self.dimension_index + 1) % self.dimension)
            else:
                self.lChild.insert(u)
        else:
            if self.rChild is None:
                self.rChild = KDTreeNode(u, self.dimension, (self.dimension_index + 1) % self.dimension)
            else:
                self.rChild.insert(u)

    def __str__(self):
        return str(self.root) + '\n' + self.lChild.__str__() + '\n' + self.rChild.__str__()


def test():
    t_2D = KDTree([(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)])
    # t_2D.insert((0,0))
    print(t_2D)

test()