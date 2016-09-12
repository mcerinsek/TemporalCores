

from Computations import FindVstar, RemainingDegree

"""
Input
G = (V, E)
(u, v) edge to be removed
core - dict for core values
"""
def EdgeRemoval(G, u, v, core, kOrder, mcd):
    K = min((core[u], core[v]))
    G.delEdge(u, v)
    print mcd, core
    if core[u] <= core[v]:
        mcd[u] -= 1
    if core[u] >= core[v]:
        mcd[v] -= 1
    Vstar, core = FindVstar(core, u, v, G, mcd)
    degPlus = RemainingDegree(G, kOrder)
    
    for w in Vstar:
        degPlus[w] = 0
        kOrderflat = [i for sublist in kOrder for i in sublist]
        for neighbor in G.neighbors(w):
            if core[neighbor] == K and kOrderflat.index(neighbor) <= kOrderflat.index(w):
                degPlus[neighbor] -= 1
            if core[neighbor] >= K or neighbor in Vstar:
                degPlus[neighbor] += 1
        # Vstar.remove(w) not necessary because of the for loop
        kOrder[K].remove(w)
        kOrder[K-1].append(w)   # append to the end
    return G, core, kOrder, mcd