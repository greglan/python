import igraph

# Undirected unweighted graph with one cycle
g1 = igraph.Graph()
g1.add_vertices(5)
g1.add_edges([(0,1), (0,2), (0,3), (0,4), (3, 4)])

# Undirected unweighted graph with two cycles
g2 = igraph.Graph()
g2.add_vertices(6)
g2.add_edges([(0,1), (0,2), (0,3), (0,4), (2,5), (3, 4), (4,5)])