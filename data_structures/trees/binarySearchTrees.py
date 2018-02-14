# !/usr/bin/env python
# -*- coding: utf-8 -*-


class BinarySearchTree:
    """
    """
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        """
        Indicates whether or not the current tree is a leaf.
        :return: bool
        """
        return (self.left_child is None) and (self.right_child is None) and (self.data is not None)

    def search(self, data):
        if self.is_leaf() and self.data == data:
            return data
        else:
            if data < self.data:
                if self.left_child is None:
                    return None
                else:
                    return self.left_child.search(data)
            elif self.data < data:
                if self.right_child is None:
                    return None
                else:
                    return self.right_child.search(data)
            else:
                return data

    def insert(self, data):
        """
        Insert the given data in the tree. Recursive method.
        :return: None
        """
        if self.data is None:
            self.data = data
        else:
            if self.is_leaf():
                if data < self.data:
                    self.left_child = BinarySearchTree(data)
                else:
                    self.right_child = BinarySearchTree(data)
            else:
                if data < self.data:
                    if self.left_child is not None:
                        self.left_child.insert(data)
                    else:
                        self.left_child = BinarySearchTree(data)
                else:
                    if self.right_child is not None:
                        self.right_child.insert(data)
                    else:
                        self.right_child = BinarySearchTree(data)

    def get_min(self):
        if self.is_leaf():
            return self.data
        else:
            if self.left_child is None:
                return self.data
            else:
                return self.left_child.get_min()

    def get_max(self):
        if self.is_leaf():
            return self.data
        else:
            if self.right_child is None:
                return self.data
            else:
                return self.right_child.get_max()

    def delete(self, data):
        min_child = self.get_min(self.right_child)
        self.right_child.delete(min_child)
