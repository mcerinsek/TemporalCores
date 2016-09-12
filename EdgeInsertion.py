

from Computations import RemainingDegree, RemoveCandidates

"""
Input
G = (V, E)
(u, v) edge to be inserted
core - dict for core values
"""
def EdgeInsertion(G, u, v, core, kOrder):
    K = min((core[u], core[v]))
    G.addEdge(u,v)
    kOrderFlat = [i for sublist in kOrder for i in sublist]
    #print kOrderFlat
    if kOrderFlat.index(u) > kOrderFlat.index(v): # for assumption that u is before v in kOrder
        u, v = v, u
    degPlus = RemainingDegree(G, kOrder)
    degPlus[u] += 1
    if degPlus[u] <= K:
        return G, core, kOrder
    kOrderKNew = []
    Vc = [] # all current potential candidates
    i = 0   # python starts with 0 and not 1
    degStar = {}
    for node in list(G.nodes()):
        degStar[node] = 0
    while i < len(kOrder[K]):
        node = kOrder[K][i]
        print K
        if degStar[node] + degPlus[node] > K:
            kOrder[K].remove(node)
            Vc.append(node)
            for neighbor in G.neighbors(node):
                if core[neighbor] == K and kOrderFlat.index(node) <= kOrderFlat.index(neighbor):
                    degStar[neighbor] += 1
            #i += 1      skip this, because you already delete one element, so the next is at the same index
        elif degStar[node] == 0:
            nodej = False
            for n in kOrder[K]:
                if kOrderFlat.index(node) <= kOrderFlat.index(n) and (degStar[n] > 0 or degPlus[n] > K):
                    nodej = n
                    break
            j = len(kOrder[K])
            if nodej:
                j = kOrder[K].index(nodej)
            nodes = kOrder[K][kOrder[K].index(node):j]
            for n in nodes:
                kOrder[K].remove(n)
                kOrderKNew.append(n)
            i = j - 1
        else:
            kOrder[K].remove(node)
            kOrderKNew.append(node)
            degPlus[node] = degPlus[node] + degStar[node]
            degStar[node] = 0
            Vc, kOrderKNew, degPlus, degStar, core, kOrderFlat = RemoveCandidates(G, Vc, kOrderKNew, node, K, degPlus, degStar, core, kOrderFlat)
            #i += 1
    Vstar = Vc
    print Vstar
    for w in Vstar:
        degStar[w] = 0
        core[w] += 1
    if K+1 == len(kOrder):  # if k+1-core did not exist in previous version of network
        kOrder.append([])
    kOrder[K+1] = Vstar + kOrder[K+1]
    kOrder[K] = kOrderKNew
    return G, core, kOrder