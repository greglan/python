# -*- coding: utf-8 -*-
# !/usr/bin/env python



## Opt transformations
# Test 2-opt
# Add a quality ratio to stop the 2-opt optimization
# 3-opt
# 4-opt
# k-opt
##




## 2-opt
def swap2opt(path, i, j):
    new_path = path[i:j]
    new_path.reverse()
    return path[:i]+new_path+path[j:]



def optimization2opt(graph, path, n):
    """ Search for a better path using 2-opt swaps """
    best_distance = getPathLength(graph, path)
    best_path = path

    for i in range(1,n):
        for j in range(i,n):
            new_path = swap2opt(path, i, j)
            new_distance = getPathLength(graph, new_path)
            if new_distance < best_distance:
                best_path = optimization2opt(graph, new_path, n)
    return best_path