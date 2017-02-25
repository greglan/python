# -*- coding: utf-8 -*-
# !/usr/bin/env python


## Todo
# Binary Heap implementation
# Priority queue implementation using binary heap
##


class Queue(list):
    """ Simple queue implementation """
    def empty(self):
        return not self
    
    def put(self, item):
        self.append(item)

    def get(self):
        try:
            return self.pop(0)
        except IndexError:
            raise Exception("Empty queue")




class priorityQueue_sorted():
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



class priorityQueue_searched():
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



from heapq import heappush, heappop
class priorityQueue_heapq():
    def __init__(self):
        self.data = []
    
    def empty(self):
        return self.data == []
    
    def put(self, e):
        heappush(self.data, e)
    
    def get(self):
        if not self.empty():
            return heappop(self.data)
        else:
            raise Exception("Empty queue")
            
            


class priorityQueue_binaryHeap(list):
    """
    Priority queue using a binary heap.
    """
    def __init__(self):
        self.data = binaryMinHeap()
    
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


class binaryMinHeap(list):
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



def test():
    t = priorityQueue_heapq()
    t.put(3)
    t.put(2)
    t.put(5)
    t.put(9)
    t.put(7)
    t.put(2)
    return t