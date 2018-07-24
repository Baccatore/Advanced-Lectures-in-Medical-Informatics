from numpy import linalg as LA

def getDistance(P1,P2):
    assert len(P1) == len(P2), 'Dimension of two points is different'
    return LA.norm(P1-P2)
