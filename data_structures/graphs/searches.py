# -*- coding: utf-8 -*-
# !/usr/bin/env python
from data_structures.graphs.utils import *
import queue


def bfs_list(g, s):
    """
    Breadth First Search algorithm for adjacency lists.
    
    :param g: the graph to visit. It is assumed the list only contains int data type. 
    :type g: list(list(int))
    :param s: the vertex to start from.
    :type s: int
    :return: (V,D,P), where V is the list of visited vertices in order,
    D is the list of the distance of each vertex from the start and
    P is the list of the predecessors of each vertex
    """

    # This list contains the distances from the start vertex.
    distances = [INFINITY for k in range(len(g))]
    distances[s] = 0

    # This list contains the predecessor of each vertex.
    predecessors = [-1 for k in range(len(g))]

    # Queue of vertices to visit
    q = queue.Queue()
    q.put(s)  # Start with the vertex given as argument
    visited_vertices = []  # List of visited vertices.

    while not q.empty():
        v = q.get()  # Vertex being visited

        for u in g[v]:
            if u not in visited_vertices:
                distances[u] = distances[v] + 1  # Update the distance
                predecessors[u] = v  # Update the predecessor
                q.put(u)
        visited_vertices.append(v)

    return visited_vertices, distances, predecessors


def dfs_rec_list(g, s):
    """
    Recursive Depth First Search for adjacency lists

    :param g: the graph to visit. It is assumed the list only contains int data type.
    :type g: list(list(int))
    :param s: the vertex to start from.
    :type s: int
    :return: list of visited vertices
    """
    
    def visit(v):
        visited_vertices.append(v)
        for u in g[v]:
            if u not in visited_vertices:
                visit(u)
    
    visited_vertices = []
    visit(s)
    return visited_vertices


def dfs_imp_list(g, s):
    """
    Imperative Depth First Search for adjacency list
    
    :param g: the graph to visit. It is assumed the list only contains int data type.
    :type g: list(list(int))
    :param s: the vertex to start from.
    :type s: int
    :return: list of visited vertices
    """
    visited_vertices = []
    stack = [s]

    while not stack == []:
        v = stack.pop()
        
        if v not in visited_vertices:
            visited_vertices.append(v)
            
            for u in g[v]:
                stack.append(u)

    return visited_vertices
