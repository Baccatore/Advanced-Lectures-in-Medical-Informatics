from matplotlib import pyplot as plt

import No14Module as mod

if __name__ == '__main__':
    f1 = "test.xlsx"
    k = 3
    n = 2

    P  = mod.getInitP(f1, n)
    m = len(P) 
    PLabel = mod.getInitPLabel(m,k)


    G  = mod.getGroup(P,PLabel,k,m)
    GG = mod.getGG(G)
    #PLabel = []
    #PLabel = mod.getPLabel(P,GG,m,k)


    color = ['red','green','yellow']
    for i,p in enumerate(P):
        plt.scatter(p[0],p[1],c=color[PLabel[i]])
    for i,g in enumerate(GG):
        plt.scatter(g[0],g[1],c=color[i],marker='H')
        plt.scatter(g[0],g[1],s=7,c='black')

    plt.grid(True)
    plt.show()

