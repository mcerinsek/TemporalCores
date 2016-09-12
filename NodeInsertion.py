
"""
Input
G = (V, E)
u node to be inserted
core - dict for core values
"""
def NodeInsertion(G, u, core, kOrder):
    G.addNode(u)
    core[u] = 0
    kOrder[0].insert(0, u)
    return G, core, kOrder