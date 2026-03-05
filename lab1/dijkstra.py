from queue import PriorityQueue

def answer(V,L,s,t):
    G=[[] for _ in range(V+1)]
    for (x,y,c) in L:
        G[x].append((y,c))
        G[y].append((x,c))
    d=[float('inf') for _ in range(V+1)]
    visited=set()
    q=PriorityQueue()
    q.put((-d[s], s))
    while not q.empty():
        _,v = q.get()
        if v==t:
            return d[t]
        for u,w in G[v]:
            if u not in visited or d[u]<min(d[v],w):
                visited.add(u)
                d[u]=min(d[v],w)
                q.put((-d[u], u))
    return None