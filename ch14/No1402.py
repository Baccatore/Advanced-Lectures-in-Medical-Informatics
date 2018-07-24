import random as rdm

def getInitPLabel(m,k):
    PLabel = [rdm.randrange(0,int(k)) for i in range(m)]
    return PLabel

