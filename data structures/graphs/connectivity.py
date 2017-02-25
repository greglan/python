# -*- coding: utf-8 -*-
# !/usr/bin/env python

## Connectivity
# TODO: calcul de composantes connexes
# TODO: tests de connexité

## Connectivity test
def connectivityTest(g):
    """
        Input: A graph as an adjacency list
        Uses an imperative dfs
        Returns:
            Boolean
    """
    V = []                                                                      # List of visited vertices
    Q = []
    Q.append(0)                                                                 # Stack
    
    while not Q == []:
        v = Q.pop()
        
        if v not in V:
            V.append(v)
            
            for u in g[v]:
                Q.append(u)
    
    return len(V)==len(g)

## Connected component computing
def sameConnectedComponent(g, u, v):
    """ Check if two vertices belong to the same connected component.
        Use a dfs from u and stop if v is visited along the way
        
        Args:
            g: adjacency list, (u,v): int

        Returns:
            Boolean
    """
    
    V = []                                                                      # List of visited vertices
    Q = []                                                                      # Stack
    Q.append(u)
    
    while Q != []:
        i = Q.pop()
        if i not in V:
            if i==v:
                return True
            else:
                V.append(i)
                for j in g[i]:
                    Q.append(j)
    return False
    