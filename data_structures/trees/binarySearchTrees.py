# !/usr/bin/env python
# -*- coding: utf-8 -*-


class BinarySearchTree:
    """
    """
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def search(self, data):
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
            return True

    def insert(self, data):
        """
        Insert the given data in the tree. Recursive method.
        :return: None
        """
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left_child is None:
                    self.left_child = BinarySearchTree(data)
                else:
                    self.left_child.insert(data)

            else:
                if self.right_child is None:
                    self.right_child = BinarySearchTree(data)
                else:
                    self.right_child.insert(data)

    def get_min(self):
        if self.left_child is None:
            return self.data
        else:
            return self.left_child.get_min()

    def get_max(self):
        if self.right_child is None:
            return self.data
        else:
            return self.right_child.get_max()

    def delete(self, data):
        # TODO
        min_child = self.get_min(self.right_child)
        self.right_child.delete(min_child)
