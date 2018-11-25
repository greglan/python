# !/usr/bin/env python
# -*- coding: utf-8 -*-


class BinarySearchTree:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.del_method = True  # True for predecessor

    def search(self, data):
        if data < self.data:
            if self.left_child is None:
                return False
            else:
                return self.left_child.search(data)
        elif self.data < data:
            if self.right_child is None:
                return False
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

    def delete(self, value):
        # Use an imperative search algorithm to find the node to delete
        target_node = self
        parent = target_node

        while target_node is not None:
            if value < target_node.data:
                parent = target_node
                target_node = self.left_child
            elif target_node.data < value:
                parent = target_node
                target_node = self.right_child
            else:
                break

        # The node to delete is a leaf
        if target_node.left_child is None and target_node.right_child is None:
            # Delete target_node by detaching it from its parent
            if parent.left_child == target_node:
                parent.left_child = None
            elif parent.right_child == target_node:
                parent.right_child = None
            else:  # target_node is the root
                parent = None
        
        # The node to delete has no left child
        elif target_node.left_child is None:
            # Replace target_node by its right child
            if parent.left_child == target_node:
                parent.left_child = target_node.right_child
            else:
                parent.right_child = target_node.right_child
        
        # The node to delete has no right child
        elif target_node.right_child is None:
            # Replace target_node by its left child
            if parent.left_child == target_node:
                parent.left_child = target_node.left_child
            else:
                parent.right_child = target_node.left_child
        
        # The node to delete has two children
        else:
            if self.del_method:
                self.__swap_with_predecessor()
            else:
                self.__swap_with_successor()

    def __swap_with_predecessor(self):
        parent = self
        child = self.left_child
        
        # Find predecessor in left subtree
        while child.right_child is not None:
            parent = child
            child = child.right_child
        predecessor = child
        
        # Swap values
        self.data = predecessor.data
        
        # Remove the predecessor
        if parent is not None:
            # The node to delete was not the root
            parent.right_child = predecessor.left_child
        else:
            parent.left_child = None












