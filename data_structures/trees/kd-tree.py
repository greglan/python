# -*- coding: utf-8 -*-
# !/usr/bin/env python

class kd_tree:
    def __init__(this, points):
        this.dimension = len(points[0])
        this.root = kd_tree_node(points[0], this.dimension, 0)

        for point in points[1:]:
            this.root.insert(point)

    def insert(this, element):
        this.root.insert(element)

    def delete(this):
        pass

    def __str__(this):
        return this.root.__str__()


class kd_tree_node:
    def __init__(this, x, dimension, dimension_index):
        this.root = x
        this.dimension = dimension
        this.dimension_index = dimension_index
        this.lChild = None
        this.rChild = None

    def insert(this, u):
        if u[this.dimension_index] < this.root[this.dimension_index]:
            if this.lChild == None:
                this.lChild = kd_tree_node(u, this.dimension, (this.dimension_index+1)%this.dimension)
            else:
                this.lChild.insert(u)
        else:
            if this.rChild == None:
                this.rChild = kd_tree_node(u, this.dimension, (this.dimension_index+1)%this.dimension)
            else:
                this.rChild.insert(u)

    def __str__(this):
        return str(this.root)+'\n'+this.lChild.__str__()+'\n'+this.rChild.__str__()


def test():
    t_2D = kd_tree([(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)])
    # t_2D.insert((0,0))
    print(t_2D)

test()