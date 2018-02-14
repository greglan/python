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


# FIXME: remove this class and use a good lib. Move this code to a file dedicated to minHeaps ?
class BinaryMinHeap(list):
    """
        Binary heap.
        Root index starts at 1.
        
        Todo:
            Comments
    """
    def __init__(self):
        self.data = [0]
        self.size = 0
    
    def __repr__(self):
        return str(self.data)
    
    def __getMinChildIndex(self, i):
        if 2*i > self.size:
            return i
        elif 2*i+1 > self.size:
            return 2*i
        else:
            if self.data[2*i] < self.data[2*i+1]:
                return 2*i
            else:
                return 2*i+1
    
    def empty(self):
        return self.size == 0
    
    def insert(self, e):
        self.data.append(e)
        self.size += 1
        
        currentIndex = self.size
        parentIndex = currentIndex // 2
        
        while self.data[currentIndex] < self.data[parentIndex] and parentIndex > 0:
            self.data[currentIndex], self.data[parentIndex] = self.data[parentIndex], self.data[currentIndex]
            currentIndex = parentIndex
            parentIndex = currentIndex // 2
    
    def get(self):
        if self.size == 0:
            print("Empty heap min")
            return None
        minNode = self.data[1]
        self.data[1] = self.data[self.size]
        self.data.pop()
        self.size -= 1
        
        if self.size > 0:
            currentIndex = 1
            minChildIndex = self.__getMinChildIndex(currentIndex)
            
            while self.data[currentIndex] > self.data[minChildIndex]:
                self.data[currentIndex], self.data[minChildIndex] = self.data[minChildIndex], self.data[currentIndex]
                currentIndex = minChildIndex
                minChildIndex = self.__getMinChildIndex(currentIndex)
        return minNode
