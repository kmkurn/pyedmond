import pytest
import numpy as np
from graph_tool.all import Graph, GraphView, complete_graph, label_components, random_spanning_tree

from pyedmond import find_minimum_branching


@pytest.fixture
def g():
    return complete_graph(100, directed=True)


@pytest.fixture
def weights(g):
    return np.abs(np.random.rand(g.num_edges()))


def test_feasibility(g, weights):
    edges = [(e[0], e[1], w) for e, w in zip(g.get_edges(), weights)]

    min_edges = find_minimum_branching(g.num_vertices(), edges, roots=[0])

    tree = Graph(directed=True)
    tree.add_edge_list(min_edges)
    assert is_arborescence(tree)


def test_optimality(g, weights):
    weight_prop = g.new_edge_property('float')
    weight_prop.a = weights
    edges = [(e[0], e[1], w) for e, w in zip(g.get_edges(), weights)]

    min_edges = find_minimum_branching(g.num_vertices(), edges, roots=[0])

    min_weight = sum(weight_prop[g.edge(i, j)] for i, j in min_edges)

    def graph_weight(graph):
        return sum(weight_prop[e] for e in graph.edges())

    for i in range(1000):
        tree_map = random_spanning_tree(g)
        t = GraphView(g, efilt=tree_map, directed=True)
        assert graph_weight(t) >= min_weight


def is_arborescence(tree):
    # is tree?
    l, _ = label_components(GraphView(tree, directed=False))
    if not np.all(np.array(l.a) == 0):
        return False

    in_degs = np.array([v.in_degree() for v in tree.vertices()])
    if in_degs.max() > 1:
        return False
    if np.sum(in_degs == 1) != (tree.num_vertices() - 1):
        return False

    roots = get_roots(tree)
    assert len(roots) == 1, '>1 roots'

    return True


def get_roots(t):
    return np.nonzero((t.degree_property_map(deg='out').a > 0)
                      & (t.degree_property_map(deg='in').a == 0))[0]
