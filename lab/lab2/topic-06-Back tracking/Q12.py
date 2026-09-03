# DAA Lab Exercise
# Topic 6 - Backtracking - Question 12

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q12/Q14 Hamiltonian Cycle
def ham(n,e):
    adj=[set() for _ in range(n)]
    for u,v in e:adj[u].add(v);adj[v].add(u)
    p=[0]
    def bt():
        if len(p)==n:return p[0] in adj[p[-1]]
        for v in range(1,n):
            if v not in p and v in adj[p[-1]]:
                p.append(v)
                if bt():return True
                p.pop()
        return False
    return p+[0] if bt() else None
print("T6 Q12:",ham(5,[(0,1),(1,2),(2,3),(3,0),(0,2),(2,4),(4,0)]))
print("T6 Q14:",ham(4,[(0,1),(1,2),(2,3),(3,0),(0,2)]))
