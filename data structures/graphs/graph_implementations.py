# -*- coding: utf-8 -*-
# !/usr/bin/env python



## Data definitions
# Priority Queue: ok.
# Stack: Update stack when faster alternative found.
# Check if order is not overflowed.
# Add vertex method
# Test connexité
# Calculs composantes connexes
# Conversion directed graph to undirected
# Detection of cycles
# See caml file.
##




## Init
infinity = float('inf')
from heapq import heappush, heappop



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
            
            

class priorityQueue():
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




## Graph implementations
class graph_uul():
    """
    Undirected unweighted graph by an adjacency list
    """
    def __init__(self, n):
        self.data = [[] for i in range(n)]
        self.order = n

    def __repr__(self):
        return repr(self.data)
        
    def getOrder(self):
        return self.order
    
    def getNeighbors(self, i):
        """ Returns the list of neighbors of vertice i """
        return self.data[i]
    
    def getAdjacencyList(self):
        return self.data

    def add(self, i, j):
        """ Add an edge between vertice i and vertice j """
        self.data[i].append(j)
        self.data[j].append(i)

    def delete(self, i, j):
        """ Delete an edge between vertice i and vertice j """
        self.data[i].remove(j)
        self.data[j].remove(i)



class graph_uwl():
    """
    Undirected weighted graph by an adjacency list.
    Uses infinity constant for two vertices that are not neighbors.
    
    """
    def __init__(self, n):
        self.data = [[infinity for j in range(n)] for i in range(n)]
        self.order = n

    def __repr__(self):
        return repr(self.data)
        
    def getOrder(self):
        return self.order
    
    def getNeighbors(self, i):
        """ Returns the list of neighbors of vertice i """
        return [j for j in range(self.order) if self.data[i][j] != infinity ]

    def getAdjacencyList(self):
        return self.data
    
    def getWeight(self, i, j):
        """ Returns the weight of the edge between i and j """
        return self.data[i][j]

    def add(self, i, j, w):
        """ Add an edge between vertice i and vertice j of weight w """
        self.data[i][j] = w
        self.data[j][i] = w

    def delete(self, i, j):
        """ Delete an edge between vertice i and vertice j """
        self.data[i][j] = infinity
        self.data[j][i] = infinity



## Tests
def test_graph():
    g = []
    g = graph_uwl(6)
    g.add(0,1,1)
    g.add(0,5,3)
    g.add(0,2,7)
    g.add(1,2,1)
    g.add(1,5,1)
    g.add(5,3,2)
    g.add(5,4,5)
    g.add(3,4,2)
    return g
