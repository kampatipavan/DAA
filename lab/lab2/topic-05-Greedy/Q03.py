# DAA Lab Exercise
# Topic 5 - Greedy - Question 3

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q3
def min_work(jobs,k):
    jobs=sorted(jobs,reverse=True);load=[0]*k;best=sum(jobs)
    def bt(i):
        nonlocal best
        if i==len(jobs):best=min(best,max(load));return
        if max(load)>=best:return
        seen=set()
        for w in range(k):
            if load[w] in seen:continue
            seen.add(load[w]);load[w]+=jobs[i];bt(i+1);load[w]-=jobs[i]
            if load[w]==0:break
    bt(0);return best
print("T5 Q3:",min_work([3,2,3],3),min_work([1,2,4,7,8],2))
