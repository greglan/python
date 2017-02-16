# -*- coding: utf-8 -*-
# !/usr/bin/env python



## Searches
# Recursive bfs?
##
from graph_implementations import *



def dfs_lrec(g, start):
    """
    Recursive Depth First Search for adjacency list
    
    Returns:
        None
    """
    def aux(g, vertice):
        visited.append(vertice)
        print(vertice)

        for neighbor in g.getNeighbors(vertice):
            if neighbor not in visited:
                aux(g, neighbor)
                visited.append(neighbor)

    visited = []
    aux(g, start)


def dfs_limp(g, start):
    """
     Imperative Depth First Search for adjacency list
    
    Returns:
        None
    """
    visited = []
    stack = Stack()
    stack.push(start)

    while not stack.empty():
        cur_vertice = stack.pop()
        
        if cur_vertice not in visited:
            visited.append(cur_vertice)
            print(cur_vertice)
    
            for neighbor in g.getNeighbors(cur_vertice):
                stack.push(neighbor)


def bfs_l(g, start):
    """
    Breadth First Search for adjacency list
    
    Returns:
        None
    """
    
    q = Queue()
    visited = []
    q.put(start)

    while not q.empty():
        current_vertice = q.get()

        if current_vertice not in visited:
            visited.append(current_vertice)
            print(current_vertice)

            for neighbor in g.getNeighbors(current_vertice):
                q.put(neighbor)