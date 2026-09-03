# DAA Lab Exercise
# Topic 5 - Greedy - Question 5

from math import inf

# Q5/Q6 Dijkstra
def dijkstra_matrix(g,s):
    n=len(g);d=[inf]*n;used=[0]*n;d[s]=0
    for _ in range(n):
        u=min((i for i in range(n) if not used[i]),key=lambda i:d[i],default=-1)
        if u<0 or d[u]==inf:break
        used[u]=1
        for v,w in enumerate(g[u]):
            if w<inf:d[v]=min(d[v],d[u]+w)
    return d
def dijkstra_edges(n,edges,s,t):
    g=[[] for _ in range(n)]
    for u,v,w in edges:g[u].append((v,w));g[v].append((u,w))
    d=[inf]*n;d[s]=0;h=[(0,s)]
    while h:
        du,u=heapq.heappop(h)
        if du!=d[u]:continue
        if u==t:return du
        for v,w in g[u]:
            if du+w<d[v]:d[v]=du+w;heapq.heappush(h,(d[v],v))
    return inf
I=inf
print("T5 Q5:",dijkstra_matrix([[0,10,3,I,I],[I,0,1,2,I],[I,4,0,8,2],[I,I,I,0,7],[I,I,I,9,0]],0))
print("T5 Q6:",dijkstra_edges(6,[(0,1,7),(0,2,9),(0,5,14),(1,2,10),(1,3,15),(2,3,11),(2,5,2),(3,4,6),(4,5,9)],0,4))
