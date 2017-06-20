# -*- coding: utf-8 -*-
# !/usr/bin/env python

# Not tested
#  TODO: add tests
#  TODO: comment
#  TODO: finish delete func and test

class binarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.lChild = None
        self.rChild = None

    def isLeaf(self):
        return (self.lChild is None) and (self.rChild is None)

    def insert(self, data):
        """
        Insert the given data in the tree. Recursive method.
        :param data: 
        :return: 
        """
        if self.isLeaf():
            if data < self.data:
                self.lChild = binarySearchTree(data)
            else:
                self.rChild = binarySearchTree(data)
        else:
            if data < self.data:
                if self.lChild is not None:
                    self.lChild.insert(data)
                else:
                    self.lChild = binarySearchTree(data)
            else:
                if self.rChild is not None:
                    self.rChild.insert(data)
                else:
                    self.rChild = binarySearchTree(data)

    def search(self, data):
        if self.isLeaf():
            return None
        else:
            if data < self.data:
                if self.lChild is None:
                    return None
                else:
                    return self.lChild.search(data)
            elif self.data < data:
                if self.rChild is None:
                    return None
                else:
                    return self.rChild.search(data)
            else:
                return data

    def getMin(self):
        if self.isLeaf():
            return self.data
        else:
            if self.lChild is None:
                return self.data
            else:
                return self.lChild.getMin()

    def getMax(self):
        if self.isLeaf():
            return self.data
        else:
            if self.rChild is None:
                return self.data
            else:
                return self.rChild.getMax()

    def delete(self, data):
        min_child = self.getMin(self.rChild)
        self.rChild.delete(min_child)
