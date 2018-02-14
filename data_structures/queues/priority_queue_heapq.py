# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is a simple wrapper using the heapq library
"""
from heapq import heappush, heappop


class PriorityQueue_heapq():
    def __init__(self):
        self.data = []
    
    def empty(self):
        return self.data == []
    
    def put(self, e):
        heappush(self.data, e)
    
    def get(self):
        if not self.empty():
            return heappop(self.data)
        else:
            raise Exception("Empty queue")
