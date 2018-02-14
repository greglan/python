# !/usr/bin/env python
# -*- coding: utf-8 -*-


class PriorityQueueSorted():
    """
    Priority queue with a list
    
    The insertion is done by inserting the element directly at the right place.
    """
    def __init__(self):
        self.data = []
        self.length = 0
    
    def __repr__(self):
        return repr(self.data)
    
    def empty(self):
        return not self.data
    
    def put(self, element):
        """ Insert an element at the right place """
        i=0
        while i < self.length:
            e = self.data[i]
            if element < e:
                self.data = self.data[:i] + [element] + self.data[i:]
                i = self.length
            i+=1
        if i == self.length:
            self.data.append(element)
        
        self.length+=1
    
    def get(self):
        try:
            self.length -= 1
            return self.data.pop(0)
        except IndexError:
            self.length += 1
            raise Exception("Empty queue")


class PriorityQueueSearched():
    """
        Priority queue with a list
    
        The insertion is done at the end, and the get method has to find the element requested.
    """
    def __init__(self):
        self.data = [] 
        self.length = 0
    
    def __repr__(self):
        return repr(self.data)
    
    def empty(self):
        return self.length == 0
    
    def put(self, element):
        """ Insert an element at the end """
        self.data = self.data + [element]
        self.length += 1
    
    def get(self):
        if self.length == 0:
            raise Exception("Empty queue")        
        else:
            min_element = self.data[0]
            min_i = 0
            
            for i in range(0, self.length):
                element = self.data[i]
                if element < min_element:
                    min_element = element
                    min_i = i
            
            self.data = self.data[:min_i] + self.data[min_i+1:]
            self.length -= 1
            return min_element
            return self.data.pop(0)
