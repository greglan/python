# -*- coding: utf-8 -*-
# !/usr/bin/env python

# Searches
# TODO: Recursive bfs?
# TODO: Add comments
# TODO: Add tests

import queue


# BFS
def bfs_list(g, s):
    """
    Breadth First Search algorithm for adjacency lists.
    
    :param g: the graph to visit. It is assumed the list only contains int data type. 
    :param s: the vertex to start from. This is an integer 
    :return: (v,d,p), where v is the order in which the vertex where visited, 
    d is the distance of each vertex to the start, p is the list of the predecessors 
    """

    # This list contains the distances from the start vertex.
    d = [float('inf') for k in range(len(g))]
    d[s] = 0

    # This list contains the predecessor of each vertex.
    p = [-1 for k in range(len(g))]

    q = queue.Queue()
    q.put(s)
    s = []  # List of visited vertices.

    while not q.empty():
        v = q.get()

        for u in g[v]:
            if u not in s:
                d[u] = d[v] + 1
                p[u] = v
                q.put(u)
        s.append(v)

    return s[:-1], d, p


# DFS
def dfsRec_list(g, s):
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


def dfsImp_list(g, s):
    """
     Imperative Depth First Search for adjacency list
    
    Returns:
        None
    """
    V = []                                                                      # List of visited vertices
    Q = []
    Q.append(s)                                                                 # Stack
    
    while not Q == []:
        v = Q.pop()
        
        if v not in V:
            print(v)
            V.append(v)
            
            for u in g[v]:
                Q.append(u)


import igraph

g1 = igraph.Graph()
g1.add_vertices(5)
g1.add_edges([(0,1), (0,2), (0,3), (0,4), (3, 4)])
print(g1.bfs(4)[0])
print(bfs_list(g1.get_adjlist(), 4))

