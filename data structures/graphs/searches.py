# -*- coding: utf-8 -*-
# !/usr/bin/env python

import queue
## Searches
# TODO: Recursive bfs?
# TODO: Add comments
# TODO: Add tests

## BFS
def bfs_l(g, s):
    """
    Breadth First Search for adjacency list.
    
    Returns:
        None
    """
    V = []                                                                      # List of visited vertices
    Q = queue.Queue()
    Q.put(s)
    
    while not Q.empty():
        v = Q.get()
        
        if v not in V:
            print(v)
            
            V.append(v)
            
            for u in g[v]:
                Q.put(u)

## DFS
def dfsRec_l(g, s):
    """
    Recursive Depth First Search for adjacency lists
    
    Returns:
        None
    """
    
    def visit(v):
        print(v)
        V.append(v)
        for u in g[v]:
            if u not in V:
                visit(u)
    
    V = []                                                                      # List of visited vertices
    visit(s)


def dfsImp_l(g, s):
    """
     Imperative Depth First Search for adjacency list
    
    Returns:
        None
    """
    V = []                                                                      # List of visited vertices
    Q = []
    Q.append(s)                                                       # Stack
    
    while not Q == []:
        v = Q.pop()
        
        if v not in V:
            print(v)
            V.append(v)
            
            for u in g[v]:
                Q.append(u)