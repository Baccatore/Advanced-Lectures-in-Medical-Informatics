import itertools
def getPLabel(P,GG,m,k):
    PLabel = [-1]*m
    for i, P_i in enumerate(P):
        for j, P_gj in enumerate(GG):
            min_dist = 0
            if min_dist > No1406.getDistance(P_i,P_gj):
                PLabel[i] = j
    return PLabel

