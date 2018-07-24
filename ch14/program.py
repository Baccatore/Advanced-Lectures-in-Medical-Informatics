import random as rdm

def getGroup(P, P_label, k)
    for i in enumerate(P_label):

if __name__ == '__main__':
    P = []
    n_dim = 2
    n_points = 10
    for i in range(n_points):
        P.append([rdm.randrange(1,11) for i in range(n_dim)])
    print(P)

    P_label = []
    n_clasters = 2
    for i in range(n_points):
        P_label.append(rdm.randrange(0,n_clasters+1))
    print(P_label)


