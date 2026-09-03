# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 22

import heapq
from math import inf

# Q19/Q20/Q21/Q22
def unique_paths(m,n):
    dp=[1]*n
    for _ in range(1,m):
        for j in range(1,n):dp[j]+=dp[j-1]
    return dp[-1]
def good_pairs(a):
    d={};ans=0
    for x in a:ans+=d.get(x,0);d[x]=d.get(x,0)+1
    return ans
def network_delay(times,n,k):
    g=[[] for _ in range(n+1)]
    for u,v,w in times:g[u].append((v,w))
    d=[inf]*(n+1);d[k]=0;h=[(0,k)]
    while h:
        du,u=heapq.heappop(h)
        if du!=d[u]:continue
        for v,w in g[u]:
            nd=du+w
            if nd<d[v]:d[v]=nd;heapq.heappush(h,(nd,v))
    return -1 if max(d[1:])==inf else max(d[1:])
print("T4 Q19:",unique_paths(3,7),unique_paths(3,2))
print("T4 Q20:",good_pairs([1,2,3,1,1,3]),good_pairs([1,1,1,1]))
print("T4 Q21:",city(4,[[0,1,3],[1,2,1],[1,3,4],[2,3,1]],4))
print("T4 Q22:",network_delay([[2,1,1],[2,3,1],[3,4,1]],4,2),network_delay([[1,2,1]],2,1),network_delay([[1,2,1]],2,2))
