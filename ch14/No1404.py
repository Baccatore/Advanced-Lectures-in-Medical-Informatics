import numpy as np

def getG(P):
    n_dim = len(P[0])
    PG = np.zeros(n_dim)
    for p in P:
        assert n_dim == len(p), 'Dimension is different from other points'
        PG += np.array(p)
    return PG / n_dim

