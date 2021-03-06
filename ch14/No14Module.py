import u
import numpy as np
import pandas as pd
import random as rdm
from numpy import linalg as LA
import itertools

def getInitP(file_name,n):
    book = pd.ExcelFile(file_name)
    dF = book.parse('01')
    m = len(dF)
    list_series = u.row2list(dF)
    P = [ [0]*n for i in range(m) ] 

    for i in range(m):
        for j in range(n):
            P[i][j] = list_series[j][i]

    return P


def getInitPLabel(m,k):
    PLabel = [ rdm.randrange(k) for i in range(m)]
    return PLabel


def getGroup(P,PLabel,k,m):
    G = [ [] for i in range(k)]

    for i in range(m):
        G[PLabel[i]].append(P[i])

    return G


def getG(P):
    n_dim = len(P[0])
    PG = np.zeros(n_dim)
    for p in P:
        PG += np.array(p)
    return list(PG / len(P))


def getGG(G):
    GG = []
    for gi in G:
        GG.append(getG(gi))
    return GG

def getDistance(P1,P2):
    assert len(P1) == len(P2), 'Dimension of two points is different'
    return LA.norm(np.array(P1)-np.array(P2))

def getPLabel(P,GG,m,k):
    PLabel = [-1]*m
    for i, P_i in enumerate(P):
        for j, P_gj in enumerate(GG):
            min_dist = 0
            if min_dist > getDistance(P_i,P_gj):
                PLabel[i] = j
    return PLabel

