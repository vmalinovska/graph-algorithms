def answer(V,L,s,t):
    L.sort(reverse=True, key = lambda x: x[2])
    parent=[x for x in range(V+1)]
    rank=[0 for _ in range(V+1)]
    tree=set()

    def find(x):
        if x!=parent[x]:
            parent[x]=find(parent[x])
        return parent[x]

    def union(x,y):
        px=find(x)
        py=find(y)
        if px==py:
            return False
        if rank[px]>rank[py]:
            parent[py]=px
        else:
            parent[px]=py
            if rank[px]==rank[py]:
                rank[py]+=1
        return True

    for x,y,w in L:
        if union(x,y):
            tree.add(x)
            tree.add(y)
        if find(s)==find(t):
            return w

    return None
