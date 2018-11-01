import igraph

g1 = igraph.Graph()
g1.add_vertices(5)
g1.add_edges([(0,1), (0,2), (0,3), (0,4), (3, 4)])
print(g1.bfs(4)[0])
print(bfs_list(g1.get_adjlist(), 4))