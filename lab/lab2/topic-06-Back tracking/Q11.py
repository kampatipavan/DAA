# DAA Lab Exercise
# Topic 6 - Backtracking - Question 11

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q11 Graph Coloring
def coloring(n,e,k):
    adj=[set() for _ in range(n)]
    for u,v in e:adj[u].add(v);adj[v].add(u)
    c=[-1]*n
    def bt(v):
        if v==n:return True
        for x in range(k):
            if all(c[u]!=x for u in adj[v]):
                c[v]=x
                if bt(v+1):return True
                c[v]=-1
        return False
    return c if bt(0) else None
print("T6 Q11:",coloring(4,[(0,1),(1,2),(2,3),(3,0),(0,2)],3))
