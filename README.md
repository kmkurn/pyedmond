# pyedmond

Edmond's optimal branching algorithm in C++ wrapped by Python. Original version is from https://github.com/xiaohan2012/pyedmond.

As it's in C++ internally, it's faster and more memory-efficient than that of [NetworkX](https://networkx.github.io/).

# Example

```python
import numpy as np
from pyedmond import find_minimum_branching

n_nodes, edges = 10, []
weights = np.abs(np.random.rand(n_nodes, n_nodes))
for u in range(n_nodes):
    for v in range(n_nodes):
        if u != v:
            edges.append((u, v, weights[u, v]))

edges = find_minimum_branching(n_nodes, edges, roots=[0, 1])  # returns a list of (int, int) edges
```

# Requirements

[Boost](https://www.boost.org/) 1.34 or later

# Installation

    pip install git+https://github.com/kmkurn/pyedmond.git#egg=pyedmond

# License

MIT

Copyright (c) 2017 Han Xiao, 2019 Kemal Kurniawan.
