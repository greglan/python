# !/usr/bin/env python
# -*- coding: utf-8 -*-


class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        representation = str(self.data)
        current_node = self

        while current_node.next is not None:
            current_node = current_node.next
            representation += " -> " + str(current_node.data)

        return representation

    def __repr__(self): return self.__str__()

    def size(self):
        size = 1
        current_node = self

        while current_node.next is not None:
            current_node = current_node.next
            size += 1

        return size

    def append(self, value):
        """
        Append the value to the end of the list
        :return: None
        """
        current_node = self

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = SinglyLinkedListNode(value)


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Empty"
        else:
            s = ""
            current_node = self.head
            while current_node.next is not None:
                s += str(current_node.data) + " -> "
                current_node = current_node.next

            return s + str(current_node.data)

    def __repr__(self): return self.__str__()

    def size(self):
        n = 0
        current_node = self.head

        while current_node is not None:
            n += 1
            current_node = current_node.next

        return n

    def append(self, data):
        new_node = SinglyLinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def delete(self, index):
        current_index = 0
        parent = self.head
        current_node = self.head

        while current_index < index and parent.next is not None and current_node.next is not None:
            parent = current_node
            current_node = current_node.next
            current_index += 1

        # Node to delete if the first node
        if parent == current_node:
            self.head = current_node.next
        else:
            parent.next = current_node.next
