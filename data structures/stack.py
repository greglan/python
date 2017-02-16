# -*- coding: utf-8 -*-
# !/usr/bin/env python

## Todo
# Using fast append and pop lib
##

# Fast append and pop func
from collections import deque

class Stack(list):
    def empty(self):
        return not self
    
    def push(self, item):
        self.append(item)

    def get(self, item):
        if not self.empty():
            self.pop()
        else:
            raise Exception("Empty stack")
