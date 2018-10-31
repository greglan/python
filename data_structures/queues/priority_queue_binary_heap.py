# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file implements a priority queue using a binary heap.
"""
# TODO: add tests, and test it


class PriorityQueueBinaryHeap(list):
    def __init__(self):
        self.data = BinaryMinHeap()
    
    def __repr__(self):
        l = []
        tmp = self.data
        while not tmp.empty():
            l.append(tmp.get())
        return str(l)
    
    def empty(self):
        return self.length == 0
    
    def put(self, e):
        self.data.insert(e)
    
    def get(self):
        return self.data.get()


# FIXME: use a good lib.
