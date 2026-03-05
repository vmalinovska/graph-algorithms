def answer(V,L,s,t):
    G=[set() for _ in range(V+1)]
    L.sort(reverse=True, key=lambda x: x[2])
    idx=0
    for _,_,limit in L:
        while idx<len(L) and L[idx][2]>=limit:
            x,y,_=L[idx]
            G[x].add(y)
            G[y].add(x)
            idx+=1
        if dfs(G,s,t):
            return limit
    return None

def dfs(G,s,t):
    visited=set()
    stack=[s]
    while stack:
        v=stack.pop()
        if v==t:
            return True
        if v in visited:
            continue
        visited.add(v)
        for u in G[v]:
            if u not in visited:
                stack.append(u)
    return False