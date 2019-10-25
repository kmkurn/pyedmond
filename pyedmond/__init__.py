from typing import List, Optional, Tuple

from ._core import build_graph, minimum_branching


def find_minimum_branching(
        n_nodes: int, edges: List[Tuple[int, int, float]],
        roots: Optional[List[int]] = None) -> List[Tuple[int, int]]:
    """Find minimum branching of a directed graph with Edmond's algorithm.

    See https://en.wikipedia.org/wiki/Edmonds%27_algorithm.

    Args:
        n_nodes: Number of nodes in the graph.
        edges: List of edges in the graph. An edge is given as a tuple ``(u, v, w)`` which
            means there is an edge from node ``u`` to node ``v`` with weight ``w``.
        roots: List of nodes to be the root(s) of the resulting branching.

    Returns:
        The minimum branching.
    """
    if roots is None:
        roots = []

    return minimum_branching(build_graph(n_nodes, edges), roots)


def find_maximum_branching(
        n_nodes: int, edges: List[Tuple[int, int, float]],
        roots: Optional[List[int]] = None) -> List[Tuple[int, int]]:
    """Find maximum branching of a directed graph with Edmond's algorithm.

    See https://en.wikipedia.org/wiki/Edmonds%27_algorithm.

    Args:
        n_nodes: Number of nodes in the graph.
        edges: List of edges in the graph. An edge is given as a tuple ``(u, v, w)`` which
            means there is an edge from node ``u`` to node ``v`` with weight ``w``.
        roots: List of nodes to be the root(s) of the resulting branching.

    Returns:
        The maximum branching.
    """
    edges_ = [(u, v, -w) for u, v, w in edges]
    return find_minimum_branching(n_nodes, edges_, roots=roots)
