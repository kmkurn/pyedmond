import networkx as nx
from ._core import build_graph


def gt2edges_and_weights(g, weights):
    """
    args:

    g: graph_tool.Graph
    weights: list of edge weight, edge order should be the same g.get_edges()

    returns:
    
    list of (source, target, weight)
    """
    from graph_tool import PropertyMap
    if isinstance(weights, PropertyMap):  # convert to np.ndarray if necessary
        weights = weights.a

    assert g.num_edges() == len(weights)
    assert g.is_directed()

    return [(e[0], e[1], w)
            for e, w in zip(g.get_edges(), weights)]


def nx2edges_and_weights(g, weight='weight'):
    """
    args:
    
    g: networkx.Graph|DiGraph
    weight: attribute name for edge weight

    return:

    list of (source, target, weight)
    """
    assert isinstance(g, nx.DiGraph)
    return [(e[0], e[1], g[e[0]][e[1]][weight])
            for e in g.edges]


def from_gt(g, weights):
    """weights: edge weights, PropertyMap or np.ndarray
    """
    return build_graph(g.num_vertices(),
                       gt2edges_and_weights(g, weights))


def from_nx(g, weight='weight'):
    """weight: key of weight
    """
    return build_graph(g.number_of_nodes(),
                       nx2edges_and_weights(g, weight))
