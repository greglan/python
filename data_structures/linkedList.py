# !/usr/bin/env python
# -*- coding: utf-8 -*-


class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node

    def size(self):
        n=0
        current_node = self.head
        
        while current_node is not None:
            n += 1
            current_node = current_node.next
            
        return n

    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            s = '('
            current_node = self.head
            while current_node.next is not None:
                s += str(current_node.data) + " -> "
                current_node = current_node.next

            return s + str(current_node.data) + ')'

    def __repr__(self): return self.__str__()