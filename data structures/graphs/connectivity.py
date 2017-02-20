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