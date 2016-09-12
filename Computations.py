from collections import deque

"""
Input:
network N
"""

def CoreDecomposition(G):
    V = list(G.nodes())
    deg = {}
    for node in V:
        deg[node] = G.degree(node)
    O = []  # ordered list of ordered lists - this is k-order
    #O.append([])
    K = 0#1
    core = {}   # starting core values for nodes
    while V:
        O.insert(K, [])
        while True:
            u = False
            for node in V:
                if deg[node] < K:
                    u = node
                    break
            if not u:  # break while true
                break
            for neighbor in intersect(V, G.neighbors(u)):
                deg[neighbor] -= 1
            V.remove(u)
            core[u] = K-1
            O[K-1].append(u)
        K += 1 
    return core, O


def MCD(G, core):
    V = list(G.nodes())
    mcd = {}
    for node in V:
        mcd[node] = 0
        for neighbor in G.neighbors(node):
            if core[neighbor] >= core[node]:
                mcd[node] += 1
    return mcd


def FindVstar(core, u, v, G, mcd):
    Vstar = []
    roots = ()
    K = min((core[u], core[v]))
    if K <= core[v]:
        roots += (u,)
    if K <= core[v]:
        roots += (v,)
    for root in roots:
        print ""
        nodes = list(G.nodes())
        cd = mcd
        S = []  # stack; use append and pop
        visited = {}
        for node in nodes:
            visited[node] = False
        S.append(root)
        while S:
            #while nodes:
            w = S.pop()
            if not visited[w]:
                if cd[w] < K:
                    #nodes.remove(w)
                    Vstar.append(w)
                    core[w] -= 1
                    for neighbor in G.neighbors(w):
                        if core[neighbor] == K:
                            cd[neighbor] -= 1
                visited[w] = True
                for neighbor in G.neighbors(w):
                    if not visited[neighbor]:
                        S.append(neighbor)
    return list(set(Vstar)), core

def RemainingDegree(G, kOrder):
    degPlus = {}
    kOrderFlat = [i for sublist in kOrder for i in sublist]
    for ok in kOrder:
        for u in ok:
            a = [i for i in kOrderFlat if kOrderFlat.index(u) <= kOrderFlat.index(i)]
            degPlus[u] = len(intersect(a, G.neighbors(u)))
    return degPlus


def RemoveCandidates(G, Vc, kOrderKNew, node, K, degPlus, degStar, core, kOrderFlat):
    Q = ([])  # queue; use append and popleft from deque
    for neighbor in G.neighbors(node):
        if neighbor in Vc:
            degPlus[neighbor] -= 1
            if degPlus[neighbor] + degStar[neighbor] <= K:
                Q.append(neighbor)
    while Q:    # TODO check if this works for dequeue object
        w = Q.popleft()
        degPlus[w] = degPlus[w] + degStar[w]
        degStar[w] = 0
        Vc.remove(w)
        kOrderKNew.append(w)
        for neighbor in G.neighbors(w):
            if core[neighbor] == K:
                if kOrderFlat.index(node) <= kOrderFlat.index(neighbor):
                    degStar[neighbor] -= 1
                elif kOrderFlat.index(w) <= kOrderFlat.index(neighbor) and neighbor in Vc:
                    degStar[neighbor] -= 1
                    if degStar[neighbor] + degPlus[neighbor] <= K and not neighbor in Q:    # TODO check if this works for dequeue object
                        Q.append(neighbor)
                elif neighbor in Vc:
                    degPlus[neighbor] -= 1
                    if degStar[neighbor] + degPlus[neighbor] <= K and not neighbor in Q:    # TODO check if this works for dequeue object
                        Q.append(neighbor)
    return Vc, kOrderKNew, degPlus, degStar, core, kOrderFlat

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

