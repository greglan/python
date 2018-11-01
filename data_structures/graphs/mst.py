# -*- coding: utf-8 -*-
# !/usr/bin/env python

import operator

## Minimum/maximum spanning tree
# TODO: Check functions
# TODO: adjList to edges func
# TODO: Add option to get the minimum or the maximum spanning tree.


def prim(g):
    """
    Return the minimum spanning tree using Prim's algorithm
    :param g:
    :return:
    """
    # TODO: Check
    global infinity
    
    order = len(g.getOrder())
    c = {} # Cheapest costs
    e = {} # Best edges.
    
    F = {} # Empty tree: adjacency list
    Q = list(graph.keys()) # List of vertices not included in F
    
    def addEdge(u,v):
        F[u].append(v)
        F[v].append(u)    
    
    # Init c, e and F
    for vertex in graph:
        c[vertex] = infinity
        e[vertex] = None
        F[vertex] = []
    
    # Prim's algorithm
    while Q != []:
        # Find and remove a vertex v from Q having the minimum possible value of C[v]
        minVertex = Q[0]
        for vertex in Q:
            if c[vertex] < c[minVertex]:
                minVertex = vertex
        Q.remove(minVertex)
        v = minVertex
        
        
        # Add v to F and, if E[v] is not the special flag value, also add E[v] to F
        if e[v] != None:
            addEdge(v, e[v])
        
        
        for w in graph[v].keys():
            if w in Q and graph[v][w] < c[w]:
                c[w] = graph[v][w]
                e[w] = v
    
    # Return the tree
    return F


def krushkal(g):
    """
    Krushkal's algorithm
        Input: a list of edges (v1,v2,w)
        Returns:
            A list of edges
    """
            
    def sameConnectedComponent():
        # TODO
        pass
    
    T = []                                                                      # MST: list of edges
    edges = g.sort(key=operator.itemgetter(2))                                  # Sort according to weight (index 2)
    
    for (u,v,w) in edges:
        if not sameConnectedComponent(u, v):
            A += [(u,v)]
    
    return A
