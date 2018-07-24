def getGroup(P,PLabel,k,m):
    G = [ [] for i in range(k)]

    for i in range(m):
        G[PLabel(i)].append(P[i])

    return G
