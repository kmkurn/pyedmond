from ._core import build_graph, minimum_branching


def find_minimum_branching(n_nodes, edges, roots=None):
    if roots is None:
        roots = []

    return minimum_branching(build_graph(n_nodes, edges), roots)
