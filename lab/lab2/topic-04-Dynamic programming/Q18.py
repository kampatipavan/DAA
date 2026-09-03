# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 18

import heapq

# Q18 Maximum probability path
def max_prob(n,edges,p,start,end):
    g=[[] for _ in range(n)]
    for (u,v),x in zip(edges,p):g[u].append((v,x));g[v].append((u,x))
    best=[0]*n;best[start]=1;h=[(-1,start)]
    while h:
        neg,u=heapq.heappop(h);cur=-neg
        if u==end:return cur
        if cur<best[u]:continue
        for v,x in g[u]:
            np=cur*x
            if np>best[v]:best[v]=np;heapq.heappush(h,(-np,v))
    return 0
print("T4 Q18:",max_prob(3,[[0,1],[1,2],[0,2]],[.5,.5,.2],0,2))
print("T4 Q18:",max_prob(3,[[0,1],[1,2],[0,2]],[.5,.5,.3],0,2))
