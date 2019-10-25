import time
import numpy as np
import networkx as nx
from pyedmond import find_minimum_branching


def make_graph(n=100, graph_type='graph_tool'):
    if graph_type == 'graph_tool':
        g = complete_graph(n, directed=True)
        weights = np.abs(np.random.rand(g.num_edges()))
        return g, weights
    elif graph_type == 'networkx':
        g = nx.complete_graph(n, create_using=nx.DiGraph())
        weights = np.abs(np.random.rand(g.number_of_edges()))
        for k, (i, j) in enumerate(g.edges):
            g[i][j]['weight'] = weights[k]
        return g


def test_pyedmond(n):
    """return the number of seconds required to run the algorithm
    """
    g = make_graph(n, 'networkx')

    s = time.time()
    find_minimum_branching(g, [])
    return time.time() - s


def test_networkx(n):
    """return the number of seconds required to run the algorithm
    """    
    g = make_graph(n, 'networkx')

    s = time.time()
    nx.maximum_spanning_arborescence(g, attr='weight', default=1)
    return time.time() - s

if __name__ == '__main__':
    n = 100
    r = 5
    pyedmond_time = np.mean([test_pyedmond(n) for i in range(r)])
    networkx_time = np.mean([test_networkx(n) for i in range(r)])

    print('#nodes: {}'.format(n))
    print('repetition: {}'.format(5))
    print('pyedmond takes {} secs on average'.format(pyedmond_time))
    print('networkx takes {} secs on average'.format(networkx_time))
    print('pyedmond is {} times faster'.format(networkx_time / pyedmond_time))
