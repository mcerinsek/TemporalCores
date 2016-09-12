
from EdgeRemoval import EdgeRemoval

"""
Input
G = (V, E)
u node to be removed
core - dict for core values
"""
def NodeRemoval(G, u, core, kOrder, mcd):
    for w in G.neighbors(u):
        G, core, kOrder = EdgeRemoval(G, u, w, core, kOrder, mcd)
    G.delNode(u)
    kOrder[core[u]].remove(u)
    del core[u]
    del mcd[u]
    return G, core, kOrder
        