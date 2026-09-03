# DAA Lab Exercise
# Topic 4 - Dynamic Programming - Question 3

from itertools import combinations, permutations
from collections import Counter, deque
from math import inf
import heapq

# Q3 Three Assembly Lines
def three_lines(a,t):
    L=len(a); n=len(a[0]); dp=[[0]*n for _ in range(L)]
    for l in range(L): dp[l][0]=a[l][0]
    for i in range(1,n):
        for l in range(L): dp[l][i]=a[l][i]+min(dp[p][i-1]+t[p][l] for p in range(L))
    return min(dp[l][-1] for l in range(L))
print("T4 Q3:",three_lines([[5,9,3],[6,8,4],[7,6,5]],[[0,2,3],[2,0,4],[3,4,0]]))
