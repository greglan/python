# -*- coding: utf-8 -*-
# !/usr/bin/env python

## Connectivity
# TODO: https://fr.wikipedia.org/wiki/Algorithmes_de_connexit%C3%A9_bas%C3%A9s_sur_des_pointeurs
# TODO: calcul de composantes connexes
# TODO: tests de connexité

## Connectivity test
def connectivityTest(g):
    """
        Input: A graph as an adjacency list
        Uses an imperative dfs
        
        Args:
            g: adjacency list of an unweighted graph
            
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
        Use a dfs from u and stop if v is visited along the way.
        
        Args:
            g: adjacency list of an unweighted graph,
            (u,v): int
        
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
    