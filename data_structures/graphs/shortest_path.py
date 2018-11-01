# -*- coding: utf-8 -*-
# !/usr/bin/env python
# FIXME: Floyd Warshall: distances to self is wrong (2 or 4?)
# TODO: Add comments
# FIXME: use a generic queue lib
# TODO: add tests


def distances_from(g, s):
    """
    Returns the list of distances from vertex s using a bfs.
    :type g: list(list(int))
    :type s: int
    :param g: unweighted graph as an adjacency list
    :param s: vertex to start from
    :return: A list distances such as distances[i] is the distance from s to vertex i
    """
    
    visited_vertices = []                   # List of visited vertices
    distances = [0 for k in range(len(g))]  # Distances
    queue = Queue()
    queue.put((s, 0))
    
    while not queue.empty():
        current_vertex, current_distance = queue.get()
        
        if current_vertex not in visited_vertices:
            visited_vertices += [current_vertex]
            for v in g[current_vertex]:
                queue.put((v, current_distance+1))
            distances[current_vertex] = current_distance
    return distances


def path_from(g, s):
    """

    :param g:
    :param s:
    :return:
    """
    """
        Returns the path to go to a vertex using a bfs
        
        Input:
            Graph as an adjacency list
        
        Returns:
            List l such as l[i] is the list of vertices to use to go to i from s
    """
    
    V = []                                                                      # List of visited vertices
    P = [None for k in range(len(g))]                                           # List of paths
    Q = queue.Queue()
    Q.put((s,[]))
    
    while not Q.empty():
        u, p = Q.get()
        
        if u not in V:
            V += [u]
            for v in g[u]:
                Q.put( (v,p+[u]) )
            P[u] = p+[u]
    return P

# Weighted graphs: Bellman-Ford
def bellman_ford(g, s):
    n = len(g)
    
    for i in range(n):
        pass
        

## Weighted graphs: Dijkstra
## Weighted graphs: Floyd Warshall
## Weighted graphs: A star
def dijkstra(g, source):
    """
    Returns the list of distances and the list of paths
    
    Todo:
        Add the paths
    """
    
    global infinity
    order = g.getOrder()
    
    distances = [ infinity for k in range(order) ]
    predecessors = [None for k in range(order) ]
    
    visited = []
    q = priorityQueue()
    
    # To get the same result as FW 
    # for neighbor in g.getNeighbors(source):
    #     if g.getWeight(source, neighbor) < distances[source]:
    #         distances[source] = 2* g.getWeight(source, neighbor)
    #         predecessors[source] = neighbor
    
    q.put((0,source))
    
    while not q.empty():
        cur_distance, cur_vertex = q.get()
        visited.append(cur_vertex)
        
        for neighbor in g.getNeighbors(cur_vertex):
            if neighbor not in visited:
                new_distance = cur_distance + g.getWeight(cur_vertex,neighbor)
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = cur_vertex
                    q.put((new_distance, neighbor))
    
    return distances, predecessors


def floyd_warshall(g):
    """
    Floyd Warshall's algorithm
    :param g:
    :return:
    """
    global infinity
    order = g.getOrder()

    # Create the adjacency matrix of the graph
    distances = [ [infinity for j in range(order)] for i in range(order) ]
    nextVertex = [[None for j in range(order)] for i in range(order) ]

    # Initialise adjacency matrix and the nextVertex matrix
    for i in range(order):
        for j in range(order):
            if j in g.getNeighbors(i):
                distances[i][j] = g.getWeight(i,j)
                nextVertex[i][j] = j

    # Floyd-Warshall
    for k in range(order):
        for i in range(order):
            for j in range(order):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    nextVertex[i][j] = nextVertex[i][k]
    
    return distances, nextVertex
