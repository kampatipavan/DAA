# DAA Lab Exercise
# Topic 5 - Greedy - Question 4

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q4
def weighted_jobs(s,e,p):
    jobs=sorted(zip(s,e,p),key=lambda x:x[1]);dp=[0]*(len(jobs)+1)
    for i in range(1,len(jobs)+1):
        st,en,pr=jobs[i-1];j=i-1
        while j and jobs[j-1][1]>st:j-=1
        dp[i]=max(dp[i-1],pr+dp[j])
    return dp[-1]
print("T5 Q4:",weighted_jobs([1,2,3,3],[3,4,5,6],[50,10,40,70]))
print("T5 Q4:",weighted_jobs([1,2,3,4,6],[3,5,10,6,9],[20,20,100,70,60]))
