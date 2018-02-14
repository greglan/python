# !/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack(list):
    """
    This is a simple stack implementation using a Python list
    """
    def empty(self):
        return not self
    
    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.empty():
            return self.pop()
        else:
            raise Exception("Empty stack")
