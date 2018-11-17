# import igraph
#
# g1 = igraph.Graph()
# g1.add_vertices(5)
# g1.add_edges([(0,1), (0,2), (0,3), (0,4), (3, 4)])
# print(g1.bfs(4)[0])
# print(bfs_list(g1.get_adjlist(), 4))
#
# # Undirected unweighted graph with one cycle
# g1 = igraph.Graph()
# g1.add_vertices(5)
# g1.add_edges([(0,1), (0,2), (0,3), (0,4), (3, 4)])
#
# # Undirected unweighted graph with two cycles
# g2 = igraph.Graph()
# g2.add_vertices(6)
# g2.add_edges([(0,1), (0,2), (0,3), (0,4), (2,5), (3, 4), (4,5)])
import matplotlib.pyplot as plt
import networkx as nx

INFINITY = float('inf')
NX_DRAW_OPTIONS = {
    'with_labels': True,
    'node_color': 'grey',
    'width': 1
}


def adjacency_list_to_nx_graph(g):
    """
    Convert a graph represented as an adjacency list to a networkx graph.
    Only for unweighted graphs.

    :type g: list(list)
    :return: networkx graph
    """
    n = len(g)
    d = {}

    for node in range(n):
        neighbours = {}
        for neighbour in g[node]:
            neighbours[neighbour] = 1
        d[node] = neighbours

    return nx.Graph(d)


def display_graph(g):
    """
    
    :type g: networkx graph
    :return: None
    """
    nx.draw(g, **NX_DRAW_OPTIONS)
    plt.show()
