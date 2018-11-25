# -*- coding: utf-8 -*-
# !/usr/bin/env python

# TODO: https://fr.wikipedia.org/wiki/Algorithmes_de_connexit%C3%A9_bas%C3%A9s_sur_des_pointeurs
# TODO: Duplicate functions for weighted graphs


def connectivity_test(g):
    """
    Indicates if all vertices in the graph are connected.
    Uses an imperative DFS.
    :param g: unweighted graph to test
    :type g: adjacency list
    :return: bool
    """
    visited_vertices = []  # List of visited vertices
    Q = []
    Q.append(0)  # Stack

    while not Q == []:
        v = Q.pop()

        if v not in visited_vertices:
            visited_verticed.append(v)

            for u in g[v]:
                Q.append(u)

    return len(visited_vertices) == len(g)


def same_connected_component(g, u, v):
    """
    Check if two vertices belong to the same connected component.
    Use a dfs from u and stop if v is visited along the way.
    
    :type g: adjacency list of an unweighted graph
    :type u: int
    :type v: int
    :return: bool
    """

    visites_vertices = []  # List of visited vertices
    Q = []  # Stack
    Q.append(u)  # Start the DFS from vertex u

    while Q != []:
        i = Q.pop()
        
        if i not in visited_vertices:
            if i == v:
                return True
            else:
                visited_verticed.append(i)
                for neighbor in g[i]:
                    Q.append(neighbor)
                    
    return False


def get_connected_component_vertices(g, s):
    """
    Returns the list of vertices in the connected component of s.
    Use a dfs and return all the visited vertices.
    
    :type g: adjacency list of an unweighted graph
    :param s: vertex
    :type s: int
    :return: list(int)
    """
    V = []  # List of visited vertices
    Q = []
    Q.append(s)  # Stack

    while not Q == []:
        v = Q.pop()

        if v not in V:
            V.append(v)

            for neighbor in g[v]:
                Q.append(neighbor)
    
    return V
